# a)
okuvcylar = {"Anna" : {"synag1" : 80,
                      "synag2" : 75,
                      "synag3" : 70},
            
            "Merdan" : {"synag1" : 90,
                      "synag2" : 85,
                      "synag3" : 80},
            
            "Oraz" : {"synag1" : 100,
                      "synag2" : 95,
                      "synag3" : 60}}

print("Merdanyn ahli synag bahalary asakda !")

for i in okuvcylar["Merdan"].values():
    print(i)

# b)
print("Annanyn dine synag_1 bahasy asakda !")
print(okuvcylar["Anna"]["synag1"])

# c)
print("Orazyn dine synag_3 bahasy asakda !")
print(okuvcylar["Oraz"]["synag3"])

# d)
ady = input("Ady: ")
howa_yok = input("Ahli synaglar: (howa/yok) ")

if howa_yok == "howa":
    print(okuvcylar[ady])
else:
    haysy = input("synag1/synag2/synag3: ")
    
    if haysy == "synag1":
        print(okuvcylar[ady][haysy])
    elif haysy == "synag2":
        print(okuvcylar[ady][haysy])
    else:
        print(okuvcylar[ady][haysy])