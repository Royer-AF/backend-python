tareas = []
while True:
    tarea = input("Ingrese una tarea 'fin' para salir: ")
    if tarea != "fin":
        tareas.append(tarea)
    else:
        print("Lista de tareas")
        for indice, tarea in enumerate(tareas, 1):
            print(f"{indice}. {tarea}")
        break