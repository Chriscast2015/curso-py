frase = input("Dime una frase y te calculo cuanto tardaras si tuvieras que decirla: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(f"dijiste {cantidad_de_palabras} palabras y tardarías {cantidad_de_palabras/2} segundos en decirlo ")
print(f"Dalto lo diria en {cantidad_de_palabras/2*1.3} segundos")
if cantidad_de_palabras > 120:
    print("Para flaco tampoco te pedí un testamento")