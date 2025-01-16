gornusler = {
"hello" : "salam",
"apple" : "alma",
"lemon" : "limon",
"cat" : "pisik",
"dog" : "it",
"flag" : "baydak",
"student" : "okuwcy",
"family" : "masgala",
"pen" : "rucka",
"water" : "suw",
"bread" : "corek"}

while True:
    sorag = int(input("""***** My dictionary Program *****
1.Show
2.Add
3.Edit
4.Delete
5.Exit
Your choice ? """))
    if sorag == 1:
        for i,j in gornusler.items():
            print(i, '-',j)
    elif sorag == 2:
        a = input("Enter the word in English: ")
        b = input("Enter the word in Turkmen: ")
        gornusler[a] = b
        print("Added successfully !")
    elif sorag == 3:
        a = input("Enter the word in English: ")
        b = input("Enter the word in Turkmen: ")
        gornusler[a] = b
    elif sorag == 4:
        c = input("Pozjak keyini ayt: ")
        gornusler.pop(c)
    elif sorag == 5:
        print("Thanks for using program !!!")
    else:
        ("wrong command !!!")
        break

