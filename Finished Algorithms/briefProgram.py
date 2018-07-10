
import numpy as np
import cv2

import sys
import time

#start timer
wstart_time = time.time()

#creating a 30x30 matrix
w, h = 30, 30;
Matrix = [[0 for x in range(w)] for y in range(h)] 

with open("fileNames.txt") as textFile:
    lines = [line.split() for line in textFile]


fileName = open("fileNames.txt","r")

def briefAlg(fname1,fname2,threshold):

	img1 = cv2.imread(fname1)
	img2 = cv2.imread(fname2)

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
		briefClassification = 1
	else:
		briefClassification = 0

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
	return briefClassification	
	
def brief(thresh):
	count = 0 #x
	temp = 0  #y
	c = 0	
	for names in fileName:
		if count % 30 >=temp:
			count = count + 1
			if count%30 == 0:
				temp = temp + 1	
			continue				
		#comparing the images in fileName
		briefClass = briefAlg(fname1 = lines[count][0], fname2 = lines[count][1],threshold = thresh)
	
		Matrix[temp][count % 30] = briefClass

		print("Class "+str(Matrix[temp][count%30]))
	
		count = count + 1

		#adding to temp, mimicking a nested loops		
		if count%30 == 0:
			temp = temp + 1	

		print(count)
		c +=1
		print(c)
		print("\n")

	#printing matrix to file
	matrixFile = open("briefMatrix_"+str(thresh)+"_.txt","w")
	for x in range(0,30):
		for y in range(0,30):
			if y==x:
				Matrix[x][y] = 1
			if y >= x:
				matrixFile.write(str(Matrix[y][x]) + " ")
			
			else:
				matrixFile.write(str(Matrix[x][y]) + " ")
			if y == 29:
				matrixFile.write("\n")


#main
brief(sys.argv[1])			










