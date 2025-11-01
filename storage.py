import pandas as pd

# ========================
# Funciones genéricas de Excel
# ========================

def _limpiar_valor(valor):
    """Elimina caracteres ilegales para Excel de un string."""
    if isinstance(valor, str):
        return ''.join(c for c in valor if c.isprintable() or c in '\t\n\r')
    return valor

def _limpiar_lista_records(lista):
    """Aplica limpieza a todos los valores de una lista de diccionarios."""
    return [{k: _limpiar_valor(v) for k, v in rec.items()} for rec in lista]

def _guardar_excel(ruta, hojas: dict):
    """Guarda un diccionario de listas/records en un archivo Excel limpiando caracteres."""
    with pd.ExcelWriter(ruta, engine="openpyxl") as writer:
        for nombre, contenido in hojas.items():
            # Limpiar si es lista de diccionarios
            if isinstance(contenido, list) and contenido and isinstance(contenido[0], dict):
                contenido = _limpiar_lista_records(contenido)
            pd.DataFrame(contenido).to_excel(writer, sheet_name=nombre, index=False)

def _cargar_excel(ruta, hojas: list):
    """Carga varias hojas de un Excel y devuelve un diccionario de DataFrames."""
    return {h: pd.read_excel(ruta, sheet_name=h) for h in hojas}

# ========================
# Funciones Simbolos (Shannon-Fano y Huffman)
# ========================

def persistir_simbolos(dic, ruta_excel):
    hojas = {
        "Simbolos": dic["ListaSimbolos"],
        "Totales": [{k: dic[k] for k in ["TotalSimbolos","ProbabilidadTotal","EntropiaTotal"]}]
    }
    _guardar_excel(ruta_excel, hojas)

def recuperar_simbolos(ruta_excel):
    dfs = _cargar_excel(ruta_excel, ["Simbolos","Totales"])
    dic = {"ListaSimbolos": dfs["Simbolos"].to_dict(orient="records")}
    for col in dfs["Totales"].columns:
        dic[col] = dfs["Totales"][col][0]
    return dic

def persistir_shannon_fano(dic, ruta_excel):
    hojas = {
        "Simbolos": dic["ListaSimbolos"],
        "Totales": [{k: dic.get(k,0) for k in ["TotalSimbolos","ProbabilidadTotal","EntropiaTotal",
                                              "LongitudPromedio","TotalBits","Eficiencia",
                                              "TiempoCodificacion","TiempoDecodificacion"]}]
    }
    _guardar_excel(ruta_excel, hojas)

def recuperar_shannon_fano(ruta_excel):
    dfs = _cargar_excel(ruta_excel, ["Simbolos","Totales"])
    dic = {"ListaSimbolos": dfs["Simbolos"].to_dict(orient="records")}
    for col in dfs["Totales"].columns:
        dic[col] = dfs["Totales"][col][0]
    # Generar diccionario de códigos si existen
    if "Code" in dfs["Simbolos"].columns and "Simbolo" in dfs["Simbolos"].columns:
        dic["Codigos"] = {row["Simbolo"]: row["Code"] for row in dic["ListaSimbolos"]}
    if "Codigo" in dfs["Simbolos"].columns and "Simbolo" in dfs["Simbolos"].columns:
        dic["Codigos"] = {row["Simbolo"]: row["Codigo"] for row in dic["ListaSimbolos"]}
    return dic

# ========================
# Funciones Huffman
# ========================

def persistir_huffman(dic, ruta_excel):
    hojas = {
        "Simbolos": dic["ListaSimbolos"],
        "Totales": [{k: dic.get(k,0) for k in ["TotalSimbolos","ProbabilidadTotal","EntropiaTotal",
                                              "LongitudPromedio","TotalBits","Eficiencia",
                                              "TiempoCodificacion","TiempoDecodificacion"]}]
    }
    _guardar_excel(ruta_excel, hojas)

def recuperar_huffman(ruta_excel):
    dfs = _cargar_excel(ruta_excel, ["Simbolos","Totales"])
    dic = {"ListaSimbolos": dfs["Simbolos"].to_dict(orient="records")}
    for col in dfs["Totales"].columns:
        dic[col] = dfs["Totales"][col][0]
    if "Codigo" in dfs["Simbolos"].columns and "Simbolo" in dfs["Simbolos"].columns:
        dic["Codigos"] = {row["Simbolo"]: row["Codigo"] for row in dic["ListaSimbolos"]}
    return dic

# ========================
# Funciones LZ77
# ========================

def persistir_lz77(dic, ruta_excel):
    hojas = {
        "Comprimido": dic["Comprimido"],
        "Totales": [{k: dic.get(k,0) for k in ["LongitudOriginal","LongitudComprimida",
                                              "Eficiencia","TiempoCodificacion","TiempoDecodificacion"]}]
    }
    _guardar_excel(ruta_excel, hojas)

def recuperar_lz77(ruta_excel):
    dfs = _cargar_excel(ruta_excel, ["Comprimido","Totales"])
    dic = {"Comprimido": [tuple(row) for row in dfs["Comprimido"].to_numpy()]}
    for col in dfs["Totales"].columns:
        dic[col] = dfs["Totales"][col][0]
    return dic

# ========================
# Funciones Promedios
# ========================

def persistir_promedios(dic_promedios, ruta_excel):
    hojas = {
        "PromediosGenerales": [_limpiar_lista_records([dic_promedios["PromediosGenerales"]])[0]],
        "SimbolosPromediados": _limpiar_lista_records(dic_promedios["SimbolosPromediados"])
    }
    _guardar_excel(ruta_excel, hojas)
