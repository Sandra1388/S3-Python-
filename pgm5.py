PhoneBook = {}

print("1)Create Entry\n2)Update\n3)Search\n4)Delete\n5)Exit")
while True:
    ch = int(input("\nEnter your choice:"))

    if ch == 1:
        name = input("Enter name:")
        number = int(input("Enter phone number:"))
        PhoneBook[name] = number
        print("Record entered successfully..")
        
    elif ch == 2:
        name = input("Enter name to update:")
        if name in PhoneBook:
            number = int(input("Enter new number:"))
            PhoneBook[name] = number
            print("Record updated successfully..")
        else:
            print("Record not found")

    elif ch == 3:
        name = input("Enter name to search:")
        if name in PhoneBook:
            print("Record found", PhoneBook[name])
        else:
            print("Record not found")
            
    elif ch == 4:
        name = input("Enter name to delete:")
        if name in PhoneBook:
            del PhoneBook[name]
            print("Record deleted successfully..")
        else:
            print("Record not found")

    elif ch == 5:
        print("Exiting...")
        break;
    
    else:
        print("Enter valid choice")
