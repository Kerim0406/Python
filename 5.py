soz = input("Enter the string: ")
for i in soz:
    if soz.count(i) == 1:
        print(f"{i} - single letter")
