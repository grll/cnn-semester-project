#!/bin/bash
# script to run process_bleu_score.py in the background on the 24 CPU
# @args:
# - $1: number of images (to split in 24 bins)
# - $2: name of the output file (gonna be filled with each bean mean bleu score comma separated)
# - $3: path of the match_index file used by the python script to retrieve the match betweem images

START=$(date +%s)
let n=$1/24+1
let c=0
for ((i=0;i<$1;i+=n)); do
    let end=$i+n
    if ((end>=$1)); then
        let end=$1
    fi

    python process_bleu_score.py $2 $3 $i $end >/dev/null 2>&1 &
    pids[${c}]=$!
    let c=c+1
done

for pid in ${pids[*]}; do 
    wait $pid
done;

END=$(date +%s)
DIFF=$(( $END - $START ))
echo "It took $DIFF seconds"