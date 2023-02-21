import numpy as np
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib import ticker

# Inizialize values for the colobar
interval = [0.1,107]
nticks = np.concatenate((np.array([0.1]), np.linspace(12,96,8), np.array([107])), axis=0)

# Load pictures
with open('polymer_stirredtank_Newt_strainRate_slice.png', 'rb') as image_file:
    newt = plt.imread(image_file)
with open('polymer_stirredtank_GPR0_strainRate_slice.png', 'rb') as image_file:
    gpr0 = plt.imread(image_file)
with open('polymer_stirredtank_GPR1_strainRate_slice.png', 'rb') as image_file:
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
norm = mpl.colors.Normalize(vmin=interval[0],vmax=interval[1])  # interval normalization
cbar = fig.colorbar(cm.ScalarMappable(norm=norm, cmap="jet"), ax=ax, fraction=0.10, aspect=40, orientation="horizontal", ticks=nticks)  # invoke colorbar
cbar.set_label(label=r"$\dot{\gamma}\mathrm{\:(s^{-1}})$", size=16) # set colorbar label
cbar.ax.tick_params(labelsize=11)   # set colorbar tick labels
cbar.ax.xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.1f}")) # format ticker label


#plt.show()
fig.savefig("strainRateContourComposition.pdf", dpi=300)
