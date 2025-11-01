import os
from docx import Document
from PyPDF2 import PdfReader


def leer_docx(ruta: str) -> str:
    """Lee y devuelve el texto de un archivo .docx."""
    doc = Document(ruta)
    return "\n".join(p.text for p in doc.paragraphs if p.text.strip())


def leer_pdf(ruta: str) -> str:
    """Lee y devuelve el texto de un archivo .pdf."""
    reader = PdfReader(ruta)
    textos = [page.extract_text() for page in reader.pages if page.extract_text()]
    return "\n".join(textos)


def leer_archivo(ruta: str) -> str:
    """
    Lee el contenido textual de un archivo .docx o .pdf.
    
    Parámetros:
        ruta (str): Ruta absoluta o relativa al archivo.
    
    Retorna:
        str: Texto plano extraído del archivo.
    
    Lanza:
        ValueError: Si el formato no está soportado.
    """
    _, extension = os.path.splitext(ruta)
    extension = extension.lower()

    lectores = {
        ".docx": leer_docx,
        ".pdf": leer_pdf
    }

    if extension not in lectores:
        raise ValueError(f"reader.py - Formato no soportado: {extension}")

    return lectores[extension](ruta)
