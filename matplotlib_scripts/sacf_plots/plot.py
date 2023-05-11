import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# Identifier for simulation folder that contains the file to read
identifier = ["OQ8X"]

# Vector initialization
Dt = []
N = []
Nfreq = []
mu0 = []

# Extract from files
for i in range(len(identifier)):
	filename = identifier[i] + "/results_" + identifier[i]+ ".txt"
	with open(filename) as f:
		for line in f:
			if line.strip():
				if line.strip().split()[0] == "NFREQ":
					Nfreq.append(float(line.strip().split()[2]))
				elif line.strip().split()[0] == "N":
					N.append(float(line.strip().split()[2]))
				elif line.strip().split()[0] == "DT":
					Dt.append(float(line.strip().split()[2]))
				elif line.strip().split()[0] == "Viscosity:":
					mu0.append(float(line.strip().split()[1]))
print(Nfreq)
print(N)
print(Dt)

# Time calculation
time = []
for i in range(len(Dt)):
	time.append(N[i]*Nfreq[i]*Dt[i])

print(time)

dmu = []
dtime = []
for i in range(len(mu0)-1):
	# print(time[i+1]-time[i])
	dtime.append(time[i]+(time[i+1]-time[i])/2)
	dmu.append((mu0[i+1]-mu0[i])/(time[i+1]-time[i]))

# Plot
plt.rcParams.update({
	"text.usetex": True,
	"font.family": "serif",
	#"font.sanserif": "Helvetica"
})

centimeters = 1/2.54
fig1 = plt.figure(figsize=(10*centimeters, 10*centimeters), constrained_layout=True)
gs1 = fig1.add_gridspec(1, 1)

ax1 = fig1.add_subplot(gs1[0, 0])
ax1.set_ylabel(r"$\mu\ (\mathrm{DPD\:units})$", fontsize=16)
ax1.set_xlabel(r"$t\ (\mathrm{DPD\:units})$", fontsize=16)
ax1.plot(time, mu0, color='tab:blue', linestyle='-')
ax1.plot(time, mu0, color='tab:orange', marker='o', markersize=6, markeredgecolor='brown', fillstyle='full', linestyle='')
#ax1.set_ylabel(r"$\frac{\Delta\mu}{\Delta t}\ (\mathrm{DPD\:units})$", fontsize=16)
#ax1.set_xlabel(r"$t\ (\mathrm{DPD\:units})$", fontsize=16)
#ax1.plot(dtime, dmu, color='tab:green', linestyle='-')
#ax1.plot(dtime, dmu, color='tab:red', marker='o', markersize=6, markeredgecolor='black', fillstyle='full', linestyle='')
ax1.grid(which='major', axis='both', color='tab:gray', linestyle=':', linewidth=0.3)

#plt.show()
fig1.savefig("mu_vs_t.pdf", dpi=300)
#fig1.savefig("dmu_on_dt.pdf", dpi=300)
