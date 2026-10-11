# Ordaz Valdez Karina Julieta

Link : https://tablero-seguros-qkcwts6drupiohqvpu55xc.streamlit.app/

Tenemos un tablero interactivo del Diplomado Machine Learning en Seguros de la Facultad de Ciencias, UNAM. El cual incluye KPIs, filtros, gráficos, ratios de rentabilidad y cotizador de primas empíricas, GLM y tarifa.

# ¿Cómo correr localmente nuestra app_stremlit.py?
## Para ejecutar localmente debemos seguir los siguientes pasos: 

1. Copiar la cartera original del Módulo 4 en `datos/datos.parquet`.
2. Desde esta carpeta, instalar dependencias: `python -m pip install -r requirements.txt`.
3. Ejecutar: `python -m streamlit run app_streamlit.py`.
4. Abrir la dirección local indicada en la terminal (http://localhost:8501).

## Para crear Deploy los pasos son los siguientes: 

Crear un repositorio público con `app_streamlit.py`, `requirements.txt`, `.gitignore`, `README.md` y `datos/datos.parquet`. 
Seleccionar repo, rama `main` y `app_streamlit.py` como archivo principal en Streamlit Community Cloud.

Nota:  `cartera.db` se crea automáticamente a partir del Parquet y no debe subirse.
