# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 12:14:43 2021

@author: jessm
"""
import os
from glob import glob
from skimage import io
import glob
import numpy as np
#from osgeo import gdal
import scipy.misc as sm
import math
import matplotlib.pyplot as plt
import skimage
from skimage import exposure 
from skimage import color


def norm(band):
    band_min, band_max = band.min(), band.max()
    return ((band - band_min)/(band_max - band_min))

b4= io.imread('B4.tif')
b3= io.imread('B3.tif')
b2= io.imread('B2.tif')
#b4=skimage.util.crop(b4, ((1500,4500), (4000,2000)))
#b3=skimage.util.crop(b3, ((1500,4500), (4000,2000)))
#b2=skimage.util.crop(b2, ((1500,4500), (4000,2000)))

b4=skimage.util.crop(b4, ((2000,2000), (2000,2000)))
b3=skimage.util.crop(b3, ((2000,2000), (2000,2000)))
b2=skimage.util.crop(b2, ((2000,2000), (2000,2000)))
#print(img.shape)

#plt.imshow(img)

#plt.show()

b2 = norm(b2 )
b3 = norm(b3)
b4 = norm(b4)

rgb = np.dstack((b4,b3,b2))
plt.imshow(rgb)
plt.show()
print(rgb.shape, rgb.max())

# tuple to select colors of each channel line
colors = ("red", "green", "blue")
channel_ids = (0, 1, 2)


# create the histogram plot, with three lines, one for
# each color
plt.xlim([0, 1])
for ch_id, c in zip(channel_ids, colors):
    histogram, bin_edges = np.histogram(rgb[:, :, ch_id], bins=256, range=(0, 1))
    plt.plot(bin_edges[0:-1], histogram, c)

plt.xlabel("Color value")
plt.ylabel("Pixels")


plt.show()

# Contrast stretching
p2, p98 = np.percentile(rgb, (1, 98))
img_rescale = exposure.rescale_intensity(rgb, in_range=(p2, p98))

plt.imshow(img_rescale)
plt.show()

# create the histogram plot, with three lines, one for
# each color
plt.xlim([0, 1])
for ch_id, c in zip(channel_ids, colors):
    histogram, bin_edges = np.histogram(img_rescale[:, :, ch_id], bins=256, range=(0, 1))
    plt.plot(bin_edges[0:-1], histogram, c)

plt.xlabel("Color value")
plt.ylabel("Pixels")

plt.show()


# Adaptive Equalization
img_adapteq = exposure.equalize_adapthist(rgb, clip_limit=0.03)
plt.imshow(img_adapteq)
plt.show()

plt.xlim([0, 1])
for ch_id, c in zip(channel_ids, colors):
    histogram, bin_edges = np.histogram(img_adapteq[:, :, ch_id], bins=256, range=(0, 1))
    plt.plot(bin_edges[0:-1], histogram, c)

plt.xlabel("Color value")
plt.ylabel("Pixels")

plt.show()