def san():
    while True:
        san_ = int(input("Bir san girizin (Durmak ucin 0): "))
        if san_ == 0:
            for i in san_:
                max_ = max(i)
                min_ = min(i)
        print(f"Max number: {max_}\nMin number: {min_}")
san()
# Doly edilmedik