import re

solution = 0
test = 'data/day8/test'
live = 'data/day8/real'

network = {}
instructions = ""

with open(live, 'r') as file:
    for line in file:
        if re.fullmatch(r'[LR]+\n', line):
            #Mache aus den instructions (L/R) int's (0/1) und packe diese in ein Array
            instructions = [int(x) for x in list(line.replace("\n", "").replace("R", "1").replace("L", "0"))]
        elif re.fullmatch(r'\n', line):
            continue
        else:
            #Entferne (, ) und \n aus dem array, anschließend splitte an = und ,
            line = re.split(r'[=,]', re.sub(r'[ \(\)\n]', "", line))
            key = line.pop(0)
            network[key] = line

pos = "AAA"
while pos != "ZZZ":
    for instruction in instructions:
        if pos == "ZZZ":
            break
        else:
            pos = network[pos][instruction]
            solution += 1

print(solution)