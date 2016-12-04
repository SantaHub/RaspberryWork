from imgproc import *
import time 
cam = Camera(320,240)
while(1):
	image = cam.grabImage()
	view = Viewer(image.width, image.height,"blob finding")
	view.displayImage(image)
	

