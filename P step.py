# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 21:46:28 2021

@author: jessm
"""
# Python program to read
# json file
#LC08_L2SP_012032_20211015_20211025_02_T1
 
import numpy as np
import math
import json
from skimage import io
import matplotlib.pyplot as plt
 
# Opening metadata text file
f= open('New Jersey Meta.txt')
meta = f.read()
print(meta)

#this is already done in the bands themselves- "SR"
def surface_reflectance(d, Ls, Lp, Tau, Edir, Ediff):
    p_i=((np.pi*d**2*Ls)-Lp)/Tau(Edir+Ediff)
    return p_i

d=1.0066210

# read the image stack
Tau = io.imread('ATRAN.tif')
# show the image
#plt.imshow(Tau,cmap='gray')
#plt.axis('off')
#plt.show()

band5=io.imread('B5.tif')
plt.imshow(band5, cmap='gray')
print(band5.shape)

plt.show()

rows = band5.shape[0]
cols = band5.shape[1]

arr=np.array([[1,2,3],[4,5,6]])
print(arr, arr.shape)
arr=arr*2
print(arr)

#band5=band5+17
#print(band5.max())
print("done")
        