# programa_calificaciones.py

# Paso 1: Entrada de una sola calificación
while True:
    try:
        calificacion = int(input("Ingresa una calificación (0 a 100): "))
        if 0 <= calificacion <= 100:
            break
        else:
            print("Error: La calificación debe estar entre 0 y 100.")
    except ValueError:
        print("Error: Ingresa un número válido.")

# Evaluar estado de aprobación
if calificacion >= 60:
    print("Resultado: Aprobado")
else:
    print("Resultado: Reprobado")

# Paso 2: Entrada de lista de calificaciones
while True:
    entrada = input("Ingresa una lista de calificaciones separadas por comas: ")
    try:
        lista_calificaciones = [int(x.strip()) for x in entrada.split(',')]
        if all(0 <= x <= 100 for x in lista_calificaciones):
            break
        else:
            print("Error: Todas las calificaciones deben estar entre 0 y 100.")
    except ValueError:
        print("Error: Asegúrate de ingresar solo números separados por comas.")

# Calcular promedio
suma = 0
for nota in lista_calificaciones:
    suma += nota
promedio = suma / len(lista_calificaciones)
print(f"Promedio de calificaciones: {promedio:.2f}")

# Paso 3: Conteo de calificaciones mayores a un valor dado
while True:
    try:
        valor_comparacion = int(input("Ingresa un valor para comparar: "))
        break
    except ValueError:
        print("Error: Ingresa un número válido.")

contador_mayores = 0
i = 0
while i < len(lista_calificaciones):
    if lista_calificaciones[i] > valor_comparacion:
        contador_mayores += 1
    i += 1
print(f"Cantidad de calificaciones mayores que {valor_comparacion}: {contador_mayores}")

# Paso 4: Verificar presencia de calificación específica
while True:
    try:
        valor_busqueda = int(input("Ingresa una calificación específica para buscar: "))
        break
    except ValueError:
        print("Error: Ingresa un número válido.")

contador = 0
for cal in lista_calificaciones:
    if cal == valor_busqueda:
        contador += 1
        continue
    if cal > 100: 
        break

if contador > 0:
    print(f"La calificación {valor_busqueda} aparece {contador} veces en la lista.")
else:
    print(f"La calificación {valor_busqueda} no aparece en la lista.")