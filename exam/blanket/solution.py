import json
import numpy as np
from datetime import datetime


# parse json to dictionary
with open('input.txt', 'r') as txt_file:
    lines = txt_file.readlines()
dict = lines[0]
dict = json.loads(dict)

# convert dictionary into list
date_list = list(dict.items())

# sort list based on first element in tuple
sorted_by_date = sorted(date_list, key=lambda date: datetime.strptime(date[0], '%d/%m/%Y'))

# put all temperatures in seperate list
list_with_temps = []
for koppel in sorted_by_date:
    list_with_temps.append(koppel[1])

# calculate mean, round them and put in list
list_mean = []
for temperatures in list_with_temps:
    list_mean.append(round(np.mean(temperatures)))

with open('output.txt', 'w') as f:
    for temp in list_mean:
        f.write(str(temp)+'\n')