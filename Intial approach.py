import numpy
import cv2


img = cv2.imread('C:\Users\Abhi\Downloads\\l.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
image,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


ix=[]
iy=[]
jx=[]
jy=[]
midx=[]
midy=[]

for n in range(0,5):
    i=2*n
    
    cv2.drawContours(img,contours,i,(0,255,0),3)

    M = cv2.moments(contours[i])
    ix.insert(n, int(M['m10']/M['m00']))
    iy.insert(n, int(M['m01']/M['m00']))
    print "Centroid1 = ", ix[n], ", ", iy[n]

    cv2.circle(img,(ix[n],iy[n]), 5, (0,0,255), -1)
    #cv2.putText(image,i, (ix[n],iy[n]), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
##############################################################
for m in range(0,5):
    j=2*m+1
    cv2.drawContours(img,contours,j,(0,255,0),3)



    N = cv2.moments(contours[j])
    jx.insert(m, int(N['m10']/N['m00']))
    jy.insert(m, int(N['m01']/N['m00']))
    print "Centroid 2= ", jx[m], ", ", jy[m]
    cv2.circle(img,(jx[m],jy[m]), 5, (0,0,255), -1)
    #cv2.putText(image,j, (jx[m],jy[m]), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
#########################################
cv2.imshow('image',img)

for a in range(0,5):

    
    midx.insert(a,(ix[a]+jx[a])/2)
    midy.insert(a,(iy[a]+jy[a])/2)
    print (ix[a]-jx[a])             
    print "Mid = ", midx[a], ", ", midy[a]
    cv2.circle(img,(midx[a],midy[a]), 5, (255,255,255), -1)
 #   ard.write(midx[a])
#    ard.write(midy[a])

cv2.waitKey(0)



