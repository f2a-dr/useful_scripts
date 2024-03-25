import numpy as np

# Parameters
numberOfBins = 10
inputFile = "inputfile.txt"
weightFile = "weightFile.txt"
# Number of line from which the data start in the files
nDataPos = 1

# Function which identify the bin in which a certain value falls
def findBin(val, bins):
    """
    :param val: value of which we want to identify the bin
    :param bins: numpy array which contains the values of the bins' edges
    """
    lower = 0
    upper = len(bins)
    if val in bins:
        rightBin = np.where(bins == val)[0][0]-1
    else:
        while upper - lower != 1:
            halfLow = int(np.floor((upper-lower)/2+lower))
            if val > bins[halfLow]:
                lower = halfLow
            else:
                upper = halfLow
        rightBin = lower

    return rightBin


# Reading input files
with open(inputFile) as f:
    for linesToSkip in range(0, nDataPos-1):
        next(f)
    nCells = int(f.readline().strip())
    next(f)
    for __, line in enumerate(f):
        if __ >= 0 and __ < nCells:
            line = line.strip()
            sr.append(float(line))

with open(weightFile) as f:
    for linesToSkip in range(0, nDataPos-1):
        next(f)
    nCells = int(f.readline().strip())
    next(f)
    for __, line in enumerate(f):
        if __ >= 0 and __ < nCells:
            line = line.strip()
            volumes.append(float(line))


# Plotting the results
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    #"font.sanserif": "Helvetica"
})

centimeters = 1/2.54
fig = plt.figure(figsize=(10*centimeters,20*centimeters),constrained_layout=True)
gs = fig.add_gridspec(2, 1)

ax1 = fig.add_subplot(gs[0, 0])
ax1.set_xlabel(r"Data",fontsize=16)
ax1.set_ylabel(r"Wieghts",fontsize=16)
ax1.tick_params(axis="both",which="both",labelsize=11)
ax1.bar(bins, pdf, align="edge", width=((max(sr)-min(sr))/numberOfBins))
plt.legend()


#plt.show()
fig.savefig("pdf.pdf", dpi=300)
