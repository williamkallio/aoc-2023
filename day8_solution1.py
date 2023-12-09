from dataclasses import dataclass
from typing import List
import math
from typing import Optional
RAW = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

RAW2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

def parse_tree(nodes: List[str]) -> dict:

    ret = {}

    for node in nodes:
        key = node.split(" = ")[0]
        tup = (node.split(" = ")[1].split(", ")[0][1:], node.split(" = ")[1].split(", ")[1][:-1])
        ret.update({key : tup})
    
    return ret


try:
    input_file = open("input/day8_input.txt")
    data = input_file.read()
finally:
    input_file.close()

node_dict = parse_tree(data.split("\n")[2:])

#directions = RAW.split("\n")[0]
directions = data.split("\n")[0]

#start at the top
current_node = 'AAA'
num_steps = 0

while(current_node != 'ZZZ'):
    
    for item in directions:
        if item == 'L':
            current_node = node_dict[current_node][0]
        elif item == 'R':
            current_node = node_dict[current_node][1]
        
        num_steps += 1

print(num_steps)










