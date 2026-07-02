'''a = input("Enter a string:")'''

#method 1
'''
print("reverse=",a[::-1])
'''

#method 2
'''
rev = ""
for ch in a:
    rev = ch+rev
print(rev)
'''

#method 3

a = list(input("Enter a string:"))
left = 0
right = len(a)-1

while left<right:
    a[left], a[right] = a[right], a[left]
    left = left+1
    right = right-1

print("".join(a))


