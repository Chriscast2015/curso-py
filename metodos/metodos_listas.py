#Creando una lista con list()
lista = list([52, 48, 89, True, False])

#Devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#Agregando un elemento a la lista
lista.append(65)

#Agregando un elemento a la lista en un indice especifico
lista.insert(2, 34)

#agregando varios elementos a la lista
lista.extend([2030])

#eliminando un elemento de la lista (por su índice)
lista.pop(-2) #-1 para eliminar el ultimo, -2 para eliminar el ante penultimo y asi sucesivamente

#removinedo un elemento de la lisa por su valor 
lista.remove(34)

#eliminando todos los elemnentos de la lista 
#lista.clear()

#ordenando la lista de forma ascendente (si usamos el parametro reverse=Tue lo ordena en reversa )
lista.sort()

#invirtiendo los elementos de uan lista
lista.reverse()
print(lista)


