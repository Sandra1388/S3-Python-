#Recursive Functions - Sum & Factorial

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)
        
n = int(input("Enter number:"))
print("Factorial = ", factorial(n))
