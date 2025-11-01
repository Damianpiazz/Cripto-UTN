from collections import Counter
import math

def calcular_informacion_simbolos(texto: str) -> dict:
    """
    Calcula las métricas de información de los símbolos de un texto:
    - Cantidad de cada símbolo
    - Probabilidad
    - Información mutua
    - Entropía
    Retorna un diccionario con estadísticas generales y la lista de símbolos.
    """
    if not texto:
        return {
            "TotalSimbolos": 0,
            "ProbabilidadTotal": 0,
            "EntropiaTotal": 0,
            "ListaSimbolos": []
        }

    total_simbolos = len(texto)
    conteos = Counter(texto)
    lista_simbolos = []

    for simbolo, cantidad in conteos.items():
        probabilidad = cantidad / total_simbolos
        info_mutua = -math.log2(probabilidad)
        entropia = probabilidad * info_mutua

        lista_simbolos.append({
            "Simbolo": simbolo,
            "Cantidad": cantidad,
            "Probabilidad": probabilidad,
            "ProbabilidadInversa": 1 / probabilidad,
            "InformacionMutua": info_mutua,
            "Entropia": entropia
        })

    # Ordenar por frecuencia descendente
    lista_simbolos.sort(key=lambda x: x["Cantidad"], reverse=True)

    probabilidad_total = sum(s["Probabilidad"] for s in lista_simbolos)
    if not math.isclose(probabilidad_total, 1.0, abs_tol=1e-9):
        raise ValueError(f"symbols.py - Probabilidad total distinta de 1: {probabilidad_total}")

    entropia_total = sum(s["Entropia"] for s in lista_simbolos)

    return {
        "TotalSimbolos": total_simbolos,
        "ProbabilidadTotal": probabilidad_total,
        "EntropiaTotal": entropia_total,
        "ListaSimbolos": lista_simbolos
    }
