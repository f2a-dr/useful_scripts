# Script to generate a `sampleDict` OpenFOAM dictionary, which contains the
# desired amount of planes to sample the velocity field.
# This samples can then be averaged to compare the spatial azimuthal average
# with an experimental temporal average.

import numpy as np

filename = "sampleDict1"
T = 0.23
R = 2*T/3
surfN = 108
angles = np.linspace(0, np.pi, surfN)
basePointX = R*np.cos(angles)
basePointY = R*np.sin(angles)
basePointZ = 0
normalsX = -np.sin(angles)
normalsY = np.cos(angles)
normalsZ = 0

header = """/*--------------------------------*- C++ -*----------------------------------*\\
  =========                 |
  \\\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\\\    /   O peration     | Website:  https://openfoam.org
    \\\\  /    A nd           | Version:  8
     \\\\/     M anipulation  |
\\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    location    "system";
    object      sampleDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

type                surfaces;

surfaceFormat       vtk;

interpolationScheme cellPointFace;

fields
(
    U
);

surfaces
(
"""

with open(filename, "w") as f:
    f.write(header)

with open(filename, "a") as f:
    for i in range(len(angles)):
        f.write("    surf"+str(i) + "\n")
        f.write("    {" + "\n")
        f.write("        type      plane;" + "\n")
        f.write("        planeType pointAndNormal;" + "\n")
        f.write("        pointAndNormalDict" + "\n")
        f.write("        {" + "\n")
        f.write("            basePoint        (" + str(basePointX[i]) + " " + str(basePointY[i]) + " " + str(basePointZ) + ");" + "\n")
        f.write("            normalVector     (" + str(normalsX[i]) + " " + str(normalsY[i]) + " " + str(normalsZ) + ");" + "\n")
        f.write("            interpolate      true;" + "\n")
        f.write("            triangulate      true;" + "\n")
        f.write("        }" + "\n")
        f.write("    }" + "\n")
    f.write(");" + "\n")
    f.write("\n\n// ************************************************************************* //")


