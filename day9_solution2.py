from dataclasses import dataclass
from typing import List
import math
from typing import Optional
RAW = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


try:
    input_file = open("input/day9_input.txt")
    data = input_file.read()
finally:
    input_file.close()

sensor_data = data.split("\n")
#sensor_data = RAW.split("\n")
total_predictions = 0

#surely there is a mathematical solution that makes this way more straightforward.

for data in sensor_data:
    predictions = []

    data_line = [int(x) for x in data.split(" ")]
    predictions.append(data_line)

    while(not all(i == 0 for i in predictions[-1])):
        prediction = []
        for item_index, item in enumerate(predictions[-1]):
            if(item_index < len(predictions[-1]) - 1):
                prediction.append(int(predictions[-1][item_index + 1]) - int(predictions[-1][item_index]))
    
        predictions.append(prediction)

    #predictions ready
    #add 0 to beginning of last
    predictions[-1][:0] = [0]

    iter = len(predictions) - 2
    while(iter >= 0):
        predictions[iter][:0] = [(predictions[iter][0] - predictions[iter+1][0])]
        iter -= 1
    
    total_predictions += predictions[0][0]

print(predictions)
    


            










