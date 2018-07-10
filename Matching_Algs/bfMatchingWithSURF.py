'''
 Based on the following tutorial:
   http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_surf_intro/py_surf_intro.html
'''

import numpy as np
import cv2

import sys

img1 = cv2.imread(sys.argv[1])
img2 = cv2.imread(sys.argv[2])

# Convert it to gray scale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Detect the SURF key points
surf = cv2.xfeatures2d.SURF_create(hessianThreshold=50000, upright=True, extended=True)
keyPoints1, descriptors1 = surf.detectAndCompute(gray1, None)
print(keyPoints1.__len__())
keyPoints2, descriptors2 = surf.detectAndCompute(gray2, None)


# Create brute-force matcher object
bf = cv2.BFMatcher()

# Match the descriptors
matches = bf.knnMatch(descriptors1, descriptors2, k=2)

# Apply ratio test
goodMatches = []

for m, n in matches:
    if m.distance < 0.75 * n.distance:
        goodMatches.append([m])

# Printing results
print("Number of keypoints in Image 1: " ) 
print(keyPoints1.__len__())
print

print("Number of keypoints in Image 2: ") 
print(keyPoints2.__len__())
print

print("Number of keypoints match amoung images")
print(goodMatches.__len__())
print 

# Draw the first 10 matches
result = cv2.drawMatchesKnn(img1, keyPoints1, img2, keyPoints2, goodMatches[:100], None)

# Display the results
cv2.imshow('BF matches SURF, ONLY TOP 100', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
