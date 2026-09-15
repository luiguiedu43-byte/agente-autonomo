import os
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun

def ejecutar_sistema_autonomo(objetivo):
    # 1. Herramienta de búsqueda web gratuita (no requiere API Key extra)
    search = DuckDuckGoSearchRun()
    
    # 2. Modelo de inteligencia artificial
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

    # 3. Fase 1: Investigación en Internet
    hallazgos_web = search.run(objetivo)

    # 4. Fase 2: Programación y Auditoría
    prompt = f"""
    Eres una IA autónoma experta en desarrollo de software e investigación.
    
    OBJETIVO DEL USUARIO: {objetivo}
    INFORMACIÓN RECIENTE DE LA WEB: {hallazgos_web}
    
    Con base en la información anterior, genera el código completo, funcional y auditado para cumplir con el objetivo.
    Muestra la explicación paso a paso y el código final sin errores.
    """
    
    respuesta = llm.invoke(prompt)
    return respuesta.content
