# Importamos la librería de Streamlit
import streamlit as st

# --- Configuración de la Página ---
# st.set_page_config se usa para configurar el título que aparece en la pestaña del navegador y el ícono.
st.set_page_config(
    page_title="Conversor de Temperatura",
    page_icon="🌡️"
)

# --- Título y Descripción de la App ---
# st.title() muestra un texto grande como el título principal de la aplicación.
st.title("🌡️ Conversor de Grados Celsius a Fahrenheit")

# st.write() se usa para escribir texto, descripciones o instrucciones.
st.write(
    "¡Bienvenido! Esta simple aplicación te ayuda a convertir la temperatura "
    "de grados Celsius (°C) a grados Fahrenheit (°F)."
)

# --- Entrada de Datos del Usuario ---
# st.number_input() crea un campo numérico donde el usuario puede introducir un valor.
# El primer argumento es la etiqueta que se muestra junto al campo.
# `value=0.0` establece el valor inicial del campo.
# `format="%.2f"` asegura que el número siempre se muestre con dos decimales.
celsius = st.number_input(
    "Ingresa la temperatura en grados Celsius (°C):",
    value=0.0,
    format="%.2f"
)

# --- Lógica de Conversión ---
# Definimos una función para mantener el código organizado.
# Esta función toma los grados Celsius como entrada y devuelve los Fahrenheit.
def convertir_a_fahrenheit(grados_celsius):
  """
  Fórmula de conversión: (Celsius * 9/5) + 32 = Fahrenheit
  """
  return (grados_celsius * 9/5) + 32

# Llamamos a la función con el valor que el usuario introdujo.
fahrenheit = convertir_a_fahrenheit(celsius)

# --- Mostrar el Resultado ---
# st.subheader() crea un subtítulo para organizar mejor el contenido.
st.subheader("Resultado de la Conversión")

# st.success() muestra un mensaje destacado en un cuadro de color verde.
# Usamos un f-string para formatear el texto y mostrar los valores de las variables.
# Los dos puntos seguidos de .2f (:.2f) se usan para formatear el número
# y mostrar solo dos decimales, haciendo el resultado más legible.
st.success(f"**{celsius:.2f} °C** equivalen a **{fahrenheit:.2f} °F**")

# --- Información Adicional (Opcional) ---
# st.info() muestra un cuadro de información de color azul.
st.info("La fórmula utilizada para la conversión es: (°C × 9/5) + 32 = °F")
