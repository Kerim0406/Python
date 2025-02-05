import random 


synansyk = 0
print("Men bir san sayladym.\nSiz ony tapyp bilersinizmi ?")

kici_san = int(input("In kici san saylan: "))
uly_san = int(input("In uly san saylan: "))

gizlin_san = random.randrange(kici_san, uly_san)
while True:

    caklama = int(input("Sany caklan: "))

    if caklama > gizlin_san:
        synansyk += 1
        print("Sizin caklamanyz uly !")

    elif caklama < gizlin_san:
        synansyk += 1
        print("Sizin caklamanyz kici !")

    else:
        synansyk += 1
        print(f"Dogry tapdynyz !\nSiz {synansyk} synansykda tapmagy basardynyz !")
        break