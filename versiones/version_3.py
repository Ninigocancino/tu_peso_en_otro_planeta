#En está versión del programa le daremos al usuario la opción de elegir entre calcular su peso en el planeta marte o la luna

#El usuario podrá interactuar con el programa ingresando su peso en la tierra y luego seleccionando el astro donde querramos calcular su peso


#---------Está sección del código hace más agradable visualmente la ejeución de esté  en consola y muestra información importante para que el usuario sepa que debe hacer en el programa--------

print("Bienvenido a la calculadora de peso en planetas v3")

print("-" * 12)

print("Menú")

print("")
print("Para Marte ingresa = 1")
print("Para Luna ingresa = 2")
print("")

print("-" * 12)

print("")

#---------Declaramos las variables que contienen los valores de gravedad relatiiva a la tierra de los diferentes astros que comtemplará el programa

gravedad_tierra = 1
gravedad_marte = 0.38
gravedad_luna = 0.165

#---------Solicitamos al usuario que seleccione una opción ingresando numeros correspondientes a las opciones del menú--------

elegir_planeta = input("¿En que planeta quieres calcular tu peso?: ")
peso_en_la_tierra = int(input("¿Cuál es tu peso en la tierra?: "))

#--------Declaramos las formulas que nos ayudarán a realizar la conversión------

peso_marte = peso_en_la_tierra * gravedad_marte / gravedad_tierra
peso_luna = peso_en_la_tierra * gravedad_luna / gravedad_tierra

#--------Utilizamos condionales para controlar las acciones que se deeben ejecutar en los casos que puedan ocurrir

if elegir_planeta == "1":
  print(f"Tu peso en marte es: {peso_marte}")
elif elegir_planeta == "2":
  print(f"Tu peso en la luna es: {peso_luna}")
else:
  print("Por favor elige una opción valida")