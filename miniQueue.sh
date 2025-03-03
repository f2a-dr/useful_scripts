#!/bin/bash

# USAGE
#
# Set USER as your account name on the mini cluster's machine.
# The array HOST can be modified to get information from different machines.
#
# For a better experience, the use of an ssh key and agent is recommended. It
# is possible to use the classic login method, but the password will be
# requested for every host.

USER=fderoma
HOSTS=(@mini01.polito.it @mini02.polito.it @mini03.polito.it)
maxCpu=46
maxMem=251


for i in "${HOSTS[@]}"
do
    length=$((${#i} + 18))
    # echo ${length}
    for a in $( seq 1 $length ); do echo -n "#"; done
    echo
    echo "### Checking ${i}: ###"
    for a in $( seq 1 $length ); do echo -n "#"; done
    echo
    result=$(ssh ${USER}${i} 'scontrol show job' | grep -oP "(MinMemoryNode=.*?(?= )|NumCPUs=.*?(?= ))")
    cpus=$(grep -E "NumCPUs" <<< ${result} | grep -Eo "[0-9]+")
    cpus=(${cpus})
    mems=$(grep -E "MinMemoryNode" <<< ${result} | grep -Eo "[0-9]+")
    mems=(${mems})
    echo -en "There are a total of ${#cpus[@]} jobs in the queue.\n"
    echo -en "List of cores requested by every job in the queue: ${cpus[*]}\n"
    echo -en "List of GB of memory requested by every job in the queue: ${mems[*]}\n"
    cpuSum=0
    memSum=0
    for index in "${!cpus[@]}"
    do
        cpuSum=$((cpuSum + cpus[index]))
        memSum=$((memSum + mems[index]))
    done
    if [[ $cpuSum -ge $maxCpu ]]
    then
        echo "There are no available cores: the jobs in the queue are asking for ${cpuSum} cores."
    else
        availCpu=$((maxCpu - cpuSum))
        echo "There are ${availCpu} available cores"
        if [[ $memSum -ge $maxMem ]]
        then
            echo "There is no available memory: the jobs in the queue are asking for ${memSum} GB."
        else
            availMem=$((maxMem - memSum))
            echo "There are ${availMem} GB of memory available"
        fi
    fi
    echo -en "\n"
done

