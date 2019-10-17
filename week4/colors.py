import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys


plt.ion()


def main():
	bgr_image = cv2.imread('./data/images/capsicum.jpg')

	#rgb colors
	

	run_type = sys.argv[1]

	if run_type == 'rgb' or run_type == 'hsv' or run_type =='ycrcb' or run_type == 'lab':
		plt.figure(figsize=(20,15))
		plt.subplot(141)
		plt.imshow(bgr_image[:,:,::-1])
		plt.title('all colors')
		
		if run_type == 'rgb':
			titles = ['blue', 'green', 'red']
			image = bgr_image

		elif run_type == 'hsv':
			image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
			titles = ['Hue', 'Saturation', 'Value']

		# Y is RGB, Cr (red diff), Cb(blue diff)
		elif run_type == 'ycrcb':
			image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2YCrCb)
			titles = ['Y Channel', 'Cr Channel', 'Cb Channel']

		# L-lightness, a-(green:magenta), b(blue-yellow)
		elif run_type == 'lab':
			image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2Lab)
			titles = ['Lightness', 'A channel', 'B Channel']

		for i in range(3):
			plt.subplot(142+i)
			plt.imshow(image[:,:,i], cmap='gray')
			plt.title(titles[i])
	
	elif run_type == 'vtest' or run_type == 'stest' \
		or run_type == 'htest' or run_type == 'stest_real':
		#basically a brighness test
		plt.figure(figsize=(50,50))
		# use a real image 
		im = cv2.imread('./data/images/girl.jpg')
		scale = 0.1
		for i in range(7):
			ax = plt.subplot(1, 7, i+1)
			# create 50x50 HSV image w/ all zeros
			imhsv = np.zeros((50, 50, 3), dtype=np.uint8)
			
			if run_type == "vtest":
				# set hue = 0, sat = 0, v = i x 40
				v = i*40
				imhsv[:,:,:] = (0, 0, v)
				ax.set_title('V='+str(v), fontdict={'fontsize': 20, 'fontweight': 'medium'})
			
			elif run_type == 'stest':
				# set hue = 0, sat = i*40, v = 128
				s = i*40
				imhsv[:,:,:] = (0, s, 128)
				ax.set_title('S='+str(s), fontdict={'fontsize': 20, 'fontweight': 'medium'})
			
			elif run_type == 'stest_real':
				hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
				hsv = np.float32(hsv)
				h, s, v = cv2.split(hsv)
				s = np.float32(s*i/6)
				imhsv = np.uint8(cv2.merge([h, s, v]))

			else:
				# set hue = i*40, sat = 200, v = 128
				h = i*30
				imhsv[:,:,:] = (h, 200, 128)
				ax.set_title('H='+str(h), fontdict={'fontsize': 20, 'fontweight': 'medium'})
			

			#conver hsv to rgb
			imrgb = cv2.cvtColor(imhsv, cv2.COLOR_HSV2BGR)
			#display image
			plt.imshow(imrgb[:,:,::-1])
			plt.axis('off')
			
	
	else:
		return 

main()