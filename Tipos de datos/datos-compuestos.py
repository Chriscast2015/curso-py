#creando una lista (se pueden modificar)
lista = ["Christian Castro", "Soy Christian", True, 1.70]

#creando una tupla (no se pueden modificar)
tupla = ("Christian Castro", "Soy Christian", True, 1.70)

#Esto es valido 
lista[3] = "Lucas"

#esto no es valido  
#tupla[3] = "Lucas"

#Creando un conjunto set (no se puede acceder a los elementos por su índice, no almacena datos duplicados)
conjunto = {"Christian Castro", "Soy Christian", True, 1.70, "Soy Christian"}

#print(conjunto[3]) -> no se puede acceder al elemento

#creando un diccionario (dict) (La estructura es key : value y separamos con comas)
diccionario = {
    "nombre" : "Christian Castro",
    "canal" : "Chriscast",
    "esta_emocionado" : True,
    "altura" : 1.7,
    "dato_duplicado" : "Chriscast" 
}

print(diccionario["altura"]) 
print(lista[3])