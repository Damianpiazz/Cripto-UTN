import time
from typing import Any

def codificar_shannon_fano(datos: dict[str, Any]) -> dict[str, Any]:
    """
    Codifica los símbolos utilizando el algoritmo de Shannon-Fano.

    Args:
        datos (dict): Diccionario con las claves:
            - 'ListaSimbolos': lista de símbolos con sus probabilidades.
            - 'EntropiaTotal': valor de entropía del texto.

    Returns:
        dict: Diccionario con los códigos generados, métricas de longitud, bits totales,
              eficiencia y tiempo de codificación.
    """
    inicio = time.perf_counter()

    # Asignar códigos binarios a cada símbolo
    datos['Codigos'] = asignar_codigos(datos['ListaSimbolos'])

    longitud_promedio = 0
    total_bits = 0

    for simbolo in datos['ListaSimbolos']:
        largo_codigo = len(simbolo['Code'])
        simbolo['LongitudCodigo'] = largo_codigo
        simbolo['TotalBits'] = simbolo['Cantidad'] * largo_codigo
        simbolo['LongitudPromedio'] = simbolo['Probabilidad'] * largo_codigo

        longitud_promedio += simbolo['LongitudPromedio']
        total_bits += simbolo['TotalBits']

    datos['LongitudPromedio'] = round(longitud_promedio, 6)
    datos['TotalBits'] = total_bits
    datos['Eficiencia'] = round(
        datos['EntropiaTotal'] / longitud_promedio, 6
    ) if longitud_promedio else 0

    fin = time.perf_counter()
    datos['TiempoCodificacion'] = round(fin - inicio, 6)
    return datos


def decodificar_shannon_fano(datos: dict[str, Any], texto_codificado: str) -> str:
    """
    Decodifica un texto binario utilizando los códigos Shannon-Fano generados previamente.

    Args:
        datos (dict): Diccionario con la clave 'Codigos' (mapa símbolo ↔ código).
        texto_codificado (str): Cadena de bits a decodificar.

    Returns:
        str: Texto decodificado.
    """
    inicio = time.perf_counter()

    codigo_a_simbolo = {v: k for k, v in datos['Codigos'].items()}
    resultado = []
    buffer = ""

    for bit in texto_codificado:
        buffer += bit
        if buffer in codigo_a_simbolo:
            resultado.append(codigo_a_simbolo[buffer])
            buffer = ""

    fin = time.perf_counter()
    datos['TiempoDecodificacion'] = round(fin - inicio, 6)
    return "".join(resultado)


def asignar_codigos(simbolos: list[dict[str, Any]], prefijo: str = "", diccionario_codigos: dict[str, str] | None = None) -> dict[str, str]:
    """
    Asigna códigos binarios a los símbolos según el algoritmo Shannon-Fano (recursivo).
    """
    if diccionario_codigos is None:
        diccionario_codigos = {}

    if len(simbolos) == 1:
        codigo = prefijo or "0"
        simbolo = simbolos[0]
        simbolo["Code"] = codigo
        diccionario_codigos[simbolo["Simbolo"]] = codigo
        return diccionario_codigos

    izquierdo, derecho = dividir_simbolos(simbolos)
    asignar_codigos(izquierdo, prefijo + "0", diccionario_codigos)
    asignar_codigos(derecho, prefijo + "1", diccionario_codigos)
    return diccionario_codigos


def dividir_simbolos(simbolos: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """
    Divide la lista de símbolos en dos grupos con probabilidades totales lo más equilibradas posible.
    """
    mitad = sum(s["Probabilidad"] for s in simbolos) / 2
    acumulado = 0
    indice_mejor = 0
    min_diff = float("inf")

    for i in range(len(simbolos) - 1):
        acumulado += simbolos[i]["Probabilidad"]
        diff = abs(mitad - acumulado)
        if diff < min_diff:
            min_diff = diff
            indice_mejor = i

    return simbolos[:indice_mejor + 1], simbolos[indice_mejor + 1:]


def generar_texto_codificado(datos: dict[str, Any], texto: str) -> str:
    """
    Genera el texto binario codificado a partir de un texto original y los códigos Shannon-Fano.

    Args:
        datos (dict): Diccionario con la clave 'Codigos' (mapa símbolo ↔ código).
        texto (str): Texto original a codificar.

    Returns:
        str: Texto codificado en binario.
    """
    inicio = time.perf_counter()

    codigos = datos["Codigos"]
    texto_codificado = "".join(codigos[s] for s in texto)

    fin = time.perf_counter()
    datos["TiempoGeneracion"] = round(fin - inicio, 6)

    return texto_codificado
