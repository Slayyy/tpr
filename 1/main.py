#!/usr/bin/env python2
import sys
import gc
import json
import math
import cPickle
from mpi4py import MPI


def gen_lengths(max_len):
    x = 1
    while x < max_len:
        yield int(x)
        if x < 50:
            x += 1
        else:
            x *= 1.03

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    results = {}

    for send_mode_name, send_function in {
            "send": lambda x: comm.send(x, dest=1),
            "ssend": lambda x: comm.ssend(x, dest=1)
    }.iteritems():

        mode_results = {}
        iteration_count = 200

        mode_results["x"] = []
        mode_results["y"] = []
        mode_results["delay"] = []
        mode_results["iteration_count"] = iteration_count

        for string_len in gen_lengths(max_len=(5 * 10**6)):
            payload = "a" * string_len
            payload_size = string_len + len(cPickle.dumps(""))

            gc.collect()
            comm.Barrier()
            begin_time = MPI.Wtime()
            for _ in xrange(iteration_count):
                if rank == 0:
                    send_function(payload)
                elif rank == 1:
                    comm.recv(source=0)
            end_time = MPI.Wtime()
            comm.Barrier()
            mode_results["x"].append(payload_size)

            m_bit_per_second = ((8 * payload_size * iteration_count)/(end_time-begin_time)) / 10**6
            mode_results["y"].append(m_bit_per_second)
            mode_results["delay"].append(((10**3) * (end_time - begin_time))/iteration_count)
            
        results[send_mode_name] = mode_results
    if rank == 0:
        print json.dumps(results, sort_keys=True)
