import heapq
import time
from typing import Any

class NodoHuffman:
    """
    Representa un nodo del árbol de Huffman.
    Cada nodo puede ser un símbolo (hoja) o un nodo intermedio con hijos.
    """
    def __init__(self, simbolo: str | None = None, frecuencia: int = 0):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izquierdo: "NodoHuffman" | None = None
        self.derecho: "NodoHuffman" | None = None

    def __lt__(self, otro: "NodoHuffman") -> bool:
        """Permite comparar nodos por frecuencia al usar heapq."""
        return self.frecuencia < otro.frecuencia


def construir_arbol_huffman(lista_simbolos: list[dict[str, Any]]) -> NodoHuffman:
    """
    Construye el árbol de Huffman a partir de una lista de símbolos y sus frecuencias.
    """
    heap: list[NodoHuffman] = [
        NodoHuffman(simbolo=s["Simbolo"], frecuencia=s["Cantidad"]) for s in lista_simbolos
    ]
    heapq.heapify(heap)

    while len(heap) > 1:
        izquierdo = heapq.heappop(heap)
        derecho = heapq.heappop(heap)
        combinado = NodoHuffman(frecuencia=izquierdo.frecuencia + derecho.frecuencia)
        combinado.izquierdo = izquierdo
        combinado.derecho = derecho
        heapq.heappush(heap, combinado)

    return heap[0]


def asignar_codigos_huffman(nodo: NodoHuffman, prefijo: str = "", codigos: dict[str, str] | None = None) -> dict[str, str]:
    """
    Asigna códigos binarios a cada símbolo de forma recursiva según el árbol de Huffman.
    """
    if codigos is None:
        codigos = {}

    if nodo.simbolo is not None:
        codigos[nodo.simbolo] = prefijo or "0"
    else:
        asignar_codigos_huffman(nodo.izquierdo, prefijo + "0", codigos)
        asignar_codigos_huffman(nodo.derecho, prefijo + "1", codigos)

    return codigos


def codificar_huffman(datos: dict[str, Any]) -> dict[str, Any]:
    """
    Codifica los símbolos utilizando el algoritmo de Huffman.

    Args:
        datos (dict): Debe incluir 'ListaSimbolos' y 'EntropiaTotal'.

    Returns:
        dict: Estructura con códigos, métricas de eficiencia y tiempos de ejecución.
    """
    inicio = time.perf_counter()

    # Construcción del árbol y generación de códigos
    arbol = construir_arbol_huffman(datos["ListaSimbolos"])
    codigos = asignar_codigos_huffman(arbol)
    datos["Codigos"] = codigos

    longitud_promedio = 0
    total_bits = 0

    for simbolo in datos["ListaSimbolos"]:
        codigo = codigos[simbolo["Simbolo"]]
        largo = len(codigo)
        simbolo["Codigo"] = codigo
        simbolo["LongitudCodigo"] = largo
        simbolo["TotalBits"] = simbolo["Cantidad"] * largo
        simbolo["LongitudPromedio"] = simbolo["Probabilidad"] * largo

        longitud_promedio += simbolo["LongitudPromedio"]
        total_bits += simbolo["TotalBits"]

    datos["LongitudPromedio"] = round(longitud_promedio, 6)
    datos["TotalBits"] = total_bits
    datos["Eficiencia"] = (
        round(datos["EntropiaTotal"] / longitud_promedio, 6)
        if longitud_promedio > 0 else 0
    )

    fin = time.perf_counter()
    datos["TiempoCodificacion"] = round(fin - inicio, 6)

    return datos


def decodificar_huffman(datos: dict[str, Any], texto_codificado: str) -> str:
    """
    Decodifica una cadena binaria utilizando los códigos Huffman generados previamente.

    Args:
        datos (dict): Debe incluir 'Codigos'.
        texto_codificado (str): Texto codificado en bits.

    Returns:
        str: Texto original decodificado.
    """
    inicio = time.perf_counter()

    codigo_a_simbolo = {v: k for k, v in datos["Codigos"].items()}
    resultado = []
    buffer = ""

    for bit in texto_codificado:
        buffer += bit
        if buffer in codigo_a_simbolo:
            resultado.append(codigo_a_simbolo[buffer])
            buffer = ""

    fin = time.perf_counter()
    datos["TiempoDecodificacion"] = round(fin - inicio, 6)
    return "".join(resultado)


def generar_texto_codificado(datos: dict[str, Any], texto_original: str) -> str:
    """
    Genera el texto binario codificado a partir del texto original
    utilizando los códigos Huffman previamente generados.

    Args:
        datos (dict): Debe incluir 'Codigos'.
        texto_original (str): Texto original a codificar.

    Returns:
        str: Texto binario codificado.
    """
    inicio = time.perf_counter()

    codigos = datos["Codigos"]
    texto_codificado = "".join(codigos[s] for s in texto_original)

    fin = time.perf_counter()
    datos["TiempoGeneracion"] = round(fin - inicio, 6)

    return texto_codificado
