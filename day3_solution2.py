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

#if a digit is validated as a part number, we need to collect the full number out of that line
def get_part_number(schematic_line: List, index: int):
    start_index = index
    #move index back to start reading number
    digit = str(schematic_line[index])
    while digit.isdigit() and start_index >= 0:
        digit = str(schematic_line[start_index])
        start_index -= 1

    #read number from index to end
    part_number = re.search("[0-9]+", schematic_line[start_index + 1:]).group()

    return part_number

gear_ratio = 0        

#check if any of the digis are adjacent a symbol
for list_index, schematic_line in enumerate(schematic_list):

    for line_index, item in enumerate(schematic_line):
        
        #Are we on a potential gear
        if(schematic_line[line_index] is "*"):
            number_of_hits = 0
            part_value = 1
            top_hit = False
            bottom_hit = False

            #check left
            if(line_index - 1 >= 0):
                if(schematic_line[line_index - 1].isdigit()):
                    part = get_part_number(schematic_line, line_index - 1)
                    part_value = part_value * int(part)
                    number_of_hits += 1      
             #check right
            if(line_index + 1 < len(schematic_line)):
                if(schematic_line[line_index + 1].isdigit()):
                    part = get_part_number(schematic_line, line_index + 1)
                    part_value = part_value * int(part)
                    number_of_hits += 1      
            #check above
            if(list_index - 1 >= 0):
                if(schematic_list[list_index - 1][line_index].isdigit()):
                    top_hit = True
                    part = get_part_number(schematic_list[list_index - 1], line_index)
                    part_value = part_value * int(part)
                    number_of_hits += 1       
            #check above left
            if(list_index - 1 >= 0 and line_index - 1 >= 0 and not top_hit):
                if(schematic_list[list_index - 1][line_index - 1].isdigit()):
                    part = get_part_number(schematic_list[list_index - 1], line_index - 1)
                    part_value = part_value * int(part)
                    number_of_hits += 1       
            #check above right
            if(list_index - 1 >= 0 and line_index + 1 < len(schematic_line) and not top_hit):
                if(schematic_list[list_index - 1][line_index + 1].isdigit()):
                    part = get_part_number(schematic_list[list_index - 1], line_index + 1)
                    part_value = part_value * int(part)
                    number_of_hits += 1      
            #check below
            if(list_index + 1 < len(schematic_list)):
                if(schematic_list[list_index + 1][line_index].isdigit()):
                    bottom_hit = True
                    part = get_part_number(schematic_list[list_index + 1], line_index)
                    part_value = part_value * int(part)
                    number_of_hits += 1          
            #check below left
            if(list_index + 1 < len(schematic_list) and line_index - 1 >= 0 and not bottom_hit):
                if(schematic_list[list_index + 1][line_index - 1].isdigit()):
                    part = get_part_number(schematic_list[list_index + 1], line_index - 1)
                    part_value = part_value * int(part)
                    number_of_hits += 1       
            #check below right
            if(list_index + 1 < len(schematic_list) and line_index + 1 < len(schematic_line) and not bottom_hit):
                if(schematic_list[list_index + 1][line_index + 1].isdigit()):
                    part = get_part_number(schematic_list[list_index + 1], line_index + 1)
                    part_value = part_value * int(part)
                    number_of_hits += 1
            
            if number_of_hits == 2:
                gear_ratio += part_value 
                    
print(gear_ratio)

           
        
