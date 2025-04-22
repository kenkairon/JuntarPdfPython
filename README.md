# JuntarPdfPython
Educativo y de Aprendizaje Personal

---

## Tabla de Contenidos
- [Requisitos](#requisitos)

---

## Requisitos

- Python 3.9 o superior
---

## Configuración del Entorno

1. Crear el entorno virtual:
   ```bash
   python -m venv venv


## Activación del Entorno

2. Activar el entorno virtual:
    ### Windows
    ```bash
    venv\Scripts\activate

3. Instalar PyPDF2
    ```bash
    pip install PyPDF2

4. Código Para Ejecutar
    ```bash
    from PyPDF2 import PdfMerger
    
    merger = PdfMerger()
    merger.append("Evolución de las bases de datos en el tiempo.pdf")
    merger.append("Introducción a la programación segura.pdf")
    merger.append("PPT Unidad II.pdf")
    merger.write("ArchivoFusion.pdf")
    merger.close()