class Resistencias : #Comienza la clase
    def __init__ ( self ):
        self.color1=None
        self.color2=None
        self.color3=None
        self.color4=None
        
    def setcolor1 ( self,a ):
        self.color1=a
    def setcolor2 ( self,a ):
        self.color2=a
    def setcolor3 ( self,a ):
        self.color3=a
    def setcolor4 ( self,a ):
        self.color4=a
    
    def getcolor1 ( self ):
        a=self.color1
        return a
    def getcolor2 ( self ):
        a=self.color2
        return a
    def getcolor3 ( self ):
        a=self.color3
        return a
    def getcolor4 ( self ):
        a=self.color4
        return a
#Termina la clase

def colores (e): #Funcion colores con los colores de las resistencias comerciales
    e=e
    if e ==  ['1','0'] :
        print 'Marron-Negro',#
    elif e == ['1','2'] :
        print 'Marron-Rojo',#
    elif e == ['1','5'] :
        print 'Marron-Verde',#
    elif e == ['1','8'] :
        print 'Marron-Gris',#
    elif e == ['2','2'] :
        print 'Rojo-Rojo',#
    elif e == ['2','7'] :
        print 'Rojo-Violeta',#
    elif e == ['3','3'] :
        print 'Naranja-Naranja',#
    elif e == ['3','9'] :
        print 'Naranja-Blanco',#
    elif e == ['4','7'] :
        print 'Amarillo-Violeta',#
    elif e == ['5','6'] :
        print 'Verde-Azul',#
    elif e == ['6','8'] :
        print 'Azul-Gris',#
    elif e == ['8','2'] :
        print  'Gris-Rojo',#
    elif e == ['9','1'] :
        print 'Blanco-Marron',#
    else  :
        print 'El numero ingresado no es parte del los valores comerciales de las resistencia'
        menu() #fin de la funcion colores
        
        
def valorcero (a): #funcion valorcero son la cantidad de cero que va despues de los dos primeros numeros
    cont=0
    for i in a :
        if i == '0' :
            cont=cont+1 
        
    if cont == 0:
        print '-Negro'
    elif cont == 1 :
        print '-Marron'
    elif cont == 2 :
        print '-Rojo'
    elif cont == 3 :
        print '-Naranja'
    elif cont == 4 :
        print '-Amarillo'
    elif cont == 5 :
        print '-Verde'
    elif cont == 6 :
        print '-Azul'
    elif cont == 7 :
        print '-Violeta'
    elif cont == 8 :
        print '-Gris'
    elif cont == 9 :
        print '-Blanco' #fin de la funcion valorcero
        
        
def tolerancia (t): #funcion tolerancia
    if t == '5%' :
        print '-Dorado'
    elif t == '10%' :
        print '-Plata'
    else  :
        print "El valor ingresado no corresponde a ningun valor existente de tolerancia" 
        menu() #fin da la funcion tolerancia

def iteracionr (a,y): #Funcion itaracion
    R=Resistencias()
    a=a
    y=y
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
    R.setcolor4(y)
    
    cont2=0
    r=[]
    while cont2 < 2 :
        if cont2 == 0 :
            e=R.getcolor1()
            r.append(e)
        elif cont2 == 1 :
            e=R.getcolor2()
            r.append(e)
        cont2=cont2+1
    
    t=R.getcolor4()
    
    colores(r)
    valorcero(b)
    tolerancia(t)
    
def menu ( ): #menu principal
    a=raw_input("Ingrese el valor de la recistencia: ")
    y=raw_input("Ingrese el valor de la tolerancia: ")
    iteracionr(a,y)


menu()