import cv2 
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mp
plt.ion()

# read image and convert it to hsv
img = cv2.imread('./data/images/jersey.jpg')
hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
H,S,V = cv2.split(hsvImg)

# remove background pixels from hue array
H_array = H[S > 10].flatten()

#create a graph of the colors 
plt.figure(figsize=[20,10])
plt.subplot(121); plt.imshow(img[:,:,::-1]); plt.title("Image"); plt.axis('off')
plt.subplot(122); plt.hist(H_array, bins=180, color='r'); plt.title("Histogram")
