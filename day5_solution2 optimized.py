import re
from typing import List
from dataclasses import dataclass

RAW = """seeds: 79 14 55 13

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
    seeds: List[tuple]
    maps: List[Almanac_Map]

def get_seed_ranges(seeds: List[str]) -> List[int]:

    return [(1263068588, 44436703), (1116624626, 2393304), (2098781025, 128251971), (2946842531, 102775703), (2361566863, 262106125), (221434439, 24088025), (1368516778, 69719147), (3326254382, 101094138), (1576631370, 357411492), (3713929839, 154258863)]
    #return [(79, 14), (55, 13)]

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

def process_map (ranges: List[Map_Range], prev_ranges: List[tuple]):
    ret = []
    for r in ranges:
        source = r.source
        dest = r.dest
        range = r.range
        max_key = range + source

        for prev_range in prev_ranges:
            seed_min = prev_range[0]
            length = prev_range[1]
            seed_max = seed_min + length

            if(seed_min >= source and seed_min < max_key):
                if(seed_max <= max_key):
                    ret.append((dest + seed_min - source, length))
                elif seed_max > max_key:
                    ret.append((dest + seed_min - source, max_key - seed_min))
            elif seed_max >= source and seed_max < max_key:
                ret.append((dest, seed_max - source))
            elif source >= seed_min and max_key <= seed_max:
                ret.append((dest, range))

    return ret

try:
    input_file = open("input/day5_input.txt")
    data = input_file.read()
finally:
    input_file.close()

almanac = parse_almanac(RAW)
#almanac = parse_almanac(data)

print("almanac created")

nearest_location = None

print("original seed size: " + str(len(almanac.seeds)))

num_evaluated = 0
range_eval = List[tuple]

soil_ranges = process_map(almanac.maps[0].ranges, almanac.seeds)
fert_ranges = process_map(almanac.maps[1].ranges, soil_ranges)
water_ranges = process_map(almanac.maps[2].ranges, fert_ranges)
light_ranges = process_map(almanac.maps[3].ranges, water_ranges)
temp_ranges = process_map(almanac.maps[4].ranges, light_ranges)
hum_ranges = process_map(almanac.maps[5].ranges, temp_ranges)
loc_ranges = process_map(almanac.maps[6].ranges, hum_ranges)

min = 99999999999999999999
for i in loc_ranges:
    if i[0] < min:
        min = i[0]

print(min)




