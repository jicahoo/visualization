import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as sp

x = np.random.randn(100000)
y = np.random.randn(100000) + 5
print type(x)

# normal distribution center at x=0 and y=5
fig1 = plt.subplot(2, 2, 1)
plt.hist2d(x, y, bins=40)
plt.colorbar()
plt.title('Heatmap without smoothing')
plt.xlabel("X")
plt.ylabel("Y")

# smoothing

X = sp.filters.gaussian_filter(x, sigma=2, order=0)
Y = sp.filters.gaussian_filter(y, sigma=2, order=0)
print X.shape
print Y.shape

heatmap, xedges, yedges = np.histogram2d(X, Y, bins=40)

print heatmap
print xedges
print yedges
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

fig1 = plt.subplot(2, 2, 2)
plt.imshow(heatmap, extent=extent)
plt.colorbar()
plt.title('Heatmap with smoothing')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
