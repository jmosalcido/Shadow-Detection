# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 14:38:35 2021

@author: jessm
"""

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

imgg =skimage.color.rgb2gray(rgb)

# create the histogram
histogram, bin_edges = np.histogram(imgg, bins=256, range=(0, 1))
# configure and draw the histogram figure
plt.figure()
plt.title("Original Gray Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim([0.0, 1.0])  # <- named arguments do not work here

plt.plot(bin_edges[0:-1], histogram)  # <- or here
plt.show()

# Contrast stretching
p2, p98 = np.percentile(rgb, (1, 99))
img_rescale = exposure.rescale_intensity(imgg, in_range=(p2, p98))

skimage.io.imshow(img_rescale)
#plt.imshow(img_rescale)
#plt.show()

# create the histogram
histogram, bin_edges = np.histogram(img_rescale, bins=256, range=(0, 1))

# configure and draw the histogram figure
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim([0.0, 1.0])  # <- named arguments do not work here

plt.plot(bin_edges[0:-1], histogram)  # <- or here
plt.show()

# Adaptive Equalization
img_adapteq = exposure.equalize_adapthist(imgg, clip_limit=0.03)

skimage.io.imshow(img_rescale)
#plt.imshow(img_adapteq)
#plt.show()

# create the histogram
histogram, bin_edges = np.histogram(img_adapteq, bins=256, range=(0, 1))

# configure and draw the histogram figure
plt.figure()
plt.title("Adaptive Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim([0.0, 1.0])  # <- named arguments do not work here

plt.plot(bin_edges[0:-1], histogram)  # <- or here
plt.show()