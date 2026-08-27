'''
You are given two integer arrays of size X and X (N & M are rows, and P is the column). Your task is to concatenate the arrays along axis 0.
import numpy as np
'''
n,m,p = map(int, input().split())
a=[]
b=[]

for i in range(n):
    a.append(list(map(int,input().split())))

for i in range(m):
    b.append(list(map(int,input().split())))
    
a = np.array(a)
b = np.array(b)

print(np.concatenate((a,b))) 
