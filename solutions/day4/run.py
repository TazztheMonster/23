import re

lösung = 0
test = 'data/day4/test'
live = 'data/day4/real'

with open(live, 'r') as datei:
    for zeile in datei:
        #Input aufräumen
        zeile = re.sub(r'Card \d+: +', '', zeile)
        zeile = re.sub(r'[ \n]+$', '', zeile)
        #Arrays aus zahlen erstellen
        winningNumbers = re.split(r' +', zeile.split(' | ')[0])
        numbers = re.split(r' +', zeile.split(' | ')[1])
        #Matches zählen
        count = len(set(winningNumbers) & set(numbers))
        #Punkte berechnen und addieren
        if count >= 2:
            lösung += pow(2, count-1)
        else:
            lösung += count
print(lösung)