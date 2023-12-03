import re
from dataclasses import dataclass
from typing import List

calibration_values = [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
]

@dataclass
class Set:
    blue: int
    red: int
    green: int

@dataclass
class Game:
    game_id: int
    sets: List[Set]

    def power(self) -> int:
        min_red = max(Set.red for Set in self.sets)
        min_blue = max(Set.blue for Set in self.sets)
        min_green = max(Set.green for Set in self.sets)

        return min_red * min_blue * min_green

def parse_game_data(list_item: str) -> Game:
    game_id = re.search("[0-9]+", list_item).group()
    sets_start = re.search(": ", list_item).end()
    sets = list_item[sets_start:] 
    sets_list = sets.split("; ")
    game = Game(game_id, [])
    
    for item in sets_list:
        scores_list = item.split(", ")
        new_set = Set(0, 0, 0)
        
        #assume we cannot guarantee order of scores
        for score in scores_list:
            if("blue" in score):
                new_set.blue = int(re.search("[0-9]+", score).group())
            elif("red" in score):
                new_set.red = int(re.search("[0-9]+", score).group())
            elif("green" in score):
                new_set.green = int(re.search("[0-9]+", score).group())

        game.sets.append(new_set)
    
    return game

def get_total_power(games_list: List[Game]) -> int:
    total_power = 0
    for game in games_list:
        total_power += game.power()

    return total_power

data = []

try:
    input_file = open("input/day2_input.txt")
    data = input_file.read()
finally:
    input_file.close()

input_list = data.split('\n')

games_list = []

for game in input_list:
    games_list.append(parse_game_data(game))

print(get_total_power(games_list))


