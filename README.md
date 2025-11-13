# 🧩 Cripto-UTN

Este proyecto implementa distintas **técnicas de compresión de texto**, incluyendo **Shannon-Fano**, **Huffman** y **Lempel-Ziv (LZ77)**.  
Permite analizar archivos, calcular información estadística de los símbolos y generar resultados **codificados, decodificados y reportes en Excel**.

---

## 📋 Requisitos

- **Python 3.10 o superior**
- Dependencias listadas en `requirements.txt`

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuración del Entorno (Windows)

### 1. Abrir PowerShell o CMD y navegar a la carpeta del proyecto:
```powershell
cd C:\ruta\a\tu\proyecto
```

### 2. Crear un entorno virtual:
```powershell
python -m venv env
```

### 3. Activar el entorno:
**PowerShell:**
```powershell
.\env\Scripts\Activate.ps1
```

**CMD:**
```cmd
.\env\Scripts\activate.bat
```

### 4. Instalar dependencias:
```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Desactivar el entorno:
```powershell
deactivate
```

---

## 🚀 Ejecución del Proyecto

1. Colocar los archivos de texto a procesar dentro de un directorio.  
2. Ejecutar el programa con:

```bash
python main.py <ruta_del_directorio>
```

### Ejemplo:
```bash
python main.py ./archivos
```

Se generarán los resultados en las carpetas:

- 📁 **codificado/** → Archivos codificados  
- 📁 **decodificado/** → Archivos decodificados  
- 📁 **planillas/** → Reportes en Excel con métricas  

---

## 🧠 Etapas del Proyecto

### **ETAPA 1: Calcular probabilidades de ocurrencia de caracteres**

**Procedimiento:**
- Recopilar datos: texto, imágenes, audio, etc.  
- Contabilizar la frecuencia de cada carácter (diccionario o tabla).  
- Calcular probabilidades dividiendo la frecuencia de cada carácter por el total de caracteres.  

**Tipos de caracteres:**
- Letras (mayúsculas y minúsculas)
- Dígitos (0–9)
- Espacios
- Signos de puntuación
- Caracteres especiales

**Registro necesario:**
- Total de caracteres leídos  
- Totales parciales y probabilidades de ocurrencia  

**Fases sugeridas:**
1. **Fase 1:** Fórmulas de Excel (ej. `=LARGO()`)  
2. **Fase 2:** Macro en VBA  
3. **Fase 3:** Automatización avanzada en Python  

---

### **ETAPA 2: Evaluar algoritmos de compresión**

**Algoritmos:**
- **Huffman:** Códigos de longitud variable eficientes para distribuciones sesgadas.  
- **Shannon-Fano:** Similar a Huffman, con otra construcción de árbol.  
- **Lempel-Ziv (LZ77):** Usa diccionario y codificación de longitud variable.  

**Métricas de eficiencia:**
- Tasa de compresión (Compression Ratio)  
- Longitud media del código (L)  
- Redundancia  
- Tiempos de codificación y decodificación  

**Otros factores:**
- Relación de compresión (tamaño comprimido vs. original)  
- Complejidad computacional  
- Implementación y facilidad de uso  

---

## 📊 Resultados Generados

- **Planillas de símbolos:** cantidad, probabilidad, entropía, información mutua  
- **Reportes de codificación:** longitud promedio, eficiencia y tamaño de salida  
- **Archivo de promedios:** resumen general con las métricas de todos los archivos procesados  

---

## 💡 Recomendaciones

- Usar archivos en **codificación UTF-8**  
- Mantener las carpetas `codificado/`, `decodificado/` y `planillas/` limpias antes de cada ejecución  
- Revisar los reportes Excel para comparar resultados entre algoritmos  
