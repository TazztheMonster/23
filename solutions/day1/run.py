import re

lösung = 0
test = 'data-01-test'
live = 'data-01-real'
with open(live, 'r') as datei:
    for zeile in datei:
        zahlen = re.findall(r'\d', zeile)
        zwischenlösung = 0
        zwischenlösung += int(zahlen[0])*10
        zwischenlösung += int(zahlen[-1])
        lösung += zwischenlösung
print(lösung)