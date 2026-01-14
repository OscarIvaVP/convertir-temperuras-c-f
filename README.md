# 🌡️ Conversor Interactivo de Temperatura

Una aplicación web educativa e interactiva desarrollada con Streamlit para convertir temperaturas entre diferentes escalas (Celsius, Fahrenheit y Kelvin). Diseñada como recurso de autoaprendizaje con visualizaciones dinámicas, ejemplos prácticos y ejercicios interactivos.

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)

---

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Instalación Local](#-instalación-local)
- [Uso de la Aplicación](#-uso-de-la-aplicación)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Despliegue en Streamlit Cloud](#-despliegue-en-streamlit-cloud)
- [Capturas de Pantalla](#-capturas-de-pantalla)
- [Funcionalidades Educativas](#-funcionalidades-educativas)
- [Contribuciones](#-contribuciones)
- [Licencia](#-licencia)

---

## ✨ Características

### 🔄 Conversor Multi-Escala
- **5 modos de conversión diferentes:**
  - Celsius → Fahrenheit
  - Fahrenheit → Celsius
  - Celsius → Kelvin
  - Kelvin → Celsius
  - Todas las escalas simultáneamente

- **Interfaz dual de entrada:**
  - Input numérico con precisión decimal
  - Slider interactivo para ajustes rápidos

- **Métricas visuales:**
  - Resultados destacados con deltas
  - Comparación visual de diferencias
  - Formato profesional con 2 decimales

### 📊 Visualización Interactiva
- **Gráfico dinámico con Plotly:**
  - Comparación visual entre escalas
  - Rango personalizable de temperaturas
  - Interactividad completa (zoom, pan, hover)
  - Líneas diferenciadas por color

- **Tabla comparativa:**
  - Temperaturas importantes de referencia
  - Conversión automática a las 3 escalas
  - Contexto educativo (cero absoluto, punto de congelación, etc.)

### 📚 Contenido Educativo
- **Sidebar informativo con:**
  - Definición científica de temperatura
  - Explicación de las 3 escalas principales
  - Fórmulas matemáticas en LaTeX
  - Datos curiosos y trivia

- **Ejemplos prácticos:**
  - Temperaturas cotidianas (congelador, ambiente, corporal)
  - Temperaturas extremas (récords mundiales, lava, superficie solar)
  - Expandibles con conversiones automáticas

### 🎯 Sistema de Quiz
- **3 ejercicios interactivos**
- **Verificación automática de respuestas**
- **Feedback inmediato:**
  - Mensaje de éxito si es correcto
  - Muestra la respuesta correcta si es incorrecto

### 🎨 Diseño Profesional
- **Layout amplio** para aprovechar el espacio de pantalla
- **CSS personalizado** con gradientes y estilos modernos
- **Organización en tabs** para navegación intuitiva
- **Responsive** y adaptable a diferentes dispositivos

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Python** | 3.7+ | Lenguaje de programación principal |
| **Streamlit** | Latest | Framework para aplicaciones web interactivas |
| **Plotly** | Latest | Gráficos interactivos y visualizaciones |
| **Pandas** | Latest | Manipulación y presentación de datos tabulares |

---

## 🚀 Instalación Local

### Prerrequisitos
- Python 3.7 o superior instalado
- pip (gestor de paquetes de Python)
- Git (opcional, para clonar el repositorio)

### Pasos de Instalación

1. **Clonar el repositorio** (o descargar el ZIP)
   ```bash
   git clone https://github.com/TU-USUARIO/convertir-temperuras-c-f.git
   cd convertir-temperuras-c-f
   ```

2. **Crear un entorno virtual** (recomendado)
   ```bash
   # En Windows
   python -m venv venv
   venv\Scripts\activate

   # En macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**
   ```bash
   streamlit run app.py
   ```

5. **Abrir en el navegador**
   - La aplicación se abrirá automáticamente en `http://localhost:8501`
   - Si no se abre, navega manualmente a esa dirección

---

## 📖 Uso de la Aplicación

### Navegación Principal

La aplicación está organizada en **4 tabs principales**:

#### 1️⃣ **Tab Conversor**
- Selecciona el tipo de conversión usando los botones de radio
- Ingresa la temperatura usando:
  - El campo numérico (para valores precisos)
  - El slider (para exploración rápida)
- Visualiza el resultado con métricas destacadas
- Observa la diferencia absoluta entre escalas

#### 2️⃣ **Tab Visualización**
- Ajusta el rango de temperaturas (mínimo y máximo)
- Explora el gráfico interactivo:
  - Pasa el mouse sobre las líneas para ver valores exactos
  - Usa zoom para enfocarte en rangos específicos
  - Compara visualmente las curvas de conversión
- Consulta la tabla comparativa con temperaturas de referencia

#### 3️⃣ **Tab Ejemplos**
- Explora temperaturas cotidianas comunes
- Descubre temperaturas extremas de la naturaleza
- Haz clic en cada ejemplo para ver conversiones automáticas
- Aprende contextos reales de aplicación

#### 4️⃣ **Tab Quiz**
- Pon a prueba tus conocimientos
- Resuelve 3 ejercicios de conversión
- Verifica tus respuestas con un clic
- Recibe feedback inmediato

### Sidebar Educativo
- Consulta información teórica sobre temperatura
- Aprende sobre las diferentes escalas
- Revisa las fórmulas matemáticas
- Descubre datos curiosos

---

## 📁 Estructura del Proyecto

```
convertir-temperuras-c-f/
│
├── app.py                 # Aplicación principal de Streamlit
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Documentación del proyecto
└── .git/                 # Control de versiones Git
```

### Descripción de Archivos

- **`app.py`**: Contiene toda la lógica de la aplicación, incluyendo:
  - Configuración de la página
  - Funciones de conversión de temperatura
  - Interfaz de usuario con tabs
  - Visualizaciones con Plotly
  - Sistema de quiz interactivo

- **`requirements.txt`**: Lista todas las bibliotecas Python necesarias:
  ```
  streamlit
  plotly
  pandas
  ```

- **`README.md`**: Documentación completa del proyecto (este archivo)

---

## ☁️ Despliegue en Streamlit Cloud

### Pasos para Desplegar

1. **Sube el código a GitHub**
   ```bash
   git add .
   git commit -m "Aplicación de conversión de temperatura lista"
   git push origin main
   ```

2. **Accede a Streamlit Cloud**
   - Visita [share.streamlit.io](https://share.streamlit.io)
   - Inicia sesión con tu cuenta de GitHub

3. **Despliega la app**
   - Haz clic en "New app"
   - Selecciona tu repositorio: `convertir-temperuras-c-f`
   - Branch: `main`
   - Main file path: `app.py`
   - Haz clic en "Deploy"

4. **Espera el despliegue**
   - El proceso toma 2-3 minutos
   - Una vez listo, obtendrás una URL pública
   - Ejemplo: `https://tu-usuario-convertir-temperatura.streamlit.app`

5. **Comparte tu aplicación**
   - La URL es pública y accesible desde cualquier dispositivo
   - Puedes compartirla con estudiantes, colegas o amigos

### Actualizaciones Automáticas
- Cada vez que hagas `git push` a tu repositorio
- Streamlit Cloud detectará los cambios automáticamente
- La aplicación se redespliegará con los cambios

---

## 🖼️ Capturas de Pantalla

### Interfaz Principal
La aplicación cuenta con un header moderno con gradiente y diseño profesional.

### Tab Conversor
Permite conversiones en 5 modos diferentes con inputs duales (numérico y slider).

### Tab Visualización
Gráfico interactivo que compara las escalas de temperatura visualmente.

### Tab Ejemplos
Ejemplos prácticos divididos en temperaturas cotidianas y extremas.

### Tab Quiz
Sistema de ejercicios con verificación automática y feedback inmediato.

---

## 🎓 Funcionalidades Educativas

### Para Estudiantes
- **Aprendizaje Visual:** Gráficos interactivos facilitan la comprensión
- **Práctica Guiada:** Ejemplos del mundo real con contexto
- **Autoevaluación:** Quiz interactivo para verificar conocimientos
- **Fórmulas Accesibles:** LaTeX rendering de ecuaciones matemáticas

### Para Docentes
- **Recurso de Clase:** Herramienta lista para usar en lecciones
- **Ejemplos Variados:** Desde cotidianos hasta extremos
- **Contenido Teórico:** Explicaciones científicas integradas
- **Interactividad:** Mantiene el engagement de los estudiantes

### Conceptos Cubiertos
- ✅ Definición de temperatura
- ✅ Escalas Celsius, Fahrenheit y Kelvin
- ✅ Conversión entre escalas
- ✅ Aplicaciones prácticas
- ✅ Datos históricos y curiosidades
- ✅ Cero absoluto y temperatura crítica

---

## 🔧 Personalización

### Modificar Rangos de Temperatura
En `app.py`, busca las líneas de los sliders y ajusta los valores:
```python
temp_slider = st.slider("O usa el slider:", -100.0, 100.0, 0.0, 0.1)
```

### Añadir Más Ejemplos
En la sección de ejemplos, añade entradas al diccionario:
```python
ejemplos_cotidianos = {
    "Tu Ejemplo": temperatura_en_celsius,
    # ...
}
```

### Cambiar Colores del Gráfico
Modifica los valores en la sección de Plotly:
```python
line=dict(color='#TU_COLOR_HEX', width=3)
```

### Agregar Más Preguntas al Quiz
Duplica el patrón de expanders en el Tab 4:
```python
with st.expander("Ejercicio N: Tu pregunta?"):
    # ... código del ejercicio
```

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas y apreciadas. Si deseas mejorar este proyecto:

1. **Fork** el repositorio
2. **Crea** una rama para tu feature (`git checkout -b feature/NuevaFuncionalidad`)
3. **Commit** tus cambios (`git commit -m 'Añadir nueva funcionalidad'`)
4. **Push** a la rama (`git push origin feature/NuevaFuncionalidad`)
5. **Abre** un Pull Request

### Ideas para Contribuir
- Añadir más escalas de temperatura (Rankine, Réaumur)
- Implementar conversión por lotes desde archivo CSV
- Agregar más idiomas (internacionalización)
- Crear visualizaciones adicionales (termómetros animados)
- Expandir el quiz con niveles de dificultad
- Añadir modo oscuro

---

## 📝 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

---

## 👨‍💻 Autor

Desarrollado como recurso educativo interactivo para el aprendizaje de conversiones de temperatura.

---

## 📞 Soporte

Si encuentras algún problema o tienes sugerencias:
- Abre un **Issue** en GitHub
- Describe el problema con detalle
- Incluye capturas de pantalla si es posible

---

## 🌟 Agradecimientos

- **Streamlit** por el excelente framework de desarrollo
- **Plotly** por las capacidades de visualización interactiva
- **Comunidad Python** por las bibliotecas de código abierto

---

## 📚 Recursos Adicionales

### Documentación Técnica
- [Streamlit Docs](https://docs.streamlit.io)
- [Plotly Python](https://plotly.com/python/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

### Información Científica
- [Escalas de Temperatura - Wikipedia](https://es.wikipedia.org/wiki/Escalas_de_temperatura)
- [Sistema Internacional de Unidades](https://es.wikipedia.org/wiki/Sistema_Internacional_de_Unidades)

---

<div align="center">

**⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub ⭐**

Desarrollado con ❤️ usando Python y Streamlit

</div>