#function that count odd numbers in the list

def OddCount(nums):
    c = 0
    for i in range(0,len(nums)):
        if nums[i] % 2 != 0:
            c += 1
    print("Total odd numbers = ", c)


n = int(input("Entre limit:"))
nums = []
for i in range(n):
    x = int(input())
    nums.append(x)

OddCount(nums)
