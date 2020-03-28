import numpy as np 
import random


def median(a):
	a.sort()
	mid = len(a)//2
	median = (a[mid]+a[~mid])/2 # ~(negation) performs operation from rear end
	return median

def apply_filter(filter_class,img,gray):

	if gray == "True":
		return apply_filter_for_gray_image(filter_class,img) 

	out_img = img.copy()

	if filter_class == "mean-filter":

		print("select type of a mean filter: \n 1: Arithmetic Mean Filter \n 2. Geometric Mean Filter \n 3. Harmonic Mean Filter \n 4. Contraharmonic Mean Filter \n")
		filter_type = int(input())

		print("Input Filter size(odd numbers) : ")
		filter_size = int(input())

		x = (int)(filter_size/2)
		#print(img.shape)
		pad_img = np.pad(img,((x,x),(x,x),(0,0)), mode='constant')
		#print(pad_img)
		#print(pad_img.shape)
		r = pad_img.shape[0]
		c = pad_img.shape[1]
		
		if filter_type == 1:
			for i in range(x,r-x):
				for j in range(x,c-x):
					bsum,gsum,rsum = 0,0,0
					for k in range(-1*(x),filter_size-x):
						for l in range(-1*(x),filter_size-x):
							bsum = bsum + pad_img.item(i+k,j+l,0)
							gsum = gsum + pad_img.item(i+k,j+l,1) 
							rsum = rsum + pad_img.item(i+k,j+l,2)
					n = filter_size * filter_size
					bavg = bsum/n
					gavg = gsum/n
					ravg = rsum/n
					out_img.itemset((i-x,j-x,0),bavg)
					out_img.itemset((i-x,j-x,1),gavg)  
					out_img.itemset((i-x,j-x,2),ravg)

			filter_ = "Arithmetic_mean_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_

		elif filter_type == 2:
			for i in range(x,r-x):
				for j in range(x,c-x):
					bmul,gmul,rmul = 1,1,1
					for k in range(-1*(x),filter_size-x):
						for l in range(-1*(x),filter_size-x):
							bmul = bmul * pad_img.item(i+k,j+l,0)
							gmul = gmul * pad_img.item(i+k,j+l,1) 
							rmul = rmul * pad_img.item(i+k,j+l,2)
					n = filter_size * filter_size
					bgeo = bmul**(1.0/(float(n)))
					ggeo = gmul**(1.0/(float(n)))
					rgeo = rmul**(1.0/(float(n)))
					out_img.itemset((i-x,j-x,0),bgeo)
					out_img.itemset((i-x,j-x,1),ggeo)  
					out_img.itemset((i-x,j-x,2),rgeo)
			filter_ = "Geometic_mean_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_

		elif filter_type == 3:
			for i in range(x,r-x):
				for j in range(x,c-x):
					bsum,gsum,rsum = 0.00000000000001,0.00000000000001,0.00000000000001
					for k in range(-1*(x),filter_size-x):
						for l in range(-1*(x),filter_size-x):
							bs = 0.0 if pad_img.item(i+k,j+l,0) == 0 else 1/float(pad_img.item(i+k,j+l,0))
							gs = 0.0 if pad_img.item(i+k,j+l,1) == 0 else 1/float(pad_img.item(i+k,j+l,1))
							rs = 0.0 if pad_img.item(i+k,j+l,2) == 0 else 1/float(pad_img.item(i+k,j+l,2))
							bsum = bsum + bs
							gsum = gsum + gs
							rsum = rsum + rs
							#print(bsum,gsum,rsum)
					n = filter_size * filter_size
					bHar = float(n)/bsum
					gHar = float(n)/gsum
					rHar = float(n)/rsum
					out_img.itemset((i-x,j-x,0),bHar)
					out_img.itemset((i-x,j-x,1),gHar)  
					out_img.itemset((i-x,j-x,2),rHar)
			filter_ = "Harmonic_mean_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_

		elif filter_type == 4:
			print("Input 'Q' :")
			Q = int(input())
			for i in range(x,r-x):
				for j in range(x,c-x):
					bnum,gnum,rnum = 0,0,0
					bden,gden,rden = 0.00000000000001,0.00000000000001,0.00000000000001
					for k in range(-1*(x),filter_size-x):
						for l in range(-1*(x),filter_size-x):
							bval = 0 if (pad_img.item(i+k,j+l,0)) == 0 else (pad_img.item(i+k,j+l,0)**(Q))
							gval = 0 if (pad_img.item(i+k,j+l,1)) == 0 else (pad_img.item(i+k,j+l,1)**(Q))
							rval = 0 if (pad_img.item(i+k,j+l,2)) == 0 else (pad_img.item(i+k,j+l,2)**(Q))
							bnum = bnum + (bval*pad_img.item(i+k,j+l,0))
							bden = bden + (bval)
							gnum = gnum + (gval*pad_img.item(i+k,j+l,1))
							gden = gden + (gval)
							rnum = rnum + (rval*pad_img.item(i+k,j+l,2))
							rden = rden + (rval)
							#print(bden,gden,rden)
					bratio = bnum/bden
					gratio = gnum/gden
					rratio = rnum/rden
					out_img.itemset((i-x,j-x,0),bratio)
					out_img.itemset((i-x,j-x,1),gratio)  
					out_img.itemset((i-x,j-x,2),rratio)
			filter_ = "Contraharmonic_mean_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_

	elif filter_class == "order-statistics-filter":

		print("select type of a 'order-statistics-filter': \n 1. Median Filter \n 2. Max Filter \n 3. Min Filter \n 4.Midpoint Filter \n 5. Alpha-Trimmed Mean Filter \n")
		filter_type = int(input())

		print("Input Filter size(odd numbers) :\n")
		filter_size = int(input())

		x = (int)(filter_size/2)
		#print(img.shape)
		pad_img = np.pad(img,((x,x),(x,x),(0,0)), mode='constant')
		#print(pad_img)
		#print(pad_img.shape)
		r = pad_img.shape[0]
		c = pad_img.shape[1]

		
		if filter_type == 1:
			for i in range(x,r-x):
				for j in range(x,c-x):
					bList,gList,rList = [],[],[]
					for k in range(-1*(x),filter_size-x):
						for l in range(-1*(x),filter_size-x):
							bList.append(pad_img.item(i+k,j+l,0))
							gList.append(pad_img.item(i+k,j+l,1)) 
							rList.append(pad_img.item(i+k,j+l,2))

					out_img.itemset((i-x,j-x,0),median(bList))
					out_img.itemset((i-x,j-x,1),median(gList))  
					out_img.itemset((i-x,j-x,2),median(rList))
			filter_ = "Median_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_

		elif filter_type == 2:
			for i in range(x,r-x):
				for j in range(x,c-x):
					bMax,gMax,rMax = 0,0,0
					for k in range(-1*(x),filter_size-x):
						for l in range(-1*(x),filter_size-x):
							bMax = pad_img.item(i+k,j+l,0) if (pad_img.item(i+k,j+l,0)) > bMax else bMax 
							gMax = pad_img.item(i+k,j+l,1) if (pad_img.item(i+k,j+l,1)) > gMax else gMax 
							rMax = pad_img.item(i+k,j+l,2) if (pad_img.item(i+k,j+l,2)) > rMax else rMax

					out_img.itemset((i-x,j-x,0),bMax)
					out_img.itemset((i-x,j-x,1),gMax)  
					out_img.itemset((i-x,j-x,2),rMax)
			filter_ = "Max_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_

		elif filter_type == 3:
			for i in range(x,r-x):
				for j in range(x,c-x):
					bMin,gMin,rMin = 255,255,255
					for k in range(-1*(x),filter_size-x):
						for l in range(-1*(x),filter_size-x):
							bMin = pad_img.item(i+k,j+l,0) if (pad_img.item(i+k,j+l,0)) < bMin else bMin 
							gMin = pad_img.item(i+k,j+l,1) if (pad_img.item(i+k,j+l,1)) < gMin else gMin 
							rMin = pad_img.item(i+k,j+l,2) if (pad_img.item(i+k,j+l,2)) < rMin else rMin

					out_img.itemset((i-x,j-x,0),bMin)
					out_img.itemset((i-x,j-x,1),gMin)  
					out_img.itemset((i-x,j-x,2),rMin)
			filter_ = "Min_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_

		elif filter_type == 4:
			for i in range(x,r-x):
				for j in range(x,c-x):
					bMax,gMax,rMax = 0,0,0
					bMin,gMin,rMin = 255,255,255
					for k in range(-1*(x),filter_size-x):
						for l in range(-1*(x),filter_size-x):
							bMax = pad_img.item(i+k,j+l,0) if (pad_img.item(i+k,j+l,0)) > bMax else bMax 
							gMax = pad_img.item(i+k,j+l,1) if (pad_img.item(i+k,j+l,1)) > gMax else gMax 
							rMax = pad_img.item(i+k,j+l,2) if (pad_img.item(i+k,j+l,2)) > rMax else rMax
							bMin = pad_img.item(i+k,j+l,0) if (pad_img.item(i+k,j+l,0)) < bMin else bMin 
							gMin = pad_img.item(i+k,j+l,1) if (pad_img.item(i+k,j+l,1)) < gMin else gMin 
							rMin = pad_img.item(i+k,j+l,2) if (pad_img.item(i+k,j+l,2)) < rMin else rMin

					out_img.itemset((i-x,j-x,0),(bMax+bMin)/2)
					out_img.itemset((i-x,j-x,1),(gMax+gMin)/2)  
					out_img.itemset((i-x,j-x,2),(rMax+rMin)/2)
			filter_ = "Midpoint_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_

		elif filter_type == 5:
			for i in range(x,r-x):
				for j in range(x,c-x):
					bsum,gsum,rsum = 0,0,0
					for k in range(-1*(x),filter_size-x):
						for l in range(-1*(x),filter_size-x):
							bsum = bsum + pad_img.item(i+k,j+l,0)
							gsum = gsum + pad_img.item(i+k,j+l,1) 
							rsum = rsum + pad_img.item(i+k,j+l,2)
					n = filter_size * filter_size
					d = random.randint(0,n-1)
					bavg = bsum/(n-d)
					gavg = gsum/(n-d)
					ravg = rsum/(n-d)
					out_img.itemset((i-x,j-x,0),bavg)
					out_img.itemset((i-x,j-x,1),gavg)  
					out_img.itemset((i-x,j-x,2),ravg)
			filter_ = "Alphatrimmed_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_



def apply_filter_for_gray_image(filter_class,img):

	out_img = img.copy()

	if filter_class == "mean-filter":

		print("select type of a mean filter: \n 1: Arithmetic Mean Filter \n 2. Geometric Mean Filter \n 3. Harmonic Mean Filter \n 4. Contraharmonic Mean Filter \n")
		filter_type = int(input())

		print("Input Filter size(odd numbers) :\n")
		filter_size = int(input())

		x = (int)(filter_size/2)
		#print(img.shape)
		pad_img = np.pad(img,((x,x),(x,x)), mode='constant')
		#print(pad_img)
		#print(pad_img.shape)
		r = pad_img.shape[0]
		c = pad_img.shape[1]

		if filter_type == 1:
			for i in range(x,r-x):
				for j in range(x,c-x):
					gsum = 0
					for k in range(-1*(x),filter_size-x):
						for l in range(-1*(x),filter_size-x):
							gsum = gsum + pad_img.item(i+k,j+l)
					n = filter_size * filter_size
					gavg = gsum/n
					out_img.itemset((i-x,j-x),gavg)
			filter_ = "Arithmetic_mean_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_
		elif filter_type == 2:
			for i in range(x,r-x):
				for j in range(x,c-x):
					gmul = 1
					for k in range(-1*(x),filter_size-x):
						for l in range(-1*(x),filter_size-x):
							gmul = gmul * pad_img.item(i+k,j+l)
					n = filter_size * filter_size
					ggeo = gmul**(1.0/(float(n)))
					out_img.itemset((i-x,j-x),ggeo) 
			filter_ = "Geometic_mean_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_

		elif filter_type == 3:
			for i in range(x,r-x):
				for j in range(x,c-x):
					gsum = 0.00000000000001
					for k in range(-1*(x),filter_size-x):
						for l in range(-1*(x),filter_size-x):
							gs = 0.0 if pad_img.item(i+k,j+l) == 0 else 1/float(pad_img.item(i+k,j+l))
							gsum = gsum + gs
					n = filter_size * filter_size
					gHar = float(n)/gsum
					out_img.itemset((i-x,j-x),gHar)
			filter_ = "Harmonic_mean_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_

		elif filter_type == 4:
			print("Input 'Q' :")
			Q = int(input())
			for i in range(x,r-x):
				for j in range(x,c-x):
					gnum = 0
					gden = 0.00000000000001
					for k in range(-1*(x),filter_size-x):
						for l in range(-1*(x),filter_size-x):
							gval = 0 if (pad_img.item(i+k,j+l)) == 0 else (pad_img.item(i+k,j+l)**(Q))
							gnum = gnum + (gval*pad_img.item(i+k,j+l))
							gden = gden + (gval)
					gratio = gnum/gden
					out_img.itemset((i-x,j-x),gratio)
			filter_ = "Contraharmonic_mean_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_ 

	elif filter_class == "order-statistics-filter":

		print("select type of a 'order-statistics-filter': \n 1. Median Filter \n 2. Max Filter \n 3. Min Filter \n 4.Midpoint Filter \n 5. Alpha-Trimmed Mean Filter \n")
		filter_type = int(input())

		print("Input Filter size(odd numbers) :\n")
		filter_size = int(input())

		x = (int)(filter_size/2)
		#print(img.shape)
		pad_img = np.pad(img,((x,x),(x,x)), mode='constant')
		#print(pad_img)
		#print(pad_img.shape)
		r = pad_img.shape[0]
		c = pad_img.shape[1]

		if filter_type == 1:
			for i in range(x,r-x):
				for j in range(x,c-x):
					gList = []
					for k in range(-1*(x),filter_size-x):
						for l in range(-1*(x),filter_size-x):
							gList.append(pad_img.item(i+k,j+l))

					out_img.itemset((i-x,j-x),median(gList))
			filter_ = "Median_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_

		elif filter_type == 2:
			for i in range(x,r-x):
				for j in range(x,c-x):
					gMax = 0
					for k in range(-1*(x),filter_size-x):
						for l in range(-1*(x),filter_size-x):
							gMax = pad_img.item(i+k,j+l) if (pad_img.item(i+k,j+l)) > gMax else gMax 
					out_img.itemset((i-x,j-x),gMax)
			filter_ = "Max_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_

		elif filter_type == 3:
			for i in range(x,r-x):
				for j in range(x,c-x):
					gMin = 255
					for k in range(-1*(x),filter_size-x):
						for l in range(-1*(x),filter_size-x): 
							gMin = pad_img.item(i+k,j+l) if (pad_img.item(i+k,j+l)) < gMin else gMin 
					out_img.itemset((i-x,j-x),gMin)
			filter_ = "Min_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_

		elif filter_type == 4:
			for i in range(x,r-x):
				for j in range(x,c-x):
					gMax = 0
					gMin = 255
					for k in range(-1*(x),filter_size-x):
						for l in range(-1*(x),filter_size-x):
							gMax = pad_img.item(i+k,j+l) if (pad_img.item(i+k,j+l)) > gMax else gMax 
							gMin = pad_img.item(i+k,j+l) if (pad_img.item(i+k,j+l)) < gMin else gMin

					out_img.itemset((i-x,j-x),(gMax+gMin)/2)
			filter_ = "Midpoint_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_

		elif filter_type == 5:
			for i in range(x,r-x):
				for j in range(x,c-x):
					gsum = 0
					for k in range(-1*(x),filter_size-x):
						for l in range(-1*(x),filter_size-x):
							gsum = gsum + pad_img.item(i+k,j+l)
					n = filter_size * filter_size
					d = random.randint(0,n-1)
					gavg = gsum/(n-d)
					out_img.itemset((i-x,j-x),gavg)
			filter_ = "Alphatrimmed_"+str(filter_size)+"*"+str(filter_size)
			return out_img,filter_