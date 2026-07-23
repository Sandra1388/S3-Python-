def largest(a,b):
    if a>b:
        return a
    else:
        return b

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

result = largest(a,b)
print("Largest number is ",result)
