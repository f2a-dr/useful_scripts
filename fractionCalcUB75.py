import numpy as np
import matplotlib.pyplot as plt

## Physical and chemical features
# Atoms mass (uma)
c = 12.01
h = 1.01
o = 16
na = 23
s = 32.06
n = 14.01
# Molar mass (g/mol)
waterMM = 2*h+o
sles12MM = c+3*h+11*(c+2*h)+(o+2*c+4*h)+o+s+3*o+na
sles14MM = c+3*h+13*(c+2*h)+(o+2*c+4*h)+o+s+3*o+na
cmea8MM = c+3*h+8*(c+2*h)+c+o+n+h+2*(c+2*h)+o+h
cmea10MM = c+3*h+10*(c+2*h)+c+o+n+h+2*(c+2*h)+o+h
cmea12MM = c+3*h+12*(c+2*h)+c+o+n+h+2*(c+2*h)+o+h
cmea14MM = c+3*h+14*(c+2*h)+c+o+n+h+2*(c+2*h)+o+h
cmea16MM = c+3*h+16*(c+2*h)+c+o+n+h+2*(c+2*h)+o+h
cmea18MM = c+3*h+18*(c+2*h)+c+o+n+h+2*(c+2*h)+o+h

## Blend composition information, mass fractions
# SLES alkyl tail "polydispersity"
sles12_sles = 0.7
sles14_sles = 1-sles12_sles
# CME/A2 alkyl tail "polidispersity"
cmea8_cmea = 0.06
cmea10_cmea = 0.06
cmea12_cmea = 0.50
cmea14_cmea = 0.18
cmea16_cmea = 0.09
cmea18_cmea = 0.11
# Inter ESA 70 composition
sles_esa70 = 0.7
water_esa70 = 1-sles_esa70
# UB75 composition
esa70_ub75 = 0.7034
cmea_ub75 = 0.0750
#esa70_ub75 = 0.6429
#cmea_ub75 = 0.00
water_ub75 = 1-esa70_ub75-cmea_ub75
# Detailed final composition
sles12_wt = sles12_sles*sles_esa70*esa70_ub75
sles14_wt = sles14_sles*sles_esa70*esa70_ub75
cmea8_wt = cmea8_cmea*cmea_ub75
cmea10_wt = cmea10_cmea*cmea_ub75
cmea12_wt = cmea12_cmea*cmea_ub75
cmea14_wt = cmea14_cmea*cmea_ub75
cmea16_wt = cmea16_cmea*cmea_ub75
cmea18_wt = cmea18_cmea*cmea_ub75
water_wt = water_esa70*esa70_ub75+water_ub75
# Print final mass fractions
print("\n\n###### Mass fractions ######")
print("## Detailed ##")
print("sles12_wt = {}".format(sles12_wt))
print("sles14_wt = {}".format(sles14_wt))
print("cmea8_wt = {}".format(cmea8_wt))
print("cmea10_wt = {}".format(cmea10_wt))
print("cmea12_wt = {}".format(cmea12_wt))
print("cmea14_wt = {}".format(cmea14_wt))
print("cmea16_wt = {}".format(cmea16_wt))
print("cmea18_wt = {}".format(cmea18_wt))
print("## Generic component ##")
print("Water, wt = {}".format(water_wt))
SLES_wt = sles12_wt+sles14_wt
print("SLES, wt = {}".format(SLES_wt))
CMEA_wt = cmea8_wt+cmea10_wt+cmea12_wt+cmea14_wt+cmea16_wt+cmea18_wt
print("CMEA, wt = {}".format(CMEA_wt))
print("#########\nCheck that the mass fractions add up to 1:\nSUM = {}\n#########\n".format(SLES_wt+CMEA_wt+water_wt))

## Blend composition information considering the coarse-graining
# Molecules coarse-graining
waterBeads = 1/2
sles12Beads = 9
sles14Beads = 10
cmea8Beads = 6
cmea10Beads = 7
cmea12Beads = 8
cmea14Beads = 9
cmea16Beads = 10
cmea18Beads = 11
# Number of beads for every species, considering the coarse graining
water_NB = water_wt/waterMM*waterBeads
sles12_NB = sles12_wt/sles12MM*sles12Beads
sles14_NB = sles14_wt/sles14MM*sles14Beads
cmea8_NB = cmea8_wt/cmea8MM*cmea8Beads
cmea10_NB = cmea10_wt/cmea10MM*cmea10Beads
cmea12_NB = cmea12_wt/cmea12MM*cmea12Beads
cmea14_NB = cmea14_wt/cmea14MM*cmea14Beads
cmea16_NB = cmea16_wt/cmea16MM*cmea16Beads
cmea18_NB = cmea18_wt/cmea18MM*cmea18Beads
total_NB = water_NB+sles12_NB+sles14_NB+cmea8_NB+cmea10_NB+cmea12_NB+cmea14_NB+cmea16_NB+cmea18_NB
# Bead fraction
water_BF = water_NB/(total_NB)
sles12_BF = sles12_NB/(total_NB)
sles14_BF = sles14_NB/(total_NB)
cmea8_BF = cmea8_NB/(total_NB)
cmea10_BF = cmea10_NB/(total_NB)
cmea12_BF = cmea12_NB/(total_NB)
cmea14_BF = cmea14_NB/(total_NB)
cmea16_BF = cmea16_NB/(total_NB)
cmea18_BF = cmea18_NB/(total_NB)
SLES_BF = sles12_BF+sles14_BF
CMEA_BF = cmea8_BF+cmea10_BF+cmea12_BF+cmea14_BF+cmea16_BF+cmea18_BF
sum_BF = water_BF+sles12_BF+sles14_BF+cmea8_BF+cmea10_BF+cmea12_BF+cmea14_BF+cmea16_BF+cmea18_BF
# Print final bead fractions
print("\n###### Bead fractions ######")
print("## Detailed ##")
print("sles12_BF = {}".format(sles12_BF))
print("sles14_BF = {}".format(sles14_BF))
print("cmea8_BF = {}".format(cmea8_BF))
print("cmea10_BF = {}".format(cmea10_BF))
print("cmea12_BF = {}".format(cmea12_BF))
print("cmea14_BF = {}".format(cmea14_BF))
print("cmea16_BF = {}".format(cmea16_BF))
print("cmea18_BF = {}".format(cmea18_BF))
print("## Generic component ##")
print("Water, bead fraction = {}".format(water_BF))
SLES_wt = sles12_wt+sles14_wt
print("SLES, bead fraction = {}".format(SLES_BF))
CMEA_wt = cmea8_wt+cmea10_wt+cmea12_wt+cmea14_wt+cmea16_wt+cmea18_wt
print("CMEA, bead fraction = {}".format(CMEA_BF))
print("#########\nCheck that the bead fractions add up to 1:\nSUM = {}\n#########\n\n".format(sum_BF))
