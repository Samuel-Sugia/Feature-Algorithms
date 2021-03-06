'''
 Based on the following tutorial:
   http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_matcher/py_matcher.html
'''

import numpy as np
import cv2

import sys

img1 = cv2.imread(sys.argv[1])

img2 = cv2.imread(sys.argv[2])

# Load the images in gray scale
#img1 = cv2.imread('../data/box.png', 0)
#img2 = cv2.imread('../data/box_in_scene.png', 0)

# Detect the SIFT key points and compute the descriptors for the two images
sift = cv2.xfeatures2d.SIFT_create()
keyPoints1, descriptors1 = sift.detectAndCompute(img1, None)
keyPoints2, descriptors2 = sift.detectAndCompute(img2, None)


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
print(len(keyPoints1))
print

print("Number of keypoints in Image 2: ") 
print(len(keyPoints2))
print

print("Number of keypoints match amoung images")
print(len(goodMatches))
print 

#ratio of matches with keyPoints
rpk1 = float(len(goodMatches)) / len(keyPoints1)


if (len(keyPoints1) >= len(keyPoints2)):
	rpk = float(len(goodMatches)) / len(keyPoints2)	
	print("correct")
else:
	rpk = float(len(goodMatches)) / len(keyPoints1)
	print("wrong")

print("%.4f"% rpk)

# Draw the first 10 matches
result = cv2.drawMatchesKnn(img1, keyPoints1, img2, keyPoints2, goodMatches[:100], None)



# Display the results
cv2.imshow('BF matches SIFT, ONLY TOP 100', result)
print("Press 'SPACEBAR' to continue")
cv2.waitKey(0)

userClassification =input("Is this a match?: 0 = yes = 1 : ")
if rpk >= .35:
	siftClassification = 1
else:
	siftClassification = 0
siftFile = open("siftData.txt", "a")

siftFile.write(str("%.4f"% rpk))
siftFile.write(" " + str(siftClassification))
siftFile.write(" " + str(userClassification))
siftFile.write(str(" "+ sys.argv[1]) + " " +sys.argv[2]+"\n")


cv2.destroyAllWindows()

siftFile.close













