# Script to convert .csv from PIV in a .csv format easier to read in Paraview.
# It also shifts the axial values by the originShift values, since in the PIV
# data the center of the axis is positioned in the center of the Rushton 
# Turbine.
# Moreover, it generates the probes to sample the velocity values from the CFD
# simulations.

import numpy as np

# Variables definition

filename = "test.csv"
dictFile = "probes"
newFile = "new" + filename
turbineRadius = 0.23/6
clearance = 0.101
originShift = clearance + 0.23/3*0.04/2
angleDiscr = 6
originShift = 0

x = []
y = []
z = []
xProbe = np.array([])
yProbe = np.array([])
zProbe = np.array([])
V = []
U = []
W = []

# Reading initial csv

print("Reading initial csv...")
with open(filename) as f:
    next(f)
    for line in f:
        line = line.strip()
        line = line.split(";")
        x.append(float(line[0])/1000)
        y.append(float("0"))
        z.append(float(line[1])/1000 + originShift)
        U.append(float(line[2]))
        W.append(float(line[3]))
        V.append(float(line[4]))
print("Initial csv read.")

# Writing new csv
print("Remove points with coordinates out of the CFD domain...")
newX = []
newY = []
newZ = []
newU = []
newV = []
newW = []
for i in range(len(x)):
    # if (not(z[i] > 0.201) and not(((z[i] >= clearance) or (z[i] <= (clearance + turbineRadius*0.04))) and (np.abs(x[i]) <= turbineRadius))):
    newX.append(x[i])
    newY.append(y[i])
    newZ.append(z[i])
    newU.append(U[i])
    newV.append(V[i])
    newW.append(W[i])

print("Writing new csv file...")
with open(newFile, "w") as f:
    f.write("x_m,y_m,z_m,U,V,W\n")
    for i in range(len(newX)):
        f.write(str(round(newX[i], 10))+","+str(round(newY[i], 10))+","+str(round(newZ[i], 10))+","+
                str(round(newU[i], 10))+","+str(round(newV[i], 10))+","+str(round(newW[i], 10))+"\n")
print("New csv file written.")

# Generate probes

print("Calculating probes coordinates...")
angles = np.linspace(0, 2*np.pi, angleDiscr, endpoint=False)

newX = np.array(newX)
newY = np.array(newY)
newZ = np.array(newZ)

for i in range(len(angles)):
    xProbe = np.append(xProbe, newX*np.cos(angles[i]))
    yProbe = np.append(yProbe, newX*np.sin(angles[i]))
    zProbe = np.append(zProbe, newZ)
print("Probes coordinates calculated.")

# Writing dictionary file

print("Writing probes dictionary file...")
with open(dictFile, "w") as f:
    f.write("""/*--------------------------------*- C++ -*----------------------------------*\\
  =========                 |
  \\\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\\\    /   O peration     | Website:  https://openfoam.org
    \\\\  /    A nd           | Version:  8
     \\\\/     M anipulation  |
-------------------------------------------------------------------------------
Description
    Writes out values of fields from cells nearest to specified locations.

\\*---------------------------------------------------------------------------*/

#includeEtc "caseDicts/postProcessing/probes/probes.cfg"

includeOutOfBounds true;

fields (U);
probeLocations
(
""")
    for i in range(len(xProbe)):
        f.write("(" + str(round(xProbe[i], 8)) + " " + str(round(yProbe[i], 8)) + " " + str(round(zProbe[i], 8)) + ")" + "\n")
    f.write(""");

// ************************************************************************* //""")
print("Probes dictionary file written.")
