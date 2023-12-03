
import re

#calibration_values = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
data = []

try:
    input_file = open("input/day1_input.txt")
    data = input_file.read()
finally:
    input_file.close()

input_list = data.split('\n')

total_sum = 0

for val in input_list:
    digits = re.findall("\d", val)
    if(len(digits) > 0):
        # find first and last digits
        code = [digits[i] for i in (0, -1)]
        converted_number = int("".join(code))

        total_sum += converted_number


print(total_sum)
