# Guarda las tareas en un archivo de texto
def guardar_tareas(tareas):
    with open("tareas.txt", "w", encoding="utf-8") as archivo:
        for tarea in tareas:
            linea = tarea.get("descripcion") + "|" + str(tarea.get("completada"))
            archivo.write(linea + "\n")


# Carga las tareas guardadas al iniciar el programa
def cargar_tareas():
    tareas = []

    try:
        with open("tareas.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                partes = linea.split("|")

                tarea = {
                    "descripcion": partes[0],
                    "completada": partes[1] == "True"
                }

                tareas.append(tarea)

    except FileNotFoundError:
        pass

    return tareas


def mostrar_tareas(tareas):
    if len(tareas) == 0:
        print("No hay tareas pendientes")
    else:
        contador = 1
        for tarea in tareas:
            if tarea.get("completada") == False:
                print(contador, tarea.get("descripcion"), "[Pendiente]")
            else:
                print(contador, tarea.get("descripcion"), "[Completada]")
            contador += 1


def añadir_tarea(tareas):
    tarea = {
        "descripcion": input("Introduzca una tarea pendiente: "),
        "completada": False
    }

    tareas.append(tarea)
    print("Tarea añadida correctamente")


def completar_tarea(tareas):
    if len(tareas) == 0:
        print("No hay tareas pendientes")
    else:
        mostrar_tareas(tareas)

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


def eliminar_tarea(tareas):
    if len(tareas) == 0:
        print("No hay tareas en la lista")
    else:
        mostrar_tareas(tareas)

        tarea_eliminar = input("Elige la tarea que desea eliminar: ")

        if tarea_eliminar.isdigit():
            tarea_eliminar_index = int(tarea_eliminar) - 1

            if 0 <= tarea_eliminar_index < len(tareas):
                tarea_eliminada = tareas.pop(tarea_eliminar_index)
                print("Tarea eliminada:", tarea_eliminada.get("descripcion"))
            else:
                print("Número de tarea no válida")
        else:
            print("Entrada no válida")


def buscar_tarea(tareas):
    busqueda = input("Introduce la tarea que desea buscar: ")
    encontrada = False

    for tarea in tareas:
        descripcion = tarea.get("descripcion")

        if busqueda.lower() in descripcion.lower():
            print(tarea.get("descripcion"))
            encontrada = True

    if not encontrada:
        print("No se han encontrado tareas")


def mostrar_menu():
    print(""" ==== GESTOR DE TAREAS ====
1. Añadir tarea
2. Ver tareas
3. Marcar tarea como completada
4. Eliminar tarea
5. Buscar tarea
6. Salir
 """)


# Lista de tareas cargadas desde el archivo
tareas = cargar_tareas()

while True:
    mostrar_menu()

    opcion = input("Elige una opción: ")

    if opcion == "1":
        añadir_tarea(tareas)

    elif opcion == "2":
        mostrar_tareas(tareas)

    elif opcion == "3":
        completar_tarea(tareas)

    elif opcion == "4":
        eliminar_tarea(tareas)

    elif opcion == "5":
        buscar_tarea(tareas)

    elif opcion == "6":
        guardar_tareas(tareas)
        print("Tareas guardadas correctamente.")
        break

    else:
        print("Opción no válida")

    print()