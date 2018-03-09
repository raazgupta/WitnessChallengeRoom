import pdb
import numpy
import matplotlib.pyplot as plt


blocksDictionary = {1:[[0,0],[1,1]],
			2:[[1,0],[2,1]],
			3:[[2,0],[3,1]],
			4:[[3,0],[4,1]],		
			5:[[0,1],[1,2]],
			6:[[1,1],[2,2]],
			7:[[2,1],[3,2]],
			8:[[3,1],[4,2]],
			9:[[0,2],[1,3]],
			10:[[1,2],[2,3]],
			11:[[2,2],[3,3]],
			12:[[3,2],[4,3]],
			13:[[0,3],[1,4]],
			14:[[1,3],[2,4]],
			15:[[2,3],[3,4]],
			16:[[3,3],[4,4]]
}

#sidesArray = [[2,1],[3,1],[5,1],[6,2],[7,2],[8,2],[11,1],[12,1]]
#sidesArray = [[2,3],[5,1]]
#sidesArray = [[1,1],[3,2],[6,2],[8,1],[10,2],[16,2]]
#sidesArray = [[2,1],[3,1],[6,3],[8,1],[11,2],[12,1],[14,2],[15,1]]
sidesArray = []

nextInput = ""
while nextInput != "s":
	nextInput = raw_input("Input:")
	if nextInput != "s" and nextInput != "b":
		if "-" in nextInput:
			blockNumber,numSides = nextInput.split('-')
			sidesArray.append([int(blockNumber),int(numSides)])		
	elif nextInput == 'b':
		sidesArray.pop()
	print sidesArray

print 'Solving...'

def checkSides(pathPoints,witnessGrid,finalCheck):
	
	#print witnessGrid
	#pdb.set_trace()
	
	
	
	for sideItem in sidesArray:
		
		blockNumber = sideItem[0]
		numLines = sideItem[1]
		gridItem = blocksDictionary[blockNumber]
		
		#create list of square sides
		giLowerCorner = gridItem[0]
		giUpperCorner = gridItem[1]
		side1 = [giLowerCorner,[giLowerCorner[0],giUpperCorner[1]]]
		side2 = [[giLowerCorner[0],giUpperCorner[1]],giUpperCorner]
		side3 = [giUpperCorner,[giUpperCorner[0],giLowerCorner[1]]]
		side4 = [giLowerCorner,[giUpperCorner[0],giLowerCorner[1]]]

		numLinesInPath = 0
		for pathPoint in pathPoints:
			if pathPoint == side1 or pathPoint == [side1[1],side1[0]]:
				numLinesInPath += 1
			if pathPoint == side2 or pathPoint == [side2[1],side2[0]]:
				numLinesInPath += 1
			if pathPoint == side3 or pathPoint == [side3[1],side3[0]]:
				numLinesInPath += 1
			if pathPoint == side4 or pathPoint == [side4[1],side4[0]]:
				numLinesInPath += 1
		
		if finalCheck == False:
			if numLinesInPath > numLines:
				return False
		else:
			if numLinesInPath != numLines:
				return False


	#if allCleared == True:
		#pdb.set_trace()
		#print witnessGrid

	return True

def plotPathPoints(pathPoints, witnessGrid):
	for pathPoint in pathPoints:
		firstPoint = pathPoint[0]
		secondPoint = pathPoint[1]
		x1 = firstPoint[0]
		x2 = secondPoint[0]
		y1 = firstPoint[1]
		y2 = secondPoint[1]
		plt.plot([x1,x2],[y1,y2],'o')
		witnessGridLabel1 = witnessGrid[firstPoint[0],firstPoint[1]]
		plt.annotate(str(int(witnessGridLabel1)),xy=(x1,y1),size=24)

	plt.axis('equal')
	plt.show()



def moveSteps(lengthOfPath,witnessGrid,startPoint,newPoint,endPoint,pathPoints):
	
	#pdb.set_trace()

	lengthOfPath = lengthOfPath + 1
	witnessGrid[newPoint[0],newPoint[1]] = lengthOfPath
	pathPoints.append([startPoint,newPoint])

	if newPoint == endPoint:
		if checkSides(pathPoints,witnessGrid,True) == True:
			print witnessGrid

			#Plot the pathPoints
			plotPathPoints(pathPoints,witnessGrid)

			pdb.set_trace()
		
	else:
		if checkSides(pathPoints,witnessGrid,False) == True:
			findPath(newPoint,endPoint,pathPoints,lengthOfPath,witnessGrid)
	
	pathPoints.pop()
	witnessGrid[newPoint[0],newPoint[1]] = 0
	lengthOfPath -= 1

	



def findPath(startPoint, endPoint, pathPoints, lengthOfPath, witnessGrid):

	#pdb.set_trace()
		
	(wgHeight,wgWidth) = witnessGrid.shape

	#Ability to move up, down, left, right, as long as you have not visited 
	#the new point before
	
	#Up
	newPoint = [startPoint[0],startPoint[1]+1]
	if newPoint[1] < wgHeight and witnessGrid[newPoint[0],newPoint[1]] == 0:
		moveSteps(lengthOfPath,witnessGrid,startPoint,newPoint,endPoint,pathPoints)

	#Right
	newPoint = [startPoint[0]+1,startPoint[1]]
	if newPoint[0] < wgWidth and witnessGrid[newPoint[0],newPoint[1]] == 0:
		moveSteps(lengthOfPath,witnessGrid,startPoint,newPoint,endPoint,pathPoints)



	
	#Down
	newPoint = [startPoint[0],startPoint[1]-1]
	if newPoint[1] >= 0 and witnessGrid[newPoint[0],newPoint[1]] == 0:
		moveSteps(lengthOfPath,witnessGrid,startPoint,newPoint,endPoint,pathPoints)

	

	#Left
	newPoint = [startPoint[0]-1,startPoint[1]]
	if newPoint[0] >= 0 and witnessGrid[newPoint[0],newPoint[1]] == 0:
		moveSteps(lengthOfPath,witnessGrid,startPoint,newPoint,endPoint,pathPoints)


		
	return False

#Main program
#pdb.set_trace()
witnessGridStart = numpy.zeros((5,5))
witnessGridStart[0,0] = -1

resultPath = findPath([0,0],[4,4],[],0,witnessGridStart)
if resultPath == False:
	print "No solution"
