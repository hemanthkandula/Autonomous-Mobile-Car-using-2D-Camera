mport numpy
import cv2
img = cv2.imread('a.png')



i = 1
j=2


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,i,(0,255,0),3)

M = cv2.moments(contours[i])
ix = int(M['m10']/M['m00'])
iy = int(M['m01']/M['m00'])
print "Centroid = ", ix, ", ", iy

cv2.circle(img,(ix,iy), 5, (0,0,255), -1)
##############################################################

cv2.drawContours(img,contours,j,(0,255,0),3)



N = cv2.moments(contours[j])
jx = int(N['m10']/N['m00'])
jy = int(N['m01']/N['m00'])
print "Centroid = ", jx, ", ", jy
cv2.circle(img,(jx,jy), 5, (0,0,255), -1)
#########################################
cv2.imshow('image',img)



midx=(ix+jx)/2
midy=(jx+jy)/2
print "Mid = ", midx, ", ", midy


cv2.circle(img,(midx,midy), 5, (0,0,255), -1)