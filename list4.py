'''
return a new array with elements greater than 5
'''
nums = [2,3,4,5,6,7]
new = []
for i in range(1,len(nums)):
    if(nums[i] > 5):
        new.append(nums[i])
print(new)
        
               
