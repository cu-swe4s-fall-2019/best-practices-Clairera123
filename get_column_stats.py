import sys
import math
import argparse

parser = argparse.ArgumentParser(description='Using argparse correctly',
                                 prog='get_column_stats')

parser.add_argument('file_name',
                    type=str,
                    help='number column')

parser.add_argument('column_number',
                    type=int,
                    help='column of number')

args = parser.parse_args()

f = open(args.file_name, 'r')

V = []

for l in f:
    A = [int(x) for x in l.split()]
    V.append(A[args.column_number])

mean = sum(V)/len(V)

stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))

print('mean:', mean)
print('stdev:', stdev)

try:
    f = open(args.file_name, 'r')
except FileNotFoundError:
    print('Could not find' + args.file_name)
except PermissionError:
    print('Could not open' + args.file_name)


try:
    args.column_number = str
except ValueError:
    print('Insert integer')


f = append_to_file('no_file.txt')
f = append_to_file('no_read_permission.txt')
