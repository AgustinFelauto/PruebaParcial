otros_curosos_min = 2.5
otros_curosos_max = 7
otros_curosos_promedio = 4
dalto_curso = 1.5

#duracion de crudo
crudo_promedio = 5
crudo_dalto = 3.5

#diferencias de duracion
diferencia_con_min = 100 - dalto_curso / otros_curosos_min * 100
diferencia_con_max = 100 - dalto_curso *1000 // otros_curosos_max / 10
diferencia_con_promedio = 100 - dalto_curso / otros_curosos_promedio * 100

#calculando el procentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - otros_curosos_promedio * 1000 / crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10

#mostrando las diferencias de duracion (ejercicio a)
print(f"el curso de dalto dura un {diferencia_con_min}% menos que el mas rapido")
print(f"el curso de dalto dura un {diferencia_con_max}% menos que el mas lento")
print(f"el curso de dalto dura un {diferencia_con_promedio}% menos que el mas promedio")

#mostrando las cantidad de vacios que se remueven (ejercicio b)
print(f"un curso promedio elimina el {tiempo_vacio_promedio}% de tiempo vacio")
print(f"este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio")

#mostrando diferencia si los cursos duraran 10 horas
print(f"ver 10 horas de este curso equivale a ver {otros_curosos_promedio * 100 // dalto_curso / 10} horas de otros cursos")

