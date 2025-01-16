soz = input("Enter the string: ")
a = 0
b = 0
c = 0
d = 0
e = 0
for i in soz:
    if i.isalpha():
        a += 1        
    if i.isupper():
        b += 1
    if i.islower:
        c += 1
    if i.isdigit():
        d += 1
    if i.isspace():
        e += 1
print()