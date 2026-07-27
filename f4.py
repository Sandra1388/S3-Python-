#find the largest number using list and function

def largest(nums):
    larg = nums[0]
    for i in range(0, len(nums)):
        if nums[i] > larg:
            larg = nums[i]
    print("Largest number is ",larg)


n = int(input("Entre limit:"))
nums = []
for i in range(n):
    x = int(input())
    nums.append(x)

largest(nums)
