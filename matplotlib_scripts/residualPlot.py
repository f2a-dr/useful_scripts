import matplotlib
import numpy as np
#from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
#matplotlib.use('Agg')

# Constant parameter definitions

pStep_0 = [] 
pRes_0 = []
pStep_1 = [] 
pRes_1 = []
pStep_2 = [] 
pRes_2 = []
pStep_3 = [] 
pRes_3 = []
pStep_4 = [] 
pRes_4 = []
pStep_5 = [] 
pRes_5 = []

UxStep = []
UxRes = []
UyStep = []
UyRes = []
UzStep = []
UzRes = []

# Results file reading
with open('logs/p_0') as f:
	next(f)
	for line in f:
		line = line.strip()
		line = line.split()
		pStep_0.append(float(line[0]))
		pRes_0.append(float(line[1]))

with open('logs/p_1') as f:
	next(f)
	for line in f:
		line = line.strip()
		line = line.split()
		pStep_1.append(float(line[0]))
		pRes_1.append(float(line[1]))

with open('logs/p_2') as f:
	next(f)
	for line in f:
		line = line.strip()
		line = line.split()
		pStep_2.append(float(line[0]))
		pRes_2.append(float(line[1]))

#with open('logs/p_3') as f:
#	next(f)
#	for line in f:
#		line = line.strip()
#		line = line.split()
#		pStep_3.append(float(line[0]))
#		pRes_3.append(float(line[1]))
#
#with open('logs/p_4') as f:
#	next(f)
#	for line in f:
#		line = line.strip()
#		line = line.split()
#		pStep_4.append(float(line[0]))
#		pRes_4.append(float(line[1]))
#
#with open('logs/p_5') as f:
#	next(f)
#	for line in f:
#		line = line.strip()
#		line = line.split()
#		pStep_5.append(float(line[0]))
#		pRes_5.append(float(line[1]))

with open('logs/Ux_0') as f:
	next(f)
	for line in f:
		line = line.strip()
		line = line.split()
		UxStep.append(float(line[0]))
		UxRes.append(float(line[1]))

with open('logs/Uy_0') as f:
	next(f)
	for line in f:
		line = line.strip()
		line = line.split()
		UyStep.append(float(line[0]))
		UyRes.append(float(line[1]))

with open('logs/Uz_0') as f:
	next(f)
	for line in f:
		line = line.strip()
		line = line.split()
		UzStep.append(float(line[0]))
		UzRes.append(float(line[1]))

fig1 = plt.figure(figsize=(6,6),constrained_layout=True)
gs1 = fig1.add_gridspec(1,1)

ax1 = fig1.add_subplot(gs1[0,0])
ax1.set_title(r"Pressure initial residuals")
ax1.set_xlabel(r"Step", fontsize=12)
ax1.set_ylabel(r"Residuals", fontsize=12)
#ax1.set_xscale("log")
ax1.set_yscale("log")
#ax1.set_ylim(bottom=4.2,top=4.7)
ax1.plot(pStep_0, pRes_0, color="tab:blue", label=r"$p_0$")
ax1.plot(pStep_1, pRes_1, color="tab:green", label=r"$p_1$")
ax1.plot(pStep_2, pRes_2, color="tab:purple", label=r"$p_2$")
#ax1.plot(pStep_3, pRes_3, color="tab:brown", label=r"$p_3$")
#ax1.plot(pStep_4, pRes_4, color="tab:olive", label=r"$p_4$")
#ax1.plot(pStep_5, pRes_5, color="tab:red", label=r"$p_5$")
ax1.grid(visible=True,which='major')
ax1.grid(visible=True,which='minor',linestyle=':')
ax1.legend(fontsize=12)

fig2 = plt.figure(figsize=(6,6),constrained_layout=True)
gs2 = fig2.add_gridspec(1,1)

ax1 = fig2.add_subplot(gs2[0,0])
ax1.set_title(r"Velocity initial residuals")
ax1.set_xlabel(r"Step", fontsize=12)
ax1.set_ylabel(r"Residuals", fontsize=12)
#ax1.set_xscale("log")
ax1.set_yscale("log")
#ax1.set_ylim(bottom=4.2,top=4.7)
ax1.plot(UxStep, UxRes, color="tab:blue", label=r"$U_x$")
ax1.plot(UyStep, UyRes, color="tab:green", label=r"$U_y$")
ax1.plot(UzStep, UzRes, color="tab:red", label=r"$U_z$")
ax1.grid(visible=True,which='major')
ax1.grid(visible=True,which='minor',linestyle=':')
ax1.legend(fontsize=12)

plt.show()
#fig1.savefig('resPressure.pdf', format='pdf')
#fig2.savefig('resVelocities.pdf', format='pdf')
