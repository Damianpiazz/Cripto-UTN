# Cripto-UTN

Este proyecto implementa distintas técnicas de compresión de texto: **Shannon-Fano**, **Huffman** y **Lempel-Ziv (LZ77)**.
Permite analizar archivos, calcular información estadística de los símbolos y generar resultados codificados, decodificados y reportes en Excel.

---

## Requisitos

* Python 3.10 o superior
* Librerías necesarias:

```
pip install pandas openpyxl numpy
```

---

## Configuración del Entorno (Windows)

1. Abrir PowerShell o CMD y navegar a la carpeta del proyecto:

```powershell
cd C:\ruta\a\tu\proyecto
```

2. Crear un entorno virtual:

```powershell
python -m venv env
```

3. Activar el entorno:

* PowerShell:

```powershell
.\env\Scripts\Activate.ps1
```

* CMD:

```cmd
.\env\Scripts\activate.bat
```

4. Instalar dependencias:

```powershell
pip install --upgrade pip
pip install pandas openpyxl numpy
```

5. Para desactivar el entorno:

```powershell
deactivate
```

---

## Ejecución del Proyecto

1. Colocar los archivos de texto en un directorio a procesar.
2. Ejecutar el programa con:

```bash
python main.py <ruta_del_directorio>
```

Ejemplo:

```bash
python main.py ./archivos
```

3. Se generarán los resultados en las carpetas:

* `codificado/` → Archivos codificados
* `decodificado/` → Archivos decodificados
* `planillas/` → Reportes en Excel con métricas

---

## Etapas del Proyecto

### ETAPA 1: Calcular probabilidades de ocurrencia de caracteres

**Procedimiento:**

1. Recopilar datos: texto, imágenes, audio, etc.
2. Contabilizar la frecuencia de cada carácter: crear un diccionario o tabla con la frecuencia de cada carácter.
3. Calcular probabilidades de ocurrencia: dividir la frecuencia de cada carácter por el total de caracteres.

**Tipos de caracteres a contabilizar:**

* Letras (mayúsculas y minúsculas)
* Dígitos (0-9)
* Espacios
* Signos de puntuación
* Otros caracteres especiales

**Observación:** Mantener un registro del total de caracteres leídos y los totales parciales de cada carácter con sus probabilidades de ocurrencia.

**Fases sugeridas:**

* **Fase 1:** Fórmulas de Excel (ej.: `=LARGO()`)
* **Fase 2:** Macro en VBA para Excel
* **Fase 3:** Automatización avanzada en Python

---

### ETAPA 2: Evaluar algoritmos de compresión

**Algoritmos:**

1. **Huffman:** códigos de longitud variable eficientes para distribuciones sesgadas.
2. **Shannon-Fano:** similar a Huffman, con otra construcción de árbol.
3. **Lempel-Ziv (LZ77):** utiliza diccionario y codificación de longitud variable.

**Métricas de eficiencia:**

* Tasa de compresión (Compression Ratio)
* Longitud media del código (L)
* Redundancia
* Tiempo de codificación y decodificación

**Otros factores:**

* Relación de compresión (tamaño comprimido vs. original)
* Complejidad computacional
* Implementación y facilidad de uso

---

## Resultados Generados

* **Planillas de símbolos:** cantidad, probabilidad, entropía e información mutua
* **Reportes de codificación:** longitud promedio, eficiencia y tamaño de salida
* **Archivo de promedios:** resumen general con las métricas de todos los archivos procesados

---

## Recomendaciones

* Usar archivos en codificación UTF-8
* Mantener las carpetas `codificado`, `decodificado` y `planillas` limpias antes de ejecutar nuevamente
* Revisar archivos Excel para comparar resultados entre algoritmos
