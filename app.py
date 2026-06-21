import streamlit as st
from storage import guardar_tareas, cargar_tareas


st.set_page_config(page_title="Gestor de tareas", page_icon="✅")

st.title("Gestor de tareas")
st.write("Aplicación web sencilla para gestionar tareas.")

if "tareas" not in st.session_state:
    st.session_state.tareas = cargar_tareas()

nueva_tarea = st.text_input("Nueva tarea")

if st.button("Añadir tarea"):
    if nueva_tarea.strip() != "":
        st.session_state.tareas.append({
            "descripcion": nueva_tarea,
            "completada": False
        })
        guardar_tareas(st.session_state.tareas)
        st.success("Tarea añadida correctamente")
        st.rerun()
    else:
        st.warning("Escribe una tarea antes de añadirla.")

st.divider()

st.subheader("Lista de tareas")

if len(st.session_state.tareas) == 0:
    st.info("No hay tareas todavía.")
else:
    for indice, tarea in enumerate(st.session_state.tareas):
        col1, col2, col3, col4 = st.columns([5, 2, 2, 2])

        estado = "Completada" if tarea["completada"] else "Pendiente"

        with col1:
            st.write(f"{indice + 1}. {tarea['descripcion']}")

        with col2:
            st.write(estado)

        with col3:
            if tarea["completada"]:
                if st.button("Pendiente", key=f"pendiente_{indice}"):
                    st.session_state.tareas[indice]["completada"] = False
                    guardar_tareas(st.session_state.tareas)
                    st.rerun()
            else:
                if st.button("Completar", key=f"completar_{indice}"):
                    st.session_state.tareas[indice]["completada"] = True
                    guardar_tareas(st.session_state.tareas)
                    st.rerun()

        with col4:
            if st.button("Eliminar", key=f"eliminar_{indice}"):
                st.session_state.tareas.pop(indice)
                guardar_tareas(st.session_state.tareas)
                st.rerun()

st.divider()

st.subheader("Buscar tarea")

busqueda = st.text_input("Buscar por texto")

if busqueda:
    resultados = [
        tarea for tarea in st.session_state.tareas
        if busqueda.lower() in tarea["descripcion"].lower()
    ]

    if resultados:
        for tarea in resultados:
            estado = "Completada" if tarea["completada"] else "Pendiente"
            st.write(f"- {tarea['descripcion']} [{estado}]")
    else:
        st.warning("No se han encontrado tareas.")

st.divider()

st.subheader("Editar tarea")

if len(st.session_state.tareas) > 0:
    opciones = [
        f"{i + 1}. {tarea['descripcion']}"
        for i, tarea in enumerate(st.session_state.tareas)
    ]

    tarea_seleccionada = st.selectbox("Selecciona una tarea", opciones)
    indice_editar = opciones.index(tarea_seleccionada)

    nueva_descripcion = st.text_input(
        "Nueva descripción",
        value=st.session_state.tareas[indice_editar]["descripcion"]
    )

    if st.button("Guardar cambios"):
        if nueva_descripcion.strip() != "":
            st.session_state.tareas[indice_editar]["descripcion"] = nueva_descripcion
            guardar_tareas(st.session_state.tareas)
            st.success("Tarea editada correctamente")
            st.rerun()
        else:
            st.warning("La descripción no puede estar vacía.")

st.divider()

if st.button("Borrar todas las tareas"):
    st.session_state.tareas.clear()
    guardar_tareas(st.session_state.tareas)
    st.success("Todas las tareas han sido eliminadas")
    st.rerun()