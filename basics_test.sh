#!/bin/bash

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest. ssshtest

#test style guides
run test_style pycodestyle style.py
assert_in_stdout 
assert_exit_code 0 

run basic_stdev pycodestyle get_column_stats.py 
assert_in_stdout 
assert_exit_code 0

(for i in `seq 1 100` do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM"
    done ) > data.txt


run test_random_file python get_column_stats.py --f data.txt --c 1
assert_exit_code 0 
assert_stdout
assert_in_stdout "mean:"
assert_in_stdout "stdev:"


V=1
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V"
done ) > data.txt

run test_one python get_column_stats.py --f data.txt --c 1 
assert_exit_code 0 
assert_stdout
assert_in_stdout "mean: 1.0"
assert_in_stdout "stdev: 0.0"

run no_file_name_test python get_column_stats.py --f wrong.txt --c 1
assert_exit_code 1 
assert_stdout
assert_in_stdout "FileNotFoundError" 

run str_instead_of_int_test python get_column_stats.py --f data.txt --c a
assert_exit_code 1
assert_stdout
assert_in_stdout "ValueError"
