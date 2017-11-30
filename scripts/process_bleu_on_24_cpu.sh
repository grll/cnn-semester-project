#!/bin/bash
START=$(date +%s)
let n=$1/24+1
let c=0
for ((i=0;i<$1;i+=n)); do
    let c=c+1
    let end=$i+n
    if ((end>=$1)); then
        let end=$1
    fi

    echo "python process_bleu_score $2 $3 $i $end"
done
END=$(date +%s)
DIFF=$(( $END - $START ))
echo "It took $DIFF seconds"