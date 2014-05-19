objetos = dict()
	
'''metodo loadContext, crea objetos que fuesen guardados en ndb,
modo indica si se va a probar el objeto o solo crear la estructura
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
	if modo == 'test':
		exec('class '+eval('objeto')+': pass')
		globals()[objeto] = eval(objeto)
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
	if modo == 'test':
		exec(aux)
	return "atributo "+atr+ " creado"
	
'''Asigna un atributo a un objeto'''
def modAttr(  obj, atr, val,modo):
	global objetos
	objetos[obj]['Atributos'][atr]=val
	if modo == 'test':
		exec(obj+'.'+atr+'='+val)
	return "atributo "+atr+" modificado"
	
'''crea method pero pensado para ser vacio, una interfaz,
param method seria el nombre del method'''
def addMethod(  objeto, method,modo):
	global objetos
	if not '_' in method:
		objetos[objeto]['Metodos'][objeto+'_'+method] = None
		aux=objeto+'.'+objeto+'_'+method+'=None'
		if modo == 'test':
			exec(aux)
	else:
		objetos[objeto]['Metodos'][method] = None
		aux=objeto+'.'+method+'=None'
		if modo == 'test':
			exec(aux)
	return "Metodo "+objeto+"_"+method+" creado"

'''Implementa un metodo de un objeto'''	
def modMethod(  objeto, method,val,modo):
	global objetos
	if val.startswith('def '):
		if not '_' in method:
			objetos[objeto]['Metodos'][objeto+'_'+method] = val
			if modo == 'test':
				exec(val)
			aux = objeto+'.'+objeto+'_'+method+'= eval(method)'
			if modo == 'test':
				exec(aux)
		else:
			objetos[objeto]['Metodos'][method] = val
			if modo == 'test':
				exec(val)
			me = method.split('_')
			m = me[1]
			aux = objeto+'.'+method+'= eval(m)'
			if modo == 'test':
				exec(aux)
	else:
		return "Valor inesperado detectado y eliminado"
	
'''comprueba si un objeto tiene un atributo'''	
def hasAtr(  obj, atr):
	global objetos
	return atr in objetos[obj]['Atributos']

'''comprueba si un objeto tiene un methodo'''
def hasMethod(  obj, method):
	global objetos
	return obj+'_'+method in objetos[obj]['Metodos']



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
	if not buscar(obj):
		insertar(obj,modo)
		
	else:
		return "Objeto "+obj+ " ya existe"

def addAtributo(  obj,name,modo ):
	if buscar(obj):
		if (not hasAtr(obj,name)):
			addAttr(obj,name,modo)
		else:
			return "El atributo "+name+\
				" ya existia para el objeto "+obj				
	else:
		return "Objeto "+obj+" no existe"
		
def addMethodo(  obj,name,modo ):
	if buscar(obj):
		addMethod(obj,name,modo)		
	else:
		return "Objeto "+obj+" no existe"

		
def modAtributo( obj,atr,val,modo ):
	if buscar(obj):
		if hasAtr(obj,atr):
			modAttr(obj,atr,val,modo)
		else:
			return "Atributo "+atr+" no existe "+\
			"en objeto "+obj
	else:
		return "Objeto "+obj+" no existe"
	
def modMethodo( obj,meth,val,modo):
	if buscar(obj):
		modMethod(obj,meth,val,modo)
	else:
		return "Objeto "+obj+" no existe"
	
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