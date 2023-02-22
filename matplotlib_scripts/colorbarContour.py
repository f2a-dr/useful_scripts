import numpy as np
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib import ticker

# Pictures to load in input and name of file to output
pics = ['polymer_stirredtank_Newt_nu_slice.png', 'polymer_stirredtank_GPR0_nu_slice.png', 'polymer_stirredtank_GPR1_nu_slice.png']
fileout = 'test.pdf'

# Initialize the labels and pictures for the axes
axlab = ['a)', 'b)', 'c)']
ax = []
axpic = []

# Inizialize values for the colobar
interval = [0.003,0.24]
#interval = [0.003,0.065]
logScale = True			# choose between logarithmic and linear scale for the colorbar
extension = 'neither'	# extend the colorbar limits: 'neither', 'both', 'min', 'max'

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
	ini = np.ceil(np.log10(interval[0]))
	fin = np.floor(np.log10(interval[1]))
	nticks = np.concatenate((np.array([interval[0]]), np.logspace(ini, fin, int(fin)-int(ini)+1), np.array([interval[1]])))
	norm = mpl.colors.LogNorm(vmin=interval[0],vmax=interval[1])  # interval normalization
else:
	nticks = np.linspace(0.003,0.065,10)
	norm = mpl.colors.Normalize(vmin=interval[0],vmax=interval[1])  # interval normalization
cbar = fig.colorbar(cm.ScalarMappable(norm=norm, cmap="jet"), ax=ax, fraction=0.10, aspect=40, orientation="horizontal", ticks=nticks, extend=extension)  # invoke colorbar
cbar.set_label(label=r"$\nu\mathrm{\:(m^2\cdot s^{-1}})$", size=16) # set colorbar label
cbar.ax.tick_params(labelsize=11)   # set colorbar tick labels
cbar.ax.xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.3f}")) # format ticker label


#plt.show()
fig.savefig(fileout, dpi=300)
