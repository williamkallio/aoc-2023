from dataclasses import dataclass
from typing import List
from typing import Optional
import math
from enum import Enum

RAW = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

card_ranks = {'A' : 'A', 'K' : 'B', 'Q' : 'C', 'J' : 'Z', 'T' : 'E', '9' : 'F', '8' : 'G', '7' : 'H', '6' : 'I', '5' : 'J', '4' : 'K', '3' : 'L', '2' : 'M'}

class Hand_Strength(Enum):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0 

@dataclass
class  Hand:
    cards: List[str]
    bid: int
    strength: Optional[Hand_Strength] = None
    cards_sorting : Optional[str] = None

    def __post_init__(self):
        card_frequency = {i: self.cards.count(i) for i in self.cards}
        #we do not care about ranking types of pairs
        val = max(card_frequency.values())

        if(val == 1):
            if 'J' in card_frequency:
                self.strength = Hand_Strength.ONE_PAIR
            else:
                self.strength = Hand_Strength.HIGH_CARD
        elif(val == 2):
            num_pairs = 0
            #check for 2 pair
            for value in card_frequency.values():
                if(value == 2):
                    num_pairs += 1

            if(num_pairs > 1):
                if 'J' in card_frequency and card_frequency['J'] == 2:
                    self.strength = Hand_Strength.FOUR_OF_A_KIND
                elif 'J' in card_frequency and card_frequency['J'] == 1:
                    self.strength = Hand_Strength.FULL_HOUSE
                else:
                    self.strength = Hand_Strength.TWO_PAIR
            else:
                if ('J' in card_frequency) and (card_frequency['J'] == 1 or card_frequency['J'] == 2):
                    self.strength = Hand_Strength.THREE_OF_A_KIND
                else:
                    self.strength = Hand_Strength.ONE_PAIR
        elif(val == 3):
            if ('J' in card_frequency) and (card_frequency['J'] == 2 or (card_frequency['J'] == 3 and 2 in card_frequency.values())):
                self.strength = Hand_Strength.FIVE_OF_A_KIND
            elif ('J' in card_frequency) and (card_frequency['J'] == 1 or card_frequency['J'] == 3):
                self.strength = Hand_Strength.FOUR_OF_A_KIND
            elif 2 in card_frequency.values():
                self.strength = Hand_Strength.FULL_HOUSE
            else:
                self.strength = Hand_Strength.THREE_OF_A_KIND
        elif(val == 4):
            if 'J' in card_frequency:
                self.strength = Hand_Strength.FIVE_OF_A_KIND
            else:
                self.strength = Hand_Strength.FOUR_OF_A_KIND
        elif(val == 5):
            self.strength = Hand_Strength.FIVE_OF_A_KIND  
        
        #a custom sorter would be the better way to do this, but hey it works
        self.cards_sorting = ""
        for card in self.cards:
            self.cards_sorting = self.cards_sorting + card_ranks[card]



def parse_hands(raw_hands: List[str]) -> List[Hand]:
    hands = []

    for raw_hand in raw_hands:
        hand = raw_hand.split(" ")[0]
        bid = int(raw_hand.split(" ")[1])
        hands.append(Hand(hand, bid))

    return hands

try:
    input_file = open("input/day7_input.txt")
    data = input_file.read()
finally:
    input_file.close()

hands = parse_hands(data.split("\n"))
#hands = parse_hands(RAW.split("\n"))

five_of_a_kind = [i for i in hands if i.strength == Hand_Strength.FIVE_OF_A_KIND]
five_of_a_kind.sort(key=lambda x: x.cards_sorting)

four_of_a_kind = [i for i in hands if i.strength == Hand_Strength.FOUR_OF_A_KIND]
four_of_a_kind.sort(key=lambda x: x.cards_sorting)

full_house = [i for i in hands if i.strength == Hand_Strength.FULL_HOUSE]
full_house.sort(key=lambda x: x.cards_sorting)

three_of_a_kind = [i for i in hands if i.strength == Hand_Strength.THREE_OF_A_KIND]
three_of_a_kind.sort(key=lambda x: x.cards_sorting)

two_pairs = [i for i in hands if i.strength == Hand_Strength.TWO_PAIR]
two_pairs.sort(key=lambda x: x.cards_sorting)

one_pair = [i for i in hands if i.strength == Hand_Strength.ONE_PAIR]
one_pair.sort(key=lambda x: x.cards_sorting)

high_card = [i for i in hands if i.strength == Hand_Strength.HIGH_CARD]
high_card.sort(key=lambda x: x.cards_sorting)

sorted_hands = five_of_a_kind + four_of_a_kind + full_house + three_of_a_kind + two_pairs + one_pair + high_card
#sort each group

sorted_hands.reverse()

total_winnings = 0
rank = 1

for hand in sorted_hands:
    total_winnings += rank * hand.bid
    rank += 1

print(total_winnings)



