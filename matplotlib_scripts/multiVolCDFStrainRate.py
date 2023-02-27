import numpy as np
import matplotlib
#matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Imposed upper limit for zero shear viscosity region
shear_0 = 0.1
nCellPos = 21 # Line in the file that contains the number of cells in the mesh (starting from 1)

# File to read and plot attribute per file
srFiles = ["strainRateOF_N", "strainRateOF_0", "strainRateOF_1"]
volFiles = ["cellVolumesOF_N", "cellVolumesOF_0", "cellVolumesOF_1"]
lab = ["Newtonian", "First GPR", "Second GPR"]
col = ["tab:blue", "tab:orange", "tab:green"]


# Initialization of the vectors
sr = [[] for _ in range(len(srFiles))]
volumes = [[] for _ in range(len(volFiles))]
volInc = [[] for _ in range(len(volFiles))]

# Open input files and store strain rate e cell volumes
for i in range(0,len(srFiles)):
        with open(srFiles[i]) as f:
            f.seek(0)
            for s in range(0, nCellPos-1):
                next(f)
            nCells = int(f.readline().strip())
            next(f)
            for j, line in enumerate(f):
                if j >= 0 and j < nCells:
                    line = line.strip()
                    sr[i].append(float(line))

        with open(volFiles[i]) as f:
            f.seek(0)
            for s in range(0, nCellPos-1):
                next(f)
            nCells = int(f.readline().strip())
            next(f)
            for j, line in enumerate(f):
                if j >= 0 and j < nCells:
                    line = line.strip()
                    volumes[i].append(float(line))


# Sort the strain rate and calculate the Cumulative Distribution Function
sR = np.array(sr)
vol = np.array(volumes)
sortIndx = sR.argsort()

srSort = [[] for _ in range(len(sR))]
volSort = [[] for _ in range(len(vol))]
for i in range(0, len(sortIndx)):
    srSort[i] = sR[i][sortIndx[i]]
    volSort[i] = vol[i][sortIndx[i]]

for j in range(0, len(volSort)):
    volSum = 0
    for i in range(0, len(volSort[j])):
        volSum = volSum + volSort[j][i]
        volInc[j].append(float(volSum))

volFrac = [[] for _ in range(len(volInc))]
for i in range(0, len(volInc)):
    volFrac[i] = np.array(volInc[i])/np.sum(volSort[i])

# Plotting the results
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    #"font.sanserif": "Helvetica"
})

centimeters = 1/2.54
fig = plt.figure(figsize=(10*centimeters,10*centimeters),constrained_layout=True)
gs = fig.add_gridspec(1,1)

ax1 = fig.add_subplot(gs[0,0])
#ax1.set_title(r"Volume weighted CDF",fontsize=24)
ax1.set_xlabel(r"$\dot{\gamma}\ (s^{-1})$",fontsize=16)
ax1.set_ylabel(r"Volume fraction",fontsize=16)
ax1.tick_params(axis="both",which="both",labelsize=11)
for i in range(0, len(srSort)):
    ax1.plot(srSort[i], volFrac[i], color=col[i], label=lab[i])
    #ax1.plot(srSort[i], (1.1+i/10)*np.ones(len(srSort[i])), color=col[i], linestyle='-', linewidth=1)
    #ax1.plot(srSort[i][0], 1.1+i/10, color=col[i], marker=r"$[$", markersize=10)
    #ax1.plot(srSort[i][-1], 1.1+i/10, color=col[i], marker=r"$]$", markersize=10)
    ax1.plot(srSort[i][0], volFrac[i][0], color=col[i], marker=r"$[$", markersize=10)
    ax1.plot(srSort[i][-1], volFrac[i][-1], color=col[i], marker=r"$]$", markersize=10)
#ax1.plot(0.1*np.ones(50), np.linspace(0.0001,1).reshape(-1,1), 'tab:red')
ax1.set_xscale("log")
ax1.grid(which='minor', axis='x', color='tab:gray', linestyle=':', linewidth=0.3)
ax1.grid(which='major', axis='x', color='tab:gray', linestyle='-', linewidth=0.3)
ax1.grid(which='major', axis='y', color='tab:gray', linestyle='-', linewidth=0.3)
plt.legend()

#plt.show()
#fig.savefig("CDF_sr_GPR.pdf", dpi=300)
fig.savefig("multiTest.pdf", dpi=300)
