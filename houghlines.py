import cv2
import numpy as np

img = cv2.imread('C:\\lanes21.jpg')
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
    print x1,y1,x2,y2
    s1=(y2-y1)/(x2-x1)
    if (y1>0):
        print "positive slope"
        if (s1>m):
            m=s1   
            f0=1
        else:
            f0=0
    else:
        s1=-s1
        print "negative slope"
        if (s1>n):
            n=s1
            g0=1
        else:
            g0=0
    if  (f0 == 1):
        y = 300
        x4 = x1+(y-y1)*(x2-x1)/(y2-y1)
    if  (g0 == 1):
        y = 300
        x5 = x1+(y-y1)*(x2-x1)/(y2-y1)
print x4
print x5
cv2.circle(img,(x4,300),5,(0,0,255),3)
cv2.circle(img,(x5,y),5,(0,0,255),3)
x6 = (x4 +x5)/2   
cv2.circle(img,(x6,300),5,(0,0,255),3)
cv2.imshow('houghlines3.jpg',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
