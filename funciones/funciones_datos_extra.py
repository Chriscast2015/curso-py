#creando una funcion de tres parametros 
#def frase(nombre, apellido, adjetivo):
#    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

#utilizando keywords arguments 
#frase_resultante = frase(nombre="Christian", adjetivo="Travieso", apellido="Castro")


#creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre, apellido, adjetivo="Tonto"):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

frase_resultante = frase("Christian", "Castro","Inteligente")


print (frase_resultante) 