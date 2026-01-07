animales = ["gato","perro","loro","cocodrilo"]
numeros = (10,62,70,12)

#recorriendo la lista animales
for animal in animales:
    print(f"ahora la variable animal es igual a {animal}")

#recorriendo la lista numeros y multiplicando cada valor por dos 
for numero in numeros:
    resultado = numero*2
    print(f"el resultado es: {resultado}")
    
#iterando dos listas del mismo tamaño al mismo tiempo    
for numero,animal in zip(animales,numeros):
    print(f"Recorriendo lista 1: {animal}")
    print(f"Recorriendo lista 2: {numero}")
    
#forma no optima de recorrer una lista con su indice (no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor es: {valor}")
    
#usando el for/else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero} ")
else:
    print("El bucle terminó")
    
#Todo lo anterior funciona exactamente igual para tuplas y conjuntos