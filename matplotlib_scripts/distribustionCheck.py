### The script works only if the output present in the log.lammps file is copied in a file with name 'nonEqResults.dat'
### in this file the first line should be the header and the columns consider come from
### similar output:
### Step    Temp    c_stat_temp    Press    Pxy    v_visc    f_vave



import matplotlib
import numpy as np
import scipy as sp
from scipy import stats
import matplotlib.pyplot as plt
#matplotlib.use('Agg')

# Constant parameter definitions
printTime = 100			# This variable is how often the result are printed in the log.lammps file
eqTime = 10000			# This variable specify after which timestep you want to start the average and standard deviation calculations
Eq = int(eqTime/printTime)

fullStep = []
fullTemp = []
fullTempCorr = []
fullPress = []
fullStress = [] 
fullVisc = []
fullAveVisc = []

# Results file reading
with open('nonEqResults.dat') as f:
    next(f)
    for line in f:
        line = line.strip()
        line = line.split()
        fullStep.append(float(line[0]))
        fullTemp.append(float(line[1]))
        fullTempCorr.append(float(line[2]))
        fullPress.append(float(line[3]))
        fullStress.append(float(line[4]))
        fullVisc.append(float(line[5]))
        fullAveVisc.append(float(line[6]))

Step = fullStep[Eq+1:]
Temp = fullTemp[Eq+1:]
TempCorr = fullTempCorr[Eq+1:]
Press = fullPress[Eq+1:]
Stress = fullStress[Eq+1:]
Visc = fullVisc[Eq+1:]
AveVisc = fullAveVisc[Eq+1:]

# Cumulative average for viscosity
cumAvVisc = []
sum = 0
for i in range(0,len(fullStep)):
    sum += fullVisc[i]
    cumAvVisc.append(sum/(i+1))


fig4 = plt.figure(figsize=(6,6),constrained_layout=True)
gs4 = fig4.add_gridspec(1,1)

ax1 = fig4.add_subplot(gs4[0,0])
ax1.set_title(r"Viscosity distribution, DPD units")
ax1.set_xlabel(r"$\mu$", fontsize=12)
ax1.set_ylabel(r"PDF", fontsize=12)
plotVisc = np.array(Visc)
viscHist, bins = np.histogram(np.array(plotVisc), bins=100, density=True)
ax1.stairs(viscHist, bins, edgecolor='tab:blue', fill=True, facecolor='dodgerblue')
test = np.linspace(np.min(plotVisc), np.max(plotVisc), 1000)
dist = 1/(np.sqrt(2*np.pi)*np.std(plotVisc))*np.exp(-1/2*((test-np.mean(plotVisc))/np.std(plotVisc))**2)
# dist = np.exp(-1/2*((test-np.mean(Visc))/np.std(Visc))**2)
ax1.plot(test, dist, color='crimson', linewidth=2)
ax1.text(1, 1, "mean = {mean}\nstdv = {stdv}".format(mean=round(np.mean(plotVisc),4), stdv=round(np.std(plotVisc),4)), ha='center', va='center', fontsize=12, bbox=dict(facecolor="dodgerblue", alpha=1), color='white', transform=ax1.transAxes)

plt.show()

p=sp.stats.mstats.normaltest(plotVisc, axis=0).pvalue
if p<0.01:
	print ('distribution is not normal')
else:
	print ('distribution is normal')
p=sp.stats.mstats.normaltest(np.log(plotVisc), axis=0).pvalue
if p<0.01:
	print ('distribution is not log-normal')
else:
	print ('distribution is log-normal')


#fig4.savefig('postprocessing_plots/final_plots/Visc.png', format='png', dpi=600)
#fig4.savefig('postprocessing_plots/final_plots/Visc.pdf', format='pdf')
