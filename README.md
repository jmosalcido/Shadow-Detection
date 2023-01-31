# Shadow-Detection
This code implements a modified Richter's Method for shadow detection in multispectral/hyperspectral aerial imagery. 

Three near visible and short wave infrared bands are used to isolate the shadows of clouds in the image
This implementation of Richter's Method follows the general steps of using the atmospherically corrected surface reflectance from the Landsat data to create a covariance matrix and zero-reflectance matched filter. 
This matched filter is applied to the data yielding unscaled shadow abundance values which can be normalized and used to create a mask that isolates the cloud shadows in the image. 

The scaled shadow values can also be utilized to de-shadow the image entirely in a future project. 
