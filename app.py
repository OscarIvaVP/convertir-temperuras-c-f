import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Conversor Interactivo de Temperatura",
    page_icon="🌡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para mejorar la apariencia
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 1rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
    }
    </style>
    """, unsafe_allow_html=True)

# Título principal con estilo
st.markdown('<div class="main-header"><h1>🌡️ Conversor Interactivo de Temperatura</h1><p>Aprende y convierte entre diferentes escalas de temperatura</p></div>', unsafe_allow_html=True)

# Sidebar con información educativa
with st.sidebar:
    st.header("📚 Información Educativa")

    with st.expander("🔍 ¿Qué es la temperatura?"):
        st.write("""
        La **temperatura** es una magnitud física que mide el nivel de calor o frío de un cuerpo o ambiente.
        Es una medida de la energía cinética promedio de las partículas que componen un objeto.
        """)

    with st.expander("🌡️ Escalas de Temperatura"):
        st.write("""
        **Celsius (°C)**: Escala métrica donde el agua se congela a 0°C y hierve a 100°C.

        **Fahrenheit (°F)**: Escala usada principalmente en EE.UU. El agua se congela a 32°F y hierve a 212°F.

        **Kelvin (K)**: Escala absoluta usada en ciencia. El cero absoluto es 0 K (-273.15°C).
        """)

    with st.expander("📐 Fórmulas de Conversión"):
        st.latex(r"°F = (°C × \frac{9}{5}) + 32")
        st.latex(r"°C = (°F - 32) × \frac{5}{9}")
        st.latex(r"K = °C + 273.15")
        st.latex(r"°C = K - 273.15")

    with st.expander("💡 Dato Curioso"):
        st.write("""
        ¿Sabías que existe una temperatura donde Celsius y Fahrenheit coinciden?
        ¡Es -40°! (-40°C = -40°F)
        """)

# Tabs principales para organizar el contenido
tab1, tab2, tab3, tab4 = st.tabs(["🔄 Conversor", "📊 Visualización", "📖 Ejemplos", "🎯 Quiz"])

with tab1:
    st.header("Conversor de Temperatura")

    # Selector de modo de conversión
    col1, col2 = st.columns([2, 1])

    with col1:
        modo_conversion = st.radio(
            "Selecciona el tipo de conversión:",
            ["Celsius → Fahrenheit", "Fahrenheit → Celsius", "Celsius → Kelvin", "Kelvin → Celsius", "Todas las escalas"],
            horizontal=True
        )

    st.divider()

    # Funciones de conversión
    def celsius_a_fahrenheit(c):
        return (c * 9/5) + 32

    def fahrenheit_a_celsius(f):
        return (f - 32) * 5/9

    def celsius_a_kelvin(c):
        return c + 273.15

    def kelvin_a_celsius(k):
        return k - 273.15

    # Input según el modo seleccionado
    if modo_conversion == "Celsius → Fahrenheit":
        col1, col2 = st.columns(2)
        with col1:
            temp_input = st.number_input("Temperatura en Celsius (°C):", value=0.0, format="%.2f", key="c_to_f")
            temp_slider = st.slider("O usa el slider:", -100.0, 100.0, 0.0, 0.1, key="slider_c_to_f")
            temp = temp_input if temp_input != 0.0 else temp_slider

        resultado = celsius_a_fahrenheit(temp)
        with col2:
            st.metric("Resultado", f"{resultado:.2f} °F", delta=f"{abs(resultado-temp):.2f}° de diferencia")
            st.success(f"**{temp:.2f} °C** = **{resultado:.2f} °F**")

    elif modo_conversion == "Fahrenheit → Celsius":
        col1, col2 = st.columns(2)
        with col1:
            temp_input = st.number_input("Temperatura en Fahrenheit (°F):", value=32.0, format="%.2f", key="f_to_c")
            temp_slider = st.slider("O usa el slider:", -148.0, 212.0, 32.0, 0.1, key="slider_f_to_c")
            temp = temp_input if temp_input != 32.0 else temp_slider

        resultado = fahrenheit_a_celsius(temp)
        with col2:
            st.metric("Resultado", f"{resultado:.2f} °C", delta=f"{abs(resultado-temp):.2f}° de diferencia")
            st.success(f"**{temp:.2f} °F** = **{resultado:.2f} °C**")

    elif modo_conversion == "Celsius → Kelvin":
        col1, col2 = st.columns(2)
        with col1:
            temp_input = st.number_input("Temperatura en Celsius (°C):", value=0.0, format="%.2f", key="c_to_k")
            temp_slider = st.slider("O usa el slider:", -273.15, 100.0, 0.0, 0.01, key="slider_c_to_k")
            temp = temp_input if temp_input != 0.0 else temp_slider

        resultado = celsius_a_kelvin(temp)
        with col2:
            st.metric("Resultado", f"{resultado:.2f} K", delta=f"{abs(resultado-temp):.2f}° de diferencia")
            st.success(f"**{temp:.2f} °C** = **{resultado:.2f} K**")

    elif modo_conversion == "Kelvin → Celsius":
        col1, col2 = st.columns(2)
        with col1:
            temp_input = st.number_input("Temperatura en Kelvin (K):", value=273.15, format="%.2f", key="k_to_c")
            temp_slider = st.slider("O usa el slider:", 0.0, 373.15, 273.15, 0.01, key="slider_k_to_c")
            temp = temp_input if temp_input != 273.15 else temp_slider

        resultado = kelvin_a_celsius(temp)
        with col2:
            st.metric("Resultado", f"{resultado:.2f} °C", delta=f"{abs(resultado-temp):.2f}° de diferencia")
            st.success(f"**{temp:.2f} K** = **{resultado:.2f} °C**")

    else:  # Todas las escalas
        temp_celsius = st.number_input("Ingresa temperatura en Celsius (°C):", value=0.0, format="%.2f", key="all")
        temp_slider = st.slider("O usa el slider:", -100.0, 100.0, 0.0, 0.1, key="slider_all")
        temp = temp_celsius if temp_celsius != 0.0 else temp_slider

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Celsius", f"{temp:.2f} °C", "Entrada")
        with col2:
            fahrenheit = celsius_a_fahrenheit(temp)
            st.metric("Fahrenheit", f"{fahrenheit:.2f} °F", f"{fahrenheit-temp:+.2f}°")
        with col3:
            kelvin = celsius_a_kelvin(temp)
            st.metric("Kelvin", f"{kelvin:.2f} K", f"{kelvin-temp:+.2f}°")

with tab2:
    st.header("📊 Visualización Interactiva")

    # Selector de rango para la gráfica
    col1, col2 = st.columns(2)
    with col1:
        temp_min = st.number_input("Temperatura mínima (°C):", value=-50.0, key="min")
    with col2:
        temp_max = st.number_input("Temperatura máxima (°C):", value=50.0, key="max")

    # Generar datos para la gráfica
    celsius_range = list(range(int(temp_min), int(temp_max) + 1))
    fahrenheit_range = [celsius_a_fahrenheit(c) for c in celsius_range]
    kelvin_range = [celsius_a_kelvin(c) for c in celsius_range]

    # Crear gráfico interactivo con Plotly
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=celsius_range,
        y=fahrenheit_range,
        mode='lines+markers',
        name='Fahrenheit',
        line=dict(color='#FF6B6B', width=3),
        marker=dict(size=5)
    ))

    fig.add_trace(go.Scatter(
        x=celsius_range,
        y=kelvin_range,
        mode='lines+markers',
        name='Kelvin',
        line=dict(color='#4ECDC4', width=3),
        marker=dict(size=5)
    ))

    fig.update_layout(
        title='Comparación de Escalas de Temperatura',
        xaxis_title='Celsius (°C)',
        yaxis_title='Temperatura',
        hovermode='x unified',
        template='plotly_white',
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

    # Tabla comparativa
    st.subheader("📋 Tabla Comparativa")

    # Crear DataFrame con temperaturas clave
    temps_importantes = [-273.15, -40, -18, 0, 20, 37, 100]
    df = pd.DataFrame({
        'Celsius (°C)': temps_importantes,
        'Fahrenheit (°F)': [celsius_a_fahrenheit(c) for c in temps_importantes],
        'Kelvin (K)': [celsius_a_kelvin(c) for c in temps_importantes],
        'Referencia': [
            'Cero Absoluto',
            'C° = F°',
            'Congelador',
            'Agua se congela',
            'Temperatura ambiente',
            'Temperatura corporal',
            'Agua hierve'
        ]
    })

    st.dataframe(df, hide_index=True, use_container_width=True)

with tab3:
    st.header("📖 Ejemplos de Temperaturas Comunes")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🌡️ Temperaturas Cotidianas")
        ejemplos_cotidianos = {
            "❄️ Congelador": -18,
            "🧊 Agua se congela": 0,
            "🏠 Temperatura ambiente": 20,
            "🏖️ Día cálido": 30,
            "🌡️ Temperatura corporal": 37,
            "☕ Café caliente": 70,
            "💧 Agua hierve": 100
        }

        for descripcion, temp_c in ejemplos_cotidianos.items():
            with st.expander(descripcion):
                col_a, col_b, col_c = st.columns(3)
                col_a.metric("Celsius", f"{temp_c}°C")
                col_b.metric("Fahrenheit", f"{celsius_a_fahrenheit(temp_c):.1f}°F")
                col_c.metric("Kelvin", f"{celsius_a_kelvin(temp_c):.2f}K")

    with col2:
        st.subheader("🌍 Temperaturas Extremas")
        ejemplos_extremos = {
            "🥶 Récord frío en Tierra": -89.2,
            "🌡️ Nitrógeno líquido": -196,
            "🔥 Récord calor en Tierra": 56.7,
            "🌋 Lava": 1200,
            "☀️ Superficie del Sol": 5500
        }

        for descripcion, temp_c in ejemplos_extremos.items():
            with st.expander(descripcion):
                col_a, col_b, col_c = st.columns(3)
                col_a.metric("Celsius", f"{temp_c}°C")
                col_b.metric("Fahrenheit", f"{celsius_a_fahrenheit(temp_c):.1f}°F")
                if temp_c >= -273.15:
                    col_c.metric("Kelvin", f"{celsius_a_kelvin(temp_c):.2f}K")

with tab4:
    st.header("🎯 Pon a Prueba tus Conocimientos")

    st.write("Resuelve estos ejercicios para practicar:")

    with st.expander("Ejercicio 1: ¿Cuántos °F son 25°C?"):
        respuesta1 = st.number_input("Tu respuesta:", key="q1")
        if st.button("Verificar", key="b1"):
            correcto = celsius_a_fahrenheit(25)
            if abs(respuesta1 - correcto) < 0.1:
                st.success(f"¡Correcto! 25°C = {correcto:.1f}°F")
            else:
                st.error(f"Incorrecto. La respuesta correcta es {correcto:.1f}°F")

    with st.expander("Ejercicio 2: ¿Cuántos °C son 68°F?"):
        respuesta2 = st.number_input("Tu respuesta:", key="q2")
        if st.button("Verificar", key="b2"):
            correcto = fahrenheit_a_celsius(68)
            if abs(respuesta2 - correcto) < 0.1:
                st.success(f"¡Correcto! 68°F = {correcto:.1f}°C")
            else:
                st.error(f"Incorrecto. La respuesta correcta es {correcto:.1f}°C")

    with st.expander("Ejercicio 3: ¿Cuántos K son 0°C?"):
        respuesta3 = st.number_input("Tu respuesta:", key="q3")
        if st.button("Verificar", key="b3"):
            correcto = celsius_a_kelvin(0)
            if abs(respuesta3 - correcto) < 0.1:
                st.success(f"¡Correcto! 0°C = {correcto:.2f}K")
            else:
                st.error(f"Incorrecto. La respuesta correcta es {correcto:.2f}K")

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    <p>💡 Desarrollado como recurso educativo interactivo | 🌡️ Aprende sobre escalas de temperatura</p>
</div>
""", unsafe_allow_html=True)
