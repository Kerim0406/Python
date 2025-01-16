first = int(input("First number:"))
second = int(input("Second number: "))
third = int(input("Third number: "))
if first > second and first < third or first < second and first > third:
    print(f"Mid number is: {first} ")
elif second > first and second < third or second < first and second > third:
    print(f"Mid number is: {second} ")
elif third > second and third < first or third < second and third > first:
    print(f"Mid number is: {third} ")