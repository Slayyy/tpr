#!/usr/bin/env python2

import os
import commands

dir = os.path.dirname(os.path.realpath( __file__))

with open('input.txt', 'r') as f:
    proc_num, points_power = f.read().split()

proc_num, points_power = int(proc_num), int(points_power)
install_commands = [
    "module load plgrid/tools/python/2.7.9",
    "pip2 install --user mpi4py"
]

install_commands = [x + " > /dev/null 2>&1" for x in install_commands]
run_mpi = lambda p: "mpirun -np {0} {1}/main.py {2}" .format(p, dir, points_power)

cmd = " && ".join(install_commands + [run_mpi(1)])
print cmd
results = commands.getoutput(cmd).strip()
print results
one_proc_time = float(results)

cmd = " && ".join(install_commands + [run_mpi(proc_num)])
results = commands.getoutput(cmd).strip()
print results
time = float(results)

speedup = float(one_proc_time) / float(time)
efficiency = speedup/proc_num
serial_fraction = None if proc_num < 2 else (1/speedup - 1/proc_num)/(1 - 1/proc_num)

with open('output.txt', 'wb+') as f:
    f.write('{0} {1} {2} {3}' .format(time, speedup, efficiency, serial_fraction))