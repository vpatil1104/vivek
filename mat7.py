# matplotlib marker to emphasize each point
import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,1,2,3])
y=np.array([2,24,25,62])

plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("vivek")

x=np.array([0,1,2,3])
y=np.array([2,24,25,62])

plt.subplot(1,2,2)
plt.plot(x,y)
plt.title("patil")

plt.suptitle("my file")
plt.show()