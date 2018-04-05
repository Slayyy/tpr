#!/usr/bin/env python2

import gc
import random
import sys

import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# 10**8, 10**10, 10**6
n = 10 ** int(sys.argv[1])
per_worker = n/size
o = 0

gc.collect()

comm.Barrier()
begin_time = MPI.Wtime()
for i in xrange(per_worker):
    x, y = random.random(), random.random()
    if x**2 + y**2 <= 1.0:
        o += 1

sum = comm.reduce(o, op=MPI.SUM, root=0)
end_time = MPI.Wtime()

if rank == 0:
    print end_time-begin_time
