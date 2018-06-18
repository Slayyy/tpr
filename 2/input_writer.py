#!/usr/bin/env python2

import json
import sys

json_data = open(sys.argv[1])
data = json.load(json_data)
json_data.close()

proc_num = data['number_of_processors']
points_power = data['points_power_of_ten']

with open('input.txt', 'wb+') as f:
    f.write("{0} {1}".format(proc_num, points_power))