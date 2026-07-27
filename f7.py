def LargestNum(nums):

    sorted_list = list(set(nums))   
    sorted_list.sort()              

    return sorted_list[-2]          

n = int(input("Enter limit: "))

nums = []

for i in range(n):
    x = int(input())
    nums.append(x)

print("Second largest =", LargestNum(nums))
