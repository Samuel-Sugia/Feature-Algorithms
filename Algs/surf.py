'''
 Based on the following tutorial:
   http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_surf_intro/py_surf_intro.html
'''

import numpy as np
import cv2

import sys

img = cv2.imread(sys.argv[1])


# Convert it to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect the SURF key points
surf = cv2.xfeatures2d.SURF_create()
keyPoints, descriptors = surf.detectAndCompute(gray, None)

# Paint the key points over the original image
result = cv2.drawKeypoints(img, keyPoints, None, flags=2)

# Display the results
cv2.imshow('Key points', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
