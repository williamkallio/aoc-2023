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
    
def parse_card(raw_line: str) -> Card:
    line_values = raw_line.split(":")
    card_num = re.search("[0-9]+", line_values[0]).group()
    #deal with spaces
    winners = list(filter(None, line_values[1].split("|")[0].split(" ")))
    numbers = list(filter(None, line_values[1].split("|")[1].split(" "))) 

    return Card(card_num, winners, numbers)

def get_points(num_matches: int) -> int:
    #we only call this when we have points to score, but let's be defensive!
    if(num_matches > 0):
        double_count = 1
        points = 1
        while(double_count < num_matches):
            points += points
            double_count += 1
        
        return points
    else:
        return 0

try:
    input_file = open("input/day4_input.txt")
    data = input_file.read()
finally:
    input_file.close()

#scratchcard_list = RAW.split("\n")
scratchcard_list = data.split("\n")

pile_points = 0

for scratchcard in scratchcard_list:
    card = parse_card(scratchcard)
    num_winners = len([num for num in card.numbers if num in card.winning_numbers])
    
    if(num_winners > 0):
        pile_points += get_points(num_winners)

print(pile_points)