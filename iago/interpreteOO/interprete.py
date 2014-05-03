import pickle
'''Usar bajo tu responsabilidad, crea objetos dinámicos y los hace persistentes
pero hace uso de exec y puedes lanzar comandos de sistema si usas eso 
como nombres de tus objetos, methodos o atributos'''
#Class acceso a datos
class Interprete:
	def __init__( self ):
		self.guardar = {"objetos": {}}
		try:
			f = open("objetos.bin","rb")
			self.objetos = pickle.load(f).objetos
			f.close()
			self.loadContext()
			print(Punto.__dict__)
		except:
			self.objetos = dict()
		self.cuerpo = {'Methods':{},'Attrs':{}}
		
	'''metodo loadContext, crea objetos que fuesen guardados en objeto.bin
	para ello no puede usar los metodos normales de creacion sino los 
	metodos *Context para no sobreescribir la informacion de objetos ya
	existentes'''
	def loadContext(self):
		for i in self.objetos.keys():
			self.insertarContext(i)
			for k,v in self.objetos[i]['Attrs'].items():
				self.modAttrContext(i,k,v)
			for s,z in self.objetos[i]['Methods'].items():
				self.addMethodContext(i,s)
				self.modMethodContext(i,s,z)
	
	'''Crea objeto a partir nombre objeto'''	
	def insertarContext(self,objeto):
		exec('class '+eval('objeto')+': pass')
		globals()[objeto] = eval(objeto)
		print("Correct inserted ")	
	
	'''Crea un metodo de un objeto vacio'''	
	def addMethodContext(self,objeto,method):
		print("Metodo "+objeto+"_"+method+" creado")
		aux=objeto+'.'+method+'=None'
		exec(aux)
		
	'''implementa el metodo de un objeto'''
	def modMethodContext(self,objeto,method,val):
		exec(val)
		aux = objeto+'.'+method+'= eval(method)'
		exec(aux)	
		
	'''Crea un atributo de un objeto con su valor guardado'''
	def modAttrContext(self,obj,atr,val):
		print("atributo "+atr+" modificado")
		exec(obj+'.'+atr+'='+val)		
		
	'''Fin carga de contexto'''
	
	'''Metodos de interprete para crear objetos no existentes
	en objetos.bin'''
	
	'''Crea objeto'''
	def insertar( self, objeto):
		exec('class '+eval('objeto')+': pass')
		globals()[objeto] = eval(objeto)
		print("Correct inserted ")	
		self.objetos[objeto] = self.cuerpo
		
	'''Borra objeto, solo para no guardarlo, en memoria sigue existiendo'''	
	def borrar( self, objeto ):
		del self.objetos[objeto]
		print("Correct deleted")
		
	'''Comprueba si ya existe un objeto, fallo inesperado hace saltar
	except'''
	def buscar( self, obj):
		try:
			return obj in self.objetos.keys()
		except:
			print("Error al buscar")
	
	'''Crea atributo en objeto'''
	def addAttr( self, obj, atr):
		self.objetos[obj]['Attrs'][atr] = None
		print("atributo "+atr+ " creado")
		aux = obj+'.'+atr+"=None"
		exec(aux)
		
	'''Asigna un atributo a un objeto'''
	def modAttr( self, obj, atr, val):
		self.objetos[obj]['Attrs'][atr]=val
		print("atributo "+atr+" modificado")
		exec(obj+'.'+atr+'='+val)
		
	'''crea method pero pensado para ser vacio, una interfaz,
	param method seria el nombre del method'''
	def addMethod( self, objeto, method):
		self.objetos[objeto]['Methods'][objeto+'_'+method] = None
		print("Metodo "+objeto+"_"+method+" creado")
		aux=objeto+'.'+objeto+'_'+method+'=None'
		exec(aux)
	
	'''Implementa un metodo de un objeto'''	
	def modMethod( self, objeto, method,val):
		self.objetos[objeto]['Methods'][objeto+'_'+method] = val
		exec(val)
		aux = objeto+'.'+objeto+'_'+method+'= eval(method)'
		exec(aux)	
	
	'''lista todos los objetos, sus metodos y atributos'''	
	def listar( self ):
		for i,v in self.objetos.items():
			print(i)
			print(v)
		
	'''comprueba si un objeto tiene un atributo'''	
	def hasAtr( self, obj, atr):
		return atr in self.objetos[obj]['Attrs']
	
	'''comprueba si un objeto tiene un methodo'''
	def hasMethod( self, obj, method):
		return obj+'_'+method in self.objetos[obj]['Methods']
	
	'''Fin clase interprete y metodos creacion normales'''

#class menu interfaz		
class Menu:
	def __init__( self ):
		self.interprete = Interprete()
		self.op = ''
		self.showMenu()

	#Menu principal
	def showMenu( self ):
		print("Menu options")
		print("1.Crear Objeto")
		print("2.Borrar Objeto")
		print("3.Crear Atributo")
		print("4.Modificar Atributo")
		print("5.Crear Metodo")
		print("6.Modificar Metodo")
		print("7. Listar")
		print("8.Exit")
		self.pedirOpcion()

	
	def pedirOpcion( self ):
		try:
			self.op = int(raw_input("Input option 1 a 6. 7 " +
				                "to finish program\n"))
			self.ejecutarOp()
		except:
			print("Input 1 a 6 o 7 para finalizar")
			self.showMenu()

	def ejecutarOp( self ):
		if self.op == 1:
			self.addObj()
		elif self.op == 2:
			self.delObj()
		elif self.op == 3:
			self.addMiembro('atributo')
		elif self.op == 4:
			self.modAttr()
		elif self.op == 5:
			self.addMiembro('metodo')
		elif self.op == 6:
			self.modMethod()
		elif self.op == 7:
			self.interprete.listar()
			self.showMenu()			
		elif self.op == 8:
			self.guardar()
			print("End program")
			 
			
		else:
			print("You input "+str(self.op)+': wrong option')
			print("Input 1 a 6 o 7 para terminar")
			self.showMenu() 
	
	def addObj( self ):
		obj = raw_input("Introduce nombre objeto a insertar: ")
		if not self.interprete.buscar(obj):
			self.interprete.insertar(obj)
		else:
			print("Objeto "+obj+ " ya existe")
		self.showMenu()

	def delObj( self ):
		obj = raw_input("Introduce nombre objeto a borrar: ")
		if self.interprete.buscar(obj):
			self.interprete.borrar(objeto)
		else:
			print("Objeto "+obj+" no existe")
		self.showMenu()
	
	def addMiembro( self, miembro ):
		obj = raw_input("Introduce nombre objeto para anhadir "+
		                miembro+": ")
		if self.interprete.buscar(obj):
			name = raw_input("Introduce nombre "+miembro+": ")
			if miembro == 'atributo':
				if (not self.interprete.hasAtr(obj,name)):
					self.interprete.addAttr(obj,name)
				else:
					print("El "+miembro+" "+name+
					" ya existia para el objeto "+obj)
			elif miembro == 'metodo':
				if (not self.interprete.hasMethod(obj,name)):
					self.interprete.addMethod(obj,name)
				else:
					print("El "+miembro+" "+name+
					      " ya existia para el objeto "+obj)				
		else:
			print("Objeto "+obj+" no existe")
		self.showMenu()
		
	def modAttr( self ):
		obj = raw_input("Introduce nombre objeto para modificar"+ 
		                 " atributo: ")
		if self.interprete.buscar(obj):
			atr = raw_input("Introduce nombre atributo a "+
			                "modificar: ")
			if self.interprete.hasAtr(obj,atr):
				val = raw_input("Introduce valor atributo: ")
				self.interprete.modAttr(obj,atr,val)
			else:
				print("Atributo "+atr+" no existe "+
				"en objeto "+obj) 
		else:
			print("Objeto "+obj+" no existe")
		self.showMenu()
	
	def modMethod( self ):
		obj = raw_input("Introduce nombre objeto para modificar"+ 
				                 " metodo: ")
		if self.interprete.buscar(obj):
			meth = raw_input("Introduce nombre metodo a "+
							"modificar: ")
			if self.interprete.hasMethod(obj,meth):
				val = raw_input("Introduce implementacion "+
				"metodo: ")
				print(val);print(meth);print(obj)
				self.interprete.modMethod(obj,meth,val)
			else:
				print("Metodo "+meth+" no existe "+
				"en objeto "+obj) 
		else:
			print("Objeto "+obj+" no existe")
		self.showMenu()		
	
	def guardar(self):
		f = open("objetos.bin","wb")
		self.interprete.guardar["objetos"] = self.interprete.objetos
		pickle.dump(self.interprete,f)
		f.close()		
		
	
	
	
		
		
		
def main():
	a = Menu()
	
	
	
	
	
if __name__=="__main__":main()