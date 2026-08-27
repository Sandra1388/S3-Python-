'''
You are given a X integer array matrix with space separated elements ( \N = rows and M = columns).
Your task is to print the transpose and flatten results.
'''
import numpy as np

n, m = map(int, input().split())
my_array = []
for i in range(n):
    row = list(map(int, input().split()))
    my_array.append(row)
my_array = np.array(my_array)

print(np.transpose(my_array))

print(my_array.flatten())


