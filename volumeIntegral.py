

cellVolumesFile = "10000/V"
variableToIntegrateFile = "10000/strainRate"

mu =  0.442
rho = 1025
nu = mu/rho
sr = []
volumes = []

nCellPos = 21 # Line in the file that contains the number of cells in the mesh (starting from 1)

with open(variableToIntegrateFile) as f:
    for s in range(0,nCellPos-1):
        next(f)
    nCells = int(f.readline().strip())
    next(f)
    for i, line in enumerate(f):
        if i >= 0 and i < nCells:
            line = line.strip()
            sr.append(float(line))

with open(cellVolumesFile) as f:
    for s in range(0,nCellPos-1):
        next(f)
    nCells = int(f.readline().strip())
    next(f)
    for i, line in enumerate(f):
        if i >= 0 and i < nCells:
            line = line.strip()
            volumes.append(float(line))

V = sum(volumes)
volumeIntegral = 0
for i in range(len(sr)):
    volumeIntegral += nu*sr[i]**2*volumes[i]

power = rho*V*volumeIntegral

print("The value of the volume integral for the laminar dissipation rate is: {}".format(volumeIntegral))
print("The power calculated with it is: {}".format(power))
