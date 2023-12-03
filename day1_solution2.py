
import regex

def convert_digits(digit: str):
    
    if(digit.isdigit()):
        return digit
    else:
        return {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"
        }[digit]

#calibration_values = ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen']
data = []

try:
    input_file = open("input/day1_input.txt")
    data = input_file.read()
finally:
    input_file.close()

input_list = data.split('\n')

total_sum = 0

for val in input_list:
    
    digits = regex.findall("\d|one|two|three|four|five|six|seven|eight|nine", val, overlapped=True)
    #map the spelled out numbers to normal numbers, rest of solution should continue to work
    digits = [convert_digits(c) for c in digits]

    if(len(digits) > 0):
        # find first and last digits
        code = [digits[i] for i in (0, -1)]
        converted_number = int("".join(code))

        total_sum += converted_number


print(total_sum)
