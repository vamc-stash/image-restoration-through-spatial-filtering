import numpy as np 

def degrade(degrade_type,img,gray):
	h = img.shape[0]
	w = img.shape[1]
	out_img = img.copy()

	print("input Kernel Size(odd numbers) for distorting image:  ")
	ksize = int(input())

	if degrade_type == "optical-blur":
		arr = (1.0/(ksize*ksize))*np.ones((ksize,ksize),dtype='float')

	elif degrade_type == "gaussian-blur":
		#generate ksize row of pascal triangle
		a = [] #contains 'ksize'th row elements of pascal traingle
		a.append(1)
		for i in range(ksize-1):
			b = []
			b.append(1)
			for j in range(1,len(a)):
				b.append(a[j-1]+a[j])
			b.append(1)
			a = b.copy()

		#get gaussian kernel by multiplying [pascal_row] of size k*1 with [pascal_row] of size 1*k
		arr = []
		tot = 0
		for i in range(len(a)):
			arr.append([])
			for j in range(len(a)):
				arr[i].append(a[i]*a[j])
				tot = tot + arr[i][j]
		print(tot)
		arr = (1.0/tot)*np.array(arr,dtype='float')
		
	elif degrade_type == "motion-blur":
		arr = np.zeros((ksize,ksize),dtype='float')
		print("select type of motion-blur : \n 1. vertical blur \n 2. horizontal blur \n")
		opt = int(input())
		if opt == 1:
			arr[:,int((ksize-1)/2)] = np.ones(ksize)
			arr = (1.0/ksize)*(arr)
		else:
			arr[int((ksize-1)/2),:] = np.ones(ksize)
			arr = (1.0/ksize)*(arr)

	
	x = (int)(ksize/2)

	#convolution-process
	
	if gray == "False":
		for i in range(x,h-x):
			for j in range(x,w-x):
				for t in range(0,3):
					Sum = 0
					for k in range(-1*(x),ksize-x):
						for l in range(-1*(x),ksize-x):
							a = img.item(i+k,j+l,t)
							p = arr[k+x,l+x]
							Sum = Sum + (a*p)
					out_img.itemset((i,j,t),Sum)
				
	else:
		for i in range(x,h-x):
			for j in range(x,w-x):
				Sum = 0
				for k in range(-1*(x),ksize-x):
					for l in range(-1*(x),ksize-x):
						a = img.item(i+k,j+l)
						p = arr[k+x,l+x]
						Sum = Sum + (a*p)

				out_img.itemset((i,j),Sum)

	return out_img,str(ksize)
