import matplotlib.pyplot as plt  # Correct import
import numpy as np

x = np.arange(0, 10)
y = np.arange(11, 21)

print("x =", x, "\n", "y =", y)

#Creating Subplots
plt.subplot(2,2,2) # 2 rows, 2 columns, second plot
plt.plot(x,y,'r*')

plt.subplot(3,3,1) # 3 rows, 3 columns, first plot
plt.plot(x,y,'g*--')
plt.show()


plt.subplot(2,3,4) # 2 rows, 3 columns,fourth plot
plt.plot(x,y,'b--')

plt.subplot(4,4,3) # 4 rows, 4 columns, third plot
plt.plot(x,y,'y')
plt.show()