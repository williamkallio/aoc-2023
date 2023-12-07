from dataclasses import dataclass
from typing import List
import math

RAW = """Time:        34     90     89     86
Distance:   204   1713   1210   1780"""

@dataclass
class  Race:
    time: int
    distance: int


def parse_races(raw_races: List[str]) -> List[Race]:
    
    races_list = []
    times = list(filter(None, raw_races[0].split(": ")[1].split(" ")))
    distances = list(filter(None, raw_races[1].split(": ")[1].split(" ")))

    for item_index, item in enumerate(times):
        races_list.append(Race(int(item), int(distances[item_index])))

    return races_list

races = parse_races(RAW.split("\n"))

race_wins = []

for race in races:
    button_hold_time = 0
    number_wins = 0
    
    while(button_hold_time <= race.time):
        distance = button_hold_time * (race.time - button_hold_time)
        button_hold_time += 1
        if distance > race.distance:
            number_wins += 1
    
    race_wins.append(number_wins)


print(math.prod(race_wins))


#brute force all possible scenarios




