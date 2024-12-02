import numpy as np
import matplotlib.pyplot as plt
import subprocess

saveFormat = 'png'
filename = 'timeCorr.txt'
nFreq = 200
nRep = 200

time = []
pxy = []

with open(filename) as f:
    next(f)
    next(f)
    next(f)
    info = str(f.readline())
    info = info.strip().split()
    n = int(info[1])

with open('tmp.dat', 'w') as fw:
    subprocess.call(['tail', '-n', str(n), filename], stdout=fw)

with open('tmp.dat') as f:
    for line in f:
        line = line.strip().split()
        time.append(0.01*float(line[1]))
        pxy.append(float(line[3]))

subprocess.run(['rm', 'tmp.dat'])

# Plot
plt.rcParams.update({
	"text.usetex": True,
	"font.family": "serif",
	#"font.sanserif": "Helvetica"
})

centimeters = 1/2.54
fig = plt.figure(figsize=(10*centimeters, 10*centimeters), constrained_layout=True)
gs = fig.add_gridspec(1, 1)

ax = fig.add_subplot(gs[0, 0])
ax.set_xlabel(r'Time, $(-)$', fontsize=16)
ax.set_ylabel(r'$\langle P_{xy}P_{xy}\rangle,\ (-)$', fontsize=16)
ax.plot(time, np.zeros(len(time)), color='black')
ax.plot(time, pxy, linewidth=0.5, marker='o', markersize=2, color='skyblue')

fig.savefig('autoCorrPxy.' + saveFormat, dpi=300)

