class PtGeo:
    def __init__(self,x,y,name):
        self.x = x
        self.y = y
        self.name = name
        
    def proc(self):
        print("Point " + " | " + str(self.name) + " | " + " de coordonées x = " + str(self.x) +" ay = " + str(self.y))
    
def createtp():
    PtGeo.name = input("Entre le nom du point : ")
    PtGeo.x = int(input("Entre le coordonée : "))
    PtGeo.y = int(input("Entre le coordonée : "))
    return PtGeo(PtGeo.x,PtGeo.y,PtGeo.name)
        
    #createtp()
    #print("le nom du point est : " +  str(PtGeo.name)  +"\n" + "la première coordonée est : " + str(PtGeo.x) + "\n" + "la deuxième coordonée est : " + str(PtGeo.y))

pt = createtp()
#pt.proc()

def align ():
   pt1 = createtp()
   pt2 = createtp()
   pt3 = createtp()
   if ((pt2.x-pt1.x))/(pt2.y-pt1.y) == (pt3.x-pt1.x)/(pt3.y-pt1.y ):
       return True
   else:
       return False
align()