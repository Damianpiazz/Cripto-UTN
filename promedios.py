def calcular_promedios(resultados):
    """
    Calcula los promedios generales y por símbolo a partir de una lista de resultados.

    Parámetros:
        resultados (list[dict]): Lista de diccionarios, cada uno con claves como:
            - TotalSimbolos
            - EntropiaTotal
            - ProbabilidadTotal
            - ListaSimbolos (lista de dict con métricas por símbolo)

    Retorna:
        dict: {
            "PromediosGenerales": {...},
            "SimbolosPromediados": [...]
        }
    """
    if not resultados:
        return {"PromediosGenerales": {}, "SimbolosPromediados": []}

    total_archivos = len(resultados)

    # Promedios generales
    def promedio_clave(clave):
        return sum(r.get(clave, 0) for r in resultados) / total_archivos

    promedios_generales = {
        "PromedioTotalSimbolos": promedio_clave("TotalSimbolos"),
        "PromedioEntropiaTotal": promedio_clave("EntropiaTotal"),
        "PromedioProbabilidadTotal": promedio_clave("ProbabilidadTotal"),
    }

    # Promedios por símbolo
    estadisticas_simbolos = {}

    for resultado in resultados:
        for simbolo_data in resultado.get("ListaSimbolos", []):
            simbolo = simbolo_data["Simbolo"]

            stats = estadisticas_simbolos.setdefault(simbolo, {
                "Cantidad": 0,
                "Probabilidad": 0,
                "ProbabilidadInversa": 0,
                "InformacionMutua": 0,
                "Entropia": 0,
                "Apariciones": 0
            })

            for campo in ["Cantidad", "Probabilidad", "ProbabilidadInversa", "InformacionMutua", "Entropia"]:
                stats[campo] += simbolo_data.get(campo, 0)
            stats["Apariciones"] += 1

    simbolos_promediados = []
    for simbolo, stats in estadisticas_simbolos.items():
        apariciones = stats["Apariciones"]
        if apariciones == 0:
            continue

        simbolos_promediados.append({
            "Simbolo": simbolo,
            "PromedioCantidad": stats["Cantidad"] / apariciones,
            "PromedioProbabilidad": stats["Probabilidad"] / apariciones,
            "PromedioProbabilidadInversa": stats["ProbabilidadInversa"] / apariciones,
            "PromedioInformacionMutua": stats["InformacionMutua"] / apariciones,
            "PromedioEntropia": stats["Entropia"] / apariciones,
        })

    return {
        "PromediosGenerales": promedios_generales,
        "SimbolosPromediados": simbolos_promediados
    }
