import planetas_sistema_solar

planetas = planetas_sistema_solar.planetas_ss

print("-" * 12)
print("Bienvenido a la calculadora de peso del sistema solar")
print("")
print("Para ingresar por favor proporciona un usuario verificado")
print("")

usuarios = [{
  "Nombre_usuario": "Victor",
  "Estatus": "Verificado"},
          {
  "Nombre_usuario": "Marcela",
  "Estatus": "Verificado"},
          ]


while True:
  #Entrada usuario
  visitante = input("Ingresa un usuario: ")
  visitante = visitante.capitalize()

  usuario_valido = next((usuario for usuario in usuarios if usuario["Nombre_usuario"] == visitante and usuario["Estatus"] == "Verificado"), None)

  if not visitante:
    print("Debes ingresar un usuario")
  
  elif not usuario_valido:
    print("Este no es un usuario validado, intenta de nuevo por favor")
  else:
    break



if usuario_valido:

  while True:
      elegir_planeta = input("¿En que planeta quieres calcular tu peso?: ")
      elegir_planeta = elegir_planeta.capitalize()
      if not elegir_planeta:
        print("Debes ingresar el nombre de un planeta")
      elif not any(i["nombre"] == elegir_planeta for i in planetas):
        print("Este astro no está en mi base de datos. Por favor, intenta con otro planeta")
      else:
        break
  
  g_relativa_tierra = 1
  gravedad_relativa_t = None 
  planeta_elegido = None

  for i in planetas:
    
    
    if i["nombre"] == elegir_planeta:
      planeta_elegido = i.get("nombre")
      gravedad_relativa_t = i.get("gravedad_relativa")

      gravedad_relativa_t = float(gravedad_relativa_t)

      while True:
        try:
          peso_en_la_tierra = float(input("¿Cuál es tu peso en la tierra?: "))
          break
        except ValueError:
          print("Debes ingresar un valor numerico")

      
      peso_en_planeta_elegido = peso_en_la_tierra * gravedad_relativa_t / g_relativa_tierra
      print(f"Tu peso en {planeta_elegido} es de: {peso_en_planeta_elegido} kg")

      break

    
  if planeta_elegido is None:
    print("Este astro no está en mi base de datos por favor intenta con otro planeta")
  

#else:
#  print("Este no es un usuario validado, intenta de nuevo por favor")