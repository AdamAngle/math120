"""
Python Basic Frequency Table Generator
"""

import numpy as np
import matplotlib.pyplot as plt

# If you would like a customized table, you may enter it below:

title = 'Time Taken for McDonald\'s Drive-Thru Orders'

data = [
    ['75-124', 11],
    ['125-174', 24],
    ['175-224', 10],
    ['225-275', 3],
    ['275-324', 2]
]

column_labels = ['Class', 'Frequency', 'Relative Frequency', 'Cumulative Frequency']

# Number of rows
n_rows = len(data)

# Find the summation of all frequencies
total_freq = sum([r[1] for r in data])

# Calculate the relative and cumulative frequencies
cmu_freq = 0
cell_text = []
for row in range(n_rows):
    cmu_freq += data[row][1]
    cell_text.append([
        data[row][0],
        data[row][1],
        '{0} ({1}%)'.format(data[row][1]/total_freq, (data[row][1]/total_freq)*100),
        '{0} ({1}%)'.format(cmu_freq, (cmu_freq/total_freq)*100)
        ])

# Initialize and show the table
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_title(title)
ax.set_axis_off()

table = ax.table(cellText=cell_text, colLabels=column_labels, loc='upper left')

fig.tight_layout()
plt.show()