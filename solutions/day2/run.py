import re

def getRoundValues(round:str):
    colorCounter = {"red": 0, "green": 0, "blue": 0}
    turns = round.split(", ")
    for turn in turns:
        number = int(re.search(r'\d+', turn).group())
        color = re.search(r'[a-zA-Z]+', turn).group()
        colorCounter[color] += number
    return colorCounter

def checkColors(dict:dict) -> bool:
    for key in dict:
        if key in colorMax:
            if colorMax[key] < dict[key]:
                return False
        else:
            return False
    return True

test = 'data/day2/test'
real = 'data/day2/real'

colorMax = {"red": 12, "green": 13, "blue": 14}
solution = 0

with open(real, 'r') as file:
    for line in file:
        print(line)
        nio = False
        split1 = line.split(": ")
        game = int(re.search(r'\d+', split1[0]).group())
        rounds = split1[1].split("; ")
        for round in rounds:
            if not checkColors(getRoundValues(round)):
                nio = True
                break
        if not nio:
            solution += game
print(solution)

#Eventuell habe ich mich verlesen und die Spiele zusammengezählt die nicht funktionieren weshalb ich den code entsprechend aufgebaut habe. :D