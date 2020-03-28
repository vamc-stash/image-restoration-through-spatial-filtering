import numpy as np
import random
import cv2

def noise(noise_typ,img,gray):
	rows = img.shape[0]
	cols = img.shape[1]
	if noise_typ == "salt-and-pepper-noise" or noise_typ == "salt-noise" or noise_typ == "pepper-noise":
		out_img = np.zeros(img.shape,np.uint8)
		prob = (1.0/1000)*random.randint(3,6)
		if gray == "False":
			for i in range(rows):
				for j in range(cols):
					randn = random.random()
					if randn < prob and noise_typ != "salt-noise":
						out_img[i][j][0] = 0
						out_img[i][j][1] = 0
						out_img[i][j][2] = 0
					elif randn > (1-prob) and noise_typ != "pepper-noise":
						out_img[i][j][0] = 255
						out_img[i][j][1] = 255
						out_img[i][j][2] = 255
					else:
						out_img[i][j][0] = img[i][j][0]
						out_img[i][j][1] = img[i][j][1]
						out_img[i][j][2] = img[i][j][2]
		else:
			for i in range(rows):
				for j in range(cols):
					randn = random.random()
					if randn < prob and noise_typ != "salt-noise":
						out_img[i][j] = 0
					elif randn > (1-prob) and noise_typ != "pepper-noise":
						out_img[i][j] = 255
					else:
						out_img[i][j] = img[i][j]
		return out_img

	elif noise_typ == "gaussian-noise":
		mean = 0 #center of the gaussian distribution
		var = random.randint(5,15)
		sigma = var**0.5 #standard deviation (width of the distribution)
		amount = (1/10)*random.randint(2,6)
		gaussian_noise = np.random.normal(mean,sigma,rows*cols)
		gaussian_noise = gaussian_noise.reshape(rows,cols)
		if gray == "False":
			img[:,:,0] = img[:,:,0] + gaussian_noise 
			img[:,:,1] = img[:,:,1] + gaussian_noise
			img[:,:,2] = img[:,:,2] + gaussian_noise 
		else:
			img[:,:] = img[:,:] + gaussian_noise * amount
		return img

	elif noise_typ == "uniform-noise":
		amount = (1/100)*random.randint(2,6)
		uniform_noise = np.random.uniform(0,1,rows*cols)
		uniform_noise = uniform_noise.reshape(rows,cols) 
		if gray == "False":
			img[:,:,0] = img[:,:,0] + uniform_noise
			img[:,:,1] = img[:,:,1] + uniform_noise
			img[:,:,2] = img[:,:,2] + uniform_noise
		else:
			img[:,:] = img[:,:] + uniform_noise 
		return img

	elif noise_typ == "exponential-noise":
		amount = (1/10)*random.randint(2,6)
		beta = random.randint(5,15)
		exponential_noise = np.random.exponential(beta,rows*cols)
		exponential_noise = exponential_noise.reshape(rows,cols) 
		if gray == "False":
			img[:,:,0] = img[:,:,0] + exponential_noise
			img[:,:,1] = img[:,:,1] + exponential_noise
			img[:,:,2] = img[:,:,2] + exponential_noise
		else:
			img[:,:] = img[:,:] +  exponential_noise
		return img