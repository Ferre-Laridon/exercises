import json
import numpy as np


# parse json to dictionary
with open('dummy.txt', 'r') as txt_file:
    lines = txt_file.readlines()
dict = lines[0]
dict = json.loads(dict)

# convert dictionary into list
date_list = list(dict.items())

# sort list on first item
sorted_by_date = sorted(date_list, key=lambda date: date[0])

mean = np.mean(sorted_by_date, key=lambda arr: arr[1])
print(mean)