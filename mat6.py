# matplotlib marker to emphasize each point
import matplotlib.pyplot as plt
import numpy as np

ypoint=np.array([10,20,5,7])

plt.plot(ypoint,marker="o",ms=15,mfc='k')
plt.show()