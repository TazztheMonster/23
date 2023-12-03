import re

def getNumberFromPos(y, x, value=0) -> int:
    if x > 0 and value == 0 and str(data[y][x-1]).isdigit():
        return getNumberFromPos(y, x-1)
    else:
        value += int(data[y][x])
        if x+1 < len(data[y]) and data[y][x+1] and str(data[y][x+1]).isdigit():
            value *= 10
            return getNumberFromPos(y, x+1, value=value)
        else:
            return value
        
def getNumberPositionsAround(y, x):
    lastWasNumber = False
    positions = []
    def checkPos(Y, X):
        nonlocal lastWasNumber
        if data[Y][X] and str(data[Y][X]).isdigit() and not lastWasNumber:
            positions.append([Y, X])
            lastWasNumber = True
        elif data[Y][X] and not str(data[Y][X]).isdigit() and lastWasNumber:
            lastWasNumber = False
    checkPos(y-1, x-1)
    checkPos(y-1, x)
    checkPos(y-1, x+1)
    lastWasNumber = False
    checkPos(y, x-1)
    lastWasNumber = False
    checkPos(y, x+1)
    lastWasNumber = False
    checkPos(y+1, x-1)
    checkPos(y+1, x)
    checkPos(y+1, x+1)
    return positions
        
test = 'data/day3/test'
real = 'data/day3/real'
data = []
solution = 0

with open(real, 'r') as file:
    for line in file:
        lineList = list(line.rstrip('\n'))
        if lineList:
            data.append(list(lineList))

for n in range(len(data)):
    for m in range(len(data[n])):
        if not str(data[n][m]).isnumeric() and data[n][m] != ".":
            for pos in getNumberPositionsAround(n, m):
                solution += getNumberFromPos(pos[0], pos[1])
                
print(solution)