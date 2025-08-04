import matplotlib.pyplot as plt 
import numpy as np

# Labels for each slice of the pie
labels = ['Python', 'R', 'Java', 'Ruby']

# Size of each slice (they will automatically be converted to percentages)
size = [5, 30, 40, 25]  

# Colors for each slice
colors = ['gold', 'lightcoral', 'yellowgreen', 'lightskyblue']

# Optional "explode" to pull a slice out for emphasis (optional step)
explode = (0, 0.1, 0, 0)  # Only "Python" slice will explode (10% out)

# Plotting the Pie Chart
# size         : Sizes of each wedge.
# explode      : Tuple to "explode" a slice outward.
# labels       : Labels for each wedge.
# colors       : Colors for each wedge.
# autopct      : String formatting for displaying percentage on each wedge.
# shadow       : Draws a shadow below the pie chart.
plt.pie(size, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True)

# axis('equal') ensures the pie chart is a perfect circle, not an ellipse.
plt.axis('equal')

# Display the plot window.
plt.show()
