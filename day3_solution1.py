import re
from typing import List

RAW = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

#schematic_list = RAW.split("\n")

try:
    input_file = open("input/day3_input.txt")
    data = input_file.read()
finally:
    input_file.close()

schematic_list = data.split('\n')

def is_part_number(value: str):
    return not (value.isdigit() or value == '.')

#if a digit is validated as a part number, we need to collect the full number out of that line
def get_part_number(schematic_line: List, index: int):
    #move index back to start reading number
    start_index = index
    forward_index = index
    index_progression = 0
    digit = str(schematic_line[index])

    #how many spaces forward will we move the index?
    while(digit.isdigit() and forward_index <= len(schematic_line)):
        forward_index += 1
        
        if(forward_index < len(schematic_line)):
            digit = schematic_line[forward_index]
        
        index_progression += 1

    #reset digit
    digit = str(schematic_line[index])
    while digit.isdigit() and start_index >= 0:
        digit = str(schematic_line[start_index])
        start_index -= 1

    #read number from index to end
    part_number = re.search("[0-9]+", schematic_line[start_index + 1:]).group()

    # We need to know how far to progress our index in the follow-up search as well. 
    # This will depend on which digit of the number matched, and how far forward it needs to go
    return (part_number, index_progression)

total_part_numbers = 0        
move_index = 1

#check if any of the digis are adjacent a symbol
for list_index, schematic_line in enumerate(schematic_list):
    
    move_index = 1

    for line_index, item in enumerate(schematic_line):
        
        if(move_index != 1):
            move_index -= 1
            continue

        #Are we currently on a digit
        if(schematic_line[line_index].isdigit()):
            #check left
            if(line_index - 1 >= 0):
                if(is_part_number(schematic_line[line_index - 1])):
                    part = get_part_number(schematic_line, line_index)
                    total_part_numbers += int(part[0])
                    move_index = part[1]
                    continue
             #check right
            if(line_index + 1 < len(schematic_line)):
                if(is_part_number(schematic_line[line_index + 1])):
                    part = get_part_number(schematic_line, line_index)
                    total_part_numbers += int(part[0])
                    move_index = part[1]
                    continue
            #check above
            if(list_index - 1 >= 0):
                if(is_part_number(schematic_list[list_index - 1][line_index])):
                    part = get_part_number(schematic_line, line_index)
                    total_part_numbers += int(part[0])
                    move_index = part[1]
                    continue
            #check above left
            if(list_index - 1 >= 0 and line_index - 1 >= 0):
                if(is_part_number(schematic_list[list_index - 1][line_index - 1])):
                    part = get_part_number(schematic_line, line_index)
                    total_part_numbers += int(part[0])
                    move_index = part[1]
                    continue
            #check above right
            if(list_index - 1 >= 0 and line_index + 1 < len(schematic_line)):
                if(is_part_number(schematic_list[list_index - 1][line_index + 1])):
                    part = get_part_number(schematic_line, line_index)
                    total_part_numbers += int(part[0])
                    move_index = part[1]
                    continue
            #check below
            if(list_index + 1 < len(schematic_list)):
                if(is_part_number(schematic_list[list_index + 1][line_index])):
                    part = get_part_number(schematic_line, line_index)
                    total_part_numbers += int(part[0])
                    move_index = part[1]
                    continue
            #check below left
            if(list_index + 1 < len(schematic_list) and line_index - 1 >= 0):
                if(is_part_number(schematic_list[list_index + 1][line_index - 1])):
                    part = get_part_number(schematic_line, line_index)
                    total_part_numbers += int(part[0])
                    move_index = part[1]
                    continue
            #check below right
            if(list_index + 1 < len(schematic_list) and line_index + 1 < len(schematic_line)):
                if(is_part_number(schematic_list[list_index + 1][line_index + 1])):
                    part = get_part_number(schematic_line, line_index)
                    total_part_numbers += int(part[0])
                    move_index = part[1]
                    continue

print(total_part_numbers)

           
        
