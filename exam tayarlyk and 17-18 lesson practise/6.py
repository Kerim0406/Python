def san(a, b):
    question = 0
    while question < b:
        sorag = int(input("Bir sany girizin (1 - 100): "))
        question += 1
        
        if sorag > a:
            print("Azyrak !")
        elif sorag < a:
            print("Koprak !")
        else:
            print("Dogry !")
            return
    if question == b:
        print(f"Utuldynyz ! Asyl san: {a}")
san(56, 5)