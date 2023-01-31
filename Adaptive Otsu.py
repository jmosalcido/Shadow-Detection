# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 17:53:45 2021

@author: jessm

code from https://scikit-image.org/docs/stable/auto_examples/applications/plot_thresholding.html


"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import disk
from skimage.filters import threshold_otsu, rank
from numpy import inf
import skimage.filters

array=np.asarray(skimage.io.imread("B5.tif", as_gray=True))
array=skimage.util.img_as_ubyte(array)
#array=np.load("con_mela.jfif")
#savename=('thresh_a26.npy')


radius =10#This is the local thresholding radius

#this function is pretty much redundant
def crop_center(img):
    y,x = img.shape
    if img.shape[0]<img.shape[1]:
        cropx=img.shape[0]
        startx = x//2-(cropx//2)
        return img[:,startx:startx+cropx]
    elif img.shape[1]<img.shape[0]:
        cropy=img.shape[1]
        starty = y//2-(cropy//2)    
        return img[starty:starty+cropy,:]
    else :
        print("it is already a cube")
        return img

cube=crop_center(array)
    
"""These three lines are the actual code, everything else is plotting"""
local_otsu_cube = rank.otsu(cube, disk(radius)) #this is the the thresholded image, not the actual binary mask
thresh=cube <= local_otsu_cube ###This createds the binary mask
inv_thresh=np.invert(thresh) ###The binary mask needs to be inverted to black out background


print(inv_thresh.shape)


plt.imshow(local_otsu_cube,  cmap=plt.cm.gray)
plt.title('Local Otsu Thresholding Image')
plt.colorbar()
plt.show()


fig, axes = plt.subplots(1, 2, figsize=(8, 5), sharex=True, sharey=True)
ax = axes.ravel()
plt.tight_layout()

ax[0].imshow(cube,  cmap=plt.cm.gray)
ax[0].set_title('Original')
ax[0].axis('off')

ax[1].imshow(inv_thresh,  cmap=plt.cm.gray)
ax[1].set_title('Local Thresholding Inverted (radius=%d)' % radius)
ax[1].axis('off')

plt.show()

#cropping in 

fig, axes = plt.subplots(1, 2, figsize=(8, 5), sharex=True, sharey=True)
ax = axes.ravel()
plt.tight_layout()


"""This is simply here to visually confirm that this code looks like its doing its job right"""
slicecube=cube[50:80,60:90]
slicethresh=inv_thresh[50:80,60:90]

ax[0].imshow(slicecube, origin='lower',  cmap=plt.cm.gray)
ax[0].set_title("Zoomed in Original")
ax[0].axis('off')

ax[1].imshow(slicethresh, origin='lower',  cmap=plt.cm.gray)
ax[1].set_title('Zoomed in Thresholding')
ax[1].axis('off')

plt.show()

#np.save(savename, inv_thresh)
