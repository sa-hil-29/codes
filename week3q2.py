import numpy as np
from scipy import stats
data = np.array([13,15,16,16,19,20,20,21,22,22,25,25,25,25,30,33,33,35,35,35,35,36,40,45,46,52,70])
#mean of data
mean = np.mean(data)
#median of data
median = np.median(data)
#mode of data
data_mode = stats.mode(data)
#first quartile Q1
Q1 = np.percentile(data,25)
#third quartile Q3
Q3 = np.percentile(data,75)
print("Mean of data is: ",mean)
print("Median of data is: ",median)
print("Mode of data is: ",data_mode.mode)
print("First quartile of data is: ",Q1)
print("Third quartile of data is: ",Q3)
