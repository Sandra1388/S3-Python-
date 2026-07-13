#Minimum number in list

nums = [2,4,1,5,-1,0]
small = nums[0]

for i in range(1,len(nums)):
    if nums[i] < small:
        small = nums[i]
print(small)
