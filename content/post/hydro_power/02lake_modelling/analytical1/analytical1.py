import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0,10,0.1)
h = -2/np.pi *np.cos(t*np.pi) + 2/np.pi

plt.plot(t,h,'r-o', linewidth=1, fillstyle='none')
plt.xlabel('t')
plt.ylabel('h')
plt.ylim([0.0, 2.0])
plt.xlim([0.0, 10.0])
plt.grid()
plt.savefig('analytical1.png')
plt.show()
