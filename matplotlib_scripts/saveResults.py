import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import ticker

folders = ["dpd_L5_sr0.00001", "dpd_L5_sr0.01", "dpd_L5_sr1", "dpd_L15_sr0.00001", "dpd_L15_sr0.01", "dpd_L15_sr1"]
timestep = 0.0025
delay = 10

def plotTimeResponsePxy(folders, onlyTTCF=False):
    for i in range(len(folders)):
        pxyTTCF = []
        pxyDAV = []
        filename = folders[i] + "/global_TTCF.txt"
        with open(filename) as f:
            for line in f:
                line = line.strip().split()
                pxyTTCF.append(float(line[0]))
        if not(onlyTTCF):
            filename = folders[i] + "/global_DAV.txt"
            with open(filename) as f:
                for line in f:
                    line = line.strip().split()
                    pxyDAV.append(float(line[0]))
        time = list(np.linspace(0, delay*timestep*len(pxyTTCF), len(pxyTTCF)))

        centimeters = 1/2.54
        fig = plt.figure(figsize=(10*centimeters, 10*centimeters), constrained_layout=True)
        gs = fig.add_gridspec(1, 1)
        ax = fig.add_subplot(gs[0, 0])
        ax.set_xlabel(r"Time", fontsize=16)
        ax.set_ylabel(r"$P_{xy}$, DPD units", fontsize=16)
        ax.plot(time, pxyTTCF, color="dodgerblue", label="TTCF")
        if not(onlyTTCF):
            ax.plot(time, pxyDAV, color="crimson", label="DAV")
        ax.tick_params(axis="both", which="major", labelsize=14)
        ax.legend(fontsize=14)

        if not(onlyTTCF):
            fig.savefig(folders[i]+"/Pxy.png", dpi=300)
        else:
            fig.savefig(folders[i]+"/Pxy_ttcf.png", dpi=300)
        plt.cla()

    plt.close('all')

def plotVelocity(folders, onlyTTCF=False, timeResponse=True):
    for i in range(len(folders)):
        filename = folders[i] + "/profile_TTCF_vx.txt"
        with open(filename) as f:
            lines = f.read().splitlines()
            for j in range(len(lines)):
                lines[j] = lines[j].strip().split()
            vxTTCF = np.array(lines, dtype='double')
            
        if not(onlyTTCF):
            filename = folders[i] + "/profile_DAV_vx.txt"
            with open(filename) as f:
                lines = f.read().splitlines()
                for j in range(len(lines)):
                    lines[j] = lines[j].strip().split()
                vxDAV = np.array(lines, dtype='double')

        binsN = np.linspace(0, len(vxTTCF[0]), len(vxTTCF[0]))
        centimeters = 1/2.54
        fig = plt.figure(figsize=(10*centimeters, 10*centimeters), constrained_layout=True)
        gs = fig.add_gridspec(1, 1)
        ax = fig.add_subplot(gs[0, 0])
        ax.set_xlabel(r"Bins", fontsize=16)
        ax.set_ylabel(r"$v_{x}$, DPD units", fontsize=16)
        ax.plot(binsN, np.mean(vxTTCF, axis=0), color="dodgerblue", label="TTCF")
        if not(onlyTTCF):
            ax.plot(binsN, np.mean(vxDAV, axis=0), color="crimson", label="DAV")
        ax.tick_params(axis="both", which="major", labelsize=14)
        # ax.yaxis.set_major_formatter(ticker.NullFormatter())
        ax.legend(fontsize=14)

        if not(onlyTTCF):
            fig.savefig(folders[i]+"/vx.png", dpi=300)
        else:
            fig.savefig(folders[i]+"/vx_ttcf.png", dpi=300)
        plt.cla()

        if timeResponse:
            bin1 = 14
            bin2 = 89
            v1_TTCF = np.transpose(vxTTCF)[bin1]
            v2_TTCF = np.transpose(vxTTCF)[bin2]
            if not(onlyTTCF):
                v1_DAV = np.transpose(vxDAV)[bin1]
                v2_DAV = np.transpose(vxDAV)[bin2]
            time = list(np.linspace(0, delay*timestep*len(v1_TTCF), len(v1_TTCF)))

            fig1 = plt.figure(figsize=(10*centimeters, 10*centimeters), constrained_layout=True)
            gs = fig1.add_gridspec(1, 1)
            ax = fig1.add_subplot(gs[0, 0])
            ax.set_xlabel(r"Time", fontsize=16)
            ax.set_ylabel(r"$v_{x}$, DPD units", fontsize=16)
            ax.plot(time, v1_TTCF, color="dodgerblue", label="TTCF - bin {}".format(bin1+1))
            ax.plot(time, v2_TTCF, color="steelblue", label="TTCF - bin {}".format(bin2+1))
            if not(onlyTTCF):
                ax.plot(time, v1_DAV, color="crimson", label="DAV - bin {}".format(bin1+1))
                ax.plot(time, v2_DAV, color="firebrick", label="DAV - bin {}".format(bin2+1))
            ax.tick_params(axis="both", which="major", labelsize=14)
            # ax.yaxis.set_major_formatter(ticker.NullFormatter())
            ax.legend(fontsize=14)

            if not(onlyTTCF):
                fig1.savefig(folders[i]+"/vx_time.png", dpi=300)
            else:
                fig1.savefig(folders[i]+"/vx_ttcf_time.png", dpi=300)

            plt.cla()

    plt.close('all')





if __name__ == "__main__":
    plotTimeResponsePxy(folders, onlyTTCF=True)
    plotTimeResponsePxy(folders)
    plotVelocity(folders, onlyTTCF=True)
    plotVelocity(folders)