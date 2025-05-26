# Trabajo 2: Predicción del Riesgo Crediticio

## Descripción del Proyecto

Este proyecto hace parte del curso _Redes Neuronales y Algoritmos Bioinspirados_ de la Universidad Nacional de Colombia. Se abordan técnicas de redes neuronales artificiales y se crea un modelo predictivo, un reporte técnico, un video promocional y un sitio web con el modelo.

## Tareas a Realizar (En Orden de Ejecución)

## Esteban (EDA, análisis exploratorio y preparación de datos)

- Limpieza y preprocesamiento del dataset (manejo de NAs, codificación binaria de `loan_status`).
- Análisis descriptivo y visualización inicial (distribución, correlaciones, variables más relevantes).
- Generación de reportes parciales con insights sobre variables riesgosas.
- Preparación de datos para el entrenamiento (split train/test, escalado).
- Documentar hipótesis y resultados del análisis exploratorio en el reporte técnico.

## Tomás (Modelado con Redes Neuronales)

- Construcción del modelo básico de red neuronal con TensorFlow/Keras.
- Optimización de la arquitectura: número de capas, neuronas, funciones de activación.
- Entrenamiento y validación del modelo con métricas (AUC, accuracy, recall).
- Generar la scorecard basada en la salida del modelo (binarización, escalado).
- Interpretación del modelo: identificar variables que influyen más en la predicción.
- Guardar el modelo entrenado y los objetos necesarios (scaler, encoder).
- Documentar el proceso de modelado y resultados en el reporte técnico.

## Marcos (Desarrollo web y video promocional)

- Estructura y diseño inicial de la aplicación web con Streamlit.
- Implementar la carga de datos de entrada desde formulario de usuario.
- Mostrar el scorecard y la comparación del score con la población general.
- Integrar gráficos y visualizaciones (interactivas o estáticas) Si existen.
- Coordinar la creación del video promocional: guion, grabación, edición.
- Asegurar que el video resalte la solución y cómo usar la app.
- Documentar el desarrollo web con una guía de uso.

## Jose (Desarrollo web y video)

- Apoyo en la implementación frontend/backend en Streamlit (formulario, carga modelo).
- Implementar funciones para calcular el score en tiempo real basado en inputs.
- Integrar enlaces al reporte técnico y material promocional en la app.
- Colaborar en la grabación y edición del video promocional.
- Revisión final y pruebas de usabilidad de la aplicación web.
- Documentar los pasos de despliegue y recomendaciones para usuarios.

## Tareas comunes / coordinadas

- Reuniones de sincronización: Todos los Lunes Reuniones cortas para mostrar avances.
- Revisión y feedback cruzado de código y documentación.
- Ensayo final del video y prueba de la aplicación web para demo.

## Links Relevantes

- 📝 [Entrada de Blog en RPubs](https://rpubs.com/)
- 🌐 [Link al sitio en Streamlit](https://streamlit.io/)

## Estructura

```
RNA_G4_Prediccion_Riesgo_Crediticio/
├── requirements.txt # ✅ Requisitos de Python para todo el proyecto (Debe actualizarse)
├── README.md # 📘 Instrucciones del proyecto
│
├── files/ # 📂 Datos y artefactos del modelo
│ ├── input/ # 📥 Datos crudos (Aquí se pone el csv del gitignore)
│ │ └── LCDataDictionary.xlsx
│ └── output/ # 📤 Modelos entrenados, escaladores, etc.
│ ├── modelo_credito.pkl
│ └── scaler_score_credito.pkl
│
├── src/ # 🔧 Código fuente
│ ├── eda_credito.py
│ ├── entrenamiento_modelo.py
│ └── utils_modelo.py
│
├── streamlit_app/ # 🌐 App web
│ └── app.py
│
├── reporte/ # 📄 Reporte en RMarkdown
│ └── reporte_blog.Rmd
│
└── video/ # 🎥 Video promocional
└── video_promocional.mp4
```

## Requisitos

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/vasquez-esteban/RNA_G4_Prediccion_Riesgo_Crediticio
   ```

### Para Visualizar y Generar el Reporte en R

Para el reporte técnico en R se necesita:

- R (versión recomendada: 4.0 o superior)
- RStudio (versión recomendada: 1.4 o superior)
  MacOS y Linux
- 1.1. Abre el archivo `/reporte/reporte_blog.Rmd` en RStudio

  1.2. Instala las dependencias necesarias ejecutando los primeros bloques de código manualmente desde RStudio:

  ```R
  # Este código se encuentra en los primeros bloques del archivo Rmd
  install.packages(c("ggplot2", "dplyr", "readxl", "gifski", "gganimate"))
  # Más dependencias según sea necesario
  ```

  1.3. Generar el archivo con RPUBS.

### Para Desarrollo en Python (EDA, Modelo de redes y Streamlit)

#### Configuración En Linux y Mac

Ejecute los siguientes comandos en el terminal:

```bash
python3 -m venv .venv
source .venv/bin/activate
source setup.sh
```

#### Configuración en Windows

Ejecute los siguientes comandos en el terminal:

```bash
python3 -m venv .venv
.venv\Scripts\activate
setup
```

```bash
# Ejecución en Streamlit
streamlit run streamlit_app/app.py
```

## Versiones

El repositorio muestra un desarrollo iterativo con diferentes versiones:

- v10.0 - Entrega Final
- v0.0 - Inicialización del proyecto
