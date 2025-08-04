import matplotlib.pyplot as plt  # Correct import
import numpy as np

x = np.arange(0, 10)
y = 3 * x + 5
plt.plot(x,y)
plt.show() # Output: The plot of y = 3x + 5 is displayed.

# Compute a nd b coordinates for points on a sine curve
a = np.arange(0,4*np.pi,0.1)
b = np.sin(a)
c=np.cos(a) 

# Set up a subplot having 2 rows and 1 column as first plot 
plt.subplot(2,1,1)

# Make first plot sine wave
plt.plot(a,b,'ro')
plt.title("Sine Wave Form")

# Set up a subplot having 2 rows and 1 column as second plot 
plt.subplot(2,1,2)

plt.plot(a,c,'b-')
plt.title("Cosine Wave Form")

# Show the figure
plt.show() 
