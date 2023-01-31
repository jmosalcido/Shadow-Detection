# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 17:17:36 2021

@author: jessm
"""

import matplotlib.pyplot as plt

from skimage import data
import skimage.filters
#from skimage.filters import threshold_otsu, threshold_adaptive
from skimage import color
from skimage import io
import numpy as np
from matplotlib.colors import LogNorm, SymLogNorm
from PIL import Image, ExifTags
#image = Image.open("B5.tif")
#exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }

#img=np.load('con_mela.jfif')


#imgRGB=image.convert('RGB')
imgnp=np.asarray(skimage.io.imread("B5.tif", as_gray=True))
#plt.imshow(imgRGB)
plt.show()
plt.imshow(imgnp)
plt.show()
print(imgnp.shape)

#code from https://scikit-image.org/docs/stable/auto_examples/applications/plot_thresholding.html

##This is a quick example of thresholding steps, and different thresholding options
#It shows that Otsu thresholding is one of the best, even when it is global instead of local


import matplotlib.pyplot as plt
img=imgnp

global_thresh = skimage.filters.threshold_otsu(img)
binary_global = img > global_thresh

block_size = 5
local_thresh = skimage.filters.threshold_local(img, block_size, offset=10)
binary_local = img >= local_thresh

plt.imshow(img)
plt.title('Image')
plt.colorbar()
plt.show()
plt.imshow(binary_global)
plt.colorbar()
plt.title('Global thresholding')
plt.show()
plt.imshow(local_thresh)
plt.title('Adaptive thresholding')
plt.colorbar()
plt.show()
plt.imshow(binary_local)
plt.title('Original >= Local')
plt.colorbar()
plt.show()

fig, ax = skimage.filters.try_all_threshold(img, figsize=(6, 10), verbose=True)

