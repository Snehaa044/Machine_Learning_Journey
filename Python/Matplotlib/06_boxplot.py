import matplotlib.pyplot as plt 
import numpy as np

# Generating 3 datasets using list comprehension.
# Each dataset contains 100 random numbers from a normal distribution.
# The standard deviation (std) increases from 1 to 3.
# So, data[0] has std=1, data[1] has std=2, data[2] has std=3
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Print the generated data (list of 3 arrays)
print(data)

# Print the type of 'data' variable (should be <class 'list'>)
print(type(data))

# Plotting a Boxplot for the datasets.
# vert=True makes the boxplot vertical.
# patch_artist=True fills the boxes with color.
plt.boxplot(data, vert=True, patch_artist=True)

# Display the plot window
plt.show()
