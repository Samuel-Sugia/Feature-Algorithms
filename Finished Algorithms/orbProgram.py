
import numpy as np
import cv2

import sys
import time
wstart_time = time.time()
w, h = 30, 30;

Matrix = [[0 for x in range(w)] for y in range(h)] 

def orbAlg(fname1,fname2,threshold):

	img1 = cv2.imread(fname1)
	img2 = cv2.imread(fname2)

	# Detect the ORB key points and compute the descriptors for the two images
	orb = cv2.ORB_create()
	keyPoints1, descriptors1 = orb.detectAndCompute(img1, None)
	keyPoints2, descriptors2 = orb.detectAndCompute(img2, None)

	# Create brute-force matcher object
	bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

	# Match the descriptors
	matches = bf.match(descriptors1, descriptors2)

	
	#ratio of matches with keyPoints
	rpk1 = float(len(matches)) / len(keyPoints1)

	if (len(keyPoints1) >= len(keyPoints2)):
		rpk = float(len(matches)) / len(keyPoints2)	
		
	else:
		rpk = float(len(matches)) / len(keyPoints1)
		
	print("%.4f"% rpk)
	print(fname1)
	print(fname2)

	#threshold
	if rpk >= float(threshold):
		orbClassification = 1
	else:
		orbClassification = 0

	return orbClassification
	
def orb(thresh):
	count = 0 #x
	temp = 0  #y
	c=0
	start_time = time.time()
	for x in fileName:

		if count % 30 >= temp:
			count = count + 1
			if count%30 == 0:
				temp = temp + 1	
			continue		
		#comparing the images in fileName
		orbClass = orbAlg(fname1 = lines[count][0], fname2 = lines[count][1],threshold =thresh)

		Matrix[temp][count % 30] = orbClass

		print("Class "+str(Matrix[temp][count%30]))


		print(str(temp) +" " + str(count % 30))
		count = count + 1
		
		#adding to temp, mimicking a nested loops
		if count%30 == 0:
			temp = temp + 1	
		print(count)
		c +=1
		print(c)
		print("\n")

	#printing matrix to file
	matrixFile = open("orbMatrix_"+str(thresh)+"_.txt","w")
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

with open("fileNames.txt") as textFile:
    lines = [line.split() for line in textFile]

fileName = open("fileNames.txt","r")
orb(sys.argv[1])








