import numpy as np 
import random


def median(a):
	a.sort()
	mid = len(a)//2
	median = (a[mid]+a[~mid])/2 # ~(negation) performs operation from rear end
	return median

def apply_filter(filter_class,img,gray):

	out_img = img.copy()

	if filter_class == "mean-filter":

		print("select type of a mean filter: \n 1: Arithmetic Mean Filter \n 2. Geometric Mean Filter \n 3. Harmonic Mean Filter \n 4. Contraharmonic Mean Filter \n")
		filter_type = int(input())

		print("Input Filter size(odd numbers) : ")
		filter_size = int(input())

		x = (int)(filter_size/2)
		n = filter_size * filter_size
		#print(img.shape)
		if gray == "False":
			pad_img = np.pad(img,((x,x),(x,x),(0,0)), mode='constant')
		else:
			pad_img = np.pad(img,((x,x),(x,x)), mode='constant')
		#print(pad_img)
		#print(pad_img.shape)
		r = pad_img.shape[0]
		c = pad_img.shape[1]
		
		if filter_type == 1:
			for i in range(x,r-x):
				for j in range(x,c-x):
					if gray == "False":
						for t in range(0,3):
							Sum = 0
							for k in range(-1*(x),filter_size-x):
								for l in range(-1*(x),filter_size-x):
									Sum = Sum + pad_img.item(i+k,j+l,t)

							Avg = float(Sum/n)
							out_img.itemset((i-x,j-x,t),Avg)

					else:
						Sum = 0
						for k in range(-1*(x),filter_size-x):
							for l in range(-1*(x),filter_size-x):
								Sum = Sum + pad_img.item(i+k,j+l)

						Avg = float(Sum/n)
						out_img.itemset((i-x,j-x),Avg)
					
			filter_ = "Arithmetic_mean_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_

		elif filter_type == 2:
			for i in range(x,r-x):
				for j in range(x,c-x):
					if gray == "False":
						for t in range(0,3):
							Mul = 1
							for k in range(-1*(x),filter_size-x):
								for l in range(-1*(x),filter_size-x):
									Mul = Mul * pad_img.item(i+k,j+l,t)

							Geo = Mul**(1.0/(float(n)))
							out_img.itemset((i-x,j-x,t),Geo)
					else:
						Mul = 1
						for k in range(-1*(x),filter_size-x):
							for l in range(-1*(x),filter_size-x):
								Mul = Mul * pad_img.item(i+k,j+l)

						Geo = Mul**(1.0/(float(n)))
						out_img.itemset((i-x,j-x),Geo)
							
			filter_ = "Geometic_mean_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_

		elif filter_type == 3:
			for i in range(x,r-x):
				for j in range(x,c-x):
					if gray == "False":
						for t in range(0,3):
							Isum = 0.00000000000001
							for k in range(-1*(x),filter_size-x):
								for l in range(-1*(x),filter_size-x):
									Is = 0.0 if pad_img.item(i+k,j+l,t) == 0 else 1/float(pad_img.item(i+k,j+l,t))
									Isum = Isum + Is
									
							Har = float(n/Isum)
							out_img.itemset((i-x,j-x,t),Har)
					else:
						Isum = 0.00000000000001
						for k in range(-1*(x),filter_size-x):
							for l in range(-1*(x),filter_size-x):
								Is = 0.0 if pad_img.item(i+k,j+l) == 0 else 1/float(pad_img.item(i+k,j+l))
								Isum = Isum + Is
									
						Har = float(n/Isum)
						out_img.itemset((i-x,j-x),Har)
											
			filter_ = "Harmonic_mean_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_

		elif filter_type == 4:
			print("Input 'Q' :")
			Q = int(input())
			for i in range(x,r-x):
				for j in range(x,c-x):
					if gray == "False":
						for t in range(0,3):
							num = 0.0
							den = 0.00000000000001
							for k in range(-1*(x),filter_size-x):
								for l in range(-1*(x),filter_size-x):
									val = 0 if (pad_img.item(i+k,j+l,t)) == 0 else (pad_img.item(i+k,j+l,t)**(Q))
									num = num + (val*pad_img.item(i+k,j+l,t))
									den = den + (val)
							ratio = float(num/den)
							out_img.itemset((i-x,j-x,t),ratio)
					else:
						num = 0.0
						den = 0.00000000000001
						for k in range(-1*(x),filter_size-x):
							for l in range(-1*(x),filter_size-x):
								val = 0 if (pad_img.item(i+k,j+l)) == 0 else (pad_img.item(i+k,j+l)**(Q))
								num = num + (val*pad_img.item(i+k,j+l))
								den = den + (val)
						ratio = float(num/den)
						out_img.itemset((i-x,j-x),ratio)
					
			filter_ = "Contraharmonic_mean_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_

	elif filter_class == "order-statistics-filter":

		print("select type of a 'order-statistics-filter': \n 1. Median Filter \n 2. Max Filter \n 3. Min Filter \n 4.Midpoint Filter \n 5. Alpha-Trimmed Mean Filter \n")
		filter_type = int(input())

		print("Input Filter size(odd numbers) :\n")
		filter_size = int(input())

		x = (int)(filter_size/2)
		n = filter_size * filter_size
		#print(img.shape)
		if gray == "False":
			pad_img = np.pad(img,((x,x),(x,x),(0,0)), mode='constant')
		else:
			pad_img = np.pad(img,((x,x),(x,x)), mode='constant')
		#print(pad_img)
		#print(pad_img.shape)
		r = pad_img.shape[0]
		c = pad_img.shape[1]

		
		if filter_type == 1:
			for i in range(x,r-x):
				for j in range(x,c-x):
					if gray == "False":
						for t in range(0,3):
							List = []
							for k in range(-1*(x),filter_size-x):
								for l in range(-1*(x),filter_size-x):
									List.append(pad_img.item(i+k,j+l,t))

							out_img.itemset((i-x,j-x,t),median(List))
					else:
						List = []
						for k in range(-1*(x),filter_size-x):
							for l in range(-1*(x),filter_size-x):
								List.append(pad_img.item(i+k,j+l))

						out_img.itemset((i-x,j-x),median(List))
				
			filter_ = "Median_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_

		elif filter_type == 2:
			for i in range(x,r-x):
				for j in range(x,c-x):
					if gray == "False":
						for t in range(0,3):
							Max = 0
							for k in range(-1*(x),filter_size-x):
								for l in range(-1*(x),filter_size-x):
									Max = pad_img.item(i+k,j+l,t) if (pad_img.item(i+k,j+l,t)) > Max else Max

							out_img.itemset((i-x,j-x,t),Max)
					else:
						Max = 0
						for k in range(-1*(x),filter_size-x):
							for l in range(-1*(x),filter_size-x):
								Max = pad_img.item(i+k,j+l) if (pad_img.item(i+k,j+l)) > Max else Max

						out_img.itemset((i-x,j-x),Max)

			filter_ = "Max_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_

		elif filter_type == 3:
			for i in range(x,r-x):
				for j in range(x,c-x):
					if gray == "False":
						for t in range(0,3):
							Min = 255
							for k in range(-1*(x),filter_size-x):
								for l in range(-1*(x),filter_size-x):
									Min = pad_img.item(i+k,j+l,t) if (pad_img.item(i+k,j+l,t)) < Min else Min 

							out_img.itemset((i-x,j-x,t),Min)
					else:
						Min = 255
						for k in range(-1*(x),filter_size-x):
							for l in range(-1*(x),filter_size-x):
								Min = pad_img.item(i+k,j+l) if (pad_img.item(i+k,j+l)) < Min else Min 

						out_img.itemset((i-x,j-x),Min)
					
			filter_ = "Min_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_

		elif filter_type == 4:
			for i in range(x,r-x):
				for j in range(x,c-x):
					if gray == "False":
						for t in range(0,3):
							Max = 0
							Min = 255
							for k in range(-1*(x),filter_size-x):
								for l in range(-1*(x),filter_size-x):
									Max = pad_img.item(i+k,j+l,t) if (pad_img.item(i+k,j+l,t)) > Max else Max 
									Min = pad_img.item(i+k,j+l,t) if (pad_img.item(i+k,j+l,t)) < Min else Min

							out_img.itemset((i-x,j-x,t),(Max+Min)/2)
					else:
						Max = 0
						Min = 255
						for k in range(-1*(x),filter_size-x):
							for l in range(-1*(x),filter_size-x):
								Max = pad_img.item(i+k,j+l) if (pad_img.item(i+k,j+l)) > Max else Max 
								Min = pad_img.item(i+k,j+l) if (pad_img.item(i+k,j+l)) < Min else Min

						out_img.itemset((i-x,j-x),(Max+Min)/2)
					
			filter_ = "Midpoint_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_

		elif filter_type == 5:
			d = random.randint(0,n-1)
			for i in range(x,r-x):
				for j in range(x,c-x):
					if gray == "False":
						for t in range(0,3):
							Sum = 0
							tmp = []
							for k in range(-1*(x),filter_size-x):
								for l in range(-1*(x),filter_size-x):
									tmp.append(pad_img.item(i+k,j+l,t))
							arr = np.sort(np.array(tmp))
							if d%2 == 1:
								s = np.floor((d/2)+1)
								e = arr.size-np.floor((d/2))
								for i in range(int(s),int(e)):
									Sum += arr[i]
							else:
								s = np.floor(d/2)
								e = arr.size-np.floor((d/2))
								for i in range(int(s),int(e)):
									Sum += arr[i]
							avg = float(Sum/(n-d))
							out_img.itemset((i-x,j-x,t),avg)
					else:
						tmp = []
						Sum = 0
						for k in range(-1*(x),filter_size-x):
							for l in range(-1*(x),filter_size-x):
								tmp.append(pad_img.item(i+k,j+l))
						arr = np.sort(np.array(tmp))
						if d%2 == 1:
							s = np.floor((d/2)+1)
							e = arr.size-np.floor((d/2))
							for i in range(int(s),int(e)):
								Sum += arr[i]
						else:
							s = np.floor(d/2)
							e = arr.size-np.floor((d/2))
							for i in range(int(s),int(e)):
								Sum += arr[i]
						avg = float(Sum/(n-d))
						out_img.itemset((i-x,j-x),avg)
					
			filter_ = "Alphatrimmed_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_

	elif filter_class == "Adaptive-filter":

		print("select type of a 'Adaptive-filter': \n 1.Local noise reduction filter \n")
		filter_type = int(input())

		print("Input Filter size(odd numbers) :\n")
		filter_size = int(input())

		x = (int)(filter_size/2)
		#print(img.shape)
		if gray == "False":
			pad_img = np.pad(img,((x,x),(x,x),(0,0)), mode='constant')
			local_mean = np.zeros((img.shape[0],img.shape[1],img.shape[2]),dtype='float')
			local_variance = np.zeros((img.shape[0],img.shape[1],img.shape[2]),dtype='float')
		else:
			pad_img = np.pad(img,((x,x),(x,x)), mode='constant')
			local_mean = np.zeros((img.shape[0],img.shape[1]),dtype='float')
			local_variance = np.zeros((img.shape[0],img.shape[1]),dtype='float')

		r = pad_img.shape[0]
		c = pad_img.shape[1]

		if filter_type == 1: 
			n = filter_size * filter_size
			for i in range(x,r-x):
					for j in range(x,c-x):
						if gray == "False":
							for t in range(0,3):
								sr = i-x
								er = i+filter_size-x
								sc = j-x
								ec = j+filter_size-x

								tmp = pad_img[sr:er,sc:ec,t]

								mean = np.mean(tmp)
								var = np.var(tmp)

								local_mean.itemset((i-x,j-x,t),mean)
								local_variance.itemset((i-x,j-x,t),var)
						else:
							sr = i-x
							er = i+filter_size-x
							sc = j-x
							ec = j+filter_size-x

							tmp = pad_img[sr:er,sc:ec]

							mean = np.mean(tmp)
							var = np.var(tmp)

							local_mean.itemset((i-x,j-x),mean)
							local_variance.itemset((i-x,j-x),var)

			r = img.shape[0]
			c = img.shape[1]

			if gray == "False":
				for t in range(0,3):
					avg_noise_var = np.mean(local_variance[:,:,t])
					for i in range(0,r-1):
						for j in range(0,c-1):
							if avg_noise_var > local_variance[i,j,t]:
								local_variance.itemset((i,j,t), avg_noise_var)
					avg_local_var = np.mean(local_variance[:,:,t])
					ratio_ = (float(avg_noise_var/avg_local_var))
					if ratio_ > 1.0:
						ratio_ = 1.0
					out_img[:,:,t] = img[:,:,t] - ((ratio_)*(img[:,:,t] - local_mean[:,:,t]))
			else:
				avg_noise_var = np.mean(local_variance[:,:])
				for i in range(0,r-1):
					for j in range(0,c-1):
						if avg_noise_var > local_variance[i,j]:
							local_variance.itemset((i,j), avg_noise_var)
				avg_local_var = np.mean(local_variance[:,:])
				ratio_ = (float(avg_noise_var/avg_local_var))
				if ratio_ > 1.0:
						ratio_ = 1.0
				out_img[:,:] = img[:,:] - ((ratio_)*(img[:,:] - local_mean[:,:]))

			filter_ = "Adaptive_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_


		