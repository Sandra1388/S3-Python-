#Simple calculator

print("1)Addition\n 2)Subtraction\n 3)Multiplication\n 4)Division\n 5)Exit")

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

while True:
    ch = int(input("Enter your choice:"))
    
    if ch == 5:
        print("Exiting....")
        break

    if ch == 1:
        print("Sum of ", a,"and", b,"=", a+b)
        
    elif ch == 2:
        print("Difference of ", a, "and", b, "=", a-b)
        
    elif ch == 3:
        print("Product of ", a, "and", b, "=", a*b)
        
    elif ch == 4:
        if a > 0:
            print("Quotient of ", a, "and", b, "=", a/b)
        else:
            print("Division by zero is not possible")
        
    else:
        print("Invalid choice")
        break
        
        
