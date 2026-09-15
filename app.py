import os
import streamlit as st
from agent import ejecutar_sistema_autonomo

st.set_page_config(page_title="Centro de Mando IA", layout="wide")

st.title("🤖 Centro de Mando de Agentes Autónomos")
st.write("Escribe una orden para que el sistema investigue en la web y programe la solución.")

# Menú lateral para la llave de OpenAI
st.sidebar.header("Configuración")
api_key = st.sidebar.text_input("OpenAI API Key", type="password")

if api_key:
    os.environ["OPENAI_API_KEY"] = api_key

    orden = st.text_area("¿Qué deseas que investigue o programe el sistema?", height=120)

    if st.button("Ejecutar Sistema Autónomo", type="primary"):
        with st.spinner("Buscando en internet y generando código..."):
            try:
                resultado = ejecutar_sistema_autonomo(orden)
                st.success("¡Tarea Completada!")
                st.markdown("### Resultado:")
                st.write(resultado)
            except Exception as e:
                st.error(f"Ocurrió un error: {e}")
else:
    st.warning("👈 Por favor ingresa tu API Key de OpenAI en el menú lateral para iniciar.")
    
