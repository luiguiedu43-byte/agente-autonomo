import os
import streamlit as st
from agent import ejecutar_sistema_autonomo

st.set_page_config(page_title="Centro de Mando IA", layout="wide")

st.title("🤖 Centro de Mando de Agentes Autónomos")
st.write("Escribe una orden para que el equipo investigue la web y programe el código.")

# Configuración de llaves en el menú lateral
st.sidebar.header("Configuración de API Keys")
api_key = st.sidebar.text_input("OpenAI API Key", type="password")
serper_key = st.sidebar.text_input("Serper API Key", type="password")

if api_key and serper_key:
    os.environ["OPENAI_API_KEY"] = api_key
    os.environ["SERPER_API_KEY"] = serper_key

    orden = st.text_area("¿Qué deseas que investigue o programe el sistema?", height=120)

    if st.button("Ejecutar Sistema Autónomo", type="primary"):
        with st.spinner("Los agentes están investigando en internet y programando..."):
            try:
                resultado = ejecutar_sistema_autonomo(orden)
                st.success("¡Tarea Completada!")
                st.markdown("### Resultado de los Agentes:")
                st.code(resultado, language="python")
            except Exception as e:
                st.error(f"Ocurrió un error durante la ejecución: {e}")
else:
    st.warning("👈 Por favor ingresa tus llaves de OpenAI y Serper en el menú lateral para comenzar.")
  
