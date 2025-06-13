
# Predicción del Riesgo Crediticio con Redes Neuronales

Este proyecto implementa un sistema de predicción de riesgo crediticio usando redes neuronales profundas. Se desarrolla un pipeline completo que incluye exploración y limpieza de datos, modelado con Keras, explicación de resultados con scorecards e interpretabilidad, y una interfaz de consulta vía web desarrollada en Streamlit.

---

## Estructura del Proyecto

```
RNA_G4_Prediccion_Riesgo_Crediticio/
├── README.md
├── requirements.txt
├── setup.sh / setup.bat        # Scripts para crear entorno virtual
│
├── files/
│   ├── input/                  # Datos de entrada (loan.csv, diccionario)
│   └── output/                 # Modelo final, escaladores y valores por defecto
│
├── src/                        # Lógica del modelo y entrenamiento
│   ├── model.py
│   └── rna-g4-predicci-n-riesgo-crediticio.ipynb
│
├── reporte/                    # Reporte técnico en RMarkdown
│   ├── reporte_blog.Rmd
│   ├── reporte_blog.html
│   └── imgs/                   # Gráficas utilizadas en el reporte
│
├── streamlit_app/             # Aplicación web
│   └── app.py
│
└── video/                      # Recursos del video
```

---

## Guía Rápida de Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/vasquez-esteban/RNA_G4_Prediccion_Riesgo_Crediticio
cd RNA_G4_Prediccion_Riesgo_Crediticio
```

### 2. Configurar entorno Python (Linux/macOS)

```bash
python3 -m venv .venv
source .venv/bin/activate
source setup.sh
```

#### En Windows:

```bash
python3 -m venv .venv
.venv\Scripts\activate
setup.bat
```

---

## Ejecutar la aplicación web

```bash
streamlit run streamlit_app/app.py
```

Permite ingresar los datos de un cliente y obtener en tiempo real su score crediticio estimado por el modelo neuronal.

---

## Generar el reporte técnico

Requiere tener instalado **R** y **RStudio**.

1. Abrir el archivo `reporte/reporte_blog.Rmd`.
2. Instalar los paquetes necesarios:

```r
install.packages(c("ggplot2", "dplyr", "readxl", "kableExtra", "gganimate"))
```

3. Ejecutar todos los chunks o compilar directamente como `HTML`.

El reporte incluye el análisis exploratorio, justificación del modelo, métricas de desempeño y scorecard interpretativo.

---

## Publicaciones

- Reporte en RPubs: [Reporte](https://rpubs.com/evasp/rna-g4-datos-tabulares)
- App en Streamlit: [App Web](https://rna-g4-prediccion-riesgo-crediticio.streamlit.app/)
- Video en YouTube: [Video](https://youtu.be/rXl06CvuGu4)

---

## Requisitos

- Python ≥ 3.10
- TensorFlow ≥ 2.12
- Streamlit ≥ 1.20
- R ≥ 4.0
- R packages: `rmarkdown`, `kableExtra`, `ggplot2`, `readxl`, `gganimate`, entre otros.

Todas las dependencias de Python están listadas en `requirements.txt`.

---

## Versión Final

- Entrega final del proyecto, con modelo optimizado, aplicación funcional y documentación completa.
