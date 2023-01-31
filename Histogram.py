# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 17:28:51 2021

@author: jessm
"""
import numpy as np
import sys
import skimage.io
from matplotlib import pyplot as plt

import skimage.color

# read image, based on command line filename argument;
# read the image as grayscale from the outset
#imagegrey = skimage.io.imread("New Jersey.jpg", as_gray=True)
image=skimage.io.imread("New Jersey.jpg")
# display the image
skimage.io.imshow(image)

img_small=skimage.util.crop(image, ((3000,0), (4000,0), (0,0)))
skimage.io.imshow(img_small)
print(image.shape, img_small.shape)

imgg = skimage.color.rgb2gray(img_small)


# create the histogram
histogram, bin_edges = np.histogram(imgg, bins=256, range=(0, 1))

#histogram, bin_edges = np.histogram(imagegrey, bins=256, range=(0, 1))

#def rgb2gray(rgb):
#    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
   
#gray = rgb2gray(img_small)    
#plt.imshow(gray, cmap=plt.get_cmap('gray'))
#plt.show()

#histogram, bin_edges = np.histogram(gray, bins=256, range=(0, 1))

# configure and draw the histogram figure
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim([0.0, 1.0])  # <- named arguments do not work here

plt.plot(bin_edges[0:-1], histogram)  # <- or here
plt.show()


# read original image, in full color, based on command
# line argument
#image = skimage.io.imread("con_mela.jfif")

# display the image
skimage.io.imshow(img_small)
plt.show()

# tuple to select colors of each channel line
colors = ("red", "green", "blue")
channel_ids = (0, 1, 2)

# create the histogram plot, with three lines, one for
# each color
plt.xlim([0, 256])
for ch_id, c in zip(channel_ids, colors):
    histogram, bin_edges = np.histogram( img_small[:, :, ch_id], bins=256, range=(0, 256))
    plt.plot(bin_edges[0:-1], histogram, c)

plt.xlabel("Color value")
plt.ylabel("Pixels")

plt.show()