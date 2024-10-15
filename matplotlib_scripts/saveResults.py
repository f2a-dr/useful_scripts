import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import ticker

folders = ["."]
timestep = 0.001
delay = 1
printFormat = ["png"]

def profileRead(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
        for j in range(len(lines)):
            lines[j] = lines[j].strip().split()
        profile = np.array(lines, dtype='double')
    return profile


def globalRead(filename, varPosition):
    variable = []
    with open(filename) as f:
        for line in f:
            line = line.strip().split()
            variable.append(float(line[varPosition]))
    return variable


def plotTimeResponsePxy(folders, onlyTTCF=False, se=True):
    for i in range(len(folders)):
        pxyTTCF = globalRead(folders[i] + "/global_TTCF.txt", 0)
        pxyTTCFse = globalRead(folders[i] + "/global_TTCF_SE.txt", 0)
        if not(onlyTTCF):
            pxyDAV = globalRead(folders[i] + "/global_DAV.txt", 0)
            pxyDAVse = globalRead(folders[i] + "/global_DAV_SE.txt", 0)
        time = list(np.linspace(0, delay*timestep*len(pxyTTCF), len(pxyTTCF)))

        centimeters = 1/2.54
        fig = plt.figure(figsize=(10*centimeters, 10*centimeters), constrained_layout=True)
        gs = fig.add_gridspec(1, 1)
        ax = fig.add_subplot(gs[0, 0])
        ax.set_xlabel(r"Time", fontsize=16)
        ax.set_ylabel(r"$P_{xy}$, DPD units", fontsize=16)
        if not(se):
            ax.plot(time, pxyTTCF, color="dodgerblue", label="TTCF")
            if not(onlyTTCF):
                ax.plot(time, pxyDAV, color="crimson", label="DAV")
        else:
            ax.errorbar(time, pxyTTCF, pxyTTCFse, linewidth=0.2, marker="o", markersize=1, capsize=2, capthick=0.5, ecolor="skyblue", elinewidth=0.5, color="dodgerblue", label="TTCF")
            if not(onlyTTCF):
                ax.errorbar(time, pxyDAV, pxyDAVse, linewidth=0.2, marker="o", markersize=1, capsize=2, capthick=0.5, ecolor="lightcoral", elinewidth=0.5, color="crimson", label="DAV")
        ax.tick_params(axis="both", which="major", labelsize=14)
        ax.legend(fontsize=14)

        if not(onlyTTCF):
            for j in printFormat:
                if se:
                    fig.savefig(folders[i]+"/Pxy_se."+j, dpi=300)
                else:
                    fig.savefig(folders[i]+"/Pxy."+j, dpi=300)
        else:
            for j in printFormat:
                if se:
                    fig.savefig(folders[i]+"/Pxy_ttcf_se."+j, dpi=300)
                else:
                    fig.savefig(folders[i]+"/Pxy_ttcf."+j, dpi=300)
        plt.cla()

    plt.close('all')

def plotPxyProfile(folders, onlyTTCF=False):
    for i in range(len(folders)):
        PxyTTCF = profileRead(folders[i] + "/profile_TTCF_c_stress[4].txt")
        PxyTTCFse = profileRead(folders[i] + "/profile_TTCF_SE_c_stress[4].txt")
            
        if not(onlyTTCF):
            PxyDAV = profileRead(folders[i] + "/profile_DAV_c_stress[4].txt")
            PxyDAVse = profileRead(folders[i] + "/profile_DAV_SE_c_stress[4].txt")

        binsN = np.linspace(0, len(PxyTTCF[0]), len(PxyTTCF[0]))
        centimeters = 1/2.54
        fig = plt.figure(figsize=(10*centimeters, 10*centimeters), constrained_layout=True)
        gs = fig.add_gridspec(1, 1)
        ax = fig.add_subplot(gs[0, 0])
        ax.set_xlabel(r"Bins", fontsize=16)
        ax.set_ylabel(r"$P_{xy}$, DPD units", fontsize=16)
        ax.plot(binsN, np.mean(PxyTTCF, axis=0), color="dodgerblue", label="TTCF")
        if not(onlyTTCF):
            ax.plot(binsN, np.mean(PxyDAV, axis=0), color="crimson", label="DAV")
        ax.tick_params(axis="both", which="major", labelsize=14)
        # ax.yaxis.set_major_formatter(ticker.NullFormatter())
        ax.legend(fontsize=14)

        if not(onlyTTCF):
            for j in printFormat:
                fig.savefig(folders[i]+"/Pxy_profile."+j, dpi=300)
        else:
            for j in printFormat:
                fig.savefig(folders[i]+"/Pxy_profile_ttcf."+j, dpi=300)
        plt.cla()


def plotVelocity(folders, onlyTTCF=False, timeResponse=True, theoreticalProfiles=False, average=True, index=-1):
    for i in range(len(folders)):
        if theoreticalProfiles:
            print("""WARNING: You are plotting also the theoretical profiles, be sure
                    to use the right box size and shear rate value""")
            L = 5
            shearRate = 1e-2

        vxTTCF = profileRead(folders[i] + "/profile_TTCF_vx.txt")
        vxTTCFse = profileRead(folders[i] + "/profile_TTCF_SE_vx.txt")
            
        if not(onlyTTCF):
            vxDAV = profileRead(folders[i] + "/profile_DAV_vx.txt")
            vxDAVse = profileRead(folders[i] + "/profile_DAV_SE_vx.txt")
            
        if average:
            avTTCF = np.mean(vxTTCF, axis=0)
            # seTTCF = np.sqrt(np.sum(vxTTCFse**2, axis=0)/len(vxTTCFse[0]))
            if not(onlyTTCF):
                avDAV = np.mean(vxDAV, axis=0)
                # seDAV = np.sqrt(np.sum(vxDAVse**2, axis=0)/len(vxDAVse[0]))

        binsN = np.linspace(0, len(vxTTCF[0]), len(vxTTCF[0]))
        centimeters = 1/2.54
        fig = plt.figure(figsize=(10*centimeters, 10*centimeters), constrained_layout=True)
        gs = fig.add_gridspec(1, 1)
        ax = fig.add_subplot(gs[0, 0])
        ax.set_xlabel(r"Bins", fontsize=16)
        ax.set_ylabel(r"$v_{x}$, DPD units", fontsize=16)
        if average:
            ax.plot(binsN, avTTCF, linewidth=0.5, marker="o", marskersize=1, color="dodgerblue", label="TTCF")
        else:
            ax.errorbar(binsN, vxTTCF[index], vxTTCFse[index], linestyle="", marker="o", markersize=1, capsize=2, capthick=0.5, ecolor="skyblue", elinewidth=0.5, color="dodgerblue", label="TTCF")
        if not(onlyTTCF):
            # ax.plot(binsN, np.mean(vxDAV, axis=0), color="crimson", label="DAV")
            if average:
                ax.errorbar(binsN, avDAV, seDAV, linestyle="", marker="o", markersize=1, capsize=2, capthick=0.5, ecolor="lightcoral", elinewidth=0.5, color="crimson", label="DAV")
            else:
                ax.errorbar(binsN, vxDAV[index], vxDAVse[index], linestyle="", marker="o", markersize=1, capsize=2, capthick=0.5, ecolor="lightcoral", elinewidth=0.5, color="crimson", label="DAV")
        if theoreticalProfiles:
            ax.plot(binsN, shearRate*np.linspace(0, L, len(binsN)), color="black")
        ax.tick_params(axis="both", which="major", labelsize=14)
        # ax.yaxis.set_major_formatter(ticker.NullFormatter())
        ax.legend(fontsize=14)

        if not(onlyTTCF):
            for j in printFormat:
                if average:
                    fig.savefig(folders[i]+"/vx."+j, dpi=300)
                else:
                    fig.savefig(folders[i]+"/vx_"+str(index)+"."+j, dpi=300)
        else:
            for j in printFormat:
                if average:
                    fig.savefig(folders[i]+"/vx_ttcf."+j, dpi=300)
                else:
                    fig.savefig(folders[i]+"/vx_ttcf_"+str(index)+"."+j, dpi=300)
        plt.cla()

        if timeResponse:
            bin1 = int(0.15*len(vxTTCF[0]))
            bin2 = int(0.5*len(vxTTCF[0]))
            bin3 = int(0.9*len(vxTTCF[0]))
            v1_TTCF = np.transpose(vxTTCF)[bin1]
            v2_TTCF = np.transpose(vxTTCF)[bin2]
            v3_TTCF = np.transpose(vxTTCF)[bin3]
            v1_TTCFse = np.transpose(vxTTCFse)[bin1]
            v2_TTCFse = np.transpose(vxTTCFse)[bin2]
            v3_TTCFse = np.transpose(vxTTCFse)[bin3]
            if not(onlyTTCF):
                v1_DAV = np.transpose(vxDAV)[bin1]
                v2_DAV = np.transpose(vxDAV)[bin2]
                v3_DAV = np.transpose(vxDAV)[bin3]
                v1_DAVse = np.transpose(vxDAVse)[bin1]
                v2_DAVse = np.transpose(vxDAVse)[bin2]
                v3_DAVse = np.transpose(vxDAVse)[bin3]
            time = list(np.linspace(0, delay*timestep*len(v1_TTCF), len(v1_TTCF)))

            fig1 = plt.figure(figsize=(10*centimeters, 10*centimeters), constrained_layout=True)
            gs = fig1.add_gridspec(1, 1)
            ax = fig1.add_subplot(gs[0, 0])
            ax.set_xlabel(r"Time", fontsize=16)
            ax.set_ylabel(r"$v_{x}$, DPD units", fontsize=16)
            # ax.plot(time, v1_TTCF, color="dodgerblue", label="TTCF - bin {}".format(bin1+1))
            # ax.plot(time, v2_TTCF, color="steelblue", label="TTCF - bin {}".format(bin2+1))
            # ax.plot(time, v3_TTCF, color="royalblue", label="TTCF - bin {}".format(bin3+1))
            ax.errorbar(time, v1_TTCF, v1_TTCFse, linestyle="", marker="o", markersize=1, capsize=2, capthick=0.5, elinewidth=0.5, color="dodgerblue", ecolor="skyblue", label="TTCF - bin {}".format(bin1+1))
            ax.errorbar(time, v2_TTCF, v2_TTCFse, linestyle="", marker="o", markersize=1, capsize=2, capthick=0.5, elinewidth=0.5, color="steelblue", ecolor="lightsteelblue", label="TTCF - bin {}".format(bin2+1))
            ax.errorbar(time, v3_TTCF, v3_TTCFse, linestyle="", marker="o", markersize=1, capsize=2, capthick=0.5, elinewidth=0.5, color="royalblue", ecolor="cornflowerblue", label="TTCF - bin {}".format(bin3+1))
            if not(onlyTTCF):
                # ax.plot(time, v1_DAV, color="crimson", label="DAV - bin {}".format(bin1+1))
                # ax.plot(time, v2_DAV, color="firebrick", label="DAV - bin {}".format(bin2+1))
                # ax.plot(time, v3_DAV, color="indianred", label="DAV - bin {}".format(bin3+1))
                ax.errorbar(time, v1_DAV, v1_DAVse, linestyle="", marker="o", markersize=1, capsize=2, capthick=0.5, elinewidth=0.5, color="crimson", ecolor="lightcoral", label="DAV - bin {}".format(bin1+1))
                ax.errorbar(time, v2_DAV, v2_DAVse, linestyle="", marker="o", markersize=1, capsize=2, capthick=0.5, elinewidth=0.5, color="firebrick", ecolor="lightsalmon", label="DAV - bin {}".format(bin2+1))
                ax.errorbar(time, v3_DAV, v3_DAVse, linestyle="", marker="o", markersize=1, capsize=2, capthick=0.5, elinewidth=0.5, color="indianred", ecolor="pink", label="DAV - bin {}".format(bin3+1))
            if theoreticalProfiles:
                ax.plot(time, shearRate*L*(bin1+0.5)/len(vxTTCF[0])*np.ones(len(time)), color="black")
                ax.plot(time, shearRate*L*(bin2+0.5)/len(vxTTCF[0])*np.ones(len(time)), color="black")
                ax.plot(time, shearRate*L*(bin3+0.5)/len(vxTTCF[0])*np.ones(len(time)), color="black")
            ax.tick_params(axis="both", which="major", labelsize=14)
            # ax.yaxis.set_major_formatter(ticker.NullFormatter())
            ax.legend(fontsize=14)

            if not(onlyTTCF):
                for j in printFormat:
                    fig1.savefig(folders[i]+"/vx_time."+j, dpi=300)
            else:
                for j in printFormat:
                    fig1.savefig(folders[i]+"/vx_ttcf_time."+j, dpi=300)

            plt.cla()

    plt.close('all')





if __name__ == "__main__":
    plotTimeResponsePxy(folders, onlyTTCF=True)
    plotTimeResponsePxy(folders)
    plotTimeResponsePxy(folders, onlyTTCF=True, se=False)
    plotTimeResponsePxy(folders, se=False)
    plotVelocity(folders, onlyTTCF=True, theoreticalProfiles=True)
    plotVelocity(folders, theoreticalProfiles=True)
    plotVelocity(folders, onlyTTCF=True, theoreticalProfiles=True, average=False)
    plotVelocity(folders, theoreticalProfiles=True, average=False)
    plotVelocity(folders, onlyTTCF=True, theoreticalProfiles=True, average=False, index=0)
    plotVelocity(folders, theoreticalProfiles=True, average=False, index=0)
    plotPxyProfile(folders, onlyTTCF=True)
    plotPxyProfile(folders)
