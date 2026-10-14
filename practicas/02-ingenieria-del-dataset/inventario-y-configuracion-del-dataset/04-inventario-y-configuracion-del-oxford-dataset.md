# 🐱🐶 Inventario y configuración del Oxford-IIIT Pet Dataset

En la práctica anterior construimos un **inventario estructurado (*manifest*)** a partir de un minidataset de Oxford-IIIT Pet. Para ello, recuperamos información de diferentes archivos, verificamos la consistencia de las imágenes y sus anotaciones, y organizamos los resultados en un archivo CSV.

También creamos un **archivo de configuración JSON** para centralizar las rutas del proyecto y facilitar el acceso a los datos.

Ahora aplicaremos estos conocimientos al **Oxford-IIIT Pet Dataset original**.

A diferencia del minidataset, las fotografías, máscaras y anotaciones se encuentran distribuidas en diferentes directorios. Además, trabajaremos con un conjunto de datos considerablemente mayor.

En esta ocasión, **no se proporcionará un repositorio ni un notebook con el procedimiento resuelto**. Deberás recuperar y adaptar las herramientas utilizadas en las prácticas anteriores para desarrollar tu propia solución.

---

## 🎯 Objetivo

Construir y validar un *manifest* del Oxford-IIIT Pet Dataset original, integrando información de identificación, clasificación, dimensiones y anotaciones espaciales.

Además, diseñar un archivo de configuración que permita localizar el dataset y el inventario generado mediante rutas centralizadas y reutilizables.

---

## 💻 Instrucciones

Para realizar esta actividad necesitarás:

- El Oxford-IIIT Pet Dataset original, descargado durante la práctica de exploración.
- El entorno de Python del taller, si trabajarás localmente.
- Visual Studio Code o Google Colab.
- Las prácticas anteriores como material de consulta.

> [!IMPORTANT]
> En esta actividad deberás construir tu propio notebook.
>
> Puedes consultar y reutilizar el código desarrollado anteriormente, pero tendrás que adaptarlo a la estructura y características del dataset original.
>
> **No modifiques ni sobrescribas los archivos originales del dataset.**

---

### 1 · Prepara la estructura del proyecto

Retoma el proyecto que utilizaste durante la práctica de exploración del Oxford-IIIT Pet Dataset original.

Organiza sus directorios para separar los datos originales, los archivos generados, la configuración y el código.

La estructura propuesta es:

```text
exploracion_oxford_pet/
├── config/
│   └── dataset.json
├── data/
│   ├── raw/
│   │   └── oxford-iiit-pet/
│   │       ├── annotations/
│   │       │   ├── trimaps/
│   │       │   ├── xmls/
│   │       │   ├── list.txt
│   │       │   ├── trainval.txt
│   │       │   └── test.txt
│   │       └── images/
│   └── manifest/
│       └── manifest.csv
└── notebooks/
    └── inventario_oxford_pet.ipynb
```

> [!NOTE]
> Si trabajas localmente, `data/raw/oxford-iiit-pet` puede ser un enlace simbólico o una unión de directorios (*junction*) que apunte a la ubicación original del dataset.
>
> Si trabajas en Google Colab, puedes acceder directamente a los archivos almacenados en Google Drive.
>
> Los archivos `manifest.csv` y `dataset.json` se generarán durante la práctica.

---

### 2 · Crea el notebook de trabajo

Dentro de `notebooks/`, crea un archivo llamado:

```text
inventario_oxford_pet.ipynb
```

Organiza el notebook en secciones que permitan distinguir las diferentes etapas del procedimiento.

Antes de comenzar, establece las rutas necesarias para acceder al dataset.

Comprueba que puedes localizar:

```text
images/
annotations/trimaps/
annotations/xmls/
annotations/list.txt
```

> [!TIP]
> Utiliza `pathlib` para construir y manipular las rutas.
>
> Evita escribir rutas absolutas repetidamente en diferentes celdas del notebook.

---

### 3 · Recupera la información de clasificación

En la práctica anterior utilizamos un archivo `list.txt` para recuperar los identificadores asociados con cada imagen.

El dataset original también proporciona esta información.

Localiza:

```text
annotations/list.txt
```

Consulta su contenido y recupera los siguientes campos:

| Campo | Descripción |
|---|---|
| `image_id` | Identificador de la imagen. |
| `class_id` | Identificador de la categoría, entre 1 y 37. |
| `species_id` | Identificador de la especie: `1` para gato y `2` para perro. |
| `breed_id` | Identificador de la raza dentro de la especie. |

Recuerda que los identificadores de raza utilizan rangos diferentes según la especie:

- Gatos: `1–25`.
- Perros: `1–12`.

A partir de esta información, prepara una estructura que permita consultar las etiquetas correspondientes a cada imagen.

**Considera:** ¿cómo relacionarás los registros de `list.txt` con las fotografías almacenadas en `images/`?

---

### 4 · Localiza las imágenes y sus máscaras

En el minidataset, las fotografías y máscaras se encontraban dentro del mismo directorio.

En el dataset original se almacenan por separado:

```text
oxford-iiit-pet/
├── images/
│   └── Abyssinian_1.jpg
└── annotations/
    └── trimaps/
        └── Abyssinian_1.png
```

Utiliza `pathlib` para recorrer las fotografías y construir las rutas de sus máscaras correspondientes.

Para cada muestra, verifica:

1. Que la fotografía exista y pueda leerse.
2. Que exista una máscara asociada.
3. Que la máscara pueda leerse correctamente.
4. Que ambas tengan dimensiones espaciales compatibles.

> [!IMPORTANT]
> No asumas que todos los archivos están completos o son válidos.
>
> El propósito de las verificaciones es identificar posibles inconsistencias antes de incorporar las muestras al inventario.

---

### 5 · Recupera las anotaciones XML

Los archivos XML se encuentran en:

```text
annotations/xmls/
```

Estos archivos contienen información descriptiva y anotaciones de la región de la cabeza del animal.

Para las muestras que cuenten con un XML, recupera:

- Dimensiones de la imagen.
- Coordenadas `xmin` y `ymin`.
- Coordenadas `xmax` y `ymax`.

Comprueba que las coordenadas sean válidas y correspondan a una región dentro de la imagen.

**Considera:** ¿qué harás cuando una fotografía no tenga un archivo XML asociado?

> [!NOTE]
> No todas las fotografías del Oxford-IIIT Pet Dataset original cuentan con anotaciones XML.
>
> Por ello, tu procedimiento debe contemplar la ausencia de estos archivos sin interrumpir la construcción del inventario.

---

### 6 · Construye los registros del manifest

Integra la información recuperada en una estructura que permita representar cada muestra mediante un registro.

Como punto de partida, utiliza los siguientes campos:

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
| `xml_path` | Ruta relativa de la anotación XML, cuando exista. |
| `width` | Ancho de la imagen en píxeles. |
| `height` | Alto de la imagen en píxeles. |
| `xmin`, `ymin` | Coordenadas iniciales del *bounding box*, cuando exista. |
| `xmax`, `ymax` | Coordenadas finales del *bounding box*, cuando exista. |

Puedes incorporar otros campos si consideras que aportan información útil para el proyecto.

> [!IMPORTANT]
> **Distingue entre una muestra inválida y una anotación opcional ausente.**
>
> Una fotografía que no tiene máscara o cuya máscara no puede leerse presenta un problema para una tarea de segmentación supervisada.
>
> En cambio, la ausencia de un XML no implica necesariamente que la fotografía y su máscara sean inválidas.
>
> Define cómo representarás los valores faltantes de las anotaciones XML sin descartar automáticamente esas muestras.

---

### 7 · Valida los registros

Antes de generar el inventario definitivo, establece un procedimiento para verificar la consistencia de cada registro.

Como mínimo, considera:

- Existencia y lectura de la fotografía.
- Existencia y lectura de la máscara.
- Compatibilidad de dimensiones entre fotografía y máscara.
- Disponibilidad de los identificadores de clasificación.
- Validez de las coordenadas del *bounding box*, cuando exista una anotación XML.

Separa los registros que cumplan los criterios definidos de aquellos que presenten problemas.

Para los registros con errores, conserva información que permita identificar la muestra y la causa del problema.

**Considera:** ¿qué información necesitarías guardar para poder revisar posteriormente una muestra inválida?

---

### 8 · Genera el manifest

Utiliza `pandas` para construir un DataFrame con los registros válidos.

Explora su contenido y comprueba:

1. El número de muestras registradas.
2. Los nombres y tipos de datos de las columnas.
3. La presencia de valores faltantes.
4. La correspondencia entre las rutas registradas y los archivos originales.

Después, exporta el inventario a:

```text
data/manifest/manifest.csv
```

> [!TIP]
> Antes de exportar, comprueba que las rutas de las fotografías, máscaras y anotaciones sean consistentes.
>
> Siempre que sea posible, utiliza rutas relativas a una ubicación conocida del proyecto o del dataset.

---

### 9 · Crea el archivo de configuración

Crea un archivo llamado:

```text
config/dataset.json
```

Este archivo deberá centralizar la información necesaria para localizar:

- El dataset original.
- El directorio de fotografías.
- El directorio de máscaras.
- El directorio de anotaciones XML.
- El archivo de etiquetas.
- El manifest generado.

Diseña una estructura JSON que permita recuperar estas rutas de forma clara.

> [!NOTE]
> No es necesario utilizar exactamente la misma estructura del archivo de configuración del minidataset.
>
> Puedes adaptarla a las características del dataset original, siempre que sea consistente y fácil de interpretar.

---

### 10 · Comprueba la configuración

Una vez generado `dataset.json`, vuelve a leerlo desde Python.

Utiliza la información almacenada para recuperar la ubicación del manifest.

Después:

1. Carga `manifest.csv` mediante `pandas`.
2. Selecciona una muestra del inventario.
3. Recupera las rutas de su fotografía y máscara.
4. Comprueba que ambos archivos existen.
5. Visualiza la fotografía y su máscara mediante Matplotlib.

> [!IMPORTANT]
> Para esta comprobación, utiliza las rutas recuperadas desde la configuración y el manifest.
>
> Evita escribir manualmente las rutas completas de la muestra seleccionada.

---

## 🤔 Observa e interpreta

Al finalizar la práctica, responde las siguientes preguntas:

1. ¿Qué modificaciones fueron necesarias para trasladar el procedimiento del minidataset al dataset original?
2. ¿Cómo influye la organización de los directorios en la construcción del manifest?
3. ¿Por qué no conviene descartar automáticamente las muestras que carecen de anotaciones XML?
4. ¿Qué tipos de inconsistencias encontraste durante la validación?
5. ¿Qué ventajas tiene separar los registros válidos de aquellos que presentan errores?
6. ¿Por qué es conveniente almacenar rutas relativas en el manifest?
7. ¿Cómo contribuye el archivo de configuración a la portabilidad del proyecto?
8. ¿Qué ventajas ofrece disponer de un manifest antes de comenzar el procesamiento de imágenes?

---

## ✅ Punto de control

Al finalizar esta práctica habrás:

- Preparado una estructura de proyecto para trabajar con el Oxford-IIIT Pet Dataset original.
- Recuperado la información de clasificación desde `list.txt`.
- Localizado fotografías y máscaras almacenadas en diferentes directorios.
- Leído anotaciones XML cuando estén disponibles.
- Validado la existencia, lectura y consistencia de los archivos.
- Definido un tratamiento para las anotaciones opcionales ausentes.
- Construido un inventario estructurado mediante `pandas`.
- Exportado el manifest a un archivo CSV.
- Creado un archivo JSON para centralizar las rutas del proyecto.
- Comprobado el acceso a una muestra utilizando el manifest y la configuración.

---

## 📚 Dataset de referencia

**Oxford-IIIT Pet Dataset**

Parkhi, O. M., Vedaldi, A., Zisserman, A., & Jawahar, C. V. (2012).

*Cats and Dogs.*

IEEE Conference on Computer Vision and Pattern Recognition (CVPR).

[Consultar el dataset original →](https://www.robots.ox.ac.uk/~vgg/data/pets/)

---

[← Volver a Inventario y configuración del dataset](../../../modulos/02-ingenieria-del-dataset/02-02-inventario-y-configuracion-del-dataset.md)