import streamlit as st
from modulos.config.conexion import obtener_conexion


def verificar_usuario(Usuario, contra):
    con = obtener_conexion()
    if not con:
        st.error("⚠️ No se pudo conectar a la base de datos.")
        return None
    else:
        # ✅ Guardar en el estado que la conexión fue exitosa
        st.session_state["conexion_exitosa"] = True

    try:
        cursor = con.cursor()
        query = "SELECT Usuario, Contra FROM Empleados WHERE Usuario = %s AND Contra = %s"
        cursor.execute(query, (Usuario, contra))
        result = cursor.fetchone()
        return result[0] if result else None
    finally:
        con.close()


def login():
    st.title("Inicio de sesión")

    # 🟢 Mostrar mensaje persistente si ya hubo conexión exitosa
    if st.session_state.get("conexion_exitosa"):
        st.success("✅ Conexión a la base de datos establecida correctamente.")

    Usuario = st.text_input("Usuario", key="Usuario_input")
    contra = st.text_input("Contraseña", type="password", key="contra_input")

    if st.button("Iniciar sesión"):
        tipo = verificar_usuario(usuario, contrasena)
        if tipo:
            st.session_state["Usuario"] = usuario
            st.session_state["tipo_Usuario"] = tipo
            st.success(f"Bienvenido ({Usuario}) 👋")
            st.session_state["sesion_iniciada"] = True
            st.rerun()
        else:
            st.error("❌ Credenciales incorrectas.")
