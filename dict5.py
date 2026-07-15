nums = [1,2,2,3,3,3,4,4,4,4,4]

new = {}
for num in nums:
    if num in new:
        new[num] += 1
    else:
        new[num] = 1

for key in new:
    if new[key] % 2 == 0:
        new[key] = "Even"
    else:
        new[key] = "Odd"
print(new)
