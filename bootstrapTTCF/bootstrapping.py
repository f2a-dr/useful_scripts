import numpy as np
from scipy.stats import bootstrap
import matplotlib.pyplot as plt

resamples = 10000

def resample(array, nResamples):
    batches = []
    arrayShape = list(array.shape)
    arrayShape.insert(0, nResamples)
    arrayShape = tuple(arrayShape)
    batches = np.zeros(arrayShape)
    for i in range(nResamples):
        newSample = np.random.randint(array.shape[-1], size=(array.shape[-1]))
        batches[i] = array[:,newSample]
    return batches

# def bootstrapping(original):
#     btsp = []
#     for i in range(len(original)):
#         btsp.append(original[np.random.randint(len(original))])
#     return np.array(btsp)

if __name__ == '__main__':
    
    original = []
    with open('body_fat.csv') as f:
        next(f)
        for line in f:
            line = line.strip()
            original.append(float(line))
    
    bsMean = []
    for i in range(resamples):
        bsMean.append(np.mean(bootstrapping(original)))
    
    meanCounts, meanBins = np.histogram(bsMean, bins=100)
    
    srtMean = np.sort(np.array(bsMean))
    ciLow = int(0.025*resamples)
    ciHigh = int(0.975*resamples)
    cLow = np.percentile(bsMean, 2.5)
    cHigh = np.percentile(bsMean, 97.5)
    original = np.array(original)
    # first = bootstrapping(original)
    # print(original)
    # print(first)
    original = (original,)
    
    res = bootstrap(original, np.mean, confidence_level=0.95, n_resamples=resamples)
    print(res.confidence_interval)
    print('95% Confidence interval = ({:.3f}, {:.3f})'.format(srtMean[ciLow], srtMean[ciHigh]))
    print('95% Confidence interval = ({:.3f}, {:.3f})'.format(cLow, cHigh))
    
    centimeters = 1/2.54
    fig = plt.figure(figsize=(10*centimeters, 10*centimeters), constrained_layout=True)
    gs = fig.add_gridspec(1, 1)
    
    ax = fig.add_subplot(gs[0, 0])
    ax.hist(res.bootstrap_distribution, bins=100, color='deepskyblue', alpha=.5, label='scipy')
    # ax.hist(bsMean, bins=100, color='deepskyblue', alpha=.5, label='scipy')
    # ax.hist(original, bins=25, color='deepskyblue')
    ax.bar(meanBins[:-1], meanCounts, width=(max(meanBins)-min(meanBins))/len(meanCounts), align='edge', color='tomato', alpha=.5, label='in house')
    # ax.hist(bsMean, bins=100, color='tomato', alpha=.5)
    ax.vlines(srtMean[ciLow], 0, 500, colors='black')
    ax.vlines(srtMean[ciHigh], 0, 500, colors='black')
    ax.set_xlabel('mean')
    ax.set_ylabel('frequency')
    ax.legend(edgecolor='black')
    
    fig.savefig('pdf.png', dpi=300)
