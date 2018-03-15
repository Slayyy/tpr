#!/usr/bin/env bash

set -x

mpiexec  -machinefile ./same_host -np 2 ./main.py | tee 1_shmem.json
MPIR_CVAR_CH3_NOLOCAL=1 mpiexec  -machinefile ./same_host -np 2 ./main.py | tee 2_no_shmem.json
MPIR_CVAR_CH3_NOLOCAL=1 mpiexec  -machinefile ./same_machine -np 2 ./main.py | tee 3_same_machine.json
MPIR_CVAR_CH3_NOLOCAL=1 mpiexec  -machinefile ./different_machines -np 2 ./main.py | tee 4_different_machines.json
