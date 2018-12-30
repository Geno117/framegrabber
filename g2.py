#g2.py
#second version of the frame grabber
#doesn't uses VideoCapture properties as mit doesn't work with me phone
#grabs 50 +/- frames (limit of 3df zephyr program)


import cv2
import sys

if len(sys.argv)!=2:
	print str(sys.argv)
	print("g2 needs exactly 1 file.")
	sys.exit()

vid= sys.argv[1]
vidcap = cv2.VideoCapture(vid)
##
#frmecnt= vidcap.get(CV_CAP_PROP_FRAME_COUNT)
#print("Frame count is : ", str(frmecnt))
##
success,image = vidcap.read()
count = 0
pic=0
success = True

while success:
	success,image = vidcap.read()
	count += 1
print('Count is ' + str(count))
skip=round(count/50)
print('Skips every '+str(skip))
vidcap.release()


vidcap = cv2.VideoCapture(vid)
success,image = vidcap.read()
success = True
count =0
while success:
	if count%skip==0:
		cv2.imwrite("pic%d.jpg" % pic, image)     # save frame as JPEG file      
		pic+=1
	success,image = vidcap.read()
	count+=1
print('Done!')
print('%d pics generated'%pic)