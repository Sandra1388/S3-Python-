#Smallest number using list and function

def SmallNum(nums):
    small = nums[0]
    for i in range(0,len(nums)):
        if nums[i] < small:
            small = nums[i]

    print("Smallest Number = ", small)

n = int(input("Enter limit:"))
nums = []
for i in range (n):
    x = int(input())
    nums.append(x)

SmallNum(nums)
