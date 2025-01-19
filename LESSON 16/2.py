frukty = {"Alma" : {"bahasy" : 15, "mukdary" : 30}, 
        
        "Mandarin" : {"bahasy" : 30, "mukdary" : 10},

        "Kivi" : {"bahasy" : 18, "mukdary" : 1},

        "Banan" : {"bahasy" : 27, "mukdary" : 20},

        "Nar" : {"bahasy" : 18, "mukdary" : 15}}

kassa = 0
while True:

    dukan_dolandyrysy = input("""*** DUKAN DOLANDYRYSY ***
1. Haryt gorkezijilerini gor
2. Haryt satyn al
3. Harytlary gos
4. Harytlaryn bahasyny uytget
5. Harytlary ayyr
6. Mukdary artdyr
7. Kassany gor
Cykys ucin "quit" yazyn !
Name etmeli ? (san girizin): """)

    if dukan_dolandyrysy == "1":

        for a, b in frukty.items():
            print(a, ("-"), b)    

    elif dukan_dolandyrysy == "2":
        haryt = input("Name satyn aljak ? ")
    
        if haryt in frukty:
            kg = input("Nace kg almak isleyaniz ? ")
            
            if kg <= frukty[haryt]["mukdary"]:
                money = kg * frukty[haryt]["bahasy"]
                kassa += money
                frukty[haryt]["mukdary"] -= kg
                print(f"{haryt} - satyn aldynyz ! {kassa} manat tolediniz.")
            



