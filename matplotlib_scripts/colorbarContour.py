import numpy as np
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib import ticker

# Inizialize values for the colobar
interval = [0.003,0.065]
nticks = np.linspace(interval[0],interval[1],10) # ticks for colorbar in linear scale
#nticks = np.concatenate((np.array([interval[0]]), np.logspace(np.log10(0.01),np.log10(0.1),2), np.array([interval[1]]))) # ticks for colorbar in logarithmic scale

# Load pictures
with open('polymer_stirredtank_Newt_nu_slice.png', 'rb') as image_file:
    newt = plt.imread(image_file)
with open('polymer_stirredtank_GPR0_nu_slice.png', 'rb') as image_file:
    gpr0 = plt.imread(image_file)
with open('polymer_stirredtank_GPR1_nu_slice.png', 'rb') as image_file:
    gpr1 = plt.imread(image_file)

# Initialize the labels and pictures for the axes
ax = ['Newt', 'GPR0', 'GPR1']
axlab = ['a)', 'b)', 'c)']
axpic =[newt, gpr0, gpr1]

# Set LaTeX fonts
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    #"font.sanserif": "Helvetica"
})

# Start matplotib figure construction
centimeters=1/2.54
fig = plt.figure(figsize=(15*centimeters,5.3*centimeters), constrained_layout=True)
gs = fig.add_gridspec(1,3, wspace=-0.5)

# Definition of the axes
ax[0] = fig.add_subplot(gs[0,0])
ax[1] = fig.add_subplot(gs[0,1])
ax[2] = fig.add_subplot(gs[0,2])

# The same operation are applied to every axes
for i in range(len(ax)):
    ax[i].imshow(axpic[i])  # load the picture
    ax[i].axis('off')       # clear x-axis and y-axis
    trans = mpl.transforms.ScaledTranslation(+10/72, -7/72, fig.dpi_scale_trans) # define saling factors to move the label outside the picture
    ax[i].text(0.0, 1.0, axlab[i], transform=ax[i].transAxes + trans, fontsize=14, va='bottom') # set the label

# Set up colorbar
norm = mpl.colors.Normalize(vmin=interval[0],vmax=interval[1])  # interval normalization in linear scale
#norm = mpl.colors.LogNorm(vmin=interval[0],vmax=interval[1])  # interval normalization in logarithmic scale
cbar = fig.colorbar(cm.ScalarMappable(norm=norm, cmap="jet"), ax=ax, fraction=0.10, aspect=40, orientation="horizontal", ticks=nticks)  # invoke colorbar
cbar.set_label(label=r"$\nu\mathrm{\:(m^2\cdot s^{-1}})$", size=16) # set colorbar label
cbar.ax.tick_params(labelsize=11)   # set colorbar tick labels
cbar.ax.xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.3f}")) # format ticker label


#plt.show()
fig.savefig("nuContourComposition.pdf", dpi=300)
