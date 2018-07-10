'''
 Based on the following tutorial:
   http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_brief/py_brief.html
'''

import numpy as np
import cv2

import sys

img1 = cv2.imread(sys.argv[1])
img2 = cv2.imread(sys.argv[2])

# Convert it to gray scale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Detect the CenSurE key points
star = cv2.xfeatures2d.StarDetector_create()
keyPoints1 = star.detect(gray1, None)
keyPoints2 = star.detect(gray2, None)

# Create the BRIEF extractor and compute the descriptors
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()
keyPoints1, descriptors1 = brief.compute(img1, keyPoints1)
keyPoints2, descriptors2 = brief.compute(img2, keyPoints2)

# Create brute-force matcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match the descriptors
matches = bf.match(descriptors1, descriptors2)

# Printing results
print("Number of keypoints in Image 1: " ) 
print(keyPoints1.__len__())
print

print("Number of keypoints in Image 2: ") 
print(keyPoints2.__len__())
print

print("Number of keypoints match amoung images")
print(matches.__len__())
print 

# Sort them in by distance
matches = sorted(matches, key=lambda x:x.distance)

# Paint the key points over the original image
#result = cv2.drawKeypoints(img, keyPoints1, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Draw the first 10 matches
result = cv2.drawMatches(img1, keyPoints1, img2, keyPoints2, matches[:100], None)

# Display the results
cv2.imshow('BF matches BRIEF, ONLY TOP 100', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
