frukty = {"Alma" : {"bahasy" : 15, "mukdary" : 30}, 
        
        "Mandarin" : {"bahasy" : 30, "mukdary" : 10},

        "Kivi" : {"bahasy" : 18, "mukdary" : 1},

        "Banan" : {"bahasy" : 27, "mukdary" : 20},

        "Nar" : {"bahasy" : 18, "mukdary" : 15}}

kassa = 0
while True:
    for a, b in frukty.items():
        print(a, "-", b)

    print()

    aljak_zady = input("Name almak isleyarsin: ")
    
    if aljak_zady in frukty:
        kg = int(input("Nace kg almak isleyarsin: "))
        
        if kg <= frukty[aljak_zady]["mukdary"]:
            money = kg * frukty[aljak_zady]["bahasy"]
            kassa += money
            frukty[aljak_zady]["mukdary"] -= kg
        else:
            print("Yeterlik mukdarda yok ! ")
    
    elif aljak_zady not in frukty:
        print(f"({aljak_zady}) dukanda yok")
    
    elif aljak_zady == "quit":
        print(f"Siz {kassa} manat tolemeli")
        break

    
        