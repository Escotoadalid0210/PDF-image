from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

carpeta_imagenes = 'C:/Users/Francisco Escoto/Music/imagnes4'

archivos = os.listdir(carpeta_imagenes)


imagenes = [archivo for archivo in archivos if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]


imagenes_por_pdf = 32


pdf_numero = 1


def agregar_imagenes_a_pdf(pdf_numero, imagenes):
    
    nombre_pdf = f'articulos y mas{pdf_numero}.pdf'

    
    c = canvas.Canvas(nombre_pdf, pagesize=letter)

    
    ancho_pagina = letter[0]
    alto_pagina = letter[1]

    
    for imagen_nombre in imagenes:
        imagen_path = os.path.join(carpeta_imagenes, imagen_nombre)
        imagen = Image.open(imagen_path)
        imagen_ancho, imagen_alto = imagen.size

        
        escala = min(ancho_pagina / imagen_ancho, alto_pagina / imagen_alto)

        
        x = (ancho_pagina - imagen_ancho * escala) / 2
        y = (alto_pagina - imagen_alto * escala) / 2

        
        c.drawImage(imagen_path, x, y, imagen_ancho * escala, imagen_alto * escala)
        c.showPage()

    
    c.save()

    print(f'Se han convertido las imágenes {pdf_numero * imagenes_por_pdf - imagenes_por_pdf + 1} a {pdf_numero * imagenes_por_pdf} en el archivo PDF: {nombre_pdf}')


while len(imagenes) > 0:
    imagenes_subset = imagenes[:imagenes_por_pdf]  
    agregar_imagenes_a_pdf(pdf_numero, imagenes_subset)
    pdf_numero += 1
    imagenes = imagenes[imagenes_por_pdf:] 

print('Se han generado todos los PDFs.')
