 # 📊 Matplotlib

Matplotlib is a Python visualization library used for creating static, animated, and interactive plots.

The main module is pyplot which works like plotting in MATLAB.


# 📥 Installation

pip install matplotlib

## 📥 Importing Pandas

import matplotlib as plt


## 📥Attributes

plt.plot(x, y, color='b', linestyle='--', marker='o', label='Line Label')
plt.title('Title Here')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.legend()
plt.show()

✔️ Use to show trends, lines, time-series data.
✔️ color, linestyle, marker are styling attributes.

🟦 2. Bar Graph

plt.bar(x, height, color='skyblue', width=0.5, label='Bar Label')
plt.xlabel('X-axis')
plt.ylabel('Values')
plt.title('Bar Graph Title')
plt.legend()
plt.show()
✔️ Used for categorical comparisons.
✔️ Adjust width for spacing, color for styling.

🥧 3. Pie Chart

plt.pie(sizes, labels=labels, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title('Pie Chart Title')
plt.show()
✔️ Use for percentage distributions.
✔️ explode pulls out slices, autopct shows % values.

📊 4. Histogram

plt.hist(data, bins=10, color='lightgreen', edgecolor='black')
plt.xlabel('Value Ranges')
plt.ylabel('Frequency')
plt.title('Histogram Title')
plt.show()
✔️ Used to show frequency distribution of numerical data.
✔️ bins defines the number of intervals (bars).

📦 5. Boxplot

plt.boxplot(data, vert=True, patch_artist=True)
plt.title('Boxplot Title')
plt.show()
✔️ Visualizes data spread (Q1, Median, Q3), Outliers.
✔️ Used to summarize percentiles & variability.

🪟 6. Subplots (Multiple Plots in One Figure)

plt.subplot(1, 2, 1)   # 1 row, 2 columns, 1st subplot
plt.plot(x, y1)

plt.subplot(1, 2, 2)   # 1 row, 2 columns, 2nd subplot
plt.bar(x, y2)

plt.suptitle('Main Title for All Subplots')
plt.show()
✔️ Used to create multiple plots in one figure.
✔️ subplot(nrows, ncols, index).

🎨 Common Plot Attributes
Attribute	Description
color	Line/bar/pie color (e.g., 'r', 'blue')
linestyle	Solid '-', Dashed '--', Dotted ':'
marker	Data point marker ('o', '*', '^')
label	Label for legends
title()	Title for the plot
xlabel()/ylabel()	Axis Labels
legend()	Displays the legend box
grid()	Adds grid lines to plot

✏️ Text, Annotations on Plots

plt.text(x, y, 'Annotation Text', fontsize=12, color='red')
✔️ Used to place text at specific (x,y) positions.

📐 Axis Limits & Scaling

plt.xlim(0, 100)
plt.ylim(0, 50)
plt.axis('equal')  # Equal scaling for x & y axes
📊 Save Plot to File
python
Copy
Edit
plt.savefig('filename.png', dpi=300)
✔️ Save the current figure as an image file.

📝 Summary:
Plot Type	Use Case
Line Plot	Trends over time
Bar Graph	Categorical Comparisons
Pie Chart	Percentage Distributions
Histogram	Frequency Distributions
Boxplot	Summary statistics (percentiles, outliers)
Subplots	Multiple graphs in a single figure

📑 Author: Sneha S S

Matplotlib is all about:

Defining data → Choosing plot type → Styling → Labels → Show/Save.

