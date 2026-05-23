while True:
    print(""" ==== GESTOR DE TAREAS ====
1. Añadir tarea
2. Ver tareas
3. Marcar tarea como completada
4. Eliminar tarea
5. Salir
 """)
    opcion=input("Elige una opción:")
    if opcion == "5":
        break
    elif opcion in ("1","2","3","4"):
        print("Has elegido la opción:", opcion)
    else:
        print("Opción no válida")