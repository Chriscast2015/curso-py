#creando una funcion  simple 
#def saludar():
 #   print("Hola, Lucas mi maestro como estas?")

#ejecutando la funcion simple    
#saludar()

#crear una funcion con parametros
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "titan"
    else:
        adjetivo = "amor"
    
    print(f"Hola, {nombre}, mi {adjetivo} como estas?")
    
saludar("Camila","MujEr") 
saludar("Dalto","HOMbre")
saludar("Xavi","aaaaaa4")

#crear una funcion que nos retorne valores

def crear_contrasena_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    
    c1 = num -2
    c2 = num
    c3 = num -5
    contrasena = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contrasena
    
password = crear_contrasena_random(3)
frase = f"Tu contraseña nueva es: {password}"
print(frase)