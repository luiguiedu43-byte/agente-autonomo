import os
from crewai import Agent, Crew, Process, Task
from crewai_tools import SerperDevTool

def ejecutar_sistema_autonomo(objetivo):
    # Buscador web para el agente
    web_search = SerperDevTool()

    # 1. Agente Investigador Web
    investigador = Agent(
        role='Investigador Tecnologico Web',
        goal='Buscar en internet la informacion mas reciente sobre el objetivo solicitado',
        backstory='Eres un experto en scraping y busqueda de datos en tiempo real.',
        tools=[web_search],
        verbose=True
    )

    # 2. Agente Programador
    programador = Agent(
        role='Arquitecto de Software e IA',
        goal='Escribir codigo funcional completo para crear la solucion o la nueva IA solicitada',
        backstory='Eres un programador senior capaz de disenar scripts avanzados.',
        verbose=True
    )

    # 3. Agente Auditor
    auditor = Agent(
        role='Supervisor de Calidad de Codigo',
        goal='Revisar el codigo generado por el programador y corregir fallos',
        backstory='Eres un auditor enfocado en la estabilidad del software.',
        verbose=True
    )

    # Tareas secuenciales
    t1 = Task(
        description=f'Investigar en la web sobre: {objetivo}',
        agent=investigador,
        expected_output='Informe detallado con los hallazgos de internet.'
    )
    t2 = Task(
        description='Diseñar y escribir el codigo completo con base en la investigacion.',
        agent=programador,
        expected_output='Codigo de programacion funcional listo para usar.'
    )
    t3 = Task(
        description='Auditar el codigo generado y entregar la version final corregida.',
        agent=auditor,
        expected_output='Codigo optimizado y libre de errores.'
    )

    # Ensamblado del equipo
    equipo = Crew(
        agents=[investigador, programador, auditor],
        tasks=[t1, t2, t3],
        process=Process.sequential
    )

    return equipo.kickoff()
  
