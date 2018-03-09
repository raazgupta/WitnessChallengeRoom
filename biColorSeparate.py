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

#whiteSquares = [8,4,23]
#blackSquares = [33,27,21]

whiteSquares = []
blackSquares = []

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
			if y == 'w':
				whiteSquares.append(int(x))
			elif y == 'b':
				blackSquares.append(int(x))
	elif nextInput == 'b':
		whiteSquares.pop()
		blackSquares.pop()
	print "White Squares:"
	print  whiteSquares
	print "Black Squares:"
	print blackSquares

print "Solving ..."

def checkSeparator(separatorLine,firstPathPoints,secondPathPoints):
	
	for firstPathPoint in firstPathPoints:
		if separatorLine == firstPathPoint:
			return True
		elif separatorLine == [firstPathPoint[1],firstPathPoint[0]]:
			return True

	for secondPathPoint in secondPathPoints:
		if separatorLine == secondPathPoint:
			return True
		elif separatorLine == [secondPathPoint[1],secondPathPoint[0]]:
			return True

	return False		



def checkBlocks(firstPathPoints,secondPathPoints,witnessGrid,finalCheck):

	for whiteSquare in whiteSquares:
		whiteBlock = blocksDictionary[whiteSquare]
		whiteBottomLeftCorner = whiteBlock[0]
		whiteTopRightCorner = whiteBlock[1]
		
		for blackSquare in blackSquares:
			blackBlock = blocksDictionary[blackSquare]
			blackBottomLeftCorner = blackBlock[0]
			blackTopRightCorner = blackBlock[1]

			#Trace the 2 possible L shaped paths from
			#white block to black block
			#Count the number of separators (line passing through points)
			#If number of separators is odd then 2 blocks are in different spaces
			#If number of separators is even then 2 blocks are in the same sapce

			numSeparators1 = 0
			
			#Trace first L shaped path
			#Check if white block to the left or right of black block
			startPoint = whiteBottomLeftCorner
			currentPoint = startPoint
			endPoint = blackBottomLeftCorner
			#White block to the right of black block
			while currentPoint[0] > endPoint[0]:
				#Go Left until same column as black block
				#Construct and Check for separators
				#separatorLine = [[currentPoint[0]+1,currentPoint[1]],[currentPoint[0]+1,currentPoint[1]+1]]		
				separatorLine = [currentPoint,[currentPoint[0],currentPoint[1]+1]]
				#Check if separator line exists in first or second path points
				if checkSeparator(separatorLine,firstPathPoints,secondPathPoints) == True:
					numSeparators1 += 1
				if (currentPoint[0] - 1) >= endPoint[0]:
					currentPoint = [currentPoint[0]-1,currentPoint[1]]
			
			#White block to the left of black block
			while currentPoint[0] < endPoint[0]:
				#Go Right until same column as black block
				#Construct and Check for separators
				#separatorLine = [currentPoint,[currentPoint[0],currentPoint[1]+1]]		
				separatorLine = [[currentPoint[0]+1,currentPoint[1]],[currentPoint[0]+1,currentPoint[1]+1]]
				#Check if separator line exists in first or second path points
				if checkSeparator(separatorLine,firstPathPoints,secondPathPoints) == True:
					numSeparators1 += 1
				if (currentPoint[0] + 1) <= endPoint[0]:
					currentPoint = [currentPoint[0]+1,currentPoint[1]]
			
			#White block and black block in the same column
			if currentPoint[0] == endPoint[0]:
				#Check if white block below or above black block

				#White block above black block
				while currentPoint[1] > endPoint[1]:
					#Go down until same row as block block
					#Construct and check for separators
					separatorLine = [currentPoint,[currentPoint[0]+1,currentPoint[1]]]
					if checkSeparator(separatorLine,firstPathPoints,secondPathPoints) == True:
						numSeparators1 += 1
					if (currentPoint[1] - 1 >= endPoint[1]):
						currentPoint = [currentPoint[0],currentPoint[1]-1]
				
				#White block below black block
				while currentPoint[1] < endPoint[1]:
					#Go up until same row as block block
					#Construct and check for separators
					separatorLine = [[currentPoint[0],currentPoint[1]+1],[currentPoint[0]+1,currentPoint[1]+1]]
					if checkSeparator(separatorLine,firstPathPoints,secondPathPoints) == True:
						numSeparators1 += 1
					if (currentPoint[1] + 1 <= endPoint[1]):
						currentPoint = [currentPoint[0],currentPoint[1]+1]
			
			

			#Check if numSeparator is even or odd
			#If even then assume blocks are in the same space
			#If odd then assume blocks are in different spaces and continue 
			if numSeparators1 % 2 == 0:
				return False

		

			

			numSeparators2 = 0
			
			#Trace second L shaped path
			#Check if white block above or below black block
			startPoint = whiteBottomLeftCorner
			currentPoint = startPoint
			endPoint = blackBottomLeftCorner

			#White block above black block
			while currentPoint[1] > endPoint[1]:
				#Go down until same row as block block
				#Construct and check for separators
				separatorLine = [currentPoint,[currentPoint[0]+1,currentPoint[1]]]
				if checkSeparator(separatorLine,firstPathPoints,secondPathPoints) == True:
					numSeparators2 += 1
				if (currentPoint[1] - 1 >= endPoint[1]):
					currentPoint = [currentPoint[0],currentPoint[1]-1]
				
			#White block below black block
			
			while currentPoint[1] < endPoint[1]:
				#Go up until same row as block block
				#Construct and check for separators
				separatorLine = [[currentPoint[0],currentPoint[1]+1],[currentPoint[0]+1,currentPoint[1]+1]]
				if checkSeparator(separatorLine,firstPathPoints,secondPathPoints) == True:
					numSeparators2 += 1
				if (currentPoint[1] + 1 <= endPoint[1]):
					currentPoint = [currentPoint[0],currentPoint[1]+1]
			
			#White block and black block are in the same row
			if currentPoint[1] == endPoint[1]:
				#White block to the right of black block
				while currentPoint[0] > endPoint[0]:
					#Go Left until same column as black block
					#Construct and Check for separators
					separatorLine = [currentPoint,[currentPoint[0],currentPoint[1]+1]]		
					#Check if separator line exists in first or second path points
					if checkSeparator(separatorLine,firstPathPoints,secondPathPoints) == True:
						numSeparators2 += 1
					if (currentPoint[0] - 1) >= endPoint[0]:
						currentPoint = [currentPoint[0]-1,currentPoint[1]]
			
				#White block to the left of black block
				while currentPoint[0] < endPoint[0]:
					#Go Right until same column as black block
					#Construct and Check for separators
					#separatorLine = [currentPoint,[currentPoint[0],currentPoint[1]+1]]		
					separatorLine = [[currentPoint[0]+1,currentPoint[1]],[currentPoint[0]+1,currentPoint[1]+1]]
					
					#Check if separator line exists in first or second path points
					if checkSeparator(separatorLine,firstPathPoints,secondPathPoints) == True:
						numSeparators2 += 1
					if (currentPoint[0] + 1) <= endPoint[0]:
						currentPoint = [currentPoint[0]+1,currentPoint[1]]


						

			#Check if numSeparator is even or odd
			#If even then assume blocks are in the same space
			#If odd then assume blocks are in different spaces and continue 
			if numSeparators2 % 2 == 0:
				return False

		#As both numSeparator1 and numSeparator2 are odd assume the block sare in different spaces
		#Continue with next block	


			
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
		
		#if [[3,0],[3,1]] in firstPathPoints and [[3,3],[4,3]] in firstPathPoints and [[4,3],[5,3]] in firstPathPoints and [[5,4],[6,4]] in firstPathPoints:
		#	print witnessGrid
		#	pdb.set_trace()

		if checkBlocks(firstPathPoints,secondPathPoints,witnessGrid,True) == True:
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
















