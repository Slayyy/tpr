#!/usr/bin/env python

import os
import commands

dir = os.path.dirname(os.path.realpath( __file__))

with open('input.txt', 'r') as f:
    proc_num, points_power = f.read().split()

load_openmpi = 'module add plgrid/tools/openmpi > /dev/null 2>&1'
commands.getoutput(load_openmpi)

run_mpi = lambda p: "mpirun -np {} {}/main.py {}" .format(p, dir, points_power)
one_proc_time = commands.getoutput(run_mpi(1).strip().split(' ')[1])

results = commands.getoutput(run_mpi(proc_num)).strip().split(' ')

time = results.split()[1]
speedup = float(one_proc_time) / float(results.split()[1])
efficiency = speedup/proc_num
serial_fraction = None if proc_num < 2 else (1/speedup - 1/proc_num)/(1 - 1/proc_num)


with open('output.txt', 'wb+') as f:
    f.write('{} {} {} {}' .format(time, speedup, efficiency, serial_fraction))