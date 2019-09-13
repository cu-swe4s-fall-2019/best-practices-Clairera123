#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest. ssshtest

run basic_mean pycodestyle style.py mean 1 3
assert_in_stdout 2
assert_exit_code 0 

run basic_stdev pycodestyle get_column_stats.py stdev 1 1
assert_in_stdout 0
assert_exit_code 0

(for i in `seq 1 100` do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM"
    done ) > data.txt


python get_column_stats.py data.txt 2


V=1
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V"
done ) > data.txt

python get_column_stats.py data.txt 2

assert_exit_code 0
