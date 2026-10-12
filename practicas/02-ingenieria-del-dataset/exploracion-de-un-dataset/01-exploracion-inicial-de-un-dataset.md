# 🔎 Exploración inicial de un dataset de segmentación

Antes de procesar imágenes o entrenar un modelo, es necesario conocer la organización de los datos, identificar los archivos disponibles y comprender cómo se relacionan las imágenes con sus anotaciones.

En esta práctica utilizaremos un **minidataset didáctico derivado del Oxford-IIIT Pet Dataset** para explorar su estructura de directorios, consultar metadatos y visualizar fotografías, máscaras de segmentación y regiones de interés.

La actividad se desarrolla en el repositorio [`del-dataset-a-unet_exploracion-inicial-datasets`](https://github.com/bettypau-open-knowledge/del-dataset-a-unet_exploracion-inicial-datasets) y puede ejecutarse tanto en un entorno local como en Google Colab.

---

## 🎯 Objetivo

Explorar la estructura y los componentes de un dataset de segmentación mediante herramientas de Python, identificando archivos, rutas, metadatos y anotaciones espaciales para comprender cómo se organiza la información que posteriormente utilizará un modelo de Deep Learning.

---

## 📁 Organización del proyecto

El notebook utiliza las siguientes ubicaciones dentro del repositorio:

```text
ejercicio_exploracion_dataset/
├── data/
│   └── raw/
│       ├── anotaciones.json
│       └── images/
│           ├── Chihuahua/
│           │   ├── Chihuahua_190.jpg
│           │   ├── Chihuahua_190.png
│           │   └── Chihuahua_190.xml
│           └── ...
└── notebooks/
    └── explorar_data.ipynb
```

Los archivos del minidataset se encuentran en `data/raw/`.

Cada categoría cuenta con su propio directorio, dentro del cual se almacenan conjuntamente las fotografías, máscaras y anotaciones individuales.

> [!NOTE]
> El minidataset contiene únicamente una pequeña selección de imágenes del Oxford-IIIT Pet Dataset original, reorganizada con fines didácticos. No representa el conjunto completo de datos.

---

## 💻 Requisitos

Para ejecutar la práctica se utilizan las siguientes bibliotecas:

| Biblioteca | Uso |
|---|---|
| `pathlib` | Construcción y exploración de rutas |
| `json` | Lectura de metadatos JSON |
| `xml.etree.ElementTree` | Lectura de anotaciones XML |
| `numpy` | Inspección de valores numéricos |
| `opencv-python` (`cv2`) | Lectura y procesamiento de imágenes |
| `matplotlib` | Visualización de imágenes y anotaciones |

También necesitarás un entorno compatible con Jupyter Notebooks.

---

## 🚀 Ejecución de la práctica

### Opción A · Google Colab

1. Abre el notebook [`explorar_data.ipynb`](https://github.com/bettypau-open-knowledge/del-dataset-a-unet_exploracion-inicial-datasets/blob/main/notebooks/explorar_data.ipynb) en Visual Studio Code.
2. Selecciona un runtime de Google Colab **únicamente con CPU** como kernel.
3. Ejecuta las primeras celdas para identificar el entorno.
4. El notebook clonará o actualizará el repositorio desde GitHub.
5. Continúa ejecutando las celdas en el orden indicado.

El repositorio utilizado es:

[**Ver repositorio en GitHub →**](https://github.com/bettypau-open-knowledge/del-dataset-a-unet_exploracion-inicial-datasets)

### Opción B · Entorno local

1. Clona el repositorio:

   ```bash
   git clone git@github.com:bettypau-open-knowledge/del-dataset-a-unet_exploracion-inicial-datasets.git
   ```

2. Abre la carpeta del proyecto en Visual Studio Code.
3. Prepara un entorno de Python con las bibliotecas necesarias.
4. Abre `notebooks/explorar_data.ipynb`.
5. Selecciona el kernel de tu entorno local.
6. Ejecuta las celdas progresivamente.

> [!IMPORTANT]
> Para la ejecución local, el notebook establece la ruta del proyecto mediante `Path("..")`. Por ello, comprueba que el directorio de trabajo del kernel sea `notebooks/`, de modo que `..` corresponda a la raíz del repositorio.

---

## 🧪 Actividades de exploración

### 1 · Exploración del árbol de archivos

Identificarás el directorio del proyecto y explorarás su estructura utilizando `pathlib`.

Compararás la exploración de un solo nivel de directorios con una exploración recursiva del árbol completo.

### 2 · Localización de archivos

Utilizarás `Path.rglob()` para buscar archivos por extensión y reconocer la ubicación de las fotografías y máscaras del minidataset.

### 3 · Exploración de metadatos JSON

Abrirás el archivo `anotaciones.json` y examinarás su estructura mediante una función que permite representar jerárquicamente diccionarios y listas.

### 4 · Exploración de anotaciones XML

Seleccionarás una muestra y consultarás su archivo XML para identificar información como la clase, las dimensiones de la imagen y las coordenadas del *bounding box* de la cabeza del animal.

### 5 · Visualización de imágenes y máscaras

Cargarás una fotografía y su máscara correspondiente utilizando OpenCV.

Examinarás sus dimensiones, tipos de datos y valores numéricos, y visualizarás ambos archivos mediante Matplotlib.

### 6 · Visualización de anotaciones espaciales

Generarás una superposición de la máscara sobre la fotografía y representarás el *bounding box* de la cabeza del animal.

Esto permitirá distinguir visualmente entre una **máscara de segmentación a nivel de píxel** y una **región delimitada por un rectángulo**.

---

## 🤔 Observa e interpreta

Durante la práctica, reflexiona sobre las siguientes preguntas:

- ¿Cómo están organizadas las muestras dentro del dataset?
- ¿Qué relación existe entre los archivos `.jpg`, `.png` y `.xml`?
- ¿Qué información proporciona `anotaciones.json`?
- ¿Qué diferencias existen entre los metadatos JSON y XML?
- ¿Por qué es importante revisar las dimensiones y los valores de las máscaras?
- ¿Qué información representa una máscara de segmentación y cuál representa un *bounding box*?

---

## ✅ Punto de control

Al finalizar esta práctica habrás:

- explorado la estructura de un dataset mediante `pathlib`;
- localizado archivos mediante búsquedas recursivas;
- consultado información almacenada en JSON y XML;
- construido rutas para acceder a imágenes y anotaciones;
- inspeccionado dimensiones, tipos de datos y valores de imágenes;
- visualizado fotografías y máscaras de segmentación;
- superpuesto una máscara sobre su imagen correspondiente;
- representado gráficamente un *bounding box*.

---

## 📚 Dataset de referencia

**Oxford-IIIT Pet Dataset**

Parkhi, O. M., Vedaldi, A., Zisserman, A., & Jawahar, C. V. (2012). *Cats and Dogs*. IEEE Conference on Computer Vision and Pattern Recognition (CVPR).

[Consultar el dataset original →](https://www.robots.ox.ac.uk/~vgg/data/pets/)

El conjunto de imágenes utilizado en esta práctica es una selección reducida y reorganizada con fines didácticos. Su utilización debe respetar las condiciones de uso de las imágenes del dataset original.

---

[← Volver a Exploración de un dataset de segmentación](../../../modulos/02-ingenieria-del-dataset/02-01-exploracion-de-un-dataset.md)
