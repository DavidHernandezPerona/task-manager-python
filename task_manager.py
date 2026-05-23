tareas = []

while True:
    print(""" ==== GESTOR DE TAREAS ====
1. Añadir tarea
2. Ver tareas
3. Marcar tarea como completada
4. Eliminar tarea
5. Salir
 """)
    opcion = input("Elige una opción:")
    if opcion == "5":
        break
    elif opcion in ("1","2","3","4"):
        print("Has elegido la opción:", opcion) 
        if opcion == "1":
            tarea=input("Introduzca una tarea pendiente: ")
            tareas.append(tarea)
            print("Tarea añadida correctamente")
        elif opcion == "2":
            if len(tareas) == 0:
                print("No hay tareas pendientes")
            else:
                for tarea in tareas:
                    print(tarea)
    else:
            print("Opción no válida")
    print()

