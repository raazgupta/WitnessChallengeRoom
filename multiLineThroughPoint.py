import pdb
import numpy
import matplotlib.pyplot as plt

blocksDictionary = {1:[[2,0],[3,1]],
			2:[[2,1],[3,2]],
			3:[[2,2],[3,3]],
			4:[[2,3],[3,4]],
			5:[[2,4],[3,5]],
			6:[[2,5],[3,6]],
			7:[[1,0],[2,1]],
			8:[[1,1],[2,2]],
			9:[[1,2],[2,3]],
			10:[[1,3],[2,4]],
			11:[[1,4],[2,5]],
			12:[[1,5],[2,6]],
			13:[[0,0],[1,1]],
			14:[[0,1],[1,2]],
			15:[[0,2],[1,3]],
			16:[[0,3],[1,4]],
			17:[[0,4],[1,5]],
			18:[[0,5],[1,6]],
			19:[[5,0],[6,1]],
			20:[[5,1],[6,2]],
			21:[[5,2],[6,3]],
			22:[[5,3],[6,4]],
			23:[[5,4],[6,5]],
			24:[[5,5],[6,6]],
			25:[[4,0],[5,1]],
			26:[[4,1],[5,2]],
			27:[[4,2],[5,3]],
			28:[[4,3],[5,4]],
			29:[[4,4],[5,5]],
			30:[[4,5],[5,6]],
			31:[[3,0],[4,1]],
			32:[[3,1],[4,2]],
			33:[[3,2],[4,3]],
			34:[[3,3],[4,4]],
			35:[[3,4],[4,5]],
			36:[[3,5],[4,6]]
}

pointsArray = []
#pointsArray = [[3,2.5],[2.5,4],[1.5,5],[1.5,6],[0,2.5],[4,2.5],[5,4.5]]
#pointsArray = [[2.5,1],[1.5,0],[0,3.5],[4,1.5],[5,2.5],[1.5,4]]
#pointsArray = [[3,1],[3,4.5],[3.5,2],[5,1]]
#pointsArray = [[3,1]]
#pointsArray = [[4.0, 1.5], [4.0, 4.5], [4.5, 5.0], [4.5, 6.0], [1.5, 2.0], [1.5, 5.0],[5.5,1]]
#pointsArray = [[3.0, 5.5], [2.0, 0.5], [1.5, 2.0], [1.0, 5.5], [4.5, 6.0], [5.0, 1.5], [5.0, 5.5]]


#Direction of movement of the 2nd line
secondLineOppositeUpDown = 1
secondLineOppositeLeftRight = -1

#Enter the 2nd start point

nextInput = ""
nextInput = raw_input("2nd start point (x-y):")
if "-" in nextInput:
	x,y = nextInput.split('-')
	if float(x) == 0.0:
		x = 6.0
	secondStartPoint = [float(x),float(y)]
	if float(y) == 0.0:
		secondEndPoint = [float(x),6.0]
		secondLineOppositeUpDown = 1
	else:
		secondEndPoint = [float(x),0.0]
		secondLineOppositeUpDown = -1


nextInput = ""
nextInput = raw_input("2nd line Left/Right direction((s)ame/(o)pposite):")
if nextInput == "s":
	secondLineOppositeLeftRight = 1
else:
	secondLineOppositeLeftRight = -1

nextInput = ""
while nextInput != "s":
	nextInput = raw_input("Input:")
	if nextInput != "s" and nextInput != "b":
		if "-" in nextInput:
			x,y = nextInput.split('-')
			if float(x) == 0.0:
				x = 6.0
			pointsArray.append([float(x),float(y)])
	elif nextInput == 'b':
		pointsArray.pop()
	print pointsArray

print "Solving ..."

#pointsArray = [[1.5,4.0],[3.5,4.0],[4.5,2.0],[4.5,3.0],[5.0,0.5],[5.5,2.0],[0.0,0.5],[0.0,2.5]]
#print pointsArray

def midPoint(point1,point2):
	
	(wgHeight, wgWidth) = witnessGrid.shape

	if point1 == 0 and point2 == (wgWidth - 2):
		return (wgWidth - 2 + 0.5)
	elif point1 == (wgWidth - 1) and point2 == 1:
		return 0.5
	else:
		return (point1 + point2)/2.0
 

def checkPointMatch(pointItem,startPoint,endPoint):
	foundPoint = False
	if pointItem == startPoint:
		foundPoint = True
	elif pointItem == endPoint:
		foundPoint = True
	elif pointItem[0] == startPoint[0] and pointItem[0] == endPoint[0] and pointItem[1] == midPoint(startPoint[1],endPoint[1]):
		foundPoint = True
	elif pointItem[1] == startPoint[1] and pointItem[1] == endPoint[1] and pointItem[0] == midPoint(startPoint[0],endPoint[0]):
		foundPoint = True

	return foundPoint



def checkPoints(firstPathPoints,secondPathPoints,witnessGrid,finalCheck):

	

	for pointItem in pointsArray:
		foundPointItem = False
		for firstPathPoint in firstPathPoints:
			startPoint = firstPathPoint[0]
			endPoint = firstPathPoint[1]
			foundPointItem = checkPointMatch(pointItem,startPoint,endPoint)
			if foundPointItem == True:
				#print pointItem, startPoint, endPoint
				break			
	
		if foundPointItem == False:
			for secondPathPoint in secondPathPoints:
				startPoint = secondPathPoint[0]
				endPoint = secondPathPoint[1]
				foundPointItem = checkPointMatch(pointItem,startPoint,endPoint)
				if foundPointItem == True:
					#print pointItem,startPoint,endPoint
					break		

		if foundPointItem == False:	
			return False 
	#pdb.set_trace()
	return True


def plotPathPoints(firstPathPoints,secondPathPoints,witnessGrid):
	for pathPoint in firstPathPoints:
                firstPoint = pathPoint[0]
                secondPoint = pathPoint[1]
                x1 = firstPoint[0]
                x2 = secondPoint[0]
                y1 = firstPoint[1]
                y2 = secondPoint[1]
                plt.plot([x1,x2],[y1,y2],'o')
                witnessGridLabel1 = witnessGrid[firstPoint[0],firstPoint[1]]
                plt.annotate(str(int(witnessGridLabel1)),xy=(x1,y1),size=24)
	
	for pathPoint in secondPathPoints:
                firstPoint = pathPoint[0]
                secondPoint = pathPoint[1]
                x1 = firstPoint[0]
                x2 = secondPoint[0]
                y1 = firstPoint[1]
                y2 = secondPoint[1]
                plt.plot([x1,x2],[y1,y2],'x')
                witnessGridLabel1 = witnessGrid[firstPoint[0],firstPoint[1]]
                plt.annotate(str(int(witnessGridLabel1)),xy=(x1,y1),size=24)



        plt.axis('equal')
        plt.show() 
	

def moveSteps(lengthOfFirstPath, lengthOfSecondPath,witnessGrid,startFirstPoint,startSecondPoint,newFirstPoint,newSecondPoint,firstEndPoint,secondEndPoint,firstPathPoints,secondPathPoints):
	
	#pdb.set_trace()

	lengthOfFirstPath = lengthOfFirstPath + 1
	lengthOfSecondPath = lengthOfSecondPath + 1
	witnessGrid[newFirstPoint[0],newFirstPoint[1]] = lengthOfFirstPath
	witnessGrid[newSecondPoint[0],newSecondPoint[1]] = lengthOfSecondPath
	firstPathPoints.append([startFirstPoint,newFirstPoint])
	secondPathPoints.append([startSecondPoint,newSecondPoint])

	if newFirstPoint == firstEndPoint or newSecondPoint == secondEndPoint or newFirstPoint == secondEndPoint or newSecondPoint == firstEndPoint:
		#print witnessGrid
		#pdb.set_trace()
		if checkPoints(firstPathPoints,secondPathPoints,witnessGrid,True) == True:
			#print witnessGrid
			plotPathPoints(firstPathPoints,secondPathPoints,witnessGrid)
			pdb.set_trace()
	else:
		findPath(newFirstPoint,firstEndPoint,newSecondPoint,secondEndPoint,lengthOfFirstPath,lengthOfSecondPath,witnessGrid,firstPathPoints,secondPathPoints)

	firstPathPoints.pop()
	secondPathPoints.pop()
	witnessGrid[newFirstPoint[0],newFirstPoint[1]] = 0
	witnessGrid[newSecondPoint[0],newSecondPoint[1]] = 0
	lengthOfFirstPath -= 1
	lengthOfSecondPath -= 1
	



def findPath(firstStartPoint,firstEndPoint,secondStartPoint,secondEndPoint,lengthOfFirstPath,lengthOfSecondPath,witnessGrid,firstPathPoints,secondPathPoints):

	#pdb.set_trace()
	
	(wgHeight, wgWidth) = witnessGrid.shape

	#Ability to move up,down,left,right as long as you do not touch the other shapre or visit point that you have already visited before. Also able to go past the left and right edges of the grid.

	#Up 
	newFirstPoint = [firstStartPoint[0],firstStartPoint[1]+1]
	newSecondPoint = [secondStartPoint[0],secondStartPoint[1]+1*secondLineOppositeUpDown]
	if (newFirstPoint[1] < wgHeight) and (newSecondPoint[1] >= 0 and newSecondPoint[1] < wgHeight) and (witnessGrid[newFirstPoint[0],newFirstPoint[1]] == 0 and witnessGrid[newSecondPoint[0],newSecondPoint[1]] == 0):
		moveSteps(lengthOfFirstPath, lengthOfSecondPath,witnessGrid,firstStartPoint,secondStartPoint,newFirstPoint,newSecondPoint,firstEndPoint,secondEndPoint,firstPathPoints,secondPathPoints)


	#Right
	if (firstStartPoint[0] + 1) < wgWidth:
		newFirstPoint = [firstStartPoint[0]+1,firstStartPoint[1]]
	else:
		newFirstPoint = [1,firstStartPoint[1]]
	
	if (secondStartPoint[0] + 1*secondLineOppositeLeftRight) < wgWidth and (secondStartPoint[0] + 1*secondLineOppositeLeftRight) >= 0:
		newSecondPoint = [secondStartPoint[0] + 1*secondLineOppositeLeftRight,secondStartPoint[1]]
	elif (secondStartPoint[0] + 1*secondLineOppositeLeftRight) >= wgWidth:
		newSecondPoint = [1,secondStartPoint[1]]
	elif (secondStartPoint[0] + 1*secondLineOppositeLeftRight) < 0:
		newSecondPoint = [wgWidth - 2,secondStartPoint[1]]
	
	if witnessGrid[newFirstPoint[0],newFirstPoint[1]] == 0 and witnessGrid[newSecondPoint[0],newSecondPoint[1]] == 0:
		moveSteps(lengthOfFirstPath, lengthOfSecondPath,witnessGrid,firstStartPoint,secondStartPoint,newFirstPoint,newSecondPoint,firstEndPoint,secondEndPoint,firstPathPoints,secondPathPoints)


	#Down
	newFirstPoint = [firstStartPoint[0],firstStartPoint[1]-1]
	newSecondPoint = [secondStartPoint[0],secondStartPoint[1]-1*secondLineOppositeUpDown]
	if (newFirstPoint[1] >= 0) and (newSecondPoint[1] >= 0 and newSecondPoint[1] < wgHeight) and (witnessGrid[newFirstPoint[0],newFirstPoint[1]] == 0 and witnessGrid[newSecondPoint[0],newSecondPoint[1]] == 0):
		moveSteps(lengthOfFirstPath, lengthOfSecondPath,witnessGrid,firstStartPoint,secondStartPoint,newFirstPoint,newSecondPoint,firstEndPoint,secondEndPoint,firstPathPoints,secondPathPoints)


	#Left
	if (firstStartPoint[0] - 1) >= 0:
		newFirstPoint = [firstStartPoint[0]-1,firstStartPoint[1]]
	else:
		newFirstPoint = [wgWidth - 2,firstStartPoint[1]]
	
	if (secondStartPoint[0] - 1*secondLineOppositeLeftRight) < wgWidth and (secondStartPoint[0] - 1*secondLineOppositeLeftRight) >= 0:
		newSecondPoint = [secondStartPoint[0] - 1*secondLineOppositeLeftRight,secondStartPoint[1]]
	elif (secondStartPoint[0] - 1*secondLineOppositeLeftRight) >= wgWidth:
		newSecondPoint = [1,secondStartPoint[1]]
	elif (secondStartPoint[0] - 1*secondLineOppositeLeftRight) < 0:
		newSecondPoint = [wgWidth - 2,secondStartPoint[1]]
	
	if witnessGrid[newFirstPoint[0],newFirstPoint[1]] == 0 and witnessGrid[newSecondPoint[0],newSecondPoint[1]] == 0:
		moveSteps(lengthOfFirstPath, lengthOfSecondPath,witnessGrid,firstStartPoint,secondStartPoint,newFirstPoint,newSecondPoint,firstEndPoint,secondEndPoint,firstPathPoints,secondPathPoints)



	return False








#main program


witnessGrid = numpy.zeros((7,7))

#Set first start point, end point. Always choose 3,0 coordinates as start and 3,6 as end
firstStartPoint = [3,0]
firstEndPoint = [3,6]

# mark start points
witnessGrid[firstStartPoint[0],firstStartPoint[1]] = -1
witnessGrid[secondStartPoint[0],secondStartPoint[1]] = -100

resultPath = findPath(firstStartPoint,firstEndPoint,secondStartPoint,secondEndPoint,0,100,witnessGrid,[],[])
















