import cv

cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
camera_index = 0
capture = cv.CaptureFromCAM(camera_index)

def repeat():
 global capture #declare as globals since we are assigning to them now	
 global camera_index
 frame = cv.QueryFrame(capture)
 cv.ShowImage("w1", frame)
 c = cv.WaitKey(10)
 if(c=='n'):
	camera_index += 1 #try the next camera index
	capture = cv.CaptureFromCAM(camera_index)
 if not capture:
	camera_index = 0
	capture = cv.CaptureFromCAM(camera_index)

while True:
	repeat()