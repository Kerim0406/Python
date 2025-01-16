star = 1
num = int(input("How many star: "))
while True:
    if star > num:
        break
    else:
        print(f"{star} {star * '*'}")
        star += 1