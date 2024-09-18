#!/bin/bash
#SBATCH --job-name=
#SBATCH --mail-type=ALL
#SBATCH --mail-user=francesco.deroma@polito.it
#SBATCH --partition=
#SBATCH --time=000:00:00
#SBATCH --ntasks=
#SBATCH --cpus-per-task=1
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=
#SBATCH --dependency=afterok:
#SBATCH --mem=
#SBATCH --output=slurm-%x-%j.out

# Following commands are needed to launch on HPC@CINECA
#module load profile/chem-phys
#module load autoload lammps/23jun2022
#export OMP_NUM_THREAD=2

#CASE_IN="in.SLES_CMEA"
#CASE_OUT="log.lammps"
#PREVIOUS_BCK="../UB75_sr1_medium_long_0/zeroth"
#cp $PREVIOUS_BCK .
#srun lmp_intel_cpu -sf omp -pk omp 2 -in $CASE_IN -log $CASE_OUT
#srun lmp_intel_cpu -in $CASE_IN -log $CASE_OUT


# Following commands are needed to launch on HPC@polito
#module load gnu8/8.3.0
#module load openmpi3/3.1.4
#module load singularity
#module load prun
#export SINGULARITY_BINDPATH="/scratch"

#CONTAINER="/home/fderoma/containers/lammps-24Mar2022_Ubuntu.sif"
#EXE=""
#CASE_IN="in.SLES_CMEA"
#CASE_OUT="log.lammps"
#PREVIOUS_BCK="../UB75_sr1_medium_long_0/zeroth"
#cp $PREVIOUS_BCK .
#prun singularity exec $CONTAINER $EXE -in $CASE_IN -log $CASE_OUT



# Following commands are needed to launch on Minicluster
CONTAINER="/home/fderoma/containers/lammps-24Mar2022_Ubuntu.sif"
EXE=""
CASE_IN="in.SLES_CMEA"
CASE_OUT="log.lammps"
#PREVIOUS_BCK="../UB75_sr1_medium_long_0/zeroth"
#cp $PREVIOUS_BCK .
mpirun --mca btl ^tcp -n singularity exec $CONTAINER $EXE -in $CASE_IN  -log $CASE_OUT
