# Script to convert .csv from PIV in a .csv format easier to read in Paraview


filename = ""
newFile = "new" + filename

x = []
y = []
z = []
V = []
U = []
W = []

with open(filename) as f:
    next(f)
    for line in f:
        line = line.strip()
        line = line.split(";")
        x.append(float(line[0])/1000)
        y.append(float("0"))
        z.append(float(line[1])/1000)
        V.append(float(line[2]))
        U.append(float(line[3]))
        W.append(float(line[4]))

with open(newFile, "w") as f:
    f.write("x_m,y_m,z_m,U,V,W\n")
    for i in range(len(x)):
        f.write(str(x[i])+","+str(y[i])+","+str(z[i])+","+
                str(U[i])+","+str(V[i])+","+str(W[i])+"\n")
