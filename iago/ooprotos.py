# OO Prototipos

class Point2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def __str__(self):
        return str.format("{0}, {1}",self.x,self.y)
    
class Point3D:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    def __str__(self):
        return str.format("{0}, {1}, {2}",self.x,self.y,self.z)

class Empleado:
    
    def __init__(self,nombre,salario):
        self.nombre=nombre
        self.salario=salario
    
    def __str__(self):
        return str.format("{0}:{1}",self.nombre,self.salario)
    
    def setSalario(self, x):
        self.salario=x
    
class Auxiliar(Empleado):
    def __init__(self,nombre,salario):
        Empleado.__init__(self,nombre,salario)
    def __str__(self):
        return Empleado.__str__(self)+" (auxiliar)"
    
    def setSalario(self, x):
            Empleado.setSalario(self,x)
            if x>=100000:
                self.__class__=Directivo    
    
class Directivo(Empleado):
    def __init__(self,nombre,salario):
        Empleado.__init__(self,nombre,salario)
        
    def __str__(self):
        return Empleado.__str__(self)+" (directivo)"
    
    def setSalario(self, x):
        Empleado.setSalario(self,x)
        if x<100000:
            self.__class__=Auxiliar
    
   
p1=Point2D(5,6)
p2=Point3D(1,2,3)
print(str(p1))
print(str(p2))

print p1.__class__
print p2.__class__

#cambiamos su parent
p2.__class__=Point2D
print (str(p2))
#comprobamos q z sigue estando ahi pero no se usa, xq se llama al str de Point2D
print dir(p2)
print p2.z

#podemos cambiar p1 para q pase a apuntar a Point3D
p1.__class__=Point3D
print str(p1)

p1.z=7

print (str(p1))
print dir(p1)

#Cambiamos el salario del directivo a uno de un auxiliar y cambia su clase
d=Directivo("Juanito",200000)
print d.salario
print (str(d))
print d.__class__
d.setSalario(50000)
print (str(d))
print d.__class__