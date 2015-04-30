class Resistencias : #Comienza la clase
    def __init__ ( self ):
        self.color1=None
        self.color2=None
        self.color3=None
        
    def setcolor1 ( self,a ):
        self.color1=a
    def setcolor2 ( self,a ):
        self.color2=a
    def setcolor3 ( self,a ):
        self.color3=a
    
    def getcolor1 ( self ):
        a=self.color1
        return a
    def getcolor2 ( self ):
        a=self.color2
        return a
    def getcolor3 ( self ):
        a=self.color3
        return a
#Termina la clase

def iteracionr (a):
    a=a
    cont=0
    b=[]
    for i in a :
        if cont == 0 :
            R.setcolor1(i)
        elif cont == 1 :
            R.setcolor2(i)
        elif cont > 1:
            b.append(i)
        cont=cont+1
    R.setcolor3(b)
        
R=Resistencias() #Aqui comienza el programa principal
a=raw_input("Ingrese el valor de la recistencia: ")
iteracionr(a)