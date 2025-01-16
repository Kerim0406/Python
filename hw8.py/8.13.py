num = int(input("How many numbers input: "))
sum = 0
for i in range(1, num+1):
    num2 = int(input(f"{i} number: "))
    sum += num2
print(f"Sum: {sum}")