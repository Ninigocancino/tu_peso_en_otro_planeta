
gravedad_tierra = 1
gravedad_marte = 0.38
gravedad_luna = 0.165

print("-" * 12)
print("Menú")
print("")
print("Para Marte ingresa = 1")
print("Para Luna ingresa = 2")
print("")

usuarios = [{
  "Nombre_usuario": "Victor",
  "Estatus": "Verificado"},
          {
  "Nombre_usuario": "Marcela",
  "Estatus": "Verificado"},
          ]

#Entrada usuario
visitante = input("Ingresa un usuario: ")

usuario_valido = next((usuario for usuario in usuarios if usuario["Nombre_usuario"] == visitante and usuario["Estatus"] == "Verificado"), None)


if usuario_valido:
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
  print("No eres un usuario valido")