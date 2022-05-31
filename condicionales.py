calificacion = input("Introduce tu calificacion de la AZ-900: ")

calificacion = int(calificacion)
# Preguntamos si la calificación es menor a 700
if calificacion < 700 :
    print("Reprobado") # Si es menor a 700, muestra esto
elif calificacion > 1000 :
    print("Mientes, no puedes sacar más de mil")
else : # Si no se cumple el IF anterior, pasa a esta linea
    print("Aprobado") # Se ejecuta si ninguno de los iff se cumple

# Verificador de mayoría de edad
edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <= 115 :
    print("Bienvenido al mamitas")
elif edad > 115 :
    print("Si vienes acompañado de tus abuelitos, si te podemos fiar")
elif edad < 0 :
    print("Ni que fueras viajero del tiempo")
else :
    print("Eres menor de edad")