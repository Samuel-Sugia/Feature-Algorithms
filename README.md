# Feature-Detection
These are implementations of the feature detection algorithms SIFT, SURF, ORB and BRIEF using opencv. Based on https://media.readthedocs.org/pdf/opencv-python-tutroals/latest/opencv-python-tutroals.pdf

Running algorithm on single image: python surf.py home.jpg

Comparing two images :python bfMatchingWithSURF.py home.jpg home_rotation1.jpg


NOTES:
-Some of the outputed images have been modify to only display their top 100 matches because it gets very cluster on an image that has over 100 matching points where you are unable to see the images.

-both bfMatchingWithSIFT.py and bfMatchingWithSURF are using the knn clasifier k = 2, while bfMatchingWithORB.py and bfMatchingWithBRIEF.py are using a brute force method with the below function call 
"bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)"
