def calculator():
    while True:
        san_1 = float(input("1 - nji sany girizin: "))
        san_2 = float(input("2 - nji sany girizin: "))
        funksiya = input("Funksiya saylan: (+, -, *, /)\nFunksiya: ")
        if funksiya == "+":
            print(f"Netije: {san_1 + san_2}")
        elif funksiya == "-":
            print(f"Netije: {san_1 - san_2}")
        elif funksiya == "*":
            print(f"Netije: {san_1 * san_2}")
        elif funksiya == "/":
            print(f"Netije: {san_1 / san_2}")
        else:
            print("Nadogry funksiya !")
        a = input("Tazden hasaplayarsynyzmy (howa/yok) ? ")
        if a == "yok":
            break
        else:
            continue

calculator()
