numeros = {10, 3, 6, 2, 8, 4, 5}

#encontrando el número mayor de una lista 
numero_mas_alto = max(numeros)
#print(numero_mas_alto)

#encontrando el número menor de una lista 
numero_mas_bajo = min(numeros)
#print(numero_mas_bajo)

#redondeando a seis decimales
numero = round(3.14159265359,2)
#print(numero)

#retorno False  -> 0, vacio, False, ninguno/ True -> distinto a 0, True, cadena, datos no vacios 
resultado_bool = bool([2222,55555])
#print(resultado_bool)

#retorna True si todos los valores son verdaderos
resultado_all = all([458,"true",[546,789]])

#suma todos los valores de un iterable 
suma_total = sum(numeros) 

print(suma_total)