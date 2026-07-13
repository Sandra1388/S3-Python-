#Reverse of list

nums = [1,2,3,4]
new = []
for i in range(len(nums)-1,-1,-1):
    new.append(nums[i])
print(new)
