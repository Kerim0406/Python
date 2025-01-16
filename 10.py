first = eval(input("First number: "))
second = eval(input("Second number: "))
third = eval(input("Third number: "))

minn = 0
maxx = 0

# MINN
if first < second and first < third:
    minn = first
elif second < first and second < third:
    minn = second
else:
    minn = third

# MAXX
if first > second and first > third:
    maxx = first
elif second > first and second > third:
    maxx = second
else:
    maxx = third

print(f"Min: {minn}")
print(f"Max:{maxx}")