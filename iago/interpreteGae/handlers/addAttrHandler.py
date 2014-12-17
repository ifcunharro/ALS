#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp2
from entities.salvar import Salvar,loadDataNdb
from entities.mensajes import Mensajes
import jinja2
import os
import lib
import time

template_dir =  os.path.join(os.path.dirname(__file__),"../templates")
JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader( template_dir ),
	extensions=[ "jinja2.ext.autoescape","jinja2.ext.loopcontrols" ],
	autoescape=True )

class AddAttrHandler(webapp2.RequestHandler):
	def __init__( self , request=None, response=None):
		self.initialize( request, response )
		try:
			self.object = self.request.get("object")
			self.attr = self.request.get("attr")
			self.valattr = self.request.get("valattr")
			
		except:
			self.answer = "<html><body><b>ERROR</b>" \
				"acquiring data</body></html>"
	

	def post(self):
		s = loadDataNdb()
		modo = 'normal'
		lib.initial(s,modo)
		self.msg,self.valid=lib.addAtributo(self.object,self.attr,modo)
		if len(self.valid)==0:
			self.msg,self.valid=lib.modAtributo(self.object,self.attr,self.valattr,modo)
			if self.valid == "success":
				objeto = Salvar.query().filter(Salvar._properties['clase']==self.object)
				if not objeto.get():
					objeto = Salvar( clase=self.object,miembros =lib.getObjeto(self.object) );
					objeto.put();
				else:
					ob = objeto.get()
					ob.clase = self.object
					ob.miembros = lib.getObjeto(self.object)
					ob.put()
			
		send = Mensajes.query().filter(Mensajes._properties['tipo']=="validar")
		if not send.get():
			send = Mensajes( tipo="validar",mensaje=self.msg,check =self.valid );
			send.put();
		else:
			ob = send.get()
			ob.mensaje = self.msg
			ob.check = self.valid
			ob.put()
		
		time.sleep(0.6)
		self.redirect("/")
		
		