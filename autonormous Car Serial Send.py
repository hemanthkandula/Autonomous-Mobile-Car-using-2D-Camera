import time
import numpy as np
import cv2
import math
import serial
import time
#The following line is for serial over GPIO
port = 'COM21'
ard = serial.Serial(port,9600)
cap = cv2.VideoCapture(1)
while(1):
 try:
 # Initialize camera

 ret,img = cap.read()
 
#cv2.imshow('a',img)
 #cv2.waitKey(0)
 blur = cv2.GaussianBlur(img, (5,5),0)
 gray = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
 #ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
 #cv2.imshow('blur',blur)
 edges = cv2.Canny(gray,100,150,apertureSize = 3)
 #.imshow('canny',edges)
 #cv2.waitKey(0)
 lines = cv2.HoughLines(edges,1,np.pi/180,150)
 m=0;
 n=0;
 mx=0;
 mn=180;
 teta=[]
 i=0
 a=0
 for rho,theta in lines[0]:
 a = np.cos(theta)
 b = np.sin(theta)
 x0 = a*rho
 y0 = b*rho
 x1 = int(x0 + 1000*(-b))
 y1 = int(y0 + 1000*(a))
 x2 = int(x0 - 1000*(-b))
 y2 = int(y0 - 1000*(a))

 
m=(y2-y1)/(x2-x1)


 teta=math.atan(m)
 teta = teta*180/3.14
 if(teta<0):
 teta =180+teta
 if (teta >mx and teta <135):
 mx=teta
 cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
 y = 300
 x4 = x1+(y-y1)*(x2-x1)/(y2-y1)
 #print x4
 y = 200
 x6 = x1+(y-y1)*(x2-x1)/(y2-y1)
 ##y=mx+k


 if (teta <mn and teta >25):
 cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
 mn= teta
 y = 300
 x5 = x1+(y-y1)*(x2-x1)/(y2-y1)
 #print x5
 y = 200
 x7 = x1+(y-y1)*(x2-x1)/(y2-y1)
 
# if teta <mn and teta
 if ((x5-x4)>50 and (x7-x6)>50):

 midx1 =(x4+x5)/2
 midx2 = (x6+x7)/2

 midy = 300

 cv2.circle(img,(midx1,300),5,(0,0,255),-1)

 cv2.circle(img,(midx2,200),5,(0,0,255),-1)


 h= 100/(midx1-midx2)
 #print h

 a=math.atan(h)
 a=a*180/3.14
 a=180-a

 ard.flush()

 if(a>180):
 a=a-180
 print a
 cv2.imshow('h',img)

 
 #print (s)
 if(a>60 and a<65):
 ard.write('6')
 if(a>65 and a<70):
 ard.write('7')
 if(a>70 and a<75):
 ard.write('8')
 if(a>75 and a<80):
 ard.write('9')
 if(a>80 and a<85):
 ard.write('a')
 if(a>85 and a<95):
 ard.write('5')
 if(a>95 and a<100):
 ard.write('0')
 if(a>100 and a<105):
 ard.write('1')
 if(a>105 and a<110):
 ard.write('2')
 if(a>110 and a<115):
 ard.write('3')
 if(a>115 and a<120):
 ard.write('4')

 time.sleep(.2)



 
 #msg = ard.readline()
 #print ("Message from arduino: ")
 #print (msg)
 #time.sleep(1)

 ## End the video loop
 if cv2.waitKey(1) == 27: ## 27 - ASCII for escape key
 #cv2.imwrite('b7.jpg',frame)
 break
############################################
 except TypeError:
 print 'no houghline'
 except ArithmeticError:
 print 'slope infinite houghline'
############################################
## Close and exit
cap.release()
cv2.destroyAllWindows()
