#EN ESTÁ VERSIÓN DEL PROGRAMA:

# 1.-Le daremos al usuario la opción de elegir entre calcular su peso en el planeta marte o la luna

# 2.-El usuario podrá interactuar con el programa ingresando su peso en la tierra y luego seleccionando el astro donde querramos calcular su peso

# 3.-El programa limitará el acceso para que solo una persona especifica pueda ingresar a la calculadora


#---------Está sección del código hace más agradable visualmente la ejeución de esté  en consola y muestra información importante para que el usuario sepa que debe hacer en el programa--------

print("Bienvenido a la calculadora de peso en planetas v4")


print("-" * 12)
print("Menú")
print("")
print("Para Marte ingresa = 1")
print("Para Luna ingresa = 2")
print("")

print("-" * 12)

print("")

#---------Declaramos los valores que queremos que sean constante para está versión del programa--------

gravedad_tierra = 1
gravedad_marte = 0.38
gravedad_luna = 0.165
usuario = "Pepe Pecas" #puedes sustituir estenombre por el tuyo propio

#---------Solicitamos al usuario que ingrese su nombre para verificar si es el usuario autorizado--------

visitante = input("Ingresa un usuario con autorización: ")

#--------Utilizamos condionales para controlar las acciones que deben ejecutarse---------

if visitante == usuario:
  elegir_planeta = input("¿En que planeta quieres calcular tu peso?: ")

  print("")
  
  if elegir_planeta == "1":
    peso_en_la_tierra = int(input("¿Cuál es tu peso en la tierra?: "))
    peso_marte = peso_en_la_tierra * gravedad_marte / gravedad_tierra
    print(f"Tu peso en Marte es: {peso_marte} kg")
  elif elegir_planeta == "2":
    peso_en_la_tierra = int(input("¿Cuál es tu peso en la tierra?: "))
    peso_luna = peso_en_la_tierra * gravedad_luna / gravedad_tierra
    print(f"Tu peso en la luna es: {peso_luna} kg")
  else:
    print("Porfavor elige una opción valida")
else:
  print("No eres un usuario autorizado")