import re
from collections import Counter

cardValues = {"A": 12, "K": 11, "Q": 10, "J": 9, "T": 8, "9": 7, "8": 6, "7": 5, "6": 4, "5": 3, "4": 2, "3": 1, "2": 0}
handValues = {"FIVE": 19, "FOUR": 18, "FULLHOUSE": 17, "THREE": 16, "TWOTWO": 15, "TWO": 14, "HIGHCARD": 13}

class Hand:
    def __init__(self, cards: str, bid: int) -> None:
        self.cards = list(cards)
        self.bid = bid
        self.value = self.getValue()

        pass

    def getValue(self):
        counted = Counter(self.cards)
        counted_list = sorted(list(counted.values()), reverse=True)
        counted_list.sort(reverse=True)
        if counted_list[0] == 5:
            return 19
        elif counted_list[0] == 4:
            return 18
        elif counted_list[0] == 3 and counted_list[1] == 2:
            return 17
        elif counted_list[0] == 3:
            return 16
        elif counted_list[0] == 2 and counted_list[1] == 2:
            return 15
        elif counted_list[0] == 2:
            return 14
        else:
            return 13
        
    def hasHigherHighcardThan(self, toCompare) -> bool:
        toCompare: Hand
        for i in range(len(self.cards)):
            if cardValues[self.cards[i]] > cardValues[toCompare.cards[i]]:
                return True
            elif cardValues[self.cards[i]] < cardValues[toCompare.cards[i]]:
                return False
            
    def getHighcardValue(self, pos:int = 0):
        return cardValues[self.cards[pos]]
            
    def __repr__(self):
        return f"Hand: {self.cards}\tGebot: {self.bid}\tWert: {self.value}"



solution = 0
test = 'data/day7/test'
live = 'data/day7/real'
hands = []

with open(live, 'r') as file:
    for line in file:
        ar = line.split()
        hands.append(Hand(ar[0], int(ar[1])))

#NICHT HINSCHAUEN!!!!
hands.sort(key=lambda obj: (obj.value, obj.getHighcardValue(0), obj.getHighcardValue(1), obj.getHighcardValue(2), obj.getHighcardValue(3), obj.getHighcardValue(4)))

for i in range(len(hands)):
    solution += hands[i].bid * (i+1)

print(solution)