import re
# EXO 1
# fichier = open("index.html", "r",encoding='utf-8') 
# content = fichier.read() 
# fichier.close() 

# EXO 2
# fichier = open("index.html", "r",encoding='utf-8') 
# content = fichier.read() 
# fichier.close()
# motif = 'href="(.*)"'
# res = re.findall(motif,content)
# print(res)
# for i in res:
#     print(i)

#EXO 3
# fichier = open("index.html", "r",encoding='utf-8') 
# content = fichier.read() 
# fichier.close()

# motif = 'href="(.*\/article\/.*)"'
# res = re.findall(motif,content)
# print(res)
# for i in res:
#     print(i)

#EXO 4
fichier = open("index.html", "r",encoding='utf-8') 
content = fichier.read() 
fichier.close()

motif = 'href=".*\/article\/.*(([0-9]{4})\/([0-9]{2})\/([0-9]{2})).*"'
res = re.findall(motif,content)
for i in res:
    print(i[1] + '-' + i[2] + '-' + i[3])