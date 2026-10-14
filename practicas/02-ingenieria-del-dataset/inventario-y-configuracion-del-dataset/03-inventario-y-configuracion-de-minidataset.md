# 📋 Inventario y configuración del minidataset

En la práctica anterior exploramos la estructura de un dataset de segmentación, identificamos sus componentes y aprendimos a localizar imágenes, máscaras y archivos de anotaciones.

Ahora utilizaremos esos conocimientos para construir un **inventario estructurado (*manifest*)** a partir de una versión reducida y reorganizada del Oxford-IIIT Pet Dataset.

El objetivo es reunir en un solo archivo la información necesaria para identificar y localizar las muestras del dataset, recuperar sus metadatos y verificar que las imágenes y sus anotaciones sean consistentes.

También crearemos un **archivo de configuración** que permita centralizar las rutas del proyecto, facilitando su mantenimiento y utilización en las siguientes etapas del taller.

---

## 🎯 Objetivo

Construir un *manifest* que registre las imágenes, máscaras y anotaciones de un minidataset de Oxford-IIIT Pet, incorporando información de identificación, clasificación, dimensiones y regiones de interés.

Además, crear un archivo de configuración que centralice las rutas necesarias para acceder a los datos y al inventario generado.

---

## 📦 Repositorio de la práctica

Los archivos necesarios para realizar esta actividad se encuentran en el siguiente repositorio:

[**🐱🐶 Acceder al repositorio de Inventario y configuración del dataset →**](https://github.com/bettypau-open-knowledge/del-dataset-a-unet_inventario-y-configuracion-minidataset)

El repositorio contiene:

- El **minidataset didáctico**, con fotografías, máscaras de segmentación y anotaciones XML.
- El archivo `list.txt`, con información de clasificación de las muestras.
- El notebook `inventario.ipynb`, donde se desarrolla la práctica.
- Un `README.md` con información adicional sobre el proyecto.

> [!IMPORTANT]
> Esta práctica utiliza una selección reducida y reorganizada del Oxford-IIIT Pet Dataset original.
>
> Su propósito es comprender y aplicar el proceso de construcción de un inventario, no generar un conjunto de datos representativo para entrenar o evaluar modelos.

---

## 📁 Organización del proyecto

El proyecto utiliza la siguiente estructura de directorios:

```text
proyecto/
├── config/
│   └── dataset.json
├── data/
│   ├── raw/
│   │   ├── list.txt
│   │   └── images/
│   │       ├── Abyssinian/
│   │       │   ├── Abyssinian_1.jpg
│   │       │   ├── Abyssinian_1.png
│   │       │   └── Abyssinian_1.xml
│   │       └── ...
│   └── manifests/
│       └── manifest.csv
└── notebooks/
    └── inventario.ipynb
```

Los archivos originales se encuentran en `data/raw/`, mientras que los directorios `config/` y `data/manifest/` contienen los resultados generados durante la práctica.

> [!NOTE]
> Los nombres de imágenes y categorías mostrados son ilustrativos.
>
> Algunos archivos y directorios se crearán durante la ejecución del notebook.

---

## 💻 Instrucciones

### 1 · Prepara el proyecto

Accede al repositorio de la práctica y descarga o clona su contenido.

Si trabajarás localmente, abre el proyecto en Visual Studio Code y selecciona el entorno de Python del taller.

Si utilizarás Google Colab, prepara el notebook y el acceso a los archivos del proyecto de acuerdo con las instrucciones del repositorio.

### 2 · Abre el notebook

Localiza el archivo:

```text
notebooks/inventario.ipynb
```

Abre el notebook y ejecuta las celdas progresivamente, siguiendo las instrucciones y observaciones de cada sección.

> [!IMPORTANT]
> Comprueba el directorio de trabajo del kernel antes de ejecutar el notebook.
>
> Las rutas relativas utilizadas en el código dependen de la ubicación desde la que se ejecuta Python.

---

## 🧪 Actividades de la práctica

### 1 · Exploración de la estructura del proyecto

Comenzaremos identificando la organización de los directorios y estableciendo las rutas necesarias para acceder a los archivos.

Utilizaremos `pathlib` para explorar el proyecto y localizar los componentes del minidataset.

### 2 · Recuperación de etiquetas de clasificación

Leeremos el archivo `list.txt` para recuperar los identificadores de clasificación asociados con cada muestra.

Entre ellos se encuentran:

| Campo | Descripción |
|---|---|
| `class_id` | Identificador de la categoría, entre 1 y 37. |
| `species_id` | Identificador de la especie: `1` para gato y `2` para perro. |
| `breed_id` | Identificador de la raza dentro de cada especie. |

Esta información permitirá complementar los registros del inventario.

### 3 · Verificación de imágenes y máscaras

Antes de incorporar una muestra al inventario, comprobaremos que sus archivos existen y pueden leerse correctamente.

También verificaremos las dimensiones de las fotografías y sus máscaras para identificar posibles inconsistencias.

### 4 · Lectura y validación de anotaciones XML

Utilizaremos `xml.etree.ElementTree` para recuperar información de las anotaciones individuales.

En particular, identificaremos las coordenadas del *bounding box* de la cabeza del animal y comprobaremos que sean consistentes con las dimensiones de la fotografía.

### 5 · Construcción del manifest

Integraremos la información recuperada en registros estructurados que describan cada muestra.

El procedimiento permitirá identificar las muestras válidas y separar aquellas que presenten errores durante la validación.

### 6 · Exportación del inventario

Utilizaremos `pandas` para construir un DataFrame con los registros válidos y exportarlo a un archivo CSV.

El resultado será un inventario que podrá consultarse sin necesidad de recorrer nuevamente todos los directorios del dataset.

### 7 · Creación del archivo de configuración

Finalmente, construiremos un archivo JSON que centralice las rutas del dataset y del inventario generado.

Comprobaremos que la configuración pueda leerse correctamente y que las rutas recuperadas permitan localizar los archivos correspondientes.

---

## 📋 Resultado 1 · Manifest del dataset

El primer resultado de la práctica será un archivo CSV que contenga un inventario estructurado de las muestras válidas.

Cada registro incluirá:

| Campo | Descripción |
|---|---|
| `image_id` | Identificador de la imagen. |
| `breed` | Nombre de la raza. |
| `class_id` | Identificador de clase. |
| `species_id` | Identificador numérico de la especie. |
| `species` | Nombre de la especie. |
| `breed_id` | Identificador de raza dentro de la especie. |
| `image_path` | Ruta relativa de la fotografía. |
| `mask_path` | Ruta relativa de la máscara. |
| `xml_path` | Ruta relativa de la anotación XML. |
| `width` | Ancho de la imagen en píxeles. |
| `height` | Alto de la imagen en píxeles. |
| `xmin`, `ymin` | Coordenadas iniciales del *bounding box*. |
| `xmax`, `ymax` | Coordenadas finales del *bounding box*. |

El inventario permitirá consultar las características de las muestras y localizar sus archivos a partir de una estructura tabular.

> [!NOTE]
> El notebook también permite identificar registros que presentan errores de validación.
>
> Estos registros se separan del inventario de muestras válidas para facilitar su revisión.

---

## ⚙️ Resultado 2 · Archivo de configuración

El segundo resultado será el archivo:

```text
config/dataset.json
```

Su propósito es centralizar la información necesaria para localizar el dataset y el manifest.

Por ejemplo, una configuración puede contener:

```json
{
    "dataset": {
        "name": "oxford-iiit-pet-mini",
        "root": "data/raw",
        "images": "images",
        "labels": "list.txt"
    },
    "manifest": {
        "path": "data/manifests/manifest.csv"
    }
}
```

De esta manera, otros notebooks y scripts podrán consultar la ubicación de los archivos desde una configuración común.

> [!TIP]
> Recuerda que el archivo de configuración no es indispensable para ejecutar un proyecto.
>
> Su utilidad aumenta cuando diferentes notebooks, scripts o experimentos necesitan acceder a las mismas rutas.

---

## 🤔 Observa e interpreta

Al finalizar la práctica, reflexiona sobre las siguientes preguntas:

1. ¿Qué información proporciona el manifest que no resulta tan fácil consultar directamente desde los directorios?
2. ¿Por qué es importante verificar la correspondencia entre imágenes y máscaras?
3. ¿Qué sucede cuando una fotografía tiene dimensiones diferentes a las de su máscara?
4. ¿Por qué es necesario validar las coordenadas de un *bounding box*?
5. ¿Qué ventajas tiene almacenar rutas relativas en el manifest?
6. ¿Qué utilidad tiene separar la configuración del código de los notebooks?
7. ¿Cómo podría aprovecharse el manifest durante las siguientes etapas de procesamiento del dataset?

---

## ✅ Punto de control

Al finalizar esta práctica habrás:

- Recuperado etiquetas y metadatos del minidataset.
- Verificado la existencia y dimensiones de imágenes y máscaras.
- Leído y validado anotaciones XML.
- Construido un inventario estructurado mediante `pandas`.
- Exportado los registros válidos a un archivo CSV.
- Identificado muestras con errores de validación.
- Creado un archivo JSON para centralizar las rutas del proyecto.
- Comprobado la lectura de la configuración.

---

## 📚 Dataset de referencia

Esta práctica utiliza una versión reducida y reorganizada del **Oxford-IIIT Pet Dataset**.

**Referencia:**

Parkhi, O. M., Vedaldi, A., Zisserman, A., & Jawahar, C. V. (2012).

*Cats and Dogs.*

IEEE Conference on Computer Vision and Pattern Recognition (CVPR).

[Consultar el dataset original →](https://www.robots.ox.ac.uk/~vgg/data/pets/)

---

[← Volver a Inventario y configuración del dataset](../../../modulos/02-ingenieria-del-dataset/02-02-inventario-y-configuracion-del-dataset.md)