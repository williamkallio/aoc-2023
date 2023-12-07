from dataclasses import dataclass
from typing import List
import math

RAW = """Time:        34     90     89     86
Distance:   204   1713   1210   1780"""

@dataclass
class  Race:
    time: int
    distance: int

#races = parse_races(RAW.split("\n"))

races = [Race(34908986, 204171312101780)]

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




