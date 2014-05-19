#!/usr/bin/python
# -*- coding: utf-8 -*-
import webapp2
from entities.salvar import Salvar,loadDataNdb
import jinja2
import os
import lib
import time

template_dir =  os.path.join(os.path.dirname(__file__),"../templates")
JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader( template_dir ),
	extensions=[ "jinja2.ext.autoescape","jinja2.ext.loopcontrols" ],
	autoescape=True )

class AddMethodHandler(webapp2.RequestHandler):
	def __init__( self , request=None, response=None):
		self.initialize( request, response )
		try:
			self.object = self.request.get("object")
			self.method = self.request.get("method")
			self.valmethod = self.request.get("valmethod")
			
		except:
			self.answer = "<html><body><b>ERROR</b>" \
				"acquiring data</body></html>"
	

	def post(self):
		s = loadDataNdb()
		lib.initial(s,'normal')
		lib.addMethodo(self.object,self.method,'normal')
		lib.modMethodo(self.object,self.method,self.valmethod,'normal')
		objeto = Salvar.query().filter(Salvar._properties['clase']==self.object)
		if not objeto.get():
			objeto = Salvar( clase=self.object,miembros =lib.getObjeto(self.object) );
			objeto.put();
		else:
			ob = objeto.get()
			ob.clase = self.object
			ob.miembros = lib.getObjeto(self.object)
			ob.put()
			
		time.sleep(0.4)	
		self.redirect("/")
		