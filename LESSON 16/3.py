dukan = { 
         "alma" : {'bahasy':15, 'mukdary':30},
        "mandarin" : {'bahasy': 30, 'mukdary': 10},
        "kivi" : {'bahasy': 18, 'mukdary': 1},
        "banan" : {'bahasy':27, 'mukdary': 20},
        "nar" : {'bahasy': 18, 'mukdary': 15},
}

kassa = 0 
operation = ""

while operation != 'quit':
    print("\n*** DUKAN DOLANDYRYS ***")
    print("1. Haryt gorkezijilerini gor")
    print("2. Haryt satyn al")
    print("3. Harytlary gos")
    print("4. Harytlaryn bahasyny uytget")
    print("5. Harytlary ayyr")
    print("6. Mukdary artdyr")
    print("7. Kassany gor")
    print("7. Cykys ucin 'quit' yazyn")

    operation = input('Nama etmeli? (san girizin): ')

    # 1.Haryt gorkezijilerini gor
    if operation == '1':
        print("\nDukandaky harytlary:")
        for i, j in dukan.items():
            print(f"{i} - Bahasy: {j['bahasy']} manat, Mukdary: {['mukdary']} kg")

    # 2. Haryt satyn al
    elif operation == '2':
        haryt = input('Nama satyn aljak ')
        if haryt in dukan:
            kg = float(input(f"Naca kg {haryt} almak isleyan? "))
            if kg <= dukan[haryt]['mukdary']:
                pul = kg * dukan[haryt]['bahasy']
                kassa += pul 
                dukan[haryt]['mukdary'] -= kg
                print(f"{haryt}-y satyn aldynyz! {pul} manat boldy.")
            else:
                print(f"{haryt}-yn yeterlik mukdary yok! Hazirlikce {dukan[haryt]['mukdary']} kg bar")
        else:
            print(f"{haryt} dukanda yok!")
    
    # 3. Harytlary gos
    elif operation == '3':
        haryt = input('Taze haryt ady girizin: ')
        baha = float(input(f"{haryt}-yn bahasy: "))
        mukdar = float(input(f"Nace kg {haryt} gosmaly? "))
        dukan[haryt] = {'bahasy': baha, 'mukdary': mukdar}
        print(f"{haryt} gosuldy.")

    # 4. Harytlaryn bahasyny uytget
    elif operation == '4':
        haryt = input('Haysy harydyn bahasyny uytgetmeli: ')
        if haryt in dukan:
            baha = float(input(f"{haryt}-yn taze bahasy: "))
            dukan[haryt]['bahasy'] =  baha
            print(f"{haryt}-yn bahasy tazelendi.")
        else:
            print(f"{haryt} dukanda yok")

    # 5. Harytlary ayyr
    elif operation == '5':
        haryt = input('Haysy harydy ayyrmaly: ')
        if haryt in dukan:
            del dukan[haryt]
            print(f"{haryt} dukanda ayryldy.")
        else:
            print(f"{haryt} dukanda yok")

    # 6. Mukdary artdyr
    elif operation == '6':
        haryt = input('Haysy harydyn mukdaryny artdyrmaly: ')
        if haryt in dukan:
            gosuljak_mukdar = float(input(f"Nace kg gosmaly?(onli mukdary:{dukan[haryt]['mukdary']}):  "))
            dukan[haryt]['bahasy'] +=  gosuljak_mukdar
            print(f"{haryt}-yn bahasy tazelendi.")
        else:
            print(f"{haryt} dukanda yok")
        
    # 7. Kassany gor 
    elif operation == '7':
        print(f"jemi kassa: {kassa} manat")

    # Cykys
    else operation == 'quit':
        print('programma tamamlady!')
    else:
        print("Nadogry operasiya! Gaytadan saylan.")