objetos = dict()
import logging	
'''metodo loadContext, crea objetos que fuesen guardados en ndb,
modo indica si se va a probar el objeto(test) o solo crear la estructura
para guardar en ndb'''

def loadContext(modo):
	global objetos
	for i in objetos.keys():
		insertar(i,modo)
		for k,v in objetos[i]['Atributos'].items():
			addAtributo(i,k,modo)
			modAtributo(i,k,v,modo)
		for s,p in objetos[i]['Metodos'].items():
			addMethodo(i,s,modo)
			modMethodo(i,s,p,modo)
			


'''Metodos de interprete para crear objetos'''

'''Crea objeto'''
def insertar( objeto,modo):
	global objetos
	try:
		objetos[objeto] 
	except:
		objetos[objeto] = {'Atributos':{},'Metodos':{}}
	return "Correct inserted "
	
'''Comprueba si ya existe un objeto, fallo inesperado hace saltar
except'''
def buscar( obj):
	global objetos
	try:
		return obj in objetos.keys()
	except:
		return "Error al buscar"

'''Crea atributo en objeto'''
def addAttr( obj, atr,modo):
	global objetos
	objetos[obj]['Atributos'][atr] = None
	aux = obj+'.'+atr+"=None"
	
'''Asigna un atributo a un objeto'''
def modAttr(  obj, atr, val,modo):
	global objetos
	objetos[obj]['Atributos'][atr]=val
	
'''crea method pero pensado para ser vacio, una interfaz,
param method seria el nombre del method'''
def addMethod(  objeto, method,modo):
	global objetos
	if not '_' in method:
		objetos[objeto]['Metodos'][objeto+'_'+method] = None
		aux=objeto+'.'+objeto+'_'+method+'=None'
	else:
		objetos[objeto]['Metodos'][method] = None
		aux=objeto+'.'+method+'=None'

'''Implementa un metodo de un objeto'''	
def modMethod(  objeto, method,val,modo):
	global objetos
	if val.startswith('def ') and '(self)' in val:
		if not '_' in method:
			objetos[objeto]['Metodos'][objeto+'_'+method] = val
			aux = objeto+'.'+objeto+'_'+method+'= eval(method)'
			return '',''
		else:
			objetos[objeto]['Metodos'][method] = val
			aux = objeto+'.'+method+'= eval(method)'
			return '',''
	else:
		return "Valor inesperado detectado y eliminado","alert"
		
'''Fin metodos que no deberían llamarse externamente a la libreria'''
		
'''metodos llamados externamente'''

#inicializa localmente objetos ndb
def initial( ob,modo):
	global objetos 
	global guardar
	guardar = {'objetos':{}}
	if len(ob)> 0:
		objetos = dict()
		for i in range(0,len(ob)):
			objetos[ob[i]['clase']]=ob[i]['miembros']
		loadContext(modo)
	else:
		objetos =dict()

def addObj( obj,modo ):
	if not obj.isalpha():
		return "No permitido usar numeros o caracteres especiales","alert"
	else:
		if not buscar(obj):
			toret = insertar(obj,modo)
			return toret,"success"
		else:
			return "Objeto "+obj+ " ya existe","warning"
	
	

def addAtributo(  obj,name,modo ):
	if not obj.isalpha() or not name.isalpha():
		return "No permitido usar numeros o caracteres especiales\
		en nombre de objeto o atributo","alert"
	else:
		if buscar(obj):
			addAttr(obj,name,modo)	
			return '',''
		else:
			return "Objeto "+obj+" no existe","warning"
			
def modAtributo( obj,atr,val,modo ):
	modAttr(obj,atr,val,modo)
	return "Atributo "+atr+ " actualizado correctamente","success"	
	
def addMethodo(  obj,name,modo ):
	if not obj.isalpha() or not name.isalpha():
		if '__' in name:
			return '',''
		else:
			return "No permitido usar numeros o caracteres especiales\
			en nombre de objeto o metodo","alert"
	else:
		if buscar(obj):
			addMethod(obj,name,modo)	
			return '',''
		else:
			return "Objeto "+obj+" no existe","warning"

		

def modMethodo( obj,meth,val,modo):
	toret,valid = modMethod(obj,meth,val,modo)
	if len(toret)>0:
		return toret,valid
	else:
		return "Metodo "+meth+ " creado correctamente","success"	
	
def getObjeto(ob):
	global objetos
	return objetos[ob]

def getAtributos(objeto):
	global objetos
	return objetos[objeto]['Atributos']


def getMetodos(objeto):
	global objetos
	return objetos[objeto]['Metodos']

def getObjetos():
	global objetos
	return objetos
'''Fin metodos llamados externamente'''