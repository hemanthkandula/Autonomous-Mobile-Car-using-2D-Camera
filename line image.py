import RPi.GPIO as GPIO
import time
import numpy as np
import cv2
import math
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
pwml=GPIO.PWM(2,50)
pwmr=GPIO.PWM(4,50)
pwmmot=GPIO.PWM(14,50)
pwml.start(5.2)
pwmr.start(5.2)
pwmmot.start(30)


img = cv2.imread('C:\Users\Abhi\Downloads\\houghlines3.jpg')
#ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#cv2.imshow('bW',thresh1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5),0)
cv2.imshow('blur',blur)
edges = cv2.Canny(blur,50,150,apertureSize = 3)

lines = cv2.HoughLines(edges,1,np.pi/180,200)
m=0;
n=0;

for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    f0 = 1
    g0 = 1

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    
    m=(y2-y1)/(x2-x1)

    teta=math.atan(m)
    cv2.imshow(i,img)
        
    def change(k):
        pwm.ChangeDutyCycle(k)
        time.sleep(1)

    try:
            
        k = float(teta)
        k = (1+(float(k)/180))/20
        change(k)
    except KeyboardInterrupt:
        pwm.stop()
        gpio.cleanup()
        exit
        ## End the video loop
    if cv2.waitKey(1) == 27:  ## 27 - ASCII for escape key
            #cv2.imwrite('b7.jpg',frame)
         break
############################################
except UnicodeError:
    print 'no houghline'

except ArithmeticError:
    print 'slope infinite houghline'
############################################
## Close and exit
cv2.waitKey(0)    
cv2.destroyAllWindows()

