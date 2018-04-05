#!/usr/bin/env python
import json
import sys

json_data = open(sys.argv[1])
data = json.load(json_data)
json_data.close()

proc_num = data['number_of_processors' ]
points_power = data['points_power_of_ten' ]

with open('input.txt', 'wb+') as f:
    f.write("{} {}".format(proc_num, points_power))