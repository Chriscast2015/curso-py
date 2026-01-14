#creando las listas
frutas = ["banana", "manzana","ciruela", "pera", "naranja", "granada", "durazno"]
cadena = "Hola dalto"
numeros = [1,2,3,4,5,6,7,8,9,10]
#Evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == "manzana":
        continue
    print(f"Me voy a comer una {fruta}")
    
#Evitar que el bucle siga ejecutándose (el else no se ejecuta tampoco)
for fruta in frutas:
    print(f"Me voy a comer una {fruta}")
    if fruta == "pera":
        break    
else:
    print("termiando")
    
#recorrer una cadena de texto 

for letra in cadena:
    print(letra)
    
#for en una sola linea de código 
numeros_duplicados = [x*2 for x in numeros ]
print(numeros_duplicados)