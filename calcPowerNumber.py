import matplotlib
import numpy as np
import matplotlib.pyplot as plt
#matplotlib.use('Agg')

## polymer
rho = 1000
D = 0.076667
RPM = [100]
# omega = [5.236]
# Mz = [+7.037482e-02+4.528103e-02]
# Mz = [+6.963997e-03+4.473137e-03]
# Mz = [7.95237311e-08+1.95467868e-03] # F1 P50M_50RPM_Re11
# Mz = [-1.41441424e-03-5.76013734e-04] # F2  P50M_50RPM_Re11
# Mz = [4.87608318e-06+8.11803750e-02] # F1  P40_450RPM_Re350
# Mz = [-7.79055668e-02-2.85337142e-03] # F2  P40_450RPM_Re350
Mz = [5.03480282e-06+2.76849338e-03] # F1  Wat_100RPM_Re9775
# Mz = [-4.03922580e-03-1.70366663e-05] # F2  Wat_100RPM_Re9775
# nu = 0.04944913129310344
# nu = 0.00489
# nu = 4.312e-4
nu = 1e-6
mu = nu*rho
# Mz = [0.0202]
# mu = 10
## Ambrasthesis
# rho = 1000
# omega = [0.0013, 0.006, 0.01265, 0.067692, 0.255213, 0.962315, 3.627706, 13.67426, 51.55289, 194.5992]
# Mz = [1.41e-9, 6.66e-9, 1.47e-8, 2e-7, 2.78e-6, 4.39e-5, 6.76e-4, 9.49e-3, 1.38e-1, 2.01]
# D = 0.076667
# # mu = 0.684458387
# mu = 1e-3

omega = []
for i in range(len(RPM)):
	omega.append(RPM[i]/60*2*np.pi)

N = []
for i in range(len(omega)):
	N.append(omega[i]/(2*np.pi))

# RPM = []
# for i in range(len(omega)):
# 	RPM.append(N[i]*60)

Re = []
for i in range(len(omega)):
	Re.append(rho*N[i]*D**2/mu)

P = []
for i in range(len(omega)):
	P.append(omega[i]*Mz[i])

Np = []
for i in range(len(P)):
	Np.append(P[i]/(rho*N[i]**3*D**5))

print("\nRPM = {}".format(RPM))
print("\nN = {}".format(N))
print("\nRe = {}".format(Re))
print("\nPower (W) = {}".format(P))
print("\nNp = {}".format(Np))
