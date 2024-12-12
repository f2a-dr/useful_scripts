import numpy as np
import bootstrapping as bts
import matplotlib.pyplot as plt
import warnings

# Variables: Omega, B, Omega*B
nTrajectories = 10000
nGroups = 100
nTimesteps = 10
nResamples = 10000

if nTrajectories % nGroups != 0:
    raise Exception('The number of nGroups must be a multiple of the number of the nTrajectories')
if (0.005*nResamples) % 1 != 0:
    warnings.warn('It would be better to use a number of resamples that is a mutiple of 200')
o = np.zeros((nTimesteps, nGroups, int(nTrajectories/nGroups)))
b = np.zeros((nTimesteps, nGroups, int(nTrajectories/nGroups)))
ob = np.zeros((nTimesteps, nGroups, int(nTrajectories/nGroups)))
for i in range(nTimesteps):
    o[i] = np.random.normal(loc=5e-3*nTimesteps-i, scale=3e-1*(nTimesteps-i), size=(nGroups, int(nTrajectories/nGroups)))
    b[i] = np.random.normal(loc=0.005*nTimesteps-i, scale=0.1*(nTimesteps-i), size=(nGroups, int(nTrajectories/nGroups)))
    ob[i] = np.random.normal(loc=1*nTimesteps-i, scale=0.2*(nTimesteps-i), size=(nGroups, int(nTrajectories/nGroups)))

# print(o)

# print(np.mean(o[0, 0]))

# Perform the AVERAGE WITHIN
oaw = np.mean(o, axis=-1)
baw = np.mean(b, axis=-1)
obaw = np.mean(ob, axis=-1)
# oaw = np.array([])
# baw = np.array([])
# obaw = np.array([])
# for i in range(nTimesteps):
#     for j in range(nGroups):
#         oaw = np.append(oaw, np.mean(o[i, j]))
#         baw = np.append(baw, np.mean(o[i, j]))
#         obaw = np.append(obaw, np.mean(o[i, j]))

# oaw = oaw.reshape(nTimesteps, nGroups)
# baw = baw.reshape(nTimesteps, nGroups)
# obaw = obaw.reshape(nTimesteps, nGroups)
# print('Here the average within for Omega')
# print(oaw)

oBatches = bts.resample(oaw, nResamples)
bBatches = bts.resample(baw, nResamples)
obBatches = bts.resample(obaw, nResamples)
# print('Here the batches for Omega')
# print(oBatches)

# Perform the AVERAGE BETWEEN
oab = np.mean(oBatches, axis=-1).T
bab = np.mean(bBatches, axis=-1).T
obab = np.mean(obBatches, axis=-1).T
print('Here the average between for Omega')
print(oab)

# Sum to obtain B(t)
bt = obab - oab*bab

# Compute confidence interval
lowPercentile = int(0.025*nResamples)
highPercentile = int(0.975*nResamples)
lowCI = []
highCI = []
for i in range(nTimesteps):
    sortedBt = np.sort(bt[i])
    lowCI.append(sortedBt[lowPercentile])
    highCI.append(sortedBt[highPercentile])

confidenceInterval = np.array([lowCI, highCI]).T
print(confidenceInterval)

# Print <B(t)> distribution
meanCounts = []
meanBins = []
for i in range(nTimesteps):
    mC, mB = np.histogram(bt[i], bins=200)
    meanCounts.append(mC)
    meanBins.append(mB)


cl = ['lightcoral', 'tomato', 'chocolate', 'orange', 'goldenrod', 'yellowgreen', 'limegreen', 'mediumturquoise', 'deepskyblue', 'mediumorchid']
centimeters = 1/2.54
fig = plt.figure(figsize=(20*centimeters, 8*centimeters), constrained_layout=True)
gs = fig.add_gridspec(2, 5)

ax = []
for i in range(nTimesteps):
    if i <= 4:
        ax.append(fig.add_subplot(gs[0, i]))
    else:
        ax.append(fig.add_subplot(gs[1, i-5]))
    # ax.hist(bsMean, bins=100, color='deepskyblue', alpha=.5, label='scipy')
    # ax.hist(original, bins=25, color='deepskyblue')
    ax[i].bar(meanBins[i][:-1], meanCounts[i], width=(max(meanBins[i])-min(meanBins[i]))/len(meanCounts[i]), align='edge', color=cl[i], alpha=.5, label='t = ' + str(i))
    # ax.hist(bsMean, bins=100, color='tomato', alpha=.5)
    ax[i].set_xlabel('mean')
    ax[i].set_ylabel('frequency')
    ax[i].legend(edgecolor='black')

fig.savefig('bootstrapped.png', dpi=300)

