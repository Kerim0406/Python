num = int(input("Enter a number: "))
if num % 2 == 0:
    if num > 100 and num < 1000:
        print("Three digit, even ")
    if num > 10 and num < 100:
        print("Two digit, even ")
    if num > 0 and num < 10:
        print("One digit, even ")
    if num > 1000:
        print("I didn't understand ")
elif num % 2 == 1:
    if num > 100 and num < 1000: 
        print("Three digit, odd")
    if num > 10 and num < 100: 
        print("Two digit, odd ")
    if num > 0 and num < 10:
        print("One digit, odd ")
    if num > 1000:
        print("I didn't understand ")