#!/usr/bin/env python2

import json

with open('output.txt', 'r') as f:
    time, speedup, efficiency, serial_fraction = f.read().split( ' ')

def is_float(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

results = {}
results["time"] = float(time)
results["speedup"] = float(speedup)
results["efficiency"] = float(efficiency)
if is_float(serial_fraction):
    results["serial_fraction"] = float(serial_fraction)

with open('output.json', 'wb+') as f:
    f.write(json.dumps({"status": "ok", "results": results}))