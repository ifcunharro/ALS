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
import lib

class gradosHandler(webapp2.RequestHandler):
	def __init__( self , request=None, response=None):
		self.initialize( request, response )
		self.grados = ""
		self.answer = ""
		try:
			self.grados = self.request.get( "grados" )
			if lib.isNumber(self.grados):
				pass
			else:
				self.answer = "<html><body><b>ERROR</b>" \
				"acquiring data</body></html>"
		except:
			self.answer = "<html><body><b>ERROR</b>" \
				"acquiring data</body></html>"
	
	def post(self):
		if ( len(self.answer ) == 0):
			if( len(self.grados ) > 0 ):
				self.answer = str.format( "<html><body>" \
					"<b>Grados Celsius: {0}</b><br>" \
					"<b>Grados Fahrenheit: {1}</b><br>" \
					"</body></html>",\
				lib.calculaCelsius( self.grados ),
				lib.calculaFahrenheit(self.grados))
			else:
				self.answer = "<html><body><b>Hola, "\
					"Anonymous</b></body></html>"
		self.response.write(self.answer )

	

app = webapp2.WSGIApplication([
    ('/celsius', gradosHandler)
], debug=True)
