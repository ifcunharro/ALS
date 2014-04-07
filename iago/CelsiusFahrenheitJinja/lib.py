def calculaCelsius( fah ):
	return (float(fah) - 32.0) * 5.0 / 9.0

def calculaFahrenheit( cel ):
	return float(cel) * 9.0 / 5.0 + 32.0 

def isNumber(grados):
	return isinstance(eval(grados),float) or isinstance(eval(grados),int)


	
	
