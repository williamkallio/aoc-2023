import re
from typing import List
from dataclasses import dataclass

RAW = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

@dataclass
class Card:
    card_number: int
    winning_numbers: List[int]
    numbers: List[int]
    card_count: int
    
def parse_card(raw_line: str) -> Card:
    line_values = raw_line.split(":")
    card_num = int(re.search("[0-9]+", line_values[0]).group())
    #deal with spaces
    winners = list(filter(None, line_values[1].split("|")[0].split(" ")))
    numbers = list(filter(None, line_values[1].split("|")[1].split(" "))) 

    return Card(card_num, winners, numbers, 1)

def generate_card_deck(raw_list: List[str]) -> dict:
    card_deck = {}
    for scratchcard in raw_list:
        new_card = parse_card(scratchcard)
        card_deck.update({new_card.card_number : new_card})

    return card_deck

try:
    input_file = open("input/day4_input.txt")
    data = input_file.read()
finally:
    input_file.close()

#scratchcard_list = RAW.split("\n")
scratchcard_list = data.split("\n")

card_deck = generate_card_deck(scratchcard_list)

for card_index, card in enumerate(card_deck):
    
    num_iterations = 0

    while(num_iterations < card_deck[card].card_count):
        #determine how many cards to copy
        num_winners = len([num for num in card_deck[card].numbers if num in card_deck[card].winning_numbers])
        
        #I think we need to preserve the order, so each is inserted at the proper location
        #First determine the cards we've won:
        won_cards = []
        counter = 1
        while(counter <= num_winners):
            #can't guarantee indexing order because we are inserting shit all over the place
            won_cards.append(card_deck[card + counter])
            counter += 1
        
        #Place each won card where it should go
        for won_card in won_cards:
            card_deck[won_card.card_number].card_count += 1
        
        num_iterations += 1

total_cards = 0
iterations = 1

while(iterations <= len(card_deck)):
    total_cards += card_deck[iterations].card_count
    iterations += 1

print(total_cards)
