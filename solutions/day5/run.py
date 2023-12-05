import re

lösung = 0
test = 'data/day5/test'
live = 'data/day5/real'

seeds = []
mapped = []

with open(live, 'r') as file:
    for line in file:

        #Initiiere Seeds
        if line.startswith("seeds: "):
            line = line.replace("seeds: ", "")
            mapped = [int(x) for x in line.split()]
            continue

        #Check für neue Gruppe und initialiesieren wenn
        if re.search(r"[a-zA-Z]", line):
            mapped.extend(seeds)
            seeds = mapped
            mapped = []
            continue
        elif len(seeds) == 0:
            continue

        #Check maps
        if re.search(r"\d+", line):
            
            #Init Values
            dataset = [int(x) for x in line.split()]
            sourceStart = dataset[1]
            dataRange = dataset[2]
            change = dataset[0] - dataset[1]

            #Rückwärts über die seeds iterieren
            for i in range(len(seeds) - 1, -1, -1):
                if seeds[i] >= sourceStart and seeds[i] < sourceStart + dataRange:
                    mapped.append(seeds[i] + change)
                    seeds.pop(i)

mapped.extend(seeds)
print(min(mapped))