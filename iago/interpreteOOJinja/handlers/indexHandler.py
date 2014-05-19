#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp2
from entities.salvar import loadDataNdb
import jinja2
import os
import logging

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
		if len(s)>0:
			template_values = {
				'objetos': s,
				'ola': 'mete'
			}
			index = JINJA_ENVIRONMENT.get_template("index.html")
			self.response.write(index.render(template_values))
		else:
			template_values = {
				'objetos': "No hay ejemplos para mostrar",
			}
			index = JINJA_ENVIRONMENT.get_template("noejemplos.html")
			self.response.write(index.render(template_values))
			
		