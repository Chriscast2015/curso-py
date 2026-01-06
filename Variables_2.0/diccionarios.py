#creando diccionarios con dict()
diccionario = dict(nombre = "Lucas", apellido = "Dalto")

#las listas no pueden ser claves y usamos frozeset para meter conjuntos
diccionario = {frozenset(["Dalto","rancio"]):"jajaja"} 

#creando diccionarios con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre", "apellido","suscriptores"])

#creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre", "apellido"], "No se")


print(diccionario)