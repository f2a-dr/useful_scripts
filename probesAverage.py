# This script reads an OpenFOAM probes file (which contains also the probes
# location) for a stirred tank and makes an average after transforming all the
# velocity values from cartesian to cylindrical coordinates.

import subprocess
import re
import numpy as np

# Identify the latest time

# dir = "."
# lsOut = subprocess.check_output(["ls", dir], text=True)
# foldList = list(str(lsOut).split("\n"))
# s = []
# for _ in range(len(foldList)):
#     if re.findall("\d+$", foldList[_]):
#         val = re.findall("\d+$", foldList[_])
#         s.append(int(val[0]))
# s.pop(0)

# Variables definition

# lsComm = subprocess.Popen(("ls",  "."), stdout=subprocess.PIPE)
# print(lsComm)
lsComm = subprocess.check_output(("ls",  "."), text=True)
lsComm = lsComm.split()
for i in range(len(lsComm)):
    if lsComm[i].startswith("new"):
        csvFile = lsComm[i]
# csvFile = subprocess.check_output(("grep",  "-E", lsComm), stdin=lsComm.stdout, text=True)
# probesFile = "postProcessing/probes/" + str(max(s)) + "/U"
probesFile = './U'
cfdCsv = 'cfd.csv'
fullCsv = 'probes.csv'

# Reading probes file

print("Reading probes file...")
nProbes = subprocess.run(['grep -E "Probe" U | tail -n 1 | grep -Eo " [1-9]+ "'], shell=True, text=True, capture_output=True)
nProbes = int(nProbes.stdout.strip()) + 1

x = []
y = []
z = []
Ux = []
Uy = []
Uz = []

with open(probesFile) as f:
    for i in range(nProbes):
        line = f.readline().split("(")[1]
        line = line.split()
        line[-1] = line[-1][0:-1]
        x.append(float(line[0]))
        y.append(float(line[1]))
        z.append(float(line[2]))
    next(f)
    line = f.readline().split(") (")
    line[0] = line[0].split("(")[1]
    line[-1] = line[-1].strip()[0:-1]
    for j in range(len(line)):
        line[j] = line[j].split()
        Ux.append(float(line[j][0]))
        Uy.append(float(line[j][1]))
        Uz.append(float(line[j][2]))
print("Positions and velocities read from probes file.")

# Transform velocity from cartesian to cylindrical coordinates

print("Transform velocities in cylindrical coordinates...")
Ur = []
Utheta = []
for i in range(len(x)):
    if (x[i] >= 0) and (y[i] >= 0):
        phi = np.arccos(x[i])
    elif (x[i] < 0) and (y[i] >= 0):
        phi = np.arccos(x[i])
    elif (x[i] <= 0) and (y[i] < 0):
        phi = np.pi - np.arcsin(y[i])
    elif (x[i] > 0) and (y[i] < 0):
        phi = 2*np.pi - np.arccos(x[i])
    # phi = np.arctan(y[i]/x[i])
    Ur.append(Ux[i]*np.cos(phi)+Uy[i]*np.sin(phi))
    Utheta.append(-Ux[i]*np.sin(phi)+Uy[i]*np.cos(phi))
print("Coordinates transform completed.")

# Average the velocity values

print("Calculate the radial and axial coordinates of the probe's grid...")
R = [np.round(np.sqrt(x[i]**2 + y[i]**2), 5) for i in range(len(x))]
singleR = list(set(R))
singleR.sort()
singleZ = list(set(z))
singleZ.sort()
print("Grid coordinates calculated.")

gridU = [[] for i in range(len(singleR)*len(singleZ))]
gridV = [[] for i in range(len(singleR)*len(singleZ))]
gridW = [[] for i in range(len(singleR)*len(singleZ))]

print("Identify points on the same circonferences...")
for i in range(len(x)):
    indexZ = singleZ.index(z[i])
    tempR = np.round(np.sqrt(x[i]**2 + y[i]**2), 5)
    indexR = singleR.index(tempR)
    indexGrid = indexR*len(singleZ) + indexZ
    gridU[indexGrid].append(Ur[i])
    gridV[indexGrid].append(Utheta[i])
    gridW[indexGrid].append(Uz[i])
print("Point identified.")

print("Averaging the velocity values of the various probes...")
gridU = np.array(gridU)
gridV = np.array(gridV)
gridW = np.array(gridW)
toPrintU = np.mean(gridU, axis=1)
toPrintV = np.mean(gridV, axis=1)
toPrintW = np.mean(gridW, axis=1)
print("Velocity values averaged.")

print("Writing csv file with results...")
with open(cfdCsv, "w") as f:
    f.write("x_m,y_m,z_m,U,V,W\n")
    for i in range(len(toPrintU)):
        iR = int(i/len(singleZ))
        iZ = i - iR*len(singleZ)
        f.write("{:.10f},".format(singleR[iR])+"0.0,"+"{:.10f},".format(singleZ[iZ])+
            "{:.10f},".format(toPrintU[i])+"{:.10f},".format(toPrintV[i])+"{:.10f}".format(toPrintW[i])+"\n")
print("Csv file written.")

print("Write csv file with all the probes...")
with open(fullCsv, "w") as f:
    f.write("x_m,y_m,z_m,U,V,W\n")
    for i in range(len(x)):
        f.write("{:.10f},".format(x[i])+"{:.10f},".format(y[i])+"{:.10f},".format(z[i])+
            "{:.10f},".format(Ux[i])+"{:.10f},".format(Uy[i])+"{:.10f}".format(Uz[i])+"\n")
print("Full csv written.")

print("Process completed.")


