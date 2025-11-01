import time

def lz77_compress(text, window_size=512):
    """
    Aplica compresión LZ77 básica.
    Retorna una lista de tuplas (distancia, longitud, siguiente_caracter).
    """
    i = 0
    compressed = []

    while i < len(text):
        match_length = 0
        match_distance = 0

        # Buscar la coincidencia más larga en la ventana anterior
        for j in range(max(0, i - window_size), i):
            length = 0
            while (i + length < len(text)) and (text[j + length] == text[i + length]):
                length += 1
                if j + length >= i:
                    break
            if length > match_length:
                match_length = length
                match_distance = i - j

        # Si hay coincidencia, guardarla; si no, símbolo literal
        if match_length > 0:
            next_char = text[i + match_length] if (i + match_length) < len(text) else ''
            compressed.append((match_distance, match_length, next_char))
            i += match_length + 1
        else:
            compressed.append((0, 0, text[i]))
            i += 1

    return compressed


def lz77_decompress(compressed):
    """
    Reconstruye el texto original a partir de la lista comprimida LZ77.
    """
    text = ""
    for dist, length, char in compressed:
        if dist == 0 and length == 0:
            text += char
        else:
            start = len(text) - dist
            for k in range(length):
                text += text[start + k]
            text += char
    return text


def lz77_compress_con_metrica(text, window_size=512):
    """
    Ejecuta la compresión LZ77 y devuelve métricas relevantes:
      - Longitud original y comprimida
      - Ratio de compresión y porcentaje de ahorro
      - Tiempo de compresión
    """
    inicio = time.time()
    compressed = lz77_compress(text, window_size)
    fin = time.time()

    # Calcular tamaño estimado (tuplas)
    longitud_comprimida = len(compressed)

    # Calcular métricas
    ratio_compresion = len(text) / longitud_comprimida if longitud_comprimida > 0 else 0
    ahorro_porcentual = (1 - (longitud_comprimida / len(text))) * 100 if len(text) > 0 else 0

    return {
        "Comprimido": compressed,
        "LongitudOriginal": len(text),
        "LongitudComprimida": longitud_comprimida,
        "RatioCompresion": round(ratio_compresion, 3),
        "AhorroPorcentual": round(ahorro_porcentual, 2),
        "TiempoCodificacion": round(fin - inicio, 3),
    }


def lz77_decompress_con_metrica(diccionario):
    """
    Ejecuta la descompresión y mide el tiempo de decodificación.
    """
    inicio = time.time()
    texto = lz77_decompress(diccionario["Comprimido"])
    fin = time.time()
    diccionario["TiempoDecodificacion"] = round(fin - inicio, 3)
    diccionario["TextoRecuperado"] = texto
    return texto
