a = int(input("Enter a number:"))
is_prime = True

if a <= 1:
        is_prime = False
else:
    for i in range(2,a):
        if a % i == 0:
            is_prime = False
            break
if is_prime:
    print("prime")
else:
    print("not")
        
