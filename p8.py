#question 8

def EvenOrOdd(a):
    if a%2 == 0:
        print("Even number")
    else:
        print("Odd number")

def palindrome(a):
    num = a
    r = 0
    while num!=0:
        n = num%10
        r = r*10+n
        num = num//10
    print(r)
    if (r == a):
        print("Palindrom")
    else:
        print("Not palindrome")

def prime(a):
    if a<2:
        print("Not prime")
        return
    
    for i in range(2,a//2+1):
        if a%i == 0:
            print("Not Prime")
            return
    print("Prime")

def armstrong(a):
    l = len(str(a))
    num = a
    total = 0
    while num!=0:
        n = num%10
        total = total + (n**l)
        num = num//10
    if (a == total):
        print("Armstrong number")
        return
    else:
        print("Not Armstrong")        

    
print(" 1)Odd or Even\n 2)Palindrome\n 3)Prime\n 4)Armstrong\n 5)Exit")
a = int(input("Enter a number:"))
while True:
    ch = int(input("Enter your choice:"))
    if ch == 1:
        EvenOrOdd(a)
    elif ch == 2:
        palindrome(a)
    elif ch == 3:
        prime(a)
    elif ch == 4:
        armstrong(a)
    elif ch == 5:
        print("Exiting...")
        break
    else:
        print("invalid choice")
