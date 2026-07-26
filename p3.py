'''
Write a Python program that defines a function named process_string() that:
Accepts a string input from the user.
Prints the string in uppercase and lowercase.
Displays the length of the string.
Reverses the string using slicing and prints the result.
check whether the given string is palindrome or not
             Then, call the function to execute these operations.
'''

def process_string(name):
    print("Uppercase:", name.upper())
    print("Lowercase:", name.lower())
    print("Length:", len(name))
    print("Reverse:", name[::-1])

    if name == name[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")


name = input("Enter a string: ")
process_string(name)
        

