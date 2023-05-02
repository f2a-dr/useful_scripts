import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Noiseless training data
# Xtrain = np.array([-4, -3, -2, -1, 1]).reshape(5,1)
trainValues = [-4, -3, -2, -1, 1, 2, 3]
# Xtrain = np.array(trainValues).reshape(len(trainValues),1)
# ytrain = np.sin(Xtrain)

# Define the kernel function
def kernel(a, b, param):
    sqdist = np.sum(a**2,1).reshape(-1,1) + np.sum(b**2,1) - 2*np.dot(a, b.T)
    # This is equivalent to the creation of a matrix in which for every (i,j) position
    # we calculate (a_i - b_j)^2. Instead of doing it with nested for cycles for every
    # position in the matrix, it is done just with arrays manipulations.
    return np.exp(-.5 * (1/param) * sqdist)

param = 1

def regression(Xtest, Xtrain, ytrain, param, n, curvesN):

	K_ss = kernel(Xtest, Xtest, param)
	K = kernel(Xtrain, Xtrain, param)
	L = np.linalg.cholesky(K + 0.00005*np.eye(len(Xtrain)))

	K_s = kernel(Xtrain, Xtest, param)
	Lk = np.linalg.solve(L, K_s)
	mu = np.dot(Lk.T, np.linalg.solve(L, ytrain)).reshape((n,))

	s2 = np.diag(K_ss) - np.sum(Lk**2, axis=0)
	stdv = np.sqrt(s2)
	L = np.linalg.cholesky(K_ss + 1e-6*np.eye(n) - np.dot(Lk.T, Lk))    # Noisy? Maybe it is to guarantee K_ss definite-positive
	f_post = mu.reshape(-1,1) + np.dot(L, np.random.normal(size=(n,curvesN)))

	return mu, f_post


class updatePlot:
	def __init__(self, ax, trainArray):
		self.ax = ax
		# Test data
		self.curvesN = 50
		self.n = 100
		self.Xtest = np.linspace(-5, 5, self.n).reshape(-1,1)
		self.yreal = np.sin(self.Xtest)
		self.trainValues = trainArray

		self.param = 1
		self.ax.set_xlabel(r"$x$", fontsize=16)
		self.ax.set_ylabel(r"$f(x)$", fontsize=16)
		self.ax.axis([-5, 5, -3, 3])

		self.funcDist = [[] for _ in range(self.curvesN)]
		for i in range(self.curvesN):
				self.funcDist[i], = self.ax.plot([], [], lw=0.5, color='tab:blue')
		self.funcReal, = self.ax.plot([], [], color='tab:red', linewidth=4, label=r"$\sin(x)$")
		# plt.fill_between(Xtest.flat, mu-2*stdv, mu+2*stdv, alpha=0.4, color="grey", label=r"95% confidence interval")
		self.funcPred, = self.ax.plot([], [], color='black', lw=4, label='Predicted values')
		self.pointTrain, = self.ax.plot([], [], markerfacecolor='tab:red', linestyle='', marker='o', markeredgecolor='black', fillstyle='full', markersize=12, label='Training points')
		self.lines = []
		for i in range(self.curvesN):
			# self.lines.append(self.ax.plot([], [], lw=0.5, color='tab:blue'))
			self.lines.append(self.funcDist[i])
		self.lines.append(self.funcReal)
		self.lines.append(self.funcPred)
		self.lines.append(self.pointTrain)
		self.leg = self.ax.legend(loc='lower left')

	def __call__(self, i):
		self.Xtrain = np.array(self.trainValues[:i]).reshape(i,1)
		self.ytrain = np.sin(self.Xtrain)
		self.mu, self.f_post = regression(self.Xtest, self.Xtrain, self.ytrain, self.param, self.n, self.curvesN)

		# self.lines[0].set_data(self.Xtest, self.f_post)
		for i in range(self.curvesN):
			self.lines[i].set_data(self.Xtest, self.f_post.transpose()[i])
		self.lines[self.curvesN].set_data(self.Xtest, self.yreal)
		self.lines[self.curvesN+1].set_data(self.Xtest, self.mu)
		self.lines[self.curvesN+2].set_data(self.Xtrain, self.ytrain)

		# self.funcDist.set_data(self.Xtest, self.f_post)
		# self.funcReal.set_data(self.Xtest, self.yreal)
		# # plt.fill_between(Xtest.flat, mu-2*stdv, mu+2*stdv, alpha=0.4, color="grey", label=r"95% confidence interval")
		# self.funcPred.set_data(self.Xtest, self.mu)
		# self.pointTrain.set_data(self.Xtrain, self.ytrain)
	
		return self.lines,

# Plots of the 3 sampled functions
plt.rcParams.update({
	"text.usetex": True,
	"font.family": "serif",
	#"font.sanserif": "Helvetica"
})
centimeters=1/2.54
fig = plt.figure(figsize=(15*centimeters,15*centimeters))
gs = fig.add_gridspec(1,1)
ax1 = fig.add_subplot(gs[0,0])
up = updatePlot(ax1, trainValues)
anim = animation.FuncAnimation(fig, up, frames=len(trainValues), interval=1400)

# plt.show()

writer = animation.FFMpegWriter(
    fps=1, metadata=dict(artist='Me'), bitrate=-1)
anim.save("GPR.mp4", writer=writer, dpi=150)
