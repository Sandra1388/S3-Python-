#Password Strength Checker

def password_checker(psw):
    num = 0
    upper = 0
    lower = 0
    spec = 0
    for ch in psw:
        if ch.isdigit():
            num += 1
        elif ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch == "!" or ch == "@" or ch =="#":
            spec += 1
            
    if len(psw) < 8:
        print("Weak Password: Password should have atleast 8 character")
    elif upper < 1:
        print("Weak Password: Password should have atleast 1 uppercase")
    elif lower < 1:
        print("Weak Password: Password should have atleast 1 lowercase")
    elif spec < 1:
        print("Weak Password: Password should have atleast 1 special character")
    elif num < 1:
        print("Weak Password: Password should have atleast 1 number")
    else:
        print("Strong Password")
        
                
psw = input("Enter your password:")
password_checker(psw)
