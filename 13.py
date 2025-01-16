while True:
    num = int(input("Enter a number: "))
    if num > 0 or num < 0:
        print(f"{num} the square is: {num**2}")
    else:
        print("Quit !")
        break