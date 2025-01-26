def jem(A):
     gos = 0
     kop = 1
     for i in A:
         gos += i
         kop *= i
     return gos, kop
print(jem([7, 7, 7, 7, 7]))