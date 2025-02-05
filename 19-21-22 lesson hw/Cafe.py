menu = {
        "Coffee" : 3,
        "Tea" : 2,
        "Sandwich" : 5,
        "Cake" : 4
        }
while True:    
    print("WELCOME TO CAFE !")
    print()
    print("Menu:")
    for a, b in menu.items():
        print(a, ':', b,'$')
    item = input("Enter the item you want to order or 'done': ")
    if item == "done":
        a = menu[item]*quantity
        print(f"{item} x{quantity}: {a} $")
        break

    quantity = int(input("Enter the quantity: "))
    print(f"{quantity} {item}s added to your order")
# duzetmeli zatlar kop