import numpy as np
import matplotlib.pyplot as plt
 
# Make a fake dataset:
height = [1/12,5/12,5/12,1/12]
x = np.arange(len(height))
 
# Create bars
plt.bar(x, height)
plt.ylim([0,1])
plt.xlabel('X')
plt.ylabel('p(X)')
plt.grid()
plt.xticks(np.arange(0, 4)) 

# Show graphic
plt.savefig('student.png')

