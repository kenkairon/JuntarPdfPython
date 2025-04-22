from PyPDF2 import PdfMerger

merger = PdfMerger()
merger.append("Evolución de las bases de datos en el tiempo.pdf")
merger.append("Introducción a la programación segura.pdf")
merger.append("PPT Unidad II.pdf")
merger.write("ArchivoFusion.pdf")
merger.close()