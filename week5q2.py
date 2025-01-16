import numpy as np
from scipy import stats
data = np.array([15,16,16,19,20,20,21,22,22,25,25,25,25,30,33,33,35,35,35,35,36,40,45,46,52,70])
#max value of data
maxvalue = np.max(data)
#min value of data
minvalue = np.min(data)
#std deviation
stdDeviation = np.std(data)
# variance of data
variance = np.var(data)
print("Max value in dataset is :",maxvalue)
print("Min value in dataset is :",minvalue)
print("Standard deviation of dataset is :",stdDeviation)
print("variance of dataset is :",variance)
