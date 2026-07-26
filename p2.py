'''
We provide you with a list of integers. In this list, every number appears twice,
except for one number that appears only once. Your task is to find that single, unique number.
Example:
If the list is [4, 1, 2, 1, 2], the unique number is 4. If the list is [7, 3, 5, 4, 5, 3, 4], the unique number is 7.
'''

limit = int(input("Enter limit:"))

num_lst = []

print("Enter numbers:")
for i in range(limit):
    x = int(input())
    num_lst.append(x)

dct = {}

for num in num_lst:
    if num in dct:
        dct[num] += 1
    else:
        dct[num] = 1

for key in dct:
    if dct[key] == 1:
        print("Unique number is ", key)
        
