frukty = {
"alma" : 8,
"uzum" : 12,
"hurma" : 18,
"banan" : 25,
"nar" : 15}

d = 0
while True:

    for a,b in frukty.items():
        print(a, "-", b)

    aljak_zadyn = input("Name almak isleyarsiniz ? ")
    
    if aljak_zadyn == "quit":
        break
    if aljak_zadyn in frukty:
        kg = int(input(f"Nace kg {aljak_zadyn} almak isleyarsiniz ? "))
        d += frukty[aljak_zadyn] * kg 

print(f"Siz {d} manat tolemeli !!!")
        
     
