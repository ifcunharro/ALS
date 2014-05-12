#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import ndb
import webapp2
import jinja2
import os
import json
import lib



template_dir =  os.path.join(os.path.dirname(__file__),"templates")
JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader( template_dir ),
	extensions=[ "jinja2.ext.autoescape","jinja2.ext.loopcontrols" ],
	autoescape=True )


	
class Salvar(ndb.Model):
	 name = ndb.StringProperty(required=True)
	 objetos = ndb.JsonProperty( required = True)
	
class IndexHandler(webapp2.RequestHandler):
	def __init__( self , request=None, response=None):
		self.initialize( request, response )
		self.answer = "No existen objetos"
		
		
				
	def get(self):
		lib.initial()
		lib.addAtributo('Punto','x')
		lib.modAtributo('Punto','x','60')
		self.ob = lib.getObjetos()
		for i in range(0,len(self.ob)):
			objeto = Salvar( name=self.ob.keys()[i],objetos =self.ob.values()[i] );
			objeto.put();
			
		s = Salvar()
		s = json.dumps([s.to_dict() for s in Salvar.query().fetch()])
		
		s = eval(s)
		template_values = {
			'objetos': s,
		}
		index = JINJA_ENVIRONMENT.get_template("index.html")
		self.response.write(index.render(template_values))
		

		
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
		lib.initial()
		lib.addAtributo(self.object,self.attr,self.valattr)
		objeto =Salvar( name=self.object,objetos =lib.getObjeto(self.object))
		objeto.put()
		
		
		
	
			
				
	
	
	

app = webapp2.WSGIApplication([
    ('/', IndexHandler),('/addAttr',AddAttrHandler)
], debug=True)
