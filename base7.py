'''
no:of changes made to make 2 strings same
'''

s1 = input("Enter string:")
s2 = input("Enter string:")
c=0
for i in range (len(s1)):
    if s1[i] != s2[i]:
        c += 1
print (c)
            
