import matplotlib
import numpy as np
import matplotlib.pyplot as plt
#matplotlib.use('Agg')

# List the file to process
directory = "logs/"
files = ["p_0", "p_1", "p_2", "Ux_0", "Uy_0", "Uz_0"]

#Specify which residual will go in each plot
#howToPlot = [3, 3]
howToPlot = [[0, 1, 2], [3, 4, 5]]
fileout = ["p", "U"]
labels = [r"$p^0$", r"$p^1$", r"$p^2$", r"$U_x^0$", r"$U_y^0$", r"$U_z^0$"]
colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", "tab:brown", "tab:pink", "tab:grey", "tab:olive", "tab:cyan"]

# Set up the needed lists
step = [[] for _ in range(len(files))]
res = [[] for _ in range(len(files))]

# Read the files and save the content
for i in range(len(files)):
    with open(directory + files[i]) as f:
        f.seek(0)
        next(f)
        for line in f:
            line = line.strip()
            line = line.split()
            step[i].append(float(line[0]))
            res[i].append(float(line[1]))

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
    ax.set_ylabel(r"Residuals", fontsize=16)
    ax.set_yscale("log")
    ax.tick_params(axis="both", which="both", labelsize=11)
    for j in range(len(howToPlot[i])):
        ax.plot(step[howToPlot[i][j]], res[howToPlot[i][j]], color=colors[j], label=labels[howToPlot[i][j]])
    ax.grid(which="major", axis="x", color="tab:gray", linestyle="-", linewidth=0.3)
    ax.grid(which="major", axis="y", color="tab:gray", linestyle="-", linewidth=0.3)
    ax.grid(which="minor", axis="y", color="tab:gray", linestyle=":", linewidth=0.3)
    plt.legend()

    #plt.show()
    fig[i].savefig("Residual_"+fileout[i]+".pdf",dpi=300)
