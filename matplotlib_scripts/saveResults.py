import numpy as np
import matplotlib
import matplotlib.pyplot as plt

folders = ["dpd_L5_sr0.00001", "dpd_L5_sr0.01", "dpd_L5_sr1"]
timestep = 0.0025
delay = 10

def plotTimeResponsePxy(folders):
    for i in range(len(folders)):
        pxyTTCF = []
        pxyDAV = []
        filename = folders[i] + "/global_TTCF.txt"
        with open(filename) as f:
            for line in f:
                line = line.strip().split()
                pxyTTCF.append(float(line[0]))
        filename = folders[i] + "/global_DAV.txt"
        with open(filename) as f:
            for line in f:
                line = line.strip().split()
                pxyDAV.append(float(line[0]))
        time = np.linspace(0, delay*timestep*len(pxyTTCF), len(pxyTTCF))

        centimeters = 1/2.54
        fig = plt.figure(figsize=(10*centimeters, 10*centimeters), constrained_layout=True)
        gs = fig.add_gridspec(1, 1)
        ax = fig.add_subplot(gs[0, 0])
        ax.set_xlabel(r"Time", fontsize=16)
        ax.set_ylabel(r"$P_{xy}$, DPD units", fontsize=16)
        ax.plot(time, pxyTTCF, color="dodgerblue", label="TTCF")
        ax.plot(time, pxyDAV, color="crimson", label="DAV")
        ax.tick_params(axis="both", which="major", labelsize=14)
        ax.legend(fontsize=14)

        fig.savefig(folders[i]+"/Pxy.png")


if __name__ == "__main__":
    plotTimeResponsePxy(folders)
