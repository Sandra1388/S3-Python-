#pPALINDROME
a = int(input("Enter a number:"))

rev = 0
n = a

while a > 0:
    num = a%10
    a = a//10
    rev = rev*10+num

if n == rev:
    print("palindrome")
else:
    print("Not")
