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
import webapp2
import jinja2
import os
import lib

template_dir =  os.path.join(os.path.dirname(__file__),"templates")
JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader( template_dir ),
	autoescape=True )
	
class gradosHandler(webapp2.RequestHandler):
	def __init__( self , request=None, response=None):
		self.initialize( request, response )
		self.grados = ""
		try:
			self.grados = self.request.get( "grados" )
			if lib.isNumber( self.grados ):
				pass
		except:
			data_error = JINJA_ENVIRONMENT.get_template("data_error.html")
			self.response.write(data_error.render())
	
	def post(self):
		try:
			if lib.isNumber( self.grados ):
				template_values = {
					'gradosCelsius' : lib.calculaCelsius( self.grados ),
					'gradosFahrenheit' : lib.calculaFahrenheit( self.grados ),
				}
				
				template = JINJA_ENVIRONMENT.get_template("answer.html")
				self.response.write(template.render(template_values))	
		except:
			number_error = JINJA_ENVIRONMENT.get_template("number_error.html")
			self.response.clear()
			self.response.write(number_error.render())

app = webapp2.WSGIApplication([
    ('/celsius', gradosHandler)
], debug=True)
