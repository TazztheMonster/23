import re

lösung = 0
test = 'data/day1/test'
live = 'data/day1/real'

with open(live, 'r') as datei:
    for zeile in datei:
        zahlen = re.findall(r'\d', zeile)

        lösung += int(zahlen[0])*10
        lösung += int(zahlen[-1])
print(lösung)