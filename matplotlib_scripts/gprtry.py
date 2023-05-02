import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Test data
n = 100
Xtest = np.linspace(-5, 5, n).reshape(-1,1)
yreal = np.sin(Xtest)

# Noiseless training data
# Xtrain = np.array([-4, -3, -2, -1, 1]).reshape(5,1)
trainValues = [-4, -3, -2, -1, 1]
Xtrain = np.array(trainValues).reshape(len(trainValues),1)
ytrain = np.sin(Xtrain)

# Define the kernel function
def kernel(a, b, param):
    sqdist = np.sum(a**2,1).reshape(-1,1) + np.sum(b**2,1) - 2*np.dot(a, b.T)
    # This is equivalent to the creation of a matrix in which for every (i,j) position
    # we calculate (a_i - b_j)^2. Instead of doing it with nested for cycles for every
    # position in the matrix, it is done just with arrays manipulations.
    return np.exp(-.5 * (1/param) * sqdist)

param = 1


K_ss = kernel(Xtest, Xtest, param)
# Apply the kernel function to our training points
K = kernel(Xtrain, Xtrain, param)
L = np.linalg.cholesky(K + 0.00005*np.eye(len(Xtrain)))
#print(L)

# Compute the mean at out test points
K_s = kernel(Xtrain, Xtest, param)
#print(K_s)
Lk = np.linalg.solve(L, K_s)
mu = np.dot(Lk.T, np.linalg.solve(L, ytrain)).reshape((n,))

# Compute the standard deviation so we can plot it
# For the posterior conditional the covariance matrix is 
# (Form Marginal and Conditional Distributions of MVN theorem)
# K_ss - K_s*K^{-1}*K_s^{Transpose simbol}
s2 = np.diag(K_ss) - np.sum(Lk**2, axis=0)
stdv = np.sqrt(s2)
# Draw sample from the posterior at out test points
L = np.linalg.cholesky(K_ss + 1e-6*np.eye(n) - np.dot(Lk.T, Lk))    # Noisy? Maybe it is to guarantee K_ss definite-positive
#L = np.linalg.cholesky(K_ss - np.dot(Lk.T, Lk))                     # Noiseless 
f_post = mu.reshape(-1,1) + np.dot(L, np.random.normal(size=(n,30)))


## Get cholesky decomposition (square root) of the covariance matrix
#L = np.linalg.cholesky(K_ss + 1e-15*np.eye(n))
## Sample 3 sets of standard normals for our test points, multiply themby the square 
## root of the covariance matrix
#f_prior = np.dot(L, np.random.normal(size=(n, 10)))

#print(mu)

# Plots of the 3 sampled functions
plt.rcParams.update({
	"text.usetex": True,
	"font.family": "serif",
	#"font.sanserif": "Helvetica"
})
centimeters=1/2.54
fig = plt.figure(figsize=(15*centimeters,15*centimeters), constrained_layout=True)
gs = fig.add_gridspec(1,1)

ax1 = fig.add_subplot(gs[0,0])
ax1.set_xlabel(r"$x$", fontsize=16)
ax1.set_ylabel(r"$f(x)$", fontsize=16)
ax1.plot(Xtest, f_post, lw=0.5, color='tab:blue')
ax1.plot(Xtest, yreal, color='tab:red', linewidth=4, label=r"$\sin(x)$")
# plt.fill_between(Xtest.flat, mu-2*stdv, mu+2*stdv, alpha=0.4, color="grey", label=r"95% confidence interval")
ax1.plot(Xtest, mu, color='black', lw=4, label='Predicted values')
ax1.plot(Xtrain, ytrain, markerfacecolor='tab:red', linestyle='', marker='o', markeredgecolor='black', fillstyle='full', markersize=12, label='Training points')
ax1.axis([-5, 5, -3, 3])
# plt.title('Samples from the GP posterior')
ax1.legend()
plt.show()
