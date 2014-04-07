import unittest
import lib

class TestLib(unittest.TestCase):
	def setUp(self):
		self.gradosFahInt = 32
		self.gradosFahFloat = 32.0
		self.gradosCelInt = 0
		self.gradosCelFloat = 0.0
		self.entero = "0"
		self.real = "0.0"
        
	def tearDown(self):
		self.gradosFahInt = None
		self.gradosFahFloat = None
		self.gradosCelInt = None
		self.gradosCelFloat = None
		self.entero = None
		self.real = None

	def testCalculaCelsius(self):
		self.assertEqual(0.0,lib.calculaCelsius(self.gradosFahInt))
		self.assertEqual(0.0,lib.calculaCelsius(self.gradosFahFloat))

	def testCalculaFahrenheit(self):
		self.assertEqual(32.0,lib.calculaFahrenheit(self.gradosCelInt))
		self.assertEqual(32.0,lib.calculaFahrenheit(self.gradosCelFloat))               

	def testIsNumber(self):
		self.assertTrue(True,lib.isNumber(self.entero))
		self.assertTrue(True,lib.isNumber(self.real))
		
if "__name__"=="__main__":
	unittest.main()
