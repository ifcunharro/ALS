import json
from google.appengine.ext import ndb



class Mensajes(ndb.Model):
	 tipo = ndb.StringProperty(required=True)
	 mensaje = ndb.StringProperty(required=True)
	 check = ndb.StringProperty(required=True)
	 
def loadMsg():
	s = Mensajes()
	s = json.dumps([s.to_dict() for s in Mensajes.query().fetch()])
	s = eval(s)
	
	return s
	


def resetMsg():
	send = Mensajes.query().filter(Mensajes._properties['tipo']=="validar")
	if send.get():
		ob = send.get()
		ob.key.delete()
	
	