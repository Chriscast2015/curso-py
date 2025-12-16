cadena1 = "Hola,soy,Xavi"
cadane2 = "Bienvenido"

#convierte a mayuscula
mayusc = cadena1.upper()

#convierte a minusculas
minusc = cadena1.lower()

#Primera letra en mayuscula
primer_letra_mayusc = cadena1.capitalize()

#Buscamos una cadena en otra cadena y en que posición está, si no hay coincidencia devuelve -1
busqueda_find = cadena1.find("a")

#Buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepción 
busqueda_index = cadena1.index("X")

#Si es numerico, devuelve true, sino devuelve false
es_numerico = cadena1.isnumeric()

#Si es alfanumerico devolvemos tru, sino devolvemos false
es_alfanumerico = cadena1.isalpha()

#Contamos las coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("a")

#Contamos cuantos caracteres tiene una cadena. Este es función, no metodo 
contar_caracteres = len(cadena1)

#Verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True 
empieza_con = cadena1.startswith("Hola")

#Verificamos si una cadena termina con otra cadena dada, si es asi devuelve True 
termina_con = cadena1.endswith("vi")

#Remplaza un pedazo de la cadena dada, por otra dada
cadena_nueva = cadena1.replace(",", " ")

#Separar cadenas con la cadena que le pasemos 
cadena_separada = cadena1.split(",")

print(cadena_separada[0])
 