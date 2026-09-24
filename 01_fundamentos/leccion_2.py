nombre_alumno = input("¿Cuál es tu nombre? ")
ciclo_actual = int(input("¿En qué ciclo estás? "))


if ciclo_actual >= 1:
    print("Bienvenido al taller de programación.")
elif ciclo_actual == 0:
    print("Aún no puedes matricularte.")
else:
    print("El ciclo debe ser un número positivo o cero.")
