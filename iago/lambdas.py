#lambdas (+prog. funcional)
#se invocan con el nombre pasando el param indicado como una funcion
doble = lambda x: x*2

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
Point.getX = lambda self: self.x
Point.getY = lambda self: self.y
Point.__str__ = lambda self: str.format("{(0), (1)}", self.getX(),
                                        self.getY())

#car([1,2] devuelve 1
#con map, filter y reduce se podría hacer cualquier algoritmo
car = lambda l: None if l == None or l == [] else l[0]
cdr = lambda l: None if l == None or l == [] else l[1:]
lcopy = lambda l: None if l == None else [] if l == [] else [car(l)] + lcopy(cdr(l))
lcopydoble = lambda l: None if l == None else [] if l == [] else [car(l)*2] + lcopydoble(cdr(l))

#mapeamos funcion doble a lista, se invoca map(doble,lista)
#map ya existe, aqui lo redefinimos
map = lambda f,l: None if l == None else [] if l == [] else [f(car(l))] + map(f,(cdr(l)))

#filter predefinido
filter(lambda x: True if x%2 == 0 else False, [1,2,3,4,5,6])

#filter propio
filter = lambda f,l: None if l == None else [] if l == [] else [car(l)] + filter(f,cdr(l)) if f(car(l)) else filter(f,cdr(l))

#reduce(lambda x,y: x+y,[1,2,3,4]
reduce = lambda f,l: None if l == None else None if l == [] else car(l) if len(l) == 1 else f(car(l),reduce(f,cdr(l)))

#lcopy con map
lcopy = lambda l: map(lambda x: x,l)

#doble con map se llama con doble a secas, ya recibio los params
doble = map(lambda x: x*2,[1,2,3])

fibonacci = lambda x: [0] if x <= 0 else [0,1] if x == 1 else fibonacci(x-1)+[fibonacci(x-1)[-1]+fibonacci(x-1)[-2]] 

#ejercicios
'''Crear funciones usando car y cdr
ultimo(l)
penultimo(l)
fibonacci
fibonacci con map filter y reduce.'''

ultimo = lambda l: None if l == None else None if l == [] else car(l) if car(cdr(l)) == None else ultimo(cdr(l)) 

penultimo = lambda l: None if l == None else None if l == [] else None if len(l) == 1 else car(l) if len(cdr(l)) == 1 else penultimo(cdr(l))





