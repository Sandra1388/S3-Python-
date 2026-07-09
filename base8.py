'''
print prime factorisation numbers
Eg:- i/p : 12
     o/p : 2 2 3
'''

n = int(input("Enter number:"))

i=2

while i <= n:
    while n%i == 0:
        print(i, end=" ")
        n = n//i
    i += 1
