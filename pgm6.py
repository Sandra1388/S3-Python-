n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))

print("\n1)Addition\n2)Subtraction\n3)Multiplication\n4)Division\n5)Exit")
while True:
    ch = int(input("\nEnter your choice:"))
    if ch == 1:
        print("Sum = ",n1+n2)
    elif ch == 2:
        print("Difference = ", n1-n2)
    elif ch == 3:
        print("Product = ", n1*n2)
    elif ch == 4:
        if n2 == 0:
            print("Division by 0 is not possible")
        else:
            print("Quotiant = ",n1/n2)
    elif ch == 5:
        print("Exiting...")
        break;
    else:
        print("Enter valid choice")
