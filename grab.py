import cv2
vidcap = cv2.VideoCapture('vid.mp4')
success,image = vidcap.read()
count = 0
pic=0
success = True
while success:
	if count%14==0:
		cv2.imwrite("pic%d.jpg" % pic, image)     # save frame as JPEG file      
		pic+=1
	success,image = vidcap.read()
	print('Read a new frame: ', success)
	count += 1