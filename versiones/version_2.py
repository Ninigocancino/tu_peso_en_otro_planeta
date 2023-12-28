#Crear un programa que solicite al usuario su peso (en kg), convierta el peso ingresado a su equivalente en el planeta Marte y lo imprima en pantalla


gravedad_marte = 0.38
gravedad_tierra = 1
peso_en_la_tierra = int(input("¿Cuàl es tu peso en la tierra? "))

peso_en_marte = peso_en_la_tierra * gravedad_marte / gravedad_tierra

print(f"En marte tu pesarìas:{peso_en_marte}")