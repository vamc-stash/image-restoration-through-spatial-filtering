
degrade_dict = {
                   "optical-blur" : "optical" , 
                   "gaussian-blur" : "gauss" , 
                   "motion-blur" : "motion"
                  }
noise_dict = {
                  "salt-and-pepper-noise" : "sap" , 
                  "salt-noise" : "salt" , 
                  "pepper-noise" :"pepper" , 
                  "gaussian-noise" : "gauss" , 
                  "uniform-noise" : "uniform" ,
                   "exponential-noise" : "exponential"
                  }
def getfilename(distort_type,noise_type,kernel_size):
	return degrade_dict[distort_type] + "_" + kernel_size +"_plus_" + noise_dict[noise_type]

