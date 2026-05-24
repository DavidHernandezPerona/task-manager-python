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
    
    elif opcion == "1":
        tarea = {
            "descripcion": input("Introduzca una tarea pendiente: "),
            "completada": False
}
        tareas.append(tarea)
        print("Tarea añadida correctamente")
    elif opcion == "2":
        if len(tareas) == 0:
            print("No hay tareas pendientes")
        else:
            contador = 1
            for tarea in tareas:
                if tarea.get("completada") == False :
                    print(contador, tarea.get("descripcion") , "[Pendiente]" )
                else:
                    print(contador, tarea.get("descripcion"), "[Completada]")
                contador += 1
    elif opcion == "3":
        if len(tareas) == 0 :
            print("No hay tareas pendientes")
        else:
            contador = 1
            for tarea in tareas:
                if tarea.get("completada") == False :
                    print(contador, tarea.get("descripcion") , "[Pendiente]" ) 
                else:
                    print(contador, tarea.get("descripcion"), "[Completada]")
                contador += 1
            tarea_elegida = input("¿Qué tarea quieres marcar como completada?: ")
            if tarea_elegida.isdigit():
                tarea_index = int(tarea_elegida) - 1
                if 0 <= tarea_index < len(tareas):
                    tareas[tarea_index]["completada"] = True
                    print("Tarea marcada como completada")
                else:
                    print("Número de tarea no válida")
            else:
                print("Entrada no válida")
    else:
            print("Opción no válida")
    print()
