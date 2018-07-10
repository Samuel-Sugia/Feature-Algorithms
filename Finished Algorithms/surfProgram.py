
import numpy as np
import cv2

import sys
import time
wstart_time = time.time()

#creating a 30x30 matrix
w, h = 30, 30;
Matrix = [[0 for x in range(w)] for y in range(h)] 

def surfAlg(fname1,fname2):

	img1 = cv2.imread(fname1)
	img2 = cv2.imread(fname2)

	# Convert it to gray scale
	gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
	gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

	# Detect the SURF key points
	surf = cv2.xfeatures2d.SURF_create()
	keyPoints1, descriptors1 = surf.detectAndCompute(gray1, None)

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
	
	#ratio of matches with keyPoints
	rpk1 = float(len(goodMatches)) / len(keyPoints1)

	if (len(keyPoints1) >= len(keyPoints2)):
		rpk = float(len(goodMatches)) / len(keyPoints2)	
	
	else:
		rpk = float(len(goodMatches)) / len(keyPoints1)	

	print("%.4f"% rpk)

	#threshold
	if rpk >= float(sys.argv[1]):
		surfClassification = 1
	else:
		surfClassification = 0
	
	return surfClassification	
	
with open("fileNames.txt") as textFile:
    lines = [line.split() for line in textFile]


fileName = open("fileNames.txt","r")
count = 0 #x
temp = 0  #y
c = 0

start_time = time.time()
for names in fileName:
	if count % 30 >= temp:
		count = count + 1
		if count%30 == 0:
			temp = temp + 1	
		continue		

	surfClass = surfAlg(fname1 = lines[count][0], fname2 = lines[count][1])

	Matrix[temp][count % 30] = surfClass

	print("Class "+str(Matrix[temp][count%30]))
	print(lines[count][0] + " "+lines[count][1])

	count = count + 1
	#adding to temp, mimicking a nested loops
	if count%30 == 0:
		temp = temp + 1	

	c +=1
	print(c)
	print("\n")

#time it took to compare all the images
print("--- %s seconds ---" % (time.time() - start_time))


#printing matrix to file
matrixFile = open("surfMatrix_"+sys.argv[1]+"_.txt","w")
for x in range(0,30):
	for y in range(0,30):
		if x == y:
			Matrix[x][y] = 1
		if y >= x:
			matrixFile.write(str(Matrix[y][x]) + " ")
			
		else:
			matrixFile.write(str(Matrix[x][y]) + " ")
		if y == 29:
			matrixFile.write("\n")

#time it took the whole program to run
print("--- %s seconds ---" % (time.time() - wstart_time))












