import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

def hist_trans(im, x, y):
	pixels = x*y
	aoi = np.ones_like(im)
	for i in range(256):
		aoi[im == i] = np.floor((len(im[im == i]) / pixels) * 255)
	return aoi


path = sys.agrv[1]

im = cv2.imread(path)
x, y, num_colors = im.shape
hsv = False

if num_colors == 3:
	# convert to hsv 
	hsv_image = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	temp = hist_trans(hsv_image[:, : , 2], x, y)
	hsv_image[:, :, 2] = aoi
	hist_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
else: 
	aoi = hist_trans(im, x, y)

if hsv: 
	hsv_image[:, :, 2] = aoi
	hist_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
else: 
	hist_image = aoi








# make an array of arrays of 