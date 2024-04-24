const fs = require('fs');
const pdfkit = require('pdfkit');
const path = require('path');

const carpeta_imagenes = 'C:/Users/DELL/Music/imagnes4';

const archivos = fs.readdirSync(carpeta_imagenes);

const imagenes = archivos.filter(archivo =>
    archivo.toLowerCase().endsWith('.png') ||
    archivo.toLowerCase().endsWith('.jpg') ||
    archivo.toLowerCase().endsWith('.jpeg') ||
    archivo.toLowerCase().endsWith('.gif')
);

const imagenes_por_pdf = 32;
let pdf_numero = 1;

function agregar_imagenes_a_pdf(pdf_numero, imagenes) {
    const nombre_pdf = `articulos_y_mas${pdf_numero}.pdf`;
    const doc = new pdfkit();

    doc.pipe(fs.createWriteStream(nombre_pdf));

    const letterWidth = 612;
    const letterHeight = 792;

    for (const imagen_nombre of imagenes) {
        const imagen_path = path.join(carpeta_imagenes, imagen_nombre);

        const imagen = fs.readFileSync(imagen_path);

        doc.image(imagen, 0, 0, { width: letterWidth, height: letterHeight });
        doc.addPage();
    }

    doc.end();

    console.log(`Se han convertido las imágenes ${pdf_numero * imagenes_por_pdf - imagenes_por_pdf + 1} a ${pdf_numero * imagenes_por_pdf} en el archivo PDF: ${nombre_pdf}`);
}

while (imagenes.length > 0) {
    const imagenes_subset = imagenes.splice(0, imagenes_por_pdf);
    agregar_imagenes_a_pdf(pdf_numero, imagenes_subset);
    pdf_numero++;
}

console.log('Se han generado todos los PDFs.');
