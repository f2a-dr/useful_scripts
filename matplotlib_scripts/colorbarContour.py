import numpy as np
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib import ticker

# Pictures to load in input and name of file to output
pics = ['polymer_Newt_strainRate_slice1.png', 'polymer_GPR0_strainRate_slice1.png', 'polymer_GPR1_strainRate_slice1.png']
fileout = 'strainRateContour_1.pdf'

# Initialize the labels and pictures for the axes
axlab = ['a)', 'b)', 'c)']
ax = []
axpic = []

# Inizialize values for the colobar
interval = [0.03,111]
#interval = [0.003,0.065]
logScale = True			# choose between logarithmic and linear scale for the colorbar
extension = 'neither'	# extend the colorbar limits: 'neither', 'both', 'min', 'max'
colorbarLabel = r"$\dot{\gamma}\:(\mathrm{s^{-1}})$"

# Load pictures
for i in range(len(pics)):
	with open(pics[i], 'rb') as image_file:
		#axpic[i] = plt.imread(image_file)
		axpic.append(plt.imread(image_file))

# Set LaTeX fonts
plt.rcParams.update({
	"text.usetex": True,
	"font.family": "serif",
	#"font.sanserif": "Helvetica"
})

# Start matplotib figure construction
centimeters=1/2.54
fig = plt.figure(figsize=(15*centimeters,5.3*centimeters), constrained_layout=True)
gs = fig.add_gridspec(1,len(pics), wspace=-0.5)


# The same operation are applied to every axes
for i in range(len(pics)):
	ax.append(i)
	ax[i] = fig.add_subplot(gs[0,i])
	ax[i].imshow(axpic[i])  # load the picture
	ax[i].axis('off')	   # clear x-axis and y-axis
	trans = mpl.transforms.ScaledTranslation(+10/72, -7/72, fig.dpi_scale_trans) # define saling factors to move the label outside the picture
	ax[i].text(0.0, 1.0, axlab[i], transform=ax[i].transAxes + trans, fontsize=14, va='bottom') # set the label

# Set up colorbar and its ticks
if logScale:
	# if interval[0] <=
	# first = str(interval[0])
	# last = str(interval[1])
	ini = np.ceil(np.log10(interval[0]))
	if (10**ini - interval[0])/10**ini <= 0.2:
		ini = ini + 1
	fin = np.floor(np.log10(interval[1]))
	if ((interval[1] - 10**fin)/10**fin) <= 0.2:
		fin = fin - 1
	iticks = np.logspace(ini, fin, int(fin)-int(ini)+1)	# internal ticks
	iticksExp = np.linspace(ini, fin, int(fin)-int(ini)+1) # exponent of the internal ticks, base 10
	nticks = np.concatenate((np.array([interval[0]]), iticks, np.array([interval[1]]))) # total ticks
	lticks = [r"$10^{{{}}}$".format(int(iticksExp[i])) for i in range(len(iticksExp.tolist()))]
	lticks.insert(0, first)
	lticks.append(last)
	norm = mpl.colors.LogNorm(vmin=interval[0],vmax=interval[1])  # interval normalization
else:
	nticks = np.linspace(interval[0],interval[1],10)
	norm = mpl.colors.Normalize(vmin=interval[0],vmax=interval[1])  # interval normalization

cbar = fig.colorbar(cm.ScalarMappable(norm=norm, cmap="jet"), ax=ax, fraction=0.10, aspect=40, orientation="horizontal", ticks=nticks, extend=extension)  # invoke colorbar

if logScale:
	cbar.ax.set_xticklabels(lticks)	# set colorbar tick labels
else:
	cbar.ax.xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.1f}")) # format ticker label

cbar.set_label(label=colorbarLabel, size=16) # set colorbar label
cbar.ax.tick_params(labelsize=11)   # set format for tick labels


#plt.show()
fig.savefig(fileout, dpi=300)
