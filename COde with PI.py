import RPi.GPIO as GPIO
import time
import numpy as np
import cv2
import math
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
pwml=GPIO.PWM(2,50)
pwmr=GPIO.PWM(4,50)
pwmmot.start(30)
def change(k):
 pwml.ChangeDutyCycle(k)
 pwmr.ChangeDutyCycle(k)
 time.sleep(1)
cap = cv2.VideoCapture(0)
while(1):
 try:
 # Initialize camera
 ############################################
 ############################################
 ## Video Loop


 
## Read the image
 ret, img = cap.read()
 blur = cv2.GaussianBlur(img, (5,5),0)
 gray = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
 #ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
 #cv2.imshow('blur',blur)
 edges = cv2.Canny(gray,100,150,apertureSize = 3)
 #cv2.imshow('canny',edges)
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

 k=math.atan(h)
 k=k*180/3.14
 k=180-k
 
 ard.flush()

 if(k>180):
 k=k-180
 print k
 cv2.imshow('h',img)
 if(a>60 and a<120):

 cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
 k = float(teta)
 k = (1+(float(k)/20))
 change(k)
 if(a<60 and a>45):
 
 cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
 teta =70
 k = float(teta)
 k = (1+(float(k)/20))
 change(k)
 if(a<135 and a>120):
 teta=130
 cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
 teta =60
 k = float(teta)
 k = (1+(float(k)/20))
 change(k)
 #cv2.imshow('a',img)
 #cv2.imshow('edg',edges)





 
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
