def process_string():
    txt = input("Enter string:") #string input from the user

    print("Uppercase:", txt.upper()) #string in uppercase 

    print("Lower:", txt.lower()) #string in lowercase

    print("Length:", len(txt)) #length of the string

    rev = txt[::-1]
    print("Reverse:", rev) #reverse of the string using slicing

    if txt == rev: #palindrome  check
        print("String is Palindrome")
    else:
        print("String is not Palindrome")

process_string() #function call
