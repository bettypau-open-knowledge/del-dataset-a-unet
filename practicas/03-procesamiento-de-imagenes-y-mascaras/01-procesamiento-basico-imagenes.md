# 🖼️ Procesamiento básico de imágenes

En el tema **3.1 · Fundamentos y procesamiento básico** estudiamos cómo se representan las imágenes digitales mediante píxeles, matrices y tensores, así como las operaciones que permiten modificar sus dimensiones, tipos de datos y valores de intensidad.

Ahora aplicaremos estos conceptos mediante Python, utilizando una fotografía y su máscara de segmentación del Oxford-IIIT Pet Dataset.

Durante esta práctica aprenderemos a **leer, visualizar y transformar imágenes digitales**, identificando cómo cambia su representación al utilizar diferentes espacios de color, tipos de datos y formatos de tensores.

También compararemos distintas estrategias de redimensionamiento y métodos de interpolación para comprender cómo afectan la apariencia de las imágenes y por qué es necesario utilizar un tratamiento diferente para las máscaras de segmentación.

---

## 🎯 Objetivo

Aplicar operaciones básicas de procesamiento digital de imágenes mediante Python, utilizando OpenCV, NumPy, Matplotlib y PyTorch.

Inspeccionar dimensiones, canales, tipos de datos y rangos de valores; realizar conversiones y transformaciones de intensidad; representar imágenes como matrices y tensores; y comparar métodos de redimensionamiento e interpolación.

Reconocer las diferencias entre el procesamiento de fotografías y máscaras de segmentación, identificando las operaciones adecuadas para preservar la información de cada una.

---

## 📁 Organización del proyecto

Antes de comenzar, crea un directorio para esta práctica y organiza los archivos de la siguiente manera:

```text
proyecto/
├── data/
│   └── raw/
│       ├── Sphynx_176.jpg
│       └── Sphynx_176.png
└── notebooks/
    └── procesamiento_imagenes.ipynb
```

Los archivos tienen las siguientes funciones:

| Archivo | Descripción |
|---|---|
| [`Sphynx_176.jpg`](../../recursos/codigo/03-procesamiento-de-imagenes-y-mascaras/Sphynx_176.jpg) | Fotografía original que utilizaremos para realizar las transformaciones. |
| [`Sphynx_176.png`](../../recursos/codigo/03-procesamiento-de-imagenes-y-mascaras/Sphynx_176.png) | Máscara de segmentación correspondiente a la fotografía. |
| [`procesamiento_imagenes.ipynb`](../../recursos/codigo/03-procesamiento-de-imagenes-y-mascaras/procesamiento_imagenes.ipynb) | Notebook que contiene los ejercicios de procesamiento básico. |

> [!IMPORTANT]
> La fotografía y su máscara deben conservar sus nombres originales y encontrarse dentro de `data/raw/`.
>
> El notebook debe almacenarse en `notebooks/`, ya que las rutas definidas en el código consideran esta organización.

---

## 💻 Instrucciones

Para realizar esta práctica necesitarás:

- Visual Studio Code con soporte para Jupyter Notebooks.
- El entorno de Python configurado para el taller.
- El notebook [`procesamiento_imagenes.ipynb`](../../recursos/codigo/03-procesamiento-de-imagenes-y-mascaras/procesamiento_imagenes.ipynb).
- Los archivos [`Sphynx_176.jpg`](../../recursos/codigo/03-procesamiento-de-imagenes-y-mascaras/Sphynx_176.jpg) y [`Sphynx_176.png`](../../recursos/codigo/03-procesamiento-de-imagenes-y-mascaras/Sphynx_176.png).

### 1 · Prepara los archivos del proyecto

Crea los directorios `data/raw/` y `notebooks/` dentro de la carpeta principal del proyecto.

Coloca la fotografía y la máscara en `data/raw/` y guarda el notebook en `notebooks/`.

Comprueba que los archivos se encuentren en las ubicaciones indicadas.

### 2 · Abre el notebook

Abre la carpeta del proyecto en **Visual Studio Code**.

Localiza y abre:

```text
notebooks/procesamiento_imagenes.ipynb
```

Selecciona el kernel correspondiente al entorno de Python del taller.

### 3 · Comprueba las dependencias

El notebook utiliza las siguientes bibliotecas:

- `pathlib`: construcción y manipulación de rutas.
- `cv2` (OpenCV): lectura y transformación de imágenes.
- `numpy`: manipulación de arreglos multidimensionales.
- `torch` (PyTorch): representación de imágenes mediante tensores.
- `matplotlib`: visualización de imágenes y resultados.

Comprueba que las bibliotecas estén disponibles en el entorno seleccionado.

### 4 · Verifica las rutas

Al inicio del notebook encontrarás las instrucciones utilizadas para localizar los archivos:

```python
PROYECTO = Path("..")
DATA = PROYECTO / "data"
RAW = DATA / "raw"

ruta_imagen_gato = RAW / "Sphynx_176.jpg"
ruta_imagen_mascara = RAW / "Sphynx_176.png"
```

Estas rutas están definidas considerando que el directorio de trabajo es `notebooks/`.

Antes de continuar, comprueba que Python puede localizar ambos archivos.

> [!NOTE]
> Las rutas relativas se interpretan a partir del directorio de trabajo del proceso de Python, no necesariamente desde la ubicación del archivo `.ipynb`.
>
> Si ejecutas el notebook desde un directorio diferente, deberás ajustar las rutas o establecer el directorio de trabajo correspondiente.

---

## 🧪 Actividades de la práctica

### 1 · Lectura y visualización de imágenes

Comenzaremos leyendo la fotografía mediante OpenCV.

Observaremos que esta biblioteca utiliza habitualmente el orden de canales **BGR**, mientras que Matplotlib interpreta las imágenes de tres canales como **RGB**.

Realizaremos las conversiones necesarias para obtener:

- Imagen original en formato BGR.
- Imagen convertida a RGB.
- Imagen convertida a escala de grises.

Después, visualizaremos las tres representaciones para identificar sus diferencias.

**Considera:** ¿por qué una imagen leída mediante OpenCV puede mostrar colores incorrectos cuando se visualiza directamente con Matplotlib?

---

### 2 · Inspección de dimensiones, canales y tipos de datos

Utilizaremos los atributos y funciones de NumPy para recuperar información sobre las imágenes RGB y en escala de grises.

Inspeccionaremos:

- Dimensiones de los arreglos.
- Número de canales.
- Tipo de dato (`dtype`).
- Valor mínimo de intensidad.
- Valor máximo de intensidad.

Compararemos las características de ambas representaciones.

**Considera:** ¿por qué una imagen RGB y una imagen en escala de grises pueden tener diferentes dimensiones en sus arreglos, aunque representen la misma fotografía?

---

### 3 · Conversión de tipos y escalado de intensidades

Convertiremos las imágenes del tipo `uint8` a `float32` y escalaremos sus intensidades al intervalo `[0, 1]`.

Analizaremos las diferencias entre:

- Cambiar el tipo de dato.
- Modificar el rango de valores de intensidad.

Comprobaremos los tipos de datos y valores mínimos y máximos obtenidos después de las operaciones.

Posteriormente, visualizaremos las imágenes transformadas.

**Considera:** ¿convertir una imagen de `uint8` a `float32` implica necesariamente que sus intensidades cambien del intervalo `[0, 255]` a `[0, 1]`?

---

### 4 · Estandarización de intensidades

Aplicaremos una transformación basada en la media y la desviación estándar:

$$
x'=\frac{x-\mu}{\sigma}
$$

Donde:

- $x$ representa un valor de intensidad.
- $\mu$ representa la media.
- $\sigma$ representa la desviación estándar.

Inspeccionaremos los valores resultantes y compararemos sus rangos con los de las imágenes escaladas a `[0, 1]`.

También observaremos qué ocurre al intentar visualizar directamente una imagen estandarizada y por qué puede ser necesario ajustar sus valores para mostrarla correctamente.

**Considera:** ¿por qué los valores de una imagen estandarizada pueden ser negativos o mayores que 1?

> [!NOTE]
> En esta práctica se utiliza la media y la desviación estándar calculadas sobre la imagen para ilustrar el procedimiento.
>
> En un flujo de entrenamiento, los parámetros de estandarización deben definirse de manera consistente, normalmente a partir del conjunto de entrenamiento.

---

### 5 · Representación de imágenes mediante matrices y tensores

Utilizaremos NumPy y PyTorch para representar la fotografía mediante diferentes organizaciones de sus dimensiones.

Trabajaremos con los formatos:

| Formato | Organización |
|---|---|
| HWC | Alto, ancho, canales. |
| CHW | Canales, alto, ancho. |
| BCHW | Lote, canales, alto, ancho. |

Primero reorganizaremos los ejes de una imagen RGB.

Después, agregaremos una dimensión para representar un lote (*batch*) y construiremos un lote de dos imágenes.

Finalmente, convertiremos los arreglos de NumPy a tensores de PyTorch.

**Considera:** ¿qué diferencia existe entre modificar el orden de los ejes de una imagen y agregar una nueva dimensión para representar un lote?

---

### 6 · Redimensionamiento y relación de aspecto

Compararemos dos estrategias para transformar una fotografía a dimensiones de `256 × 256` píxeles.

**a) Redimensionamiento proporcional con *padding***

La imagen se redimensionará conservando su relación de aspecto original.

Después, se agregarán bordes para completar las dimensiones requeridas.

**b) Redimensionamiento directo**

La imagen se transformará directamente a `256 × 256` píxeles, sin conservar necesariamente su relación de aspecto.

Visualizaremos ambos resultados para identificar las diferencias.

**Considera:** ¿qué ventajas y desventajas presenta cada estrategia? ¿En qué casos podría resultar problemático modificar la relación de aspecto?

---

### 7 · Comparación de métodos de interpolación

Aplicaremos tres métodos de interpolación para redimensionar la fotografía:

- Vecino más cercano (*Nearest Neighbor*).
- Interpolación bilineal.
- Interpolación bicúbica.

Generaremos una visualización comparativa de las tres imágenes redimensionadas a `256 × 256` píxeles.

Observaremos las diferencias en los bordes, las transiciones de color y la apariencia general.

**Considera:** ¿por qué distintos métodos de interpolación pueden producir resultados visuales diferentes cuando las dimensiones finales son idénticas?

---

### 8 · Interpolación aplicada a máscaras de segmentación

Finalmente, repetiremos la comparación de interpolaciones, pero utilizando la máscara `Sphynx_176.png`.

Aplicaremos los mismos tres métodos:

- Vecino más cercano.
- Bilineal.
- Bicúbica.

Visualizaremos los resultados para observar cómo cambia la representación de las regiones etiquetadas.

> [!IMPORTANT]
> Las máscaras de segmentación contienen **etiquetas categóricas**, no intensidades fotográficas.
>
> Los métodos de interpolación que calculan valores intermedios pueden generar valores que no corresponden a las etiquetas originales.
>
> Por esta razón, para redimensionar máscaras categóricas se utiliza normalmente la interpolación por **vecino más cercano**.

**Considera:** ¿qué consecuencias tendría introducir valores de etiqueta incorrectos en las máscaras utilizadas para entrenar un modelo de segmentación?

---

## 🤔 Observa e interpreta

Al finalizar la práctica, responde las siguientes preguntas:

1. ¿Qué diferencias existen entre una imagen BGR y una RGB?
2. ¿Cómo cambia la representación matricial de una fotografía al convertirla a escala de grises?
3. ¿Qué diferencia existe entre convertir el tipo de dato de una imagen y escalar sus intensidades?
4. ¿Por qué la estandarización puede producir valores negativos?
5. ¿Qué representa cada dimensión de un tensor en formato BCHW?
6. ¿Qué sucede con la apariencia de una fotografía cuando se modifica su relación de aspecto?
7. ¿Qué diferencias visuales identificaste entre los tres métodos de interpolación?
8. ¿Por qué una máscara de segmentación requiere un tratamiento diferente al de una fotografía durante el redimensionamiento?
9. ¿Qué problemas podrían surgir si se utiliza interpolación bilineal o bicúbica sobre una máscara de etiquetas categóricas?
10. ¿Qué operaciones de esta práctica consideras necesarias para preparar las imágenes antes de entrenar una red U-Net?

---

## ✅ Punto de control

Al finalizar esta práctica habrás:

- Creado una estructura de proyecto con directorios para datos y notebooks.
- Leído y visualizado imágenes mediante OpenCV y Matplotlib.
- Convertido imágenes entre BGR, RGB y escala de grises.
- Inspeccionado dimensiones, canales, tipos de datos y rangos de intensidad.
- Convertido imágenes de `uint8` a `float32`.
- Aplicado escalado y estandarización de intensidades.
- Representado imágenes mediante arreglos de NumPy y tensores de PyTorch.
- Reorganizado dimensiones entre los formatos HWC, CHW y BCHW.
- Comparado estrategias de redimensionamiento con y sin conservación de la relación de aspecto.
- Aplicado y visualizado diferentes métodos de interpolación.
- Identificado los efectos de la interpolación sobre máscaras categóricas.
- Reconocido la importancia de seleccionar transformaciones adecuadas para fotografías y máscaras.

---

## 📚 Dataset de referencia

Esta práctica utiliza una fotografía y su máscara de segmentación del **Oxford-IIIT Pet Dataset**.

**Referencia:**

Parkhi, O. M., Vedaldi, A., Zisserman, A., & Jawahar, C. V. (2012).

*Cats and Dogs.*

IEEE Conference on Computer Vision and Pattern Recognition (CVPR).

[Consultar el dataset original →](https://www.robots.ox.ac.uk/~vgg/data/pets/)

---

[← Volver a Fundamentos y procesamiento básico](../../modulos/03-procesamiento-de-imagenes-y-mascaras/03-01-fundamentos-y-procesamiento-basico.md)