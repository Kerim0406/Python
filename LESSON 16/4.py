KITAPHANA = {101 : {"ady" : "Perman", "awtory" : "A.Govshudov", "sany" : 8},
    
    102 : {"ady" : "Saylanan eserler", "awtory" : "G.Ezizov", "sany" : 12},
    
    103 : {"ady" : "Ykbal", "awtory" : "H.Deryayev", "sany" : 6},
    
    104 : {"ady" : "Leyli Mejnun", "awtory" : "N.Andalyp", "sany" : 4},
    
    105 : {"ady" : "Oylanma bayry", "awtory" : "K.Gurbannepesov", "sany" : 9}}

while True:

    saylow = input("""***** KITAPHANA *****
1. Kitaplary gormek
2. Kitap almak
3. Kitap tabshyrmak
4. Chykmak
Saylan: """)

    if saylow == "1":
        for a, b in KITAPHANA.items():
            print(a, "-", b)

    elif saylow == "2":
        kitap_belgisi = int(input("Kitap belgisi: "))
    
        if kitap_belgisi in KITAPHANA: 
            kitap_sany = int(input("Kitap sany: "))
            
            if kitap_sany <= KITAPHANA[kitap_belgisi]["sany"]:
                KITAPHANA[kitap_belgisi]["sany"] -= kitap_sany
                a = KITAPHANA[kitap_belgisi]["awtory"]
                b = KITAPHANA[kitap_belgisi]["ady"]
                print(f"Siz {a} - yn {b} kitabyndan {kitap_sany} sany aldynyz !")
    
    elif saylow == "3":
        kitap_belgisi = int(input("Kitap belgisi: "))
        
        if kitap_belgisi in KITAPHANA: 
            kitap_sany = int(input("Kitap sany: "))
            KITAPHANA[kitap_belgisi]["sany"] += kitap_sany
            a = KITAPHANA[kitap_belgisi]["awtory"]
            b = KITAPHANA[kitap_belgisi]["ady"]
            print(f"Siz {a} - yn {b} kitabyndan {kitap_sany} sany tabshyrdynyz !")

    elif saylow == "4":
        print("Sagbolun kitaphanamyza gelip durun ! ")
        break

    else:
        print("Nadogry buyruk ! ")
        break

    