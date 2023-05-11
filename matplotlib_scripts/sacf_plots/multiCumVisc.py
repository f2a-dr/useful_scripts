### The script works only if the output present in the log.lammps file is copied in a file with name 'time_corr.dat'

#import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import subprocess
#matplotlib.use('Agg')

# Identifier for simulation folder that contains the file to read
identifier = ["OQ8X"]

nonDecorrelated = True

deltat = []

# Extract deltat from files
for i in range(len(identifier)):
	filename = identifier[i] + '/results_' + identifier[i] + '.txt'
	with open(filename) as f:
		for line in f:
			if line.strip():
				if line.strip().split()[0] == "DT":
					deltat.append(float(line.strip().split()[2]))

# calculation of K
side = 20
vol = side**3
T = 1
kB = 1
Nev = 1 
K = Nev*vol/(kB*T)

v11 = [[] for _ in range(len(identifier))]
v22 = [[] for _ in range(len(identifier))]
v33 = [[] for _ in range(len(identifier))]
vAv = [[] for _ in range(len(identifier))]
time = [[] for _ in range(len(identifier))]
timeStep = [[] for _ in range(len(identifier))]

#cum11 = [[] for _ in range(len(identifier))]
#cum22 = [[] for _ in range(len(identifier))]
#cum33 = [[] for _ in range(len(identifier))]
cumAv = [[] for _ in range(len(identifier))]
#cumInt = [[] for _ in range(len(identifier))]

# Results file reading
for i in range(len(identifier)):
	filename = identifier[i] + '/time_cor.txt_' + identifier[i]
	with open(filename) as f:
		next(f)
		next(f)
		next(f)
		info = str(f.readline())
		info = info.strip()
		info = info.split()
		n = int(info[1])

	with open("tmp.dat", "w") as fw:
		subprocess.call(["tail", "-n", str(n), filename], stdout=fw)

	with open('tmp.dat') as f:
		for line in f:
			line = line.strip()
			line = line.split()
			timeStep[i].append(float(line[1]))
			time[i].append(deltat[i]*float(line[1]))
			v11[i].append(float(line[3]))
			v22[i].append(float(line[4]))
			v33[i].append(float(line[5]))
			vAv[i].append((float(line[3])+float(line[4])+float(line[5]))/3)

	subprocess.run(["rm", "tmp.dat"])


	# Cumulative integral
	for j in range(0,len(vAv[i])):
		#cum11.append(K*np.trapz(v11[0:j], time[0:j]))
		#cum22.append(K*np.trapz(v22[0:j], time[0:j]))
		#cum33.append(K*np.trapz(v33[0:j], time[0:j]))
		cumAv[i].append(K*np.trapz(vAv[i][0:j], time[i][0:j]))
		#cumInt.append(K*(np.trapz(v11[0:j], time[0:j])+np.trapz(v22[0:j], time[0:j])+np.trapz(v33[0:j], time[0:j]))/3)

# Correction for uncomplete decorrelation
if nonDecorrelated:
	# Calculate the mean of the plateau
	startAveragingTime = 10
	timeStepStartAveraging = int(startAveragingTime/deltat[-1])
	index = timeStep[-1].index(timeStepStartAveraging)
	baseValue = np.mean(np.array(vAv[-1][index::]))
	print(baseValue)

	for i in range(len(cumAv)):
		# Calculate the area to remove from the integral
		#toSubtract = []
		for j in range(len(cumAv[i])):
			cumAv[i][j] = cumAv[i][j] - K*baseValue*time[i][j]
			#toSubtract.append(baseValue*time[i][0:j])
		# Remove the area from the cumulative integral
		




# Plot
plt.rcParams.update({
	"text.usetex": True,
	"font.family": "serif",
	#"font.sanserif": "Helvetica"
})

centimeters = 1/2.54
cmap = plt.get_cmap('jet')
fig1 = plt.figure(figsize=(15*centimeters,7.5*centimeters),constrained_layout=True)
gs = fig1.add_gridspec(1,2)

ax1 = fig1.add_subplot(gs[0,0])
ax1.set_title(r"SACF")
ax1.set_xlabel(r"Time", fontsize=12)
ax1.set_ylabel(r"SACF", fontsize=12)
ax1.set_yscale('log')
ax1.plot(time[-1], 1e-5*np.ones(len(time[-1])), linewidth=0.5, color='black')
for k in range(len(vAv)):
	ax1.plot(time[k], vAv[k], linewidth=0.5, color=cmap(float(k/len(cumAv))))

ax2 = fig1.add_subplot(gs[0,1])
ax2.set_title(r"Cumulative viscosity")
ax2.set_xlabel(r"Time", fontsize=12)
ax2.set_ylabel(r"Cumulative viscosity", fontsize=12)
for k in range(len(cumAv)):
	ax2.plot(time[k], cumAv[k], linewidth=1, color=cmap(float(k/len(cumAv))))
#ax1.set_xlim(left=-0.01,right=0.2)
#ax1.set_ylim(bottom=-0.002,top=0.006)
#ax1.plot(time, cumInt, color='tab:orange', label="Int")
#ax1.plot(time, np.zeros(len(time)), 'r', label="zero")
#ax1.plot(time, v11, 'r', label="11")
#ax1.plot(time, v22, 'b', label="22")
#ax1.plot(time, v33, 'g', label="33")
#ax1.legend()

#plt.show()
if nonDecorrelated:
	fig1.savefig("cumulativeViscosity.pdf", format="pdf")
else:
	fig1.savefig("cumulativeViscosity_nonEpurated.pdf", format="pdf")
