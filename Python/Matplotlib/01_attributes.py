import matplotlib.pyplot as plt  # Correct import
import numpy as np

x = np.arange(0, 10)
y = np.arange(11, 21)

print("x =", x, "\n", "y =", y)

# Plotting the scatter points
plt.scatter(x, y, c='g')  # 'c' specifies color (green)

plt.title("Graph in 2D")  # Title of the plot
plt.xlabel("X-axis")      # Label for X-axis
plt.ylabel("Y-axis")      # Label for Y-axis

plt.savefig('Fig1.png')  # ✅ Save BEFORE plt.show(), otheriwse it will be blank
plt.show()               # Display the plot

plt.plot(x, y, 'r*')  # Plotting points at (x, y) using red (*) star markers
plt.show()            # Display the plot on the screen

# Plotting a dashed blue line with linewidth 5
plt.plot(x, y, color='b',marker='o', linestyle='dashed', linewidth=5, markersize=12)

plt.title("Dashed Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()