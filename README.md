List of current scripts:

* `dependancy`: bash script used to launch consecutive jobs through the SLURM scheduler. The simulations are run in separate folders and every simulation is a restart from the previous one. Written for LAMMPS simulations.
* `join_sims`: used to join the results of consecutive simulations (in different folders) obtained from restarts. These way the post process will be done from the first folder.
* `fractionCalcUB75.py`: calculate the bead fractions for a solvay's blend starting from the mass fractions
