import re

lösung = 0
test = 'data-01-test'
live = 'data-01-real'

with open(live, 'r') as datei:
    for zeile in datei:
        zahlen = re.findall(r'\d', zeile)

        lösung += int(zahlen[0])*10
        lösung += int(zahlen[-1])
print(lösung)