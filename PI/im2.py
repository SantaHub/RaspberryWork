import os
import scipy
from scipy import misc
import matplotlib.pyplot as plt
img=misc.imread('/home/pi/im.jpg')
plt.axis('off')
lum_img=img[:,:,0]
imgplot=plt.imshow(lum_img)
imgplot.set_cmap('hot')
plt.colorbar()
plt.show()



