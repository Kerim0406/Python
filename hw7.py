star = 1
num = int(input("How many: "))
while True:
    if star <= num:
        if star % 2 == 0:
            print(f"{star} {star * '@'}")
            star += 1
        else:
            print(f"{star} {star * '&'}")
            star += 1
    else:
        break


