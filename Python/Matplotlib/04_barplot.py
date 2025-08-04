import matplotlib.pyplot as plt  # Correct import
import numpy as np

x = [2,8,10]
y = [11,16,9]

x2= [3,9,11]
y2 = [6,15,7,]

plt.bar(x,y,align='center')
plt.bar(x2,y2,color='g')
plt.title('Bar graph')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()