# Islendik zady terslikan yazmak
# num = input("San girizin:\n")
# print(f"{num}-sanyn tersi: {num[::-1]}")



# 1
# num = int(input("Iki belgili san girizin:\n"))
# first = num % 10
# second = num // 10
# print(f"{num}-sanyn tersi: {first}{second}")

# 2
# num = int(input("Uch belgili san girizin:\n"))
# first = num % 10
# second = num // 10 % 10
# third = num // 100
# print(f"{num}-sanyn tersi: {first}{second}{third}")


# 3
price = eval(input("Price (bahasy): "))
weight = eval(input("Weight (agramy): "))
kg = 25
tl = 1.18
print("- - - - - - - - - -")
print(f"Money due: {(price * tl) + (weight * kg)}")