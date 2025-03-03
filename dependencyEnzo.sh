#!/bin/bash

# Input
folderPattern="folder"
jobName=""
submitNumber=5
depend="#SBATCH --dependency=afterany:"
sbatchName="#SBATCH --job-name="
n_id=""

for dir in folderPattern*; do
    echo "    Entering in $dir"
    cd dir
    jobName=${dir/$folderPattern/}
    for i in $(seq $submitNumber); do
        if [ $i -eq 1 ]; then
            # Reset dependecy id to Null
            n_id=""
            # Comment the dependency for the first submit
            echo "    Comment dependency line in $dir/submit$i.sbatch"
            sed -i "/^$depend.*/ s;^;#;" submit$i.sbatch
            # Change job name
            echo "    Update job name in $dir/submit$i.sbatch"
            sed -i "/^$sbatch_name/ s;$;$jobName-$i;" submit$i.sbatch
            # Launch the job via slurm
            n_id=$(sbatch submit$i.sbatch | grep -Eo ['0-9']+)
            echo "    Job number $i launched in $dir, job id = $n_id"
        else
            # Insert the previous job id for the submit after the first one
            echo "    Set dependency id in $dir/submit$i.sbatch"
            sed -i "/^$depend/ s;$;$n_id;" $curr_fold/SLES_CMEA.sbatch
            # Change job name
            echo "    Update job name in $dir/submit$i.sbatch"
            sed -i "/^$sbatch_name/ s;$;$jobName-$i;" submit$i.sbatch
            # Launch the job via slurm
            n_id=$(sbatch submit$i.sbatch | grep -Eo ['0-9']+)
            echo "    Job number $i launched in $dir, job id = $n_id"
        fi
    done
    echo "    Exit from $dir directory"
    cd ..
done
