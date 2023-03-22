'''
EXO 1

list = [1990, 1996, 1994, 1997, 1993, 2001, 1999, 2000]
list.sort()
print(list[1])
'''

'''
EXO 2

maroc = {"president": "Mohammed VI" , "capitale": "Rabat" , "superficie":
710850}
algerie = {"president": "Abdelaziz Bouteflika" , "capitale": "Alger" ,
"superficie": 2382000}
tunisie = {"president": "Kaïs Saïed" , "capitale": "Tunis", "superficie":
163610}
algerie['president'] = "Abdelmadjid Tebboune"
Dico = {}
Dico['algerie'] = algerie
Dico ['maroc'] = maroc
Dico ['tunisie'] = tunisie
print (Dico)
'''

'''
EXO 3
etudiants = {"etudiant_1":13,
                    "etudiant_2":17,
                    "etudiant_3":9,
                    "etudiant_4":15, 
                    "etudiant_5":8, 
                    "etudiant_6":14, 
                    "etudiant_7":14, 
                    "etudiant_8":12,
                    "etudiant_9":13, 
                    "etudiant_10":15,
                    "etudiant_11":14, 
                    "etudiant_112":9,
                    "etudiant_13":12,
                    "etudiant_14":12,
                    "etudiant_15":13, 
                    "etudiant_16":7, 
                    "etudiant_17":12, 
                    "etudiant_18":15, 
                    "etudiant_19":9, 
                    "etudiant_20":17,
                    "etudiant_21":18
             }
Admis = {
    
}
NonAdmis = {
    
}
for key, value in etudiants.items(): 
    if value > 10:
        Admis[key] = value
    if value <=10:
        NonAdmis[key] = value
        
Notes  = {}
Notes ['Admis'] = Admis
Notes ['NonAdmis'] = NonAdmis
print ( "Admis"+str(Admis) )
print("")
print( "NonAdmis"+str(NonAdmis))
'''

'''
EXO 4

d = { "Adam": [12, 15 , 17], 
     "Karim" : [15, 12 , 16],
     "Joshua": [13, 15 , 7] 
}
for key, value in d.items():
    value = sum(value)/len(value)
    d[key] = value
print(d)
'''

'''
EXO 5


Nbr = int(input("Entrez un nombre pour factorielle : "))
n = Nbr 
fact = 1
for i in range (1,n+1):
   fact = fact*i
print (fact)
'''

'''
EXO 6



Nbr_Note = int(input("Entrez un nombre de note pour la moyenne : "))
list = []
for i in range (0,Nbr_Note):
  Note = int(input("Rentre tes notes : "))
  list.append (Note)
print (sum(list)/Nbr_Note)
'''

'''
EXO 7 



long = int(input("Rentre la longueur de la matrice : "))
for i in range (1, long +1):
    line = ""
    for x in range (1, long+1):
        line = line + " | " + str(x*i) + " | "
    print (line)
    '''