import numpy as np
import sys
import cv2



import degradation_model as dgm
import noise_models as nsm
import spatial_filters as sf
import filename_shortcuts as fsc

degrade_models = ["optical-blur" , "gaussian-blur" , "motion-blur"]
noise_models = ["salt-and-pepper-noise" , "salt-noise" , "pepper-noise" , "gaussian-noise" , "uniform-noise" , "exponential-noise"]
spatial_filters = ["mean-filter" , "order-statistics-filter" ,"Adaptive-filter"]

#mean filters : 1. Arithmetic Mean Filter  2. Geometric Mean Filter 3. Harmonic Mean Filter 4. Contraharmonic Mean Filter 
#order-statistics-filters : 1. Median Filter 2. Max Filter 3. Min Filter 4.Midpoint Filter 5. Alpha-Trimmed Mean Filter
#Adaptive-filter : 1. Local noise reduction Filter

if __name__ == '__main__':

	#get image filename from command line
	image_name = sys.argv[1]
	image_path = "input_images/"+image_name

	#load-image  ------- f(x,y)
	img = cv2.imread(image_path)

	print("Do you want to convert Image to Gray Scale? [y/n]")
	opt = str(input())
	gray = "False"
	if (opt == "n" or opt == "y") and len(img.shape)<3:
		gray = "True"
	elif opt == "y":
		img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		gray = "True"
	else:
		print("Incorrect input")
		sys.exit()

	img = cv2.resize(img,(250,250),interpolation = cv2.INTER_AREA)
	cv2.imshow("Test Image :",img)
	cv2.waitKey(10)

	#distort image --------- h(x,y) * f(x,y)
	print("Select distort model : \n 1. optical-blur \n 2. gaussian-blur \n 3. motion-blur \n")
	dg_opt = int(input())
	distort_img,k = dgm.degrade(degrade_models[dg_opt-1],img,gray)

	cv2.imshow('Distorted image',distort_img)
	cv2.waitKey(10)

	#add noise ----------- h(x,y)*f(x,y) + n(x,y) = g(x,y)
	print("Select Noise : \n 1. salt-and-pepper-noise \n 2. salt-noise \n 3. pepper-noise \n 4. gaussian-noise \n 5. uniform-noise \n 6. exponential-noise")
	ns_opt = int(input())
	noisy_img = nsm.noise(noise_models[ns_opt-1],distort_img,gray)

	deg_filename = fsc.getfilename(degrade_models[dg_opt-1],noise_models[ns_opt-1],k)
	deg_filename = deg_filename + "-" + image_name

	cv2.imshow('noise image',noisy_img)
	cv2.imwrite("degraded_images/"+deg_filename,noisy_img)
	cv2.waitKey(10)

	#Restoration through spatial filters
	print("Select a filter class \n 1. mean-filter \n 2. order-statistics-filter \n 3. Adaptive-filter \n ")
	fil_opt = int(input())
	restored_img,filter_ = sf.apply_filter(spatial_filters[fil_opt-1],noisy_img,gray)

	res_filename = filter_ + "-for-" + deg_filename 


	cv2.imshow('restored image',restored_img)
	cv2.imwrite("restored_images/"+res_filename,restored_img)
	cv2.waitKey(10000)

	cv2.destroyAllWindows()

	sys.exit()