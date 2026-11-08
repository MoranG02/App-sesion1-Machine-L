import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Plataforma de Aprendizaje Iterativo", layout="wide")

# Barra lateral para navegación estructurada
st.sidebar.title("Ruta de Aprendizaje")
st.sidebar.info("Módulos de Diseño de Procesos y Productos Químicos")

modulo = st.sidebar.radio(
    "Selecciona la etapa actual:",
    (
        "1. Introducción y Conceptos", 
        "2. Actividad Práctica", 
        "3. Evaluación y Retroalimentación"
    )
)

st.title("Aplicación de Aprendizaje Interactivo")

# ---------------------------------------------------------
# MÓDULO 1: Teoría
# ---------------------------------------------------------
if modulo == "1. Introducción y Conceptos":
    st.header("Conceptos Base")
    st.write("""
    En esta sección se integrará la teoría extraída de las celdas Markdown de tu cuaderno de Colab. 
    Aquí podrás visualizar fórmulas, diagramas de flujo y principios termodinámicos antes de pasar a la práctica.
    """)
    
    st.info("💡 **Tip de estudio:** Revisa la documentación de los modelos matemáticos antes de avanzar a la Actividad Práctica.")

# ---------------------------------------------------------
# MÓDULO 2: Práctica
# ---------------------------------------------------------
elif modulo == "2. Actividad Práctica":
    st.header("Actividad Iterativa")
    st.write("Modifica los parámetros para observar cómo cambian los resultados del proceso.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Entrada de Datos")
        temperatura = st.slider("Temperatura de operación (°C)", min_value=20.0, max_value=200.0, value=117.0)
        presion = st.number_input("Presión del sistema (bar)", min_value=1.0, value=1.0)
        
    with col2:
        st.subheader("Resultados del Modelo")
        # Aquí se integrarán los scripts de Python de tu cuaderno original
        resultado_ficticio = (temperatura * 1.5) / presion
        st.metric(label="Rendimiento Teórico Estimado", value=f"{resultado_ficticio:.2f} %")
        
    st.write("---")
    st.write("*Espacio reservado para gráficas generadas con Matplotlib o integración de resultados de simulación.*")

# ---------------------------------------------------------
# MÓDULO 3: Evaluación
# ---------------------------------------------------------
elif modulo == "3. Evaluación y Retroalimentación":
    st.header("Control de Comprensión")
    st.write("Pon a prueba tus conocimientos sobre los módulos anteriores.")
    
    with st.form("evaluacion_form"):
        st.write("**Pregunta 1:** ¿Cuál es el impacto de aumentar la temperatura en esta etapa del diseño conceptual?")
        respuesta_1 = st.radio(
            "Opciones:",
            ("Disminuye la eficiencia global", "Aumenta la cinética pero requiere evaluación económica", "No tiene impacto en el sistema")
        )
        
        st.write("**Pregunta 2:** Escribe la variable más crítica para asegurar la viabilidad técnica:")
        respuesta_2 = st.text_input("Respuesta corta:")
        
        submitted = st.form_submit_button("Enviar respuestas")
        
        if submitted:
            # Lógica de retroalimentación
            if respuesta_1 == "Aumenta la cinética pero requiere evaluación económica":
                st.success("¡Correcto! En diseño de procesos, las variables operativas siempre deben balancearse con el análisis tecnoeconómico.")
            else:
                st.error("Incorrecto. Recuerda revisar la sección de Conceptos Base, específicamente la relación entre cinética y costos.")
                
            if respuesta_2.strip().lower() in ["presion", "presión", "temperatura"]:
                st.success("Buena identificación de la variable crítica.")
            else:
                st.warning("Revisa nuevamente los parámetros de entrada de la Actividad Práctica.")
