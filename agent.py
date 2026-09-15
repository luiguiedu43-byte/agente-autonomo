import os
from langchain_openai import ChatOpenAI
from ddgs import DDGS

def ejecutar_sistema_autonomo(objetivo):
    # 1. Búsqueda web directa con el paquete ddgs
    hallazgos_web = ""
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(objetivo, max_results=3))
            for r in results:
                hallazgos_web += f"- {r.get('title')}: {r.get('body')}\n"
    except Exception as e:
        hallazgos_web = f"No se pudieron obtener resultados web directo: {e}"

    # 2. Modelo de Inteligencia Artificial
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

    # 3. Prompt de integración y análisis
    prompt = f"""
    Eres una IA autónoma experta en desarrollo de software, mecánica e investigación.
    
    OBJETIVO DEL USUARIO: {objetivo}
    INFORMACIÓN EXTRAÍDA DE LA WEB:
    {hallazgos_web}
    
    Con base en el objetivo y los datos recabados, genera la respuesta o el código más completo, estructurado y detallado posible.
    """
    
    respuesta = llm.invoke(prompt)
    return respuesta.content
