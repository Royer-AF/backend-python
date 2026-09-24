suma_notas = 0
for i in range(3):
    nota = float(input(f"Ingresa nota {i + 1}: "))
    suma_notas += nota
    print(f"Nota {i + 1} = {nota}")

promedio = suma_notas / 3
print(f"Promedio final: {promedio:.2f}")
print(f"Usted esta: {'Aprobado' if promedio >= 13 else 'Desaprobado'}")

notas = []
for i in range(1, 4):
    nota = float(input(f"Ingresa nota {i}: "))
    notas.append(nota)
promedio = sum(notas) / len(notas)
print(f"Promedio final: {promedio:.2f}")