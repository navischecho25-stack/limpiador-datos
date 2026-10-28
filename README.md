# 🧹 Limpiador y Validador Automático de Datos (`limpiador_datos.py`)

## 🎯 Descripción del Proyecto
Este script de automatización en Python (BPA - Business Process Automation) resuelve un problema crítico en la gestión de datos empresariales: la limpieza y estandarización de archivos CSV caóticos. El programa elimina duplicados exactos, detecta registros vacíos o corruptos, normaliza textos (mayúsculas/minúsculas y espacios) y valida tipos de datos numéricos antes de cualquier análisis financiero.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.14
* **Módulos Nativos:** `os` (gestión de rutas) y `csv` (procesamiento de datos tabulares).

## 🚀 Características
* **Generación de Datos Sucios de Prueba:** Crea automáticamente un archivo con errores simulados (espacios sobrantes, registros vacíos, duplicados y montos no válidos) si la fuente no existe.
* **Normalización Inteligente:** Estandariza nombres de clientes con formato título y ciudades en mayúsculas, eliminando espacios en blanco innecesarios.
* **Control de Errores y Duplicados:** Filtra filas incompletas y descarta duplicados exactos mediante estructuras de conjuntos (`set`), generando un reporte métrico final y un archivo limpio (`datos_limpios_final.csv`).

## 💻 Instrucciones de Uso
1. Coloca tu archivo CSV con datos sin procesar en la carpeta del proyecto.
2. Ejecuta el script:
   ```bash
   python limpiador_datos.py