# install fswebcam  -- sudo apt get-install fswebcam
#take image -- fswwebcamImage.jp

#At rasberry pi --- save as any.py
import os

os.system("fswebcam -p YUYV -d /dev/video0 /home/pi/image.jpg")
# to remove banner os.system("fswebcam -p YUYV -d /dev/video0 --no-banner /home/pi/image.jpg")


#At Terminal 
#Converting any.py to read or write format
sudo chmod +rw any.py
sudo python any.py

#To save image to another location
import scipy   
from scipy import misc  # or  import scipy.misc 
img = misc.imread('/home/pi/image.jpg')
misc.imsave('/home/pi/newName.jpg',img)


#Display image
# Install matplotlib ---Thi library is to display image
import matplotlib.pyplot as mb
import scipy.misc
import os
img = misc.imread('/home/pi/image.jpg')
mb.imshow(img)
# to remove axis --  mb.axis('off')
mb.show()