#!/usr/bin/env python

import json

with open('output.txt', 'r') as f:
    time, speedup, efficiency, serial_fraction = map(float, f.read().split( ' '))

results = { 
    "status": "ok", 
    "results": {
        "time": time,
        "speedup": speedup,
        "efficiency": efficiency,
        "serial_fraction" : serial_fraction
    }
}

with open('output.json', 'wb+') as f:
    f.write(json.dumps(results))