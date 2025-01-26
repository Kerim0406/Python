def faktorial_():
    faktorial = 1
    san = int(input("Bir sany girizin: "))
    if san < 0:
        print("Faktorial: Yalnys san ! Pozitiw san girizin.")
        return
    else:
        for i in range(1, san + 1):
            faktorial *= i
        print(f"Faktoriyal: {faktorial}")
faktorial_()