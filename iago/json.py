#soporte JSON python
import json

str_json_data = "{\"x\":5,\"y\":6}"
data = json.loads(str_json_data)
print(data)
print(data["x"])

# cambio en x
data["x"]=100
print(data)

#volver a JSON
print( json.dumps( data ) )