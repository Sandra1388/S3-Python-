
#Storing the elements in a dictionary and counting the freq of how numbers occur
nums = [1,2,3,2,3,4,5,5]

count = {}

for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
print (count)
