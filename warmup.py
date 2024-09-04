#!/usr/bin/env python3
import os
import math
from math import pi
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, MaxNLocator

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
plt.tight_layout()

# Define the specified ranges 
dims = np.arange(0,51,1)
rad = np.arange(1, 2.05, 0.05)
volumes = np.zeros(shape=(21, 51))

# Generate Volume for given n and R
for n in dims:
    for idx,r in enumerate(rad):
        gamma_value = float(math.gamma(n/2 + 1))
        Volume = pi**(n/2)*r**n/gamma_value
        volumes[idx][n] = Volume

dims, rad = np.meshgrid(dims, rad) # Create the 2D array from the 1D arrays dims and rad

# Plot the surface.
surf = ax.plot_surface(dims,rad,volumes,cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Set axes labels and title
ax.set_xlabel('Dimensions (n)')
ax.set_ylabel('Radius (R)')
ax.set_zlabel('Volume')
ax.set_title('Volume versus (n,R)')

# Customize colobar
fig.colorbar(surf, shrink=0.5, aspect=5, pad=0.15 )

plt.savefig("warmup.pdf", format="pdf", bbox_inches="tight")

plt.show()
