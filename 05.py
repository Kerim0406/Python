num = [1, 2, 3, 4, 5, 6]
jubut = []
tak = []
    
for i in num:
    if i % 2 == 0:
        jubut.append(i)
    else:
        tak.append(i)
print(f"Jubut sanlar: {jubut}")
print(f"Tak sanlar: {tak}")
