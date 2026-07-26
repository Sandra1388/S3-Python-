'''
Check whether the given string can be used as a valid variable name in Python.
Explanation:
In Python, a valid variable name:
Can only contain letters (a–z, A–Z), digits (0–9), and underscores (_).
The variable name cannot begin with a digit.
The string cannot contain reserved keywords such as "for," "if," "class," and so on.
'''

n = input("Enter a name:")
f = 0
if n[0].isdigit():
        f += 1
for ch in n:
    if ch == "!" or ch == "@" or ch == "#" or ch == "$" or ch == "%" or ch == "%" or ch == "^" or ch == "&":
        f += 1
    elif n == "for" or n == "if" or n == "class" or n == "elif":
        f += 1
if f > 0:
    print("Invalid variable name")
else:
    print("Valid varibale name")
