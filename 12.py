a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(b ** 2 - 4 * c)
if d > 0:
    print(f"x1 = {-b + d**0.5 / 2*a}")
    print(f"x2 = {-b - d**0.5 / 2*a}")
elif d == 0:
    print(f"x1 = {-b / 2*a}")
else:
    print("No roots")