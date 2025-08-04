import matplotlib.pyplot as plt 
import numpy as np

x =np.array([2,3,4,2,3,2,11,34,29,76,87,88,97,45,36,10,1,58])
plt.hist(x)  # Plots a histogram of the data with their densities - frequency of elements in a particular range
plt.title('Histogram')
plt.show()