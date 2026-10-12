# 🐱🐶 Exploración inicial del Oxford-IIIT Pet Dataset

En la práctica anterior, [**Exploración inicial de un dataset de segmentación**](./01-exploracion-inicial-de-un-dataset), trabajamos con una versión reducida y reorganizada del Oxford-IIIT Pet Dataset.

A través de ese ejercicio aprendimos a explorar directorios, localizar archivos mediante `pathlib`, consultar anotaciones JSON y XML, visualizar fotografías y máscaras de segmentación, y representar regiones de interés mediante *bounding boxes*.

Ahora trasladaremos esos conocimientos al **Oxford-IIIT Pet Dataset original**, que contiene miles de imágenes y utiliza una organización de archivos diferente.

El propósito de esta actividad es reconocer esas diferencias y adaptar las herramientas de exploración a un conjunto de datos real.

---

## 🎯 Objetivo

Aplicar las técnicas de exploración de archivos, lectura de metadatos y visualización de anotaciones al Oxford-IIIT Pet Dataset completo, identificando su estructura original y las relaciones entre sus componentes.

---

## 💻 Instrucciones

Para esta práctica necesitarás:

- El [entorno de Python del taller](../00-environment-taller.md), si trabajarás localmente.
- Visual Studio Code con soporte para Jupyter Notebooks y Google Colab.
- Acceso a Internet para descargar el dataset.
- El notebook utilizado en la práctica anterior como referencia.

> [!IMPORTANT]
> Esta práctica utiliza el **dataset original**, no el minidataset de la actividad anterior.
>
> No es necesario modificar los archivos originales. La exploración se realizará mediante código Python.

---

### 1 · Descarga el Oxford-IIIT Pet Dataset

Accede a la página oficial:

[**Oxford-IIIT Pet Dataset →**](https://www.robots.ox.ac.uk/~vgg/data/pets/)

En la sección de descargas, utiliza los enlaces **HTTP** para obtener:

1. **Dataset images:** fotografías de perros y gatos (**images.tar.gz (dataset)**).
2. **Ground truth data:** máscaras de segmentación, anotaciones XML y archivos de información (**annotations.tar.gz (groundtruth data)**).

Descarga ambos archivos comprimidos y extrae su contenido.

Organiza los archivos de manera que las carpetas `images` y `annotations` queden dentro de un mismo directorio llamado `oxford-iiit-pet`.

La estructura resultante deberá ser:

```text
oxford-iiit-pet/
├── annotations/
│   ├── trimaps/
│   ├── xmls/
│   ├── list.txt
│   ├── trainval.txt
│   └── test.txt
└── images/
    ├── Abyssinian_1.jpg
    ├── Abyssinian_2.jpg
    ├── ...
    └── ...
```

> [!NOTE]
> El contenido anterior muestra la estructura general del dataset.
> Las carpetas incluyen muchos más archivos de los que aparecen en el ejemplo.

**Si trabajarás localmente:**

Guarda el dataset en una ubicación permanente de tu computadora, por ejemplo:

```text
Data/
└── oxford-iiit-pet/
    ├── annotations/
    └── images/
```

**Si trabajarás en Google Colab:**

Sube la carpeta completa `oxford-iiit-pet` a tu Google Drive.

Por ejemplo:

```text
Mi unidad/
└── Datasets/
    └── oxford-iiit-pet/
        ├── annotations/
        └── images/
```

> [!IMPORTANT]
> Asegúrate de que ambas carpetas, `images` y `annotations`, se encuentren dentro de `oxford-iiit-pet` antes de continuar.

---

### 2 · Crea un directorio para el proyecto

Dentro de la ubicación donde guardas tus proyectos del taller, crea una carpeta para esta actividad.

Por ejemplo:

```text
exploracion_oxford_pet/
```

Abre esa carpeta como proyecto en Visual Studio Code.

La idea es mantener separados los **archivos de código** y el **dataset original**.

---

### 3 · Agrega el directorio `data`

Dentro del proyecto, crea una carpeta llamada:

```text
data/
```

Este directorio se utilizará para organizar las referencias a los datos que emplearemos.

---

### 4 · Agrega el subdirectorio `raw`

Dentro de `data`, crea una carpeta llamada `raw`.

Tu proyecto deberá tener inicialmente la siguiente estructura:

```text
exploracion_oxford_pet/
└── data/
    └── raw/
```

El directorio `raw` se utilizará para acceder a los datos originales, sin modificarlos.

---

### 5 · Configura el acceso al dataset

La forma de acceder al dataset dependerá de dónde ejecutes el código.

#### 🖥️ Opción A · Ejecución local (macOS o Linux)

Para evitar duplicar el dataset dentro de cada proyecto, utilizaremos un **enlace simbólico**.

Un enlace simbólico permite acceder a un archivo o directorio desde otra ubicación sin copiar su contenido.

Abre la terminal de Visual Studio Code y sitúate en la raíz de tu proyecto.

La sintaxis general es:

```bash
ln -s "RUTA_ORIGINAL" "RUTA_DEL_ENLACE"
```

Por ejemplo, si el dataset se encuentra en:

```text
/Users/usuario/Data/oxford-iiit-pet
```

Ejecuta:

```bash
ln -s "/Users/usuario/Data/oxford-iiit-pet" "./data/raw/oxford-iiit-pet"
```

Después, el proyecto tendrá esta estructura:

```text
exploracion_oxford_pet/
└── data/
    └── raw/
        └── oxford-iiit-pet/  →  /Users/usuario/Data/oxford-iiit-pet
```

Aunque el directorio aparece dentro del proyecto, los archivos permanecen almacenados en su ubicación original.

> [!IMPORTANT]
> Sustituye `/Users/usuario/Data/oxford-iiit-pet` por la ruta real donde guardaste el dataset.
>
> El directorio `data/raw` debe existir antes de crear el enlace.

#### 🪟 Opción B · Ejecución local (Windows)

En Windows utilizaremos una **unión de directorios** (*junction*), que permite acceder a una carpeta desde otra ubicación sin duplicar sus archivos.

Abre la terminal PowerShell de Visual Studio Code y sitúate en la raíz del proyecto.

La sintaxis general es:

```powershell
New-Item -ItemType Junction -Path "RUTA_DEL_ENLACE" -Target "RUTA_ORIGINAL"
```

Por ejemplo, si el dataset está almacenado en:

```text
D:\Datasets\oxford-iiit-pet
```

Ejecuta:

```powershell
New-Item -ItemType Junction -Path ".\data\raw\oxford-iiit-pet" -Target "D:\Datasets\oxford-iiit-pet"
```

También puedes utilizar el comando `mklink` mediante CMD:

```powershell
cmd /c mklink /J ".\data\raw\oxford-iiit-pet" "D:\Datasets\oxford-iiit-pet"
```

Utiliza **solo una de las dos alternativas**.

El resultado será equivalente:

```text
exploracion_oxford_pet/
└── data/
    └── raw/
        └── oxford-iiit-pet/  →  D:\Datasets\oxford-iiit-pet
```

> [!NOTE]
> Una unión de directorios no crea una copia del dataset.
>
> Si modificas los archivos a través de la unión, estarás modificando los archivos originales. Por ello, evita sobrescribir las imágenes y anotaciones.

#### ☁️ Opción C · Ejecución en Google Colab

Si utilizarás Google Colab, no necesitas crear enlaces simbólicos en tu computadora.

En su lugar, conecta tu Google Drive al notebook:

```python
from google.colab import drive

drive.mount("/content/drive")
```

Después, identifica la ruta del dataset dentro de Drive.

Por ejemplo:

```python
from pathlib import Path

DATASET = Path("/content/drive/MyDrive/Datasets/oxford-iiit-pet")
```

Comprueba que la ruta existe:

```python
print(DATASET.exists())
```

El resultado esperado es:

```text
True
```

> [!IMPORTANT]
> La ruta anterior es un ejemplo.
>
> Debes ajustarla de acuerdo con la ubicación donde guardaste el dataset en tu Google Drive.

---

### 6 · Realiza la exploración del dataset

Ahora que tienes acceso a los archivos, retoma el notebook de la práctica **Exploración inicial de un dataset de segmentación**.

Utilízalo como referencia para construir un nuevo notebook y adaptar los ejercicios al dataset original.

#### 6.1 · Identifica la estructura de directorios

Utiliza `pathlib` para explorar la organización de `oxford-iiit-pet`.

Observa las diferencias entre la estructura del minidataset y la estructura del dataset original.

Identifica dónde se encuentran:

- Las fotografías.
- Las máscaras de segmentación.
- Las anotaciones XML.
- Los archivos de texto con información del dataset.

#### 6.2 · Localiza los archivos

Utiliza `glob()` o `rglob()` para identificar los archivos de interés.

Explora las extensiones:

```text
.jpg
.png
.xml
.txt
```

Comprueba en qué directorios se encuentra cada tipo de archivo.

#### 6.3 · Explora los archivos de anotaciones

En el minidataset utilizamos un archivo `anotaciones.json` para consultar metadatos.

En el dataset original, la información se distribuye de otra manera.

Localiza y explora:

```text
annotations/list.txt
annotations/trainval.txt
annotations/test.txt
annotations/xmls/
```

Consulta la documentación original para comprender el significado de los identificadores y los archivos de anotación.

> [!NOTE]
> No todos los datasets proporcionan archivos JSON.
>
> Parte del trabajo de exploración consiste en reconocer los formatos disponibles y adaptar las herramientas de lectura a ellos.

#### 6.4 · Selecciona una imagen

Elige una fotografía del directorio `images`.

Identifica su nombre y localiza la máscara correspondiente dentro de:

```text
annotations/trimaps/
```

Comprueba cómo se relacionan ambos archivos.

Después, busca si existe una anotación XML correspondiente a la imagen seleccionada.

> [!IMPORTANT]
> No asumas que todas las fotografías tienen necesariamente un archivo XML disponible.
>
> Comprueba la existencia de cada anotación antes de intentar abrirla.

#### 6.5 · Visualiza la fotografía y su máscara

Utiliza OpenCV y Matplotlib para:

1. Cargar la fotografía seleccionada.
2. Cargar su máscara de segmentación.
3. Consultar sus dimensiones.
4. Identificar los valores presentes en la máscara.
5. Mostrar ambos archivos.
6. Generar una visualización con la máscara superpuesta sobre la fotografía.

Recuerda que las máscaras del Oxford-IIIT Pet Dataset utilizan la siguiente convención:

| Valor | Significado |
|:---:|---|
| `1` | Primer plano (*foreground*) |
| `2` | Fondo (*background*) |
| `3` | Región no clasificada (*not classified*) |

#### 6.6 · Explora el bounding box

Si la imagen seleccionada cuenta con una anotación XML:

1. Abre el archivo mediante `xml.etree.ElementTree`.
2. Identifica las dimensiones de la imagen.
3. Localiza las coordenadas del *bounding box*.
4. Representa el rectángulo sobre la fotografía.

Compara visualmente el *bounding box* con la máscara de segmentación.

---

## 🤔 Observa e interpreta

Al finalizar la exploración, responde:

1. ¿Qué diferencias encontraste entre la organización del minidataset y la del Oxford-IIIT Pet Dataset original?
2. ¿Cómo se relacionan las fotografías con sus máscaras?
3. ¿Qué información proporciona `list.txt`?
4. ¿Cuál es la función de `trainval.txt` y `test.txt`?
5. ¿Qué ventajas tiene mantener el dataset original fuera del directorio del proyecto?
6. ¿Qué cambios tuviste que realizar al código de la práctica anterior?
7. ¿Por qué es importante conocer la estructura de un dataset antes de procesarlo?

---

## ✅ Punto de control

Al finalizar esta práctica habrás:

- descargado y organizado el Oxford-IIIT Pet Dataset original;
- creado una estructura básica de proyecto;
- configurado el acceso a los datos mediante enlaces locales o Google Drive;
- explorado los directorios del dataset utilizando `pathlib`;
- identificado fotografías, máscaras y archivos de anotación;
- consultado los metadatos disponibles;
- visualizado una fotografía y su máscara correspondiente;
- representado un *bounding box* cuando la anotación esté disponible;
- adaptado un procedimiento de exploración a una organización de datos diferente.

---

## 📚 Referencia

**Oxford-IIIT Pet Dataset**

Parkhi, O. M., Vedaldi, A., Zisserman, A., & Jawahar, C. V. (2012).

[*Cats and Dogs.*](https://www.robots.ox.ac.uk/~vgg/publications/2012/parkhi12a/parkhi12a.pdf)

IEEE Conference on Computer Vision and Pattern Recognition (CVPR).

[Consultar el dataset original →](https://www.robots.ox.ac.uk/~vgg/data/pets/)

---

[← Volver a Exploración de un dataset de segmentación](../../../modulos/02-ingenieria-del-dataset/02-01-exploracion-de-un-dataset.md)