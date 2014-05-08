class Punto:
   def __init__(self, a, b):
      self.x = a
      self.y = b
        
def Punto_getX(self):
      return self.x
def Punto_getY(self):
      return self.y
    
def Punto__gt__(self, other):
      if (isinstance(other, Punto)):
	 return(self.getX()>other.getX()
                   or self.getY() > other.getY())
      else:
	 return False
    
def Punto__lt__(self,other):
      if (isinstance(other,Punto)):
           return(self.getX() < other.getX()
                   or self.getY() < other.getY())
      else:
           return False
    
    
def Punto__eq__(self, other):
      if (isinstance(other, Punto)):
           return(self.getX()== other.getX()
                   and self.getY() == other.getY() )
    
def Punto__str__(self):
      return str.format("({0},{1})",
                         self.getX(),
                         self.getY() )

'''Asignacion dinamica de miembros a clases existentes'''
Punto.getX = Punto_getX
Punto.getY = Punto_getY
Punto.__str__ = Punto__str__
Punto.__gt__ = Punto__gt__ 
Punto.__lt__ = Punto__lt__
Punto.__eq__ = Punto__eq__   

#leer miembros con dir(objeto)
#anhadir un miembro con objeto.miembro = miembro a anhadir
#eliminar un miembro con del obj.miembro
'''callable(obj.miembro) devuelve si tiene o no ese miembro el objeto,
devuelve True si es metodo,False en caso contrario'''
#getattr(obj,miembro) devulve el valor

'''Ejercicio, dado un objeto pasado a una funcion devuelve todos sus miembros.
Si es attr imprime su valor, si es un metodo imprime nombreMetodo()'''
p1 = Punto(1,2)
def muestraMiembros(obj):
      toret = []
      miembros = dir(obj)
      for i in miembros:
	member = getattr(obj,i)
	if callable(member):
	   toret.append(str(i)+'()')
	else:
	   toret.append(i+'='+str(member))
      print(toret)

muestraMiembros(p1)	




#eval es muy lento y muy inseguro si no se comprueba entrada
def doble(x):
   return x*2

'''Otra forma'''
exec("def f(x): return x*2")
print f(3)

'''veamos el metodo __getattr__, se llama cuando no se encuentra 
el miembro buscado'''
class A:
   def __getattr__(self,x):
      if x == "test":	
	 return 1
      else:
	 return 0

a = A()
a.x
a.test
a.__dict__
A.__dict__
A.z = 10
a.z

a.hola
a.test

'''Ejercicio a hacer,
Un pequenho interprete que permita crear y eliminar objetos
Anhadir y modificar atributos
Anhadir y modificar metodos
Se puede, noooo, se debe hacer aceptando codigo python'''
