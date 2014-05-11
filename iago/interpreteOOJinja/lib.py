import pickle
'''Usar bajo tu responsabilidad, crea objetos dinamicos y los hace persistentes
pero hace uso de exec y puedes lanzar comandos de sistema si usas eso 
como nombres de tus objetos, methodos o atributos'''
#Class acceso a datos
guardar =''
objetos = ''
cuerpo = ''
def initial( ):
	global guardar 
	global cuerpo
	guardar = {"objetos": {}}
	global objetos 
	try:
		f = open("objetos.bin","rb")
		
		objetos = pickle.load(f)['objetos']
		f.close()
		loadContext()
	except:
		print('mal')
		objetos =dict()
	cuerpo = {'Methods':{},'Attrs':{}}
	
'''metodo loadContext, crea objetos que fuesen guardados en objeto.bin
para ello no puede usar los metodos normales de creacion sino los 
metodos *Context para no sobreescribir la informacion de objetos ya
existentes'''
def loadContext():
	global objetos
	for i in objetos.keys():
		insertarContext(i)
		for k,v in objetos[i]['Attrs'].items():
			modAttrContext(i,k,v)
		for s,p in objetos[i]['Methods'].items():
			addMethodContext(i,s)
			modMethodContext(i,s,p)

'''Crea objeto a partir nombre objeto'''	
def insertarContext(objeto):
	exec('class '+eval('objeto')+': pass')
	globals()[objeto] = eval(objeto)
	print("Correct inserted ")	

'''Crea un metodo de un objeto vacio'''	
def addMethodContext(objeto,method):
	print("Metodo "+objeto+"_"+method+" creado")
	aux=objeto+'.'+method+'=None'
	exec(aux)
	
'''implementa el metodo de un objeto'''
def modMethodContext(objeto,method,val):
	exec(val)
	st = eval(objeto).__name__+'_'
	name_method = method.split(st)[1]
	aux = objeto+'.'+method+'='+name_method
	exec(aux)
	
	
'''Crea un atributo de un objeto con su valor guardado'''
def modAttrContext(obj,atr,val):
	print("atributo "+atr+" modificado")
	exec(obj+'.'+atr+'='+val)		
	
'''Fin carga de contexto'''

'''Metodos de interprete para crear objetos no existentes
en objetos.bin'''

'''Crea objeto'''
def insertar( objeto):
	global objetos
	global cuerpo
	exec('class '+eval('objeto')+': pass')
	globals()[objeto] = eval(objeto)
	print("Correct inserted ")	
	objetos[objeto] = cuerpo
	
'''Borra objeto, solo para no guardarlo, en memoria sigue existiendo'''	
def borrar( objeto ):
	global objetos
	objetos[objeto]
	print("Correct deleted")
	
'''Comprueba si ya existe un objeto, fallo inesperado hace saltar
except'''
def buscar( obj):
	global objetos
	try:
		return obj in objetos.keys()
	except:
		print("Error al buscar")

'''Crea atributo en objeto'''
def addAttr( obj, atr):
	global objetos
	objetos[obj]['Attrs'][atr] = None
	print("atributo "+atr+ " creado")
	aux = obj+'.'+atr+"=None"
	exec(aux)
	
'''Asigna un atributo a un objeto'''
def modAttr(  obj, atr, val):
	global objetos
	objetos[obj]['Attrs'][atr]=val
	print("atributo "+atr+" modificado")
	exec(obj+'.'+atr+'='+val)
	
'''crea method pero pensado para ser vacio, una interfaz,
param method seria el nombre del method'''
def addMethod(  objeto, method):
	global objetos
	objetos[objeto]['Methods'][objeto+'_'+method] = None
	print("Metodo "+objeto+"_"+method+" creado")
	aux=objeto+'.'+objeto+'_'+method+'=None'
	exec(aux)

'''Implementa un metodo de un objeto'''	
def modMethod(  objeto, method,val):
	global objetos
	if val.startswith('def '):
		objetos[objeto]['Methods'][objeto+'_'+method] = val
		exec(val)
		aux = objeto+'.'+objeto+'_'+method+'= eval(method)'
		exec(aux)
	else:
		print("Payload o inesperado detectado y eliminado")

'''lista todos los objetos, sus metodos y atributos'''	
def listar(  ):
	global objetos
	for i,v in objetos.items():
		print(i)
		print(v)
			
	
'''comprueba si un objeto tiene un atributo'''	
def hasAtr(  obj, atr):
	global objetos
	return atr in objetos[obj]['Attrs']

'''comprueba si un objeto tiene un methodo'''
def hasMethod(  obj, method):
	global objetos
	return obj+'_'+method in objetos[obj]['Methods']

'''Fin clase interprete y metodos creacion normales'''

#class menu interfaz		



def addObj( obj ):
	if not buscar(obj):
		insertar(obj)
	else:
		print("Objeto "+obj+ " ya existe")

def delObj( obj ):
	if buscar(obj):
		borrar(obj)
	else:
		print("Objeto "+obj+" no existe")

def addAtributo(  name ):
	if buscar(obj):
		if (not hasAtr(obj,name)):
			addAttr(obj,name)
		else:
			print("El atributo "+name+
				" ya existia para el objeto "+obj)				
	else:
		print("Objeto "+obj+" no existe")
		
def addMetodo(  name ):
	if buscar(obj):
		if (not hasMethod(obj,name)):
			addMethod(obj,name)
		else:
			print("El "+miembro+" "+name+
					  " ya existia para el objeto "+obj)				
	else:
		print("Objeto "+obj+" no existe")

		
def modAtributo( atr,val ):
	if buscar(obj):
		if hasAtr(obj,atr):
			modAttr(obj,atr,val)
		else:
			print("Atributo "+atr+" no existe "+
			"en objeto "+obj) 
	else:
		print("Objeto "+obj+" no existe")
	
def modMethodo( meth,val):
	if buscar(obj):
		if hasMethod(obj,meth):
			modMethod(obj,meth,val)
		else:
			print("Metodo "+meth+" no existe "+
			"en objeto "+obj) 
	else:
		print("Objeto "+obj+" no existe")	
	
def guardarya():
	global guardar
	global objetos
	f = open("objetos.bin","wb")
	guardar['objetos'] = objetos
	print(guardar)
	pickle.dump(guardar,f)
	f.close()	
	
def getObjeto(x):
	global objetos
	return objetos[x]

def getAtributos(objeto):
	global objetos
	return objetos[objeto]['Attrs']


def getMetodos(objeto):
	global objetos
	return objetos[objeto]['Methods']

def getObjetos():
	global objetos
	return objetos
