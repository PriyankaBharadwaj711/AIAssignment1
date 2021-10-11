
import copy
import sys
import time

board=[]
maxLength=0

boxRobot=[]
wallsStorageSpaces=[]
possibleMoves = {'UP':[-1,0],'DOWN':[1,0], 'RIGHT':[0,1],'LEFT':[0,-1]}

maxRowLength = 0	
lines=0

if "-f" in sys.argv:
	data = open(sys.argv[sys.argv.index('-f') + 1])
	board = data.read().split("\n")
	board = [line for line in board if line != ""]
	maxRowLength = len(board[0])
	lines = len(board)
else: 
	data = open("sample.txt")
	board = data.read().split("\n")
	board = [line for line in board if line != ""]
	maxRowLength = len(board[0])
	lines = len(board)


time_start = time.time()
for i in range(0,lines):
	boxRobot.append([])
	wallsStorageSpaces.append([])
	for j in range(0,maxRowLength):
		boxRobot[-1].append('-')
		wallsStorageSpaces[-1].append('-')

for i in range(0,len(board)):
	if len(board[i])<maxRowLength:
		for j in range(len(board[i]),maxRowLength):
			board[i]+='O'

for i in range(0,len(board)):
	for j in range(0,maxRowLength):
		if board[i][j]=='B' or board[i][j]=='R':
			boxRobot[i][j]=board[i][j]
			wallsStorageSpaces[i][j]=' '
		elif board[i][j]=='S' or board[i][j]=='O':
			wallsStorageSpaces[i][j] = board[i][j]
			boxRobot[i][j] = ' '
		elif board[i][j]==' ':
			boxRobot[i][j] = ' '
			wallsStorageSpaces[i][j]=' '
		elif board[i][j] == '*':
			boxRobot[i][j] = 'B'
			wallsStorageSpaces[i][j] = 'S'
		elif board[i][j] == '.':
			boxRobot[i][j] = 'R'
			wallsStorageSpaces[i][j] = 'S'

movesList=[]
visitedMoves=[]

queue = []
source = [boxRobot,movesList]
if boxRobot not in visitedMoves:
	visitedMoves.append(boxRobot)
queue.append(source)
robot_x = -1
robot_y = -1
completed = 0
nodesExpanded = 0
while len(queue) and completed==0:

	temp = queue.pop()
	curPosition = temp[0]
	movesTillNow = temp[1]
	nodesExpanded = nodesExpanded + 1

	for i in range(0,lines):
		for j in range(0,maxRowLength):
			if curPosition[i][j]=='R':
				robot_y, robot_x = j, i
				break
		else:
			continue
		break


	for key in possibleMoves:

		robotNew_x = robot_x+possibleMoves[key][0]
		robotNew_y = robot_y+possibleMoves[key][1] 
		curPositionCopy = copy.deepcopy(curPosition)

		movesTillNowCopy = copy.deepcopy(movesTillNow)
		if curPositionCopy[robotNew_x][robotNew_y] == 'B':

			boxNew_x = robotNew_x + possibleMoves[key][0]
			boxNew_y = robotNew_y + possibleMoves[key][1]
			if curPositionCopy[boxNew_x][boxNew_y]=='B' or wallsStorageSpaces[boxNew_x][boxNew_y]=='O':
				continue
			else:
				curPositionCopy[boxNew_x][boxNew_y] = 'B'
				curPositionCopy[robotNew_x][robotNew_y] = 'R'
				curPositionCopy[robot_x][robot_y] = ' '
				if curPositionCopy not in visitedMoves:
					matches= 0
					for k in range(0,lines):
						for l in range(0,maxRowLength):
							if wallsStorageSpaces[k][l]=='S' and curPositionCopy[k][l]!='B':
								matches=1
					movesTillNowCopy.append(key)
					if not matches:
						completed = 1
						print("Steps taken to complete the game - " + str(len(movesTillNowCopy)))
						print(movesTillNowCopy)
					else:
						queue.append([curPositionCopy,movesTillNowCopy])
						visitedMoves.append(curPositionCopy)
		else:

			if wallsStorageSpaces[robotNew_x][robotNew_y]=='O': 
				continue
			else:
				curPositionCopy[robotNew_x][robotNew_y]='R'
				curPositionCopy[robot_x][robot_y]=' '
				if curPositionCopy not in visitedMoves:
					movesTillNowCopy.append(key)
					queue.append([curPositionCopy,movesTillNowCopy])
					visitedMoves.append(curPositionCopy)

if not completed:
	print("Cannot find a solution")

print("Run time: " + str(round(time.time() - time_start, 3)) + " seconds\n")
print("Number of nodes expanded - " + str(nodesExpanded) + "\n")