# a)
telefon_belgi = {
"Anna" : "63188199",
"Gurban" : "63115599",
"Oraz" : "62111444"}
print(telefon_belgi)

# b)
print(telefon_belgi["Anna"])

# c)
sorag = input("Kimin telefon belgisi gerek ? ")
if sorag in telefon_belgi:
    print(f"{sorag} - yn telefon belgisi: {telefon_belgi[sorag]}")
else:
    print(f"{sorag} - yn telefon belgisi tapylmady !")

# d)
print(len(telefon_belgi))

# e)
telefon_belgi["Gurban"] = "63625495"
print(telefon_belgi)

# f)
telefon_belgi["Muhhamet"] = "63384289"
print(telefon_belgi)

# g)
telefon_belgi.pop("Gurban")
print(telefon_belgi)

# h)
for i in telefon_belgi.keys():
    print(i)

# i)
for i in telefon_belgi.values():
    print(i)

# j)
for i,k in telefon_belgi.items():
    print(i,k)

# k)
telefon_belgi.clear()
print(telefon_belgi)
