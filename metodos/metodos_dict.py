diccionario = {
    "nombre" : "lucas",
    "apellido" : "dalto",
    "subs" : 1000000
}
#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get() (si no encuentra nada el programa continua)
valor_de_aaaaa = diccionario.get("aaaaa")

print("Hola papa, el programa continua")

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elelmento del diccionario
diccionario.pop("subs")

#obteniendo un elemento dict_item iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)
