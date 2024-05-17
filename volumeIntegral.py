import subprocess
import re
import numpy as np

newtonian = True
nu = 6.195e-4
rho = 1025
mu =  nu*rho
RPM = []
N = [x/60 for x in RPM]
omega = [x/60*2*np.pi for x in RPM]
T = 0.230
D = T/3
Re = [rho*x*D**2/mu for x in N]

# Read the list of folders in which are OpenFOAM case direcories
foldToCheck = []
foldCount = 0
for dir in foldToCheck:
    sr = []
    volumes = []

    lsOut = subprocess.check_output(["ls", dir], text=True)
    foldList = list(str(lsOut).split("\n"))
    
    # Identify the last iteration folder
    s = []
    for _ in range(len(foldList)):
        if re.findall("\d+$", foldList[_]):
            val = re.findall("\d+$", foldList[_])
            s.append(int(val[0]))
    
    cellVolumesFile = dir + "/" + str(max(s)) + "/V"
    strainRateFile = dir + "/" + str(max(s)) + "/strainRate"
    viscosityFile = dir + "/" + str(max(s)) + "/nu"
    
    
    nCellPos = 21 # Line in the file that contains the number of cells in the mesh (starting from 1)
    
    with open(strainRateFile) as f:
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
    if newtonian:
        for _ in range(len(sr)):
            volumeIntegral += nu*sr[_]**2*volumes[_]
    else:
        nu = []

        with open(viscosityFile) as f:
            for s in range(0,nCellPos-1):
                next(f)
            nCells = int(f.readline().strip())
            next(f)
            for i, line in enumerate(f):
                if i >= 0 and i < nCells:
                    line = line.strip()
                    nu.append(float(line))

        for _ in range(len(sr)):
            volumeIntegral += nu[_]*sr[_]**2*volumes[_]
    
    power = rho*volumeIntegral
    powerNumber = volumeIntegral/(N[foldCount]**3*D**5)
    
    print("###############################")
    print("folder: " + dir)
    print("The value of the volume integral for the laminar dissipation rate is: {}".format(volumeIntegral))
    print("The power calculated with it is: {}".format(power))
    print("The power number calculated with it is: {}".format(powerNumber))
    print("###############################")
    foldCount += 1
