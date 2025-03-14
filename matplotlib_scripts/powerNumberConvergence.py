import matplotlib
import numpy as np
import matplotlib.pyplot as plt
#matplotlib.use('Agg')

# Physical properties needed for the calculation
rho = 1000
mu = 1e-3
nu = mu/rho
V = 10e-3
RPM = 100
N = RPM/60
omega = RPM/60*2*np.pi
T = 0.230
D = T/3
Re = rho*N*D**2/mu

laminar = False

# List the file to process
directory = "postProcessing/"
if laminar:
    subdir = ["forces_1/", "forces_2/"]
    files = ["forces.dat", "forces.dat"]
else:
    subdir = ["forces_1/", "forces_2/", "epsilon_avg/", "power_dissipation/"]
    files = ["forces.dat", "forces.dat", "volFieldValue.dat", "volFieldValue.dat"]

# Specify what will go in each plot
if laminar:
    howToPlot = [[0, 1], [2, 3], [4, 5]]
    fileout = ["momenta", "power", "powerNumber"]
    labels = [r"$M_z^\mathrm{stat}$", r"$M_z^\mathrm{rot}$", r"$P^\mathrm{stat}$", r"$P^\mathrm{rot}$", r"$N_p^{\mathrm{stat}}$", r"$N_p^{\mathrm{rot}}$"]
else:
    howToPlot = [[0, 1], [2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
    fileout = ["momenta", "dissipation", "power", "powerNumber"]
    labels = [r"$M_z^\mathrm{stat}$", r"$M_z^\mathrm{rot}$", r"$\bar{\epsilon}$", r"$\frac{\int_{V}\epsilon\,dV}{V}$", r"$P^\mathrm{stat}$", r"$P^\mathrm{rot}$", r"$P^{\bar{\epsilon}}$", r"$P^{\epsilon V}$", r"$N_p^{\mathrm{stat}}$", r"$N_p^{\mathrm{rot}}$", r"$N_p^{\bar{\epsilon}}$", r"$N_p^{\epsilon V}$"]
colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", "tab:brown", "tab:pink", "tab:grey", "tab:olive", "tab:cyan"]

# Momenta_static    Momenta_rotating    Epsilon_average     Epsilon_integrated
# 
times = [[] for _ in range(3*len(files))]
values = [[] for _ in range(3*len(files))]
powers = [[] for _ in range(len(files))]
powerNumbers = [[] for _ in range(len(files))]

# Read the files
for i in range(len(files)):
    filename = directory+subdir[i]+"0/"+files[i]
    if files[i] == "forces.dat":
        with open(filename) as f:
            next(f)
            next(f)
            next(f)
            for line in f:
                line = line.replace('(', '').replace(')', '')
                line = line.strip()
                line = line.split()
                times[i].append(float(line[0]))
                values[i].append(np.abs(float(line[12])+float(line[15])))
    elif subdir[i] == "power_dissipation/":
        with open(filename) as f:
            next(f)
            next(f)
            next(f)
            next(f)
            for line in f:
                line = line.strip()
                line = line.split()
                times[i].append(float(line[0]))
                values[i].append(float(line[1])/V)
    else:
        with open(filename) as f:
            next(f)
            next(f)
            next(f)
            next(f)
            for line in f:
                line = line.strip()
                line = line.split()
                times[i].append(float(line[0]))
                values[i].append(float(line[1]))

for i in range(len(files)):
    if laminar:
        for j in range(len(values[i])):
            times[i+2].append(times[i][j])
            times[i+4].append(times[i][j])
            values[i+2].append(omega*values[i][j])
            values[i+4].append(omega*values[i][j]/(rho*N**3*D**5))
    else:
        if i < 2:
            for j in range(len(values[i])):
                times[i+4].append(times[i][j])
                times[i+8].append(times[i][j])
                values[i+4].append(omega*values[i][j])
                values[i+8].append(omega*values[i][j]/(rho*N**3*D**5))
        elif i == 2:
            for j in range(len(values[i])):
                times[i+4].append(times[i][j])
                times[i+8].append(times[i][j])
                values[i+4].append(values[i][j]*V*rho)
                values[i+8].append(values[i][j]*V/(N**3*D**5))
        else:
            for j in range(len(values[i])):
                times[i+4].append(times[i][j])
                times[i+8].append(times[i][j])
                values[i+4].append(values[i][j]*V*rho)
                values[i+8].append(values[i][j]*V/(N**3*D**5))


# Plot the results
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    #"font.sanserif": "Helvetica"
})

fig = [0]*len(howToPlot)
gs = [0]*len(howToPlot)
centimeters = 1/2.54
for i in range(len(howToPlot)):
    fig[i] = plt.figure(figsize=(10*centimeters,10*centimeters), constrained_layout=True)
    gs[i] = fig[i].add_gridspec(1,1)

    ax = fig[i].add_subplot(gs[i][0,0])
    ax.set_xlabel(r"Step", fontsize=16)
    ax.set_ylabel(fileout[i], fontsize=16)
    # ax.set_yscale("log")
    ax.tick_params(axis="both", which="both", labelsize=11)
    for j in range(len(howToPlot[i])):
        ax.plot(times[howToPlot[i][j]], values[howToPlot[i][j]], color=colors[j], label=labels[howToPlot[i][j]])
    ax.grid(which="major", axis="x", color="tab:gray", linestyle="-", linewidth=0.3)
    ax.grid(which="major", axis="y", color="tab:gray", linestyle="-", linewidth=0.3)
    ax.grid(which="minor", axis="y", color="tab:gray", linestyle=":", linewidth=0.3)
    plt.legend()

    #plt.show()
    fig[i].savefig("plots/Power_"+fileout[i]+".pdf",dpi=300)


print("\nRPM = {}".format(RPM))
print("\nN = {}".format(N))
print("\nRe = {}".format(Re))
print("\n### Power Number ###")
print("Static parts, Np = {}".format(values[2*len(files)][-1]))
print("Rotating parts, Np = {}".format(values[1+2*len(files)][-1]))
if not(laminar):
    print("Epsilon, Np = {}".format(values[2+2*len(files)][-1]))
