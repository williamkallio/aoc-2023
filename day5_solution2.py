import re
from typing import List
from dataclasses import dataclass

RAW = """seeds: 79 14

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

@dataclass
class Map_Range:
    source: int
    dest: int
    range: int

@dataclass
class Almanac_Map:
    name: str
    ranges: List[Map_Range]

    #given an item, determine its mapping per the rules
    def get_mapping(self, item: int) -> int:
        for i in self.ranges:
            if item >= i.source and item <= i.source + i.range:
                #valid range found, get offset
                offset = item - i.source
                return i.dest + offset
        
        #no valid ranges found, return same value
        return item

@dataclass
class Almanac:
    seeds: List[int]
    maps: List[Almanac_Map]

def get_seed_ranges(seeds: List[str]) -> List[int]:
    #every other item is the range
    isRange = False
    all_seeds = []
    #save seed since we lose index
    current_seed = 0
    for seed_index, seed in enumerate(seeds):
        num_seed = int(seed)
        if(not isRange):
            all_seeds.append(num_seed)
            current_seed = num_seed
            isRange = True
        else:
            all_seeds.extend(range(current_seed + 1, all_seeds[seed_index - 1] + num_seed))
            isRange = False
    
    return all_seeds
        
def parse_almanac(raw_string: str) -> Almanac:
    seeds = get_seed_ranges(raw_string.split("\n")[0].split(": ")[1].split(" "))
    raw_maps = list(filter(None, raw_string.split("\n")[1:]))
    new_map = Almanac_Map("", [])
    map_name = ""
    almanac = Almanac(seeds, [])
    
    #this is gross
    for item in raw_maps:
        if not item[0].isdigit():
            if len(new_map.ranges) > 0:
                #only add if we have ranges defined
                almanac.maps.append(new_map)
                new_map = Almanac_Map("", [])

            new_map.name = item[:-1]
            continue

        map_values = item.split(" ")
        map_range = Map_Range(int(map_values[1]), int(map_values[0]), int(map_values[2]))
        new_map.ranges.append(map_range)

    #add final map :-/
    almanac.maps.append(new_map)

    return almanac

try:
    input_file = open("input/day5_input.txt")
    data = input_file.read()
finally:
    input_file.close()

#almanac = parse_almanac(RAW)
almanac = parse_almanac(data)

nearest_location = None

for seed in almanac.seeds:
    mapped_value = int(seed)
    for map in almanac.maps:
        mapped_value = map.get_mapping(mapped_value)
        
    if(nearest_location is None or nearest_location > mapped_value):
            nearest_location = mapped_value

print(nearest_location)




