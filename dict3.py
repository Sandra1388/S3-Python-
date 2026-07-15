
nums = [4,1,4,3,2]

c = {}

for num in nums:
    if num in c:
        c[num] += 1
    else:
        c[num] = 1

for key in c:
    if c[key] == 1:
        print(key)

