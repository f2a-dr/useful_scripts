################################################################################
# This script plots all the time series data in a `result.dat` file, which has
# the following structure:
#
# Time  Variable1   Variable2   Variable3   ...
#
# It calculate the average of the properties starting from a certain
# equilibration time and the associated standard deviation.
# Since I use it with very noisy variables, from MD or DPD simulations, the
# limit of the axis are imposed to enlarge the view to +/- 10 times the value
# of the standard deviation.
################################################################################



import matplotlib
import numpy as np
#from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
#matplotlib.use('Agg')

toSave = False

# Constant parameter definitions
printTime = 100			# This variable is how often the result are printed in the log.lammps file
eqTime = 300000			# This variable specify at which timestep you want to consider the equilibration finished (must be a multiple of printTime)
Eq = int(eqTime/printTime)

# Results file reading
filename = "results.dat"
with open(filename) as f:
    header = f.readline()
    header = header.strip().split()
    fullData = [[] for i in range(len(header))]
    for line in f:
        line = line.strip()
        line = line.split()
        for j in range(len(header)):
            fullData[j].append(float(line[j]))

data = [[] for i in range(len(header))]
for i in range(len(header)):
    data[i] = fullData[i][Eq+1:]
    header[i] = header[i].replace("_", " ")


plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
})

fig = [0]*len(header)
gs = [0]*len(header)
centimeters = 1/2.54
for i in range(1, len(header)):

    fig[i] = plt.figure(figsize=(15*centimeters, 15*centimeters), constrained_layout=True)
    gs[i] = fig[i].add_gridspec(1, 1)

    ax = fig[i].add_subplot(gs[i][0, 0])
    ax.set_xlabel(r"Step", fontsize=16)
    ax.set_ylabel(header[i]+", DPD units", fontsize=16)
    ax.set_ylim(np.mean(fullData[i])-10*np.std(fullData[i]), np.mean(fullData[i])+10*np.std(fullData[i]))
    ax.plot(fullData[0], fullData[i], color="dodgerblue", label=header[i])
    ax.plot(data[0], np.mean(data[i])*np.ones(len(data[0])), color="crimson", label=r"$\langle$"+header[i]+r"$\rangle$")
    ax.text(0.5, 0.25, "mean = {ave}\nstdv = {stdv}".format(ave=round(np.mean(data[i]),4), stdv=round(np.std(data[i]),4)), ha="center", va="center", fontsize=16, bbox=dict(edgecolor="crimson", facecolor="dodgerblue", alpha=1), color="white", transform=ax.transAxes)
    ax.tick_params(axis="both", which="major", labelsize=14)
    ax.legend(fontsize=14)

if toSave:
    for i in range(1, len(header)):
        fig[i].savefig(header[i]+".pdf")
else:
    plt.show()

