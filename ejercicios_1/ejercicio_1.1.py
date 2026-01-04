#promedio de duracion 
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5 

#duració de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#diferencias de duracion
diferencia_con_min = ((otros_cursos_min - dalto_curso)/otros_cursos_min)*100 
diferencia_con_max = ((otros_cursos_max - dalto_curso)/otros_cursos_max)*100
diferencia_con_promedio = ((otros_cursos_promedio - dalto_curso)/otros_cursos_promedio)*100

#Calculando el porcentaje de tiempo vacio removido  
tiempo_vacio_promedio = ((crudo_promedio - otros_cursos_promedio)/ crudo_promedio) *100 
tiempo_vacio_dalto = ((crudo_dalto - dalto_curso)/ crudo_dalto) *100

#Mostrando las diferencias de duración (ejercicio a)
print("---------------------")
print("El curso de Dalto dura:")
print(f" - {diferencia_con_min}% menos que el mas rapido")
print(f" -{diferencia_con_max: .2f}% menos que el mas lento")
print(f" - {diferencia_con_promedio}% menos que el mas promedio")
print("---------------------")


#Mostrando la  cantidad de espacios vacios que se remueven (ejercicio b)
print(f"El curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio")
print(f"El curso de dalto elimina un {tiempo_vacio_dalto :.2f}% de tiempo vacio")
print("---------------------")

#Mostrando diferencias si los cursos duraran 10 horas
print(f"Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos ")
print(f"Ver 10 horas de otros cursos equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de otros cursos")
print("---------------------")