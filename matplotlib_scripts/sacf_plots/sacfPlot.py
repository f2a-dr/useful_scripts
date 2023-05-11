### The script works only if the output present in the log.lammps file is copied in a file with name 'time_corr.dat'

#import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import subprocess
#matplotlib.use('Agg')


# Identifier for simulation folder that contains the file to read
identifier = ["OQ8X"]

nfreq = []
# Extract nfreq=nrep from files
for i in range(len(identifier)):
	filename = identifier[i] + '/results_' + identifier[i] +'.txt'
	with open(filename) as f:
		for line in f:
			if line.strip():
				if line.strip().split()[0] == "NFREQ":
					nfreq.append(float(line.strip().split()[2]))

for i in range(len(identifier)):
	v11 = []
	v22 = []
	v33 = []
	vAv = []
	time = []

# Results file reading
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
			time.append(0.04/3*float(line[1]))
			v11.append(float(line[3]))
			v22.append(float(line[4]))
			v33.append(float(line[5]))
			vAv.append((float(line[3])+float(line[4])+float(line[5]))/3)

	subprocess.run(["rm", "tmp.dat"])

	# Plot
	plt.rcParams.update({
		"text.usetex": True,
		"font.family": "serif",
		#"font.sanserif": "Helvetica"
	})

	centimeters = 1/2.54
	fig1 = plt.figure(figsize=(7.5*centimeters,7.5*centimeters),constrained_layout=True)
	gs = fig1.add_gridspec(1,1)
	
	ax1 = fig1.add_subplot(gs[0,0])
	ax1.set_title(r"SACF, $N_\mathrm{{freq}} = {}$".format(nfreq[i]))
	ax1.set_xlabel(r"Time", fontsize=12)
	ax1.set_ylabel(r"SACF", fontsize=12)
	# ax1.set_xlim(left=-0.01,right=0.2)
	ax1.set_ylim(bottom=-1e-4,top=1e-3)
	ax1.plot(time, v11, color='darkorange', label="11")
	ax1.plot(time, v22, color='dodgerblue', label="22")
	ax1.plot(time, v33, color='forestgreen', label="33")
	ax1.plot(time, vAv, color='crimson', label="av")
	ax1.plot(time, np.zeros(len(time)), color='black', label="zero")
	ax1.ticklabel_format(style='scientific', scilimits=(-1, 10))
	ax1.yaxis.get_offset_text().set_fontsize(6)
	ax1.tick_params(labelsize=8)
	ax1.legend(fontsize=8)

	# plt.show()
	fig1.savefig("SACF_{}.pdf".format(identifier[i]), format='pdf')
