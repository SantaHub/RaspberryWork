import os
import scipy
from scipy import misc
import matplotlib.pyplot as plt
img=misc.imread('/home/pi/im.jpg')
plt.imshow(img)
plt.axis('off')
plt.show()
