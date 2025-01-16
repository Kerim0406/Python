summ = 0
while True:
    num = int(input("Enter a number:"))
    if num == 0:
        break
    else:
        summ += num
print(f"Sum: {summ}")