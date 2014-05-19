import json
from google.appengine.ext import ndb


class Salvar(ndb.Model):
	 clase = ndb.StringProperty(required=True)
	 miembros = ndb.JsonProperty( required = True)

'''carga informacion de ndb, usada para trabajar a nivel local
mostrarla en plantillas o actualizarla'''	 
def loadDataNdb():
	s = Salvar()
	s = json.dumps([s.to_dict() for s in Salvar.query().order(-Salvar.clase).fetch()])
	s = eval(s)
	
	return s
