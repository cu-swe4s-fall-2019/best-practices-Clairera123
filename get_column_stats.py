import sys
import os
import math
import argparse


def calc_mean(data_set):
    """ Calculate the mean of a column in an array.

    Arguments
    ---------
    data_set: single column of integers

    Returns
    -------
    mean: mean
    """
 
    mean = sum(data_set)/len(data_set)
    print('mean:', mean)
    return(mean)

def calc_stdev(data_set):
    """ Calculate the standard deviation of a column in an array

    Arguments
    ---------
    data_set: single column of integers

    Returns
    -------
    stdev: stdev
    """

    stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))
    print('stdev:', stdev)
    return(stdev) 

def main():
    
    parser = argparse.ArgumentParser(
                description='input file and column of interest, returns mean and stdev',
                prog='arg')

    parser.add_argument('file_name',
                        type=str,
                        help='Name of file',
                        required=True)

    parser.add_argument('column_number',
                        type=int,
                        help='column of interest',
                        required=True)

    args = parser.parse_args()

    V=[]

    try:
        f = open(args.file_name, 'r')
    except FileNotFoundError:
        print('Could not find' + args.file_name)
        sys.exit(1)
    except PermissionError:
        print('Could not open' + args.file_name)
        sys.exit(1)

    a = calc_mean(V)
    b = calc_stdev(V)
    print(a) 
    print(b)

if __name__ == '__main__':
    main()
