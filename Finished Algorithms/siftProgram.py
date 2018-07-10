
import numpy as np
import cv2

import sys
import time
wstart_time = time.time()

w, h = 30, 30;

Matrix = [[0 for x in range(w)] for y in range(h)] 
siftFile = open("siftData.txt", "a")

def siftAlg(fname1,fname2):
	img1 = cv2.imread(fname1)
	img2 = cv2.imread(fname2)

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

	#ratio of matches with keyPoints
	rpk1 = float(len(goodMatches)) / len(keyPoints1)

	if (len(keyPoints1) >= len(keyPoints2)):
		rpk = float(len(goodMatches)) / len(keyPoints2)	
		#print("img1 has less points")
	else:
		rpk = float(len(goodMatches)) / len(keyPoints1)
		#print("img2 has less points")

	print("%.4f"% rpk)


	if rpk >= float(sys.argv[1]:
		siftClassification = 1
	else:
		siftClassification = 0
	
	siftFile.write(str("%.4f"% rpk))
	siftFile.write(" " + str(siftClassification))
	#siftFile.write(" " + str(userClassification))
	siftFile.write(str(" " + fname1) + " " + fname2 +"\n")
	
	#cv2.destroyAllWindows()
	return siftClassification	
	


with open("fileNames.txt") as textFile:
    lines = [line.split() for line in textFile]


fileName = open("fileNames.txt","r")
count = 0
temp = 0
c = 0
start_time = time.time()
for x in fileName:
	
	if count % 30 <= temp:
		count = count + 1
		if count%30 == 0:
			temp = temp + 1	
		continue		

	siftClass = siftAlg(fname1 = lines[count][0], fname2 = lines[count][1])

	Matrix[temp][count % 30] = siftClass

	print("Class "+str(Matrix[temp][count%30]))

	
	print(str(temp) +" " + str(count % 30))
	count = count + 1
	if count%30 == 0:
		temp = temp + 1	
	c +=1
	print(c)
	print(count)
	print("\n")

print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

#printing matrix to file
matrixFile = open("siftMatrix_"+sys.argv[1]+"_.txt","w")
for x in range(0,30):
	for y in range(0,30):
		if x == y:
			Matrix[x][y] = 1
		if y <= x:
			matrixFile.write(str(Matrix[y][x]) + " ")
			
		else:
			matrixFile.write(str(Matrix[x][y]) + " ")
		if y == 29:
			matrixFile.write("\n")

print("--- %s seconds ---" % (time.time() - start_time))

print("--- %s seconds ---" % (time.time() - wstart_time))
w, h = 30, 30;
cmatrix = [[0 for x in range(w)] for y in range(h)] 
siftFile = open("siftData.txt", "a")


matrixFile.close
siftFile.close
fileName.close










