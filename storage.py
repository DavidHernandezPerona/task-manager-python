ARCHIVO_TAREAS = "tareas.txt"


def guardar_tareas(tareas):
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
        for tarea in tareas:
            linea = tarea["descripcion"] + "|" + str(tarea["completada"])
            archivo.write(linea + "\n")


def cargar_tareas():
    tareas = []

    try:
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                partes = linea.split("|")

                if len(partes) == 2:
                    tareas.append({
                        "descripcion": partes[0],
                        "completada": partes[1] == "True"
                    })

    except FileNotFoundError:
        pass

    return tareas
