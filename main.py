import argparse
import os
import lector
import simbolos
import storage
import shannon
import huffman
import lempel
import promedios

# --- Configuración de directorios ---
DIRECTORIOS_SALIDA = ["./planillas", "./codificado", "./decodificado"]
for d in DIRECTORIOS_SALIDA:
    os.makedirs(d, exist_ok=True)

# --- Argumentos ---
parser = argparse.ArgumentParser(description="Procesa un directorio de archivos de texto")
parser.add_argument("directorio", help="Directorio a procesar")
args = parser.parse_args()


def guardar_archivos_codificados(nombre_base, codificado, decodificado, sufijo):
    """Guarda archivos codificados y decodificados en las carpetas correspondientes"""
    path_codificado = f"./codificado/{nombre_base}_{sufijo}.txt"
    path_decodificado = f"./decodificado/{nombre_base}_{sufijo}.txt"

    with open(path_codificado, "w", encoding="utf-8") as f:
        f.write(codificado)
    with open(path_decodificado, "w", encoding="utf-8") as f:
        f.write(decodificado)


def procesar_archivo(ruta_archivo):
    """Procesa un archivo: símbolos, codificación Shannon, Huffman y Lempel-Ziv"""
    contenido = lector.leer_archivo(ruta_archivo)
    nombre_base = os.path.splitext(os.path.basename(ruta_archivo))[0]

    # --- Información de símbolos ---
    ruta_simbolos = f"./planillas/{nombre_base}_simbolo.xlsx"
    info_simbolos = simbolos.calcular_informacion_simbolos(contenido)
    storage.persistir_simbolos(info_simbolos, ruta_simbolos)

    # --- Codificación ---
    shan = shannon.codificar_shannon_fano(storage.recuperar_simbolos(ruta_simbolos))
    huff = huffman.codificar_huffman(storage.recuperar_simbolos(ruta_simbolos))
    lemp = lempel.lz77_compress_con_metrica(contenido)

    # --- Guardar codificado y decodificado ---
    guardar_archivos_codificados(
        nombre_base,
        shannon.generar_texto_codificado(shan, contenido),
        shannon.decodificar_shannon_fano(shan, shannon.generar_texto_codificado(shan, contenido)),
        "shannon"
    )

    guardar_archivos_codificados(
        nombre_base,
        huffman.generar_texto_codificado(huff, contenido),
        huffman.decodificar_huffman(huff, huffman.generar_texto_codificado(huff, contenido)),
        "huffman"
    )

    guardar_archivos_codificados(
        nombre_base,
        str(lemp["Comprimido"]),
        lempel.lz77_decompress(lemp["Comprimido"]),
        "lempel-ziv"
    )

    # --- Guardar Excel ---
    storage.persistir_shannon_fano(shan, f"./planillas/{nombre_base}_shannon.xlsx")
    storage.persistir_huffman(huff, f"./planillas/{nombre_base}_huffman.xlsx")
    storage.persistir_lz77(lemp, f"./planillas/{nombre_base}_lempel-ziv.xlsx")

    return info_simbolos


def main():
    if not os.path.isdir(args.directorio):
        print(f"main.py - Error: '{args.directorio}' no es un directorio válido")
        return

    # --- Lista de archivos a procesar ---
    archivos = [
        os.path.join(args.directorio, f)
        for f in os.listdir(args.directorio)
        if os.path.isfile(os.path.join(args.directorio, f))
    ]

    resultados_simbolos = [procesar_archivo(a) for a in archivos]

    # --- Calcular y persistir promedios ---
    promedios_generales = promedios.calcular_promedios(resultados_simbolos)
    storage.persistir_promedios(promedios_generales, "./planillas/promedio_simbolos.xlsx")


if __name__ == "__main__":
    main()
