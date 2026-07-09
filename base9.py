n = input("Enter string:")

repeated = set()
seen = set()
for ch in n:
    if ch == " ":
        continue
    
    if ch in seen and ch not in repeated:
        print (ch, end= " ")
        repeated.add(ch)

    seen.add(ch)
