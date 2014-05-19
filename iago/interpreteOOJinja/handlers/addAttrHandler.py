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
		lib.initial(s,'normal')
		lib.addAtributo(self.object,self.attr,'normal')
		lib.modAtributo(self.object,self.attr,self.valattr,'normal')
		objeto = Salvar.query().filter(Salvar._properties['clase']==self.object)
	
		ob = objeto.get()
		ob.clase = self.object
		ob.miembros = lib.getObjeto(self.object)
		ob.put()
		
		time.sleep(0.4)
		self.redirect("/")
		