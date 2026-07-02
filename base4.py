#REVERSE A NUMBER

a = int(input("Enter a number:"))
rev = 0
while a > 0:
    
    n = a%10
    a = a//10
    rev = rev*10+n
print(rev)
