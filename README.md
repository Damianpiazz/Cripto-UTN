# Criptografia-Modular

## Storytelling y Contexto Histórico

Los sumergibles Tipo VII alemanes, desplazaban en inmersión 871 toneladas, con 66.6 metros de eslora y 6.2 metros de manga. Se sumergían hasta 280 metros y estaban armados con 5 tubos lanzatorpedos de 533 mm, cargando 14 torpedos o 39 minas. Contaban con cañones de cubierta y antiaéreos, motores diésel de 2800-3200 cv y motores eléctricos de 750 cv, alcanzando 17.7 nudos en superficie y 7.6 nudos sumergidos. Con 707 unidades construidas entre 1936 y 1944, el Tipo VII fue clave en la Kriegsmarine alemana en el Atlántico Norte.

Era un atardecer de septiembre de 1942, cuando el sumergible U-573 navegaba en superficie y fue sorprendido por un avión de la Royal Air Force. Tras una inmersión apresurada y daños parciales, logró evadir al atacante y enviar un mensaje encriptado de emergencia solicitando ayuda. Este mensaje, interceptado por fuerzas aliadas, debía ser descifrado rápidamente para evitar la pérdida de información crítica.

El servicio de inteligencia inglés pudo capturar documentación útil que facilita el descifrado. La misión: analizar y descifrar el mensaje antes de que venza su plazo de vigencia.

## Requisitos

* Python 3.9 o superior
* Archivo `requirements.txt` con las dependencias del proyecto

## Instalación y Entorno Virtual

1. Crear un entorno virtual:

### Windows (CMD)

```
python -m venv venv
venv\Scripts\activate.bat
```

### Windows (PowerShell)

```
python -m venv venv
venv\Scripts\Activate.ps1
```

### Linux / macOS

```
python3 -m venv venv
source venv/bin/activate
```

2. Instalar dependencias desde `requirements.txt`:

```
pip install -r requirements.txt
```

## Configuración

El archivo `config.json` debe contener:

```json
{
  "tabla": { "0": "9", "1": "8", ... },
  "b": 375839,
  "datos_descubiertos": { "H": "'", "S": "Ñ", "P": "3" },
  "mensaje_encriptado": "BYC2YC1'V#J1RKQ1 Y#1QÑ VC13.V6YZ2V1Q#1QZU.J3 .2V11"
}
```

Opcionalmente se puede agregar una semilla:

```json
"semilla": 7
```

## Ejecución

Activar el entorno virtual y ejecutar el script principal pasando el archivo de configuración:

```
python main.py -c config.json
```

La salida mostrará:

* Tabla de símbolos utilizada
* Mensaje encriptado y desencriptado
* Semilla y su inverso multiplicativo (si se calculó)

## Tablas de Asignación de Símbolos Capturadas

```
A B C D E F G H I J K L M N Ñ  => 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
O P Q R S T U V W X Y Z ! @    => 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
# $ % * ( ) - + / & : ; , . ¿    => 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44
? "  ́ [ ] 0 1 2 3 4 5 6 7 8 9 => 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59
Á É Í Ó Ú °                        => 60 61 62 63 64 65
```

### Símbolos Descubiertos

| Símbolo Original | Encriptado |
| ---------------- | ---------- |
| U                | @          |
| S                | B          |
| P                | 8          |

### Fórmulas de Encriptación Detectadas

```
Y = a.X + 375600
Y = a.X + 375836
Y = a.X + 300050
```

## Mensaje de Emergencia Enviado por el U-573

```
Á U % K V  ́ A @ U @
  ́  ́ & @ V  ́ [ % U  ́
V B [ L S  ́ 8 T L N
% ] ; L  ́ V U  ́ V ]
Á T M 8 [ % ; L  ́  ́
```
