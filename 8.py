num = int(input("Enter a number: "))
if num % 2 == 0:
    if num > 0: 
        print("Positive, even")
    if num < 0:
        print("Negative, even")
    else:
        print("Zero")
elif num % 2 == 1:
    if num > 0: 
        print("Positive, odd") 
    else:
        print("Zero")
else:
    print("Negative, odd ")
