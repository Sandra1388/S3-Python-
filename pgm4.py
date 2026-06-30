text = input("Enter the main string:")
print("\n1)Check if the string is a substring of another string")
print("\n2)Count Occurrences of Character")
print("\n3)Replace a substring with another substring")
print("\n4)Convert to Capital Letters")
print("\n5)Exit")
while True:

    ch = int(input("\nEnter your choice:"))

    if ch ==1:
        sub_str1 = input("Enter substring:")
        if sub_str1 in text:
            print("Entered string is a substring of main string")
        else:
            print("Entered string is not a substring of main string")
                
    elif ch ==2:
        c = input("Enter a character:")
        print("Occurance:", text.count(c))

    elif ch == 3:
        sub_str2 = input("Enter substring:")
        if sub_str2 in text:
            sub_str3 = input("Enter new substring:")
            print("New string:",text.replace(sub_str2, sub_str3))
        else:
            print("Substring not found")

    elif ch == 4:
        print("Uppercase:",text.upper())

    elif ch == 5:
        print("Exiting...")
        break;
    else:
        print("Enter valid choice")
