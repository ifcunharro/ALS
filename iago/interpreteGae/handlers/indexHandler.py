#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp2
from entities.salvar import loadDataNdb
from entities.mensajes import loadMsg,resetMsg
import jinja2
import os
import time

template_dir =  os.path.join(os.path.dirname(__file__),"../templates")
JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader( template_dir ),
	extensions=[ "jinja2.ext.autoescape","jinja2.ext.loopcontrols" ],
	autoescape=True )

class IndexHandler(webapp2.RequestHandler):
	def __init__( self , request=None, response=None):
		self.initialize( request, response )
			
	def get(self):
		s = loadDataNdb()
		m = loadMsg()
		if len(s)>0:
			if len(m)>0:
				a = m[0]['check']
				b = m[0]['mensaje']
				template_values = {
					'objetos': s,
					'validar': a,
					'mensaje':b,
				}
				
				index = JINJA_ENVIRONMENT.get_template("index.html")
				self.response.write(index.render(template_values))
				resetMsg()
			else:
				template_values = {
					'objetos': s,
					'validar': '',
					'mensaje':'',
				}
				index = JINJA_ENVIRONMENT.get_template("index.html")
				self.response.write(index.render(template_values))
			
		else:
			template_values = {
				'objetos': "No hay ejemplos para mostrar",
			}
			index = JINJA_ENVIRONMENT.get_template("noejemplos.html")
			self.response.write(index.render(template_values))
			
		