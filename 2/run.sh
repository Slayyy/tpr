#!/bin/bash -l

#SBATCH -N 1
#SBATCH --cpus-per-task=12
#SBATCH --time=48:00:00 
#SBATCH -p plgrid
#SBATCH --output="output.out"
#SBATCH --error="error.err"
 
srun /bin/hostname
 
module load plgrid/tools/python/2.7.9
 
cd $SLURM_SUBMIT_DIR
 
python2 run.py
