import re

class Race:
    def __init__(self, time:int, distance:int) -> None:
        self.time = time
        self.distance = distance
        self.solution = self.calc()
        pass

    def calc(self) -> int:
        counter = 0
        for i in range(self.time):
            if self.distance < (self.time - i) * i:
                counter += 1
            elif counter >= 1:
                break
        return counter

solution = 1
test = 'data/day6/test'
live = 'data/day6/real'

times = []
distances = []

#Daten aus der Datei auslesen
with open(live, 'r') as file:
    for line in file:
        if line.startswith("Time:"):
            line = re.sub(r'Time:*', "", line)
            times = [int(x) for x in line.split()]
        if line.startswith("Distance:  "):
            line = re.sub(r'Distance:*', "", line)
            distances = [int(x) for x in line.split()]

#Race Objekte erstellen
races = []
for i in range(len(times)):
    races.append(Race(times[i], distances[i]))

#Lösungen multiplizieren
race:Race
for race in races:
    print(race.solution)
    solution *= race.solution

print(solution)