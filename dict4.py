#Find the number with most repetation

nums = [5,5,8,8,8,2,1,2]

count = {}
largest = 0
answer = None
for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
        
for key in count:
    if count[key] > largest:
        largest = count[key]
        answer = key

print("Key:", answer, "Value:", largest)
