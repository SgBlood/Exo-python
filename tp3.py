'''
EXO 1


def nbrChiffrCarre (carre):
   nbr = carre * carre 
   nbr = str(nbr)
   return len(nbr)
base = int(input("rentre un carré a calculer : "))
print (nbrChiffrCarre(base))
'''

'''
EXO 2 

def premier(n):
   for i in range(2,n):
      if (n % 2) == 0:
         return True
   return False
n = int(input("Entre un nombre pour verifier la primalité : "))
print(premier(n))
'''

"""
EXO 3

"""
nbrPrem = []
b = int(input("Rentre un nombre d'itérations : "))
def premier(n):
   for i in range(2,n):
      if (n % 2) == 0:
         return True
   return False
n = int(input("Entre un nombre pour verifier la primalité : "))
for x in range(2,b):
   premier(n)
list.append(premier(n))
print(nbrPrem)




