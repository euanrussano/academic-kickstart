import numpy as np
import matplotlib.pyplot as plt
 
# Make a fake dataset:
height = [0.167]*6
x = np.arange(len(height))
 
# Create bars
plt.bar(x, height)
plt.ylim([0,1])
plt.xlabel('X')
plt.ylabel('p(X)')
plt.grid()

# Show graphic
plt.savefig('discrete.png')

