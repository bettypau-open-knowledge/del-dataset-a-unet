# 📐 Estrategias de redimensionamiento con Albumentations

En las prácticas anteriores aprendimos a procesar imágenes digitales y a utilizar **Albumentations** para aplicar transformaciones geométricas y fotométricas a fotografías y máscaras de segmentación.

Una de las operaciones más importantes en la preparación de datos para Deep Learning es el **redimensionamiento (*resize*)**, ya que frecuentemente necesitamos que las imágenes y máscaras tengan dimensiones uniformes antes de utilizarlas en un modelo.

Sin embargo, existen diferentes estrategias para conseguirlo, y cada una puede modificar la información original de distintas maneras.

En esta práctica compararemos **tres estrategias de redimensionamiento** mediante Albumentations:

1. **Redimensionamiento directo:** ajustar una imagen a dimensiones fijas, aunque se modifique su relación de aspecto.
2. **Redimensionamiento proporcional con *padding*:** conservar la relación de aspecto y agregar bordes para completar las dimensiones deseadas.
3. **Redimensionamiento proporcional con *crop*:** conservar la relación de aspecto y recortar parte de la imagen para obtener las dimensiones deseadas.

Aplicaremos las tres estrategias a una fotografía y su máscara de segmentación del Oxford-IIIT Pet Dataset, observando sus efectos sobre la geometría de la imagen, la información visual y las etiquetas de segmentación.

---

## 🎯 Objetivo

Comparar diferentes estrategias de redimensionamiento de imágenes y máscaras mediante Albumentations, identificando sus efectos sobre la relación de aspecto, la conservación de información y la correspondencia espacial entre fotografías y anotaciones.

Utilizar `A.Resize()`, `A.LongestMaxSize()`, `A.SmallestMaxSize()`, `A.PadIfNeeded()` y `A.CenterCrop()` para transformar imágenes a dimensiones uniformes de **256 × 256 píxeles**.

Reconocer las ventajas, limitaciones y posibles consecuencias de cada estrategia al preparar datos para el entrenamiento de modelos de segmentación.

---

## 📁 Organización del proyecto

Para esta práctica **continuaremos utilizando el proyecto de Visual Studio Code de las prácticas anteriores**.

No es necesario crear un proyecto nuevo ni volver a descargar las imágenes.

Únicamente incorpora el notebook [`diferentes_resize.ipynb`](../../recursos/codigo/03-procesamiento-de-imagenes-y-mascaras/diferentes_resize.ipynb) dentro del directorio `notebooks/`.

La estructura del proyecto deberá quedar de la siguiente manera:

```text
proyecto/
├── data/
│   └── raw/
│       ├── Sphynx_176.jpg
│       └── Sphynx_176.png
└── notebooks/
    ├── procesamiento_imagenes.ipynb
    ├── aumento_datos.ipynb
    └── diferentes_resize.ipynb
```

| Archivo | Descripción |
|---|---|
| `Sphynx_176.jpg` | Fotografía original utilizada para comparar las estrategias de redimensionamiento. |
| `Sphynx_176.png` | Máscara de segmentación correspondiente a la fotografía. |
| `procesamiento_imagenes.ipynb` | Notebook de procesamiento básico de imágenes. |
| `aumento_datos.ipynb` | Notebook de transformaciones y aumento de datos. |
| [`diferentes_resize.ipynb`](../../recursos/codigo/03-procesamiento-de-imagenes-y-mascaras/diferentes_resize.ipynb) | Notebook de comparación de estrategias de redimensionamiento. |

> [!IMPORTANT]
> Conserva la estructura del proyecto y los archivos originales.
>
> Todas las transformaciones se aplicarán en memoria, por lo que no es necesario modificar ni sobrescribir la fotografía o su máscara.

---

## 💻 Instrucciones

### 1 · Abre el proyecto en Visual Studio Code

Abre el proyecto utilizado en las prácticas anteriores.

Comprueba que los archivos `Sphynx_176.jpg` y `Sphynx_176.png` continúen disponibles dentro de `data/raw/`.

Después, coloca el notebook [`diferentes_resize.ipynb`](../../recursos/codigo/03-procesamiento-de-imagenes-y-mascaras/diferentes_resize.ipynb) dentro de `notebooks/` y ábrelo.

### 2 · Selecciona el entorno de Python

Selecciona el kernel correspondiente al entorno de Python del taller.

El notebook utiliza las siguientes bibliotecas:

| Biblioteca | Función |
|---|---|
| `pathlib` | Construcción y manipulación de rutas. |
| `albumentations` | Aplicación de transformaciones geométricas sincronizadas. |
| `cv2` (OpenCV) | Lectura de imágenes y configuración de interpolación. |
| `numpy` | Manipulación de arreglos. |
| `matplotlib` | Visualización comparativa de los resultados. |

Comprueba que todas se encuentren disponibles antes de comenzar.

### 3 · Verifica las rutas

El notebook utiliza las siguientes instrucciones para localizar los archivos:

```python
PROYECTO = Path("..")
DATA = PROYECTO / "data"
RAW = DATA / "raw"

ruta_imagen_gato = RAW / "Sphynx_176.jpg"
ruta_imagen_mascara = RAW / "Sphynx_176.png"
```

Estas rutas consideran que el directorio de trabajo de Python es `notebooks/`.

> [!NOTE]
> Si ejecutas el notebook desde otro directorio de trabajo, deberás ajustar las rutas para que Python pueda localizar correctamente los archivos.

---

## 🧪 Actividades de la práctica

### 1 · Lectura y visualización de los archivos originales

Comenzaremos leyendo la fotografía mediante OpenCV y convirtiéndola del formato BGR a RGB.

También leeremos su máscara de segmentación en escala de grises.

Visualizaremos ambos archivos para identificar la imagen original y sus regiones etiquetadas.

Antes de continuar, observa la relación de aspecto de la fotografía y la correspondencia espacial entre la imagen y su máscara.

**Considera:** ¿qué podría ocurrir si modificamos las dimensiones de la fotografía sin aplicar la misma transformación a su máscara?

---

### 2 · Redimensionamiento directo con `A.Resize()`

La primera estrategia consiste en modificar directamente las dimensiones de una imagen para ajustarla a un tamaño específico.

Utilizaremos:

```python
transform_resize = A.Compose([
    A.Resize(
        height=256,
        width=256,
        interpolation=cv2.INTER_LINEAR,
        mask_interpolation=cv2.INTER_NEAREST
    )
])
```

Esta transformación ajusta tanto la fotografía como su máscara a **256 × 256 píxeles**.

Para ello, utiliza:

- Interpolación bilineal para la fotografía.
- Interpolación por vecino más cercano para la máscara.

La principal característica de esta estrategia es que **no conserva necesariamente la relación de aspecto original**.

Por lo tanto, los objetos pueden experimentar deformaciones geométricas si las proporciones de la imagen original son diferentes a las del tamaño de destino.

**Considera:** ¿qué cambios esperarías observar en la forma del animal al transformar una fotografía rectangular en una imagen cuadrada?

---

### 3 · Redimensionamiento proporcional con *padding*

La segunda estrategia consiste en conservar la relación de aspecto de la imagen y completar las dimensiones restantes mediante bordes.

Utilizaremos dos transformaciones consecutivas:

```python
transform_resize_padding = A.Compose([
    A.LongestMaxSize(max_size=256),

    A.PadIfNeeded(
        min_height=256,
        min_width=256,
        border_mode=cv2.BORDER_CONSTANT,
        fill=0,
        fill_mask=2,
        position="center"
    )
])
```

**`A.LongestMaxSize()`**

Redimensiona la imagen proporcionalmente, de manera que su dimensión más larga alcance el tamaño especificado.

**`A.PadIfNeeded()`**

Agrega bordes hasta alcanzar las dimensiones requeridas.

En este caso:

- La fotografía se completa con píxeles de valor `0`.
- La máscara se completa con píxeles de valor `2`.
- El contenido se mantiene centrado.

> [!IMPORTANT]
> En las máscaras del Oxford-IIIT Pet Dataset, el valor `2` corresponde a la etiqueta de fondo.
>
> Por ello, el notebook utiliza `fill_mask=2` para que las regiones agregadas mediante *padding* se etiqueten como fondo.
>
> Utilizar `0` en estas regiones introduciría un valor distinto de las etiquetas originales `1`, `2` y `3`.

Esta estrategia permite conservar las proporciones del objeto, aunque incorpora regiones adicionales alrededor de la imagen.

**Considera:** ¿qué ventajas ofrece conservar la relación de aspecto? ¿Qué efecto podrían tener los bordes agregados sobre los datos utilizados durante el entrenamiento?

---

### 4 · Redimensionamiento proporcional con *crop*

La tercera estrategia también conserva la relación de aspecto, pero utiliza un recorte para obtener las dimensiones finales.

Aplicaremos:

```python
transform_crop = A.Compose([
    A.SmallestMaxSize(max_size=256),

    A.CenterCrop(
        height=256,
        width=256
    )
])
```

**`A.SmallestMaxSize()`**

Redimensiona proporcionalmente la imagen hasta que su dimensión más corta alcanza el tamaño especificado.

**`A.CenterCrop()`**

Extrae una región central de **256 × 256 píxeles**.

A diferencia de la estrategia anterior, esta transformación no necesita agregar bordes.

Sin embargo, puede eliminar regiones de la fotografía original.

**Considera:** ¿qué sucedería si una parte importante del animal se encontrara cerca de los bordes de la fotografía?

---

### 5 · Aplicación sincronizada a imagen y máscara

Una vez definidas las tres estrategias, las aplicaremos conjuntamente a la fotografía y su máscara.

El notebook utiliza:

```python
resultado_resize = transform_resize(
    image=imagen_rgb,
    mask=mascara
)

resultado_padding = transform_resize_padding(
    image=imagen_rgb,
    mask=mascara
)

resultado_crop = transform_crop(
    image=imagen_rgb,
    mask=mascara
)
```

Albumentations aplica las operaciones geométricas de manera sincronizada a ambos elementos.

Esto permite conservar la correspondencia espacial entre la fotografía transformada y su máscara.

> [!IMPORTANT]
> Aunque las fotografías pueden utilizar métodos de interpolación que calculan valores intermedios, las máscaras categóricas deben conservar sus etiquetas originales.
>
> Por ello, las transformaciones de redimensionamiento utilizan normalmente interpolación por vecino más cercano para las máscaras.

---

### 6 · Visualización comparativa de los resultados

Finalmente, ejecutaremos la celda que genera una figura organizada en tres filas y dos columnas.

Cada fila corresponde a una estrategia:

1. Redimensionamiento directo.
2. Redimensionamiento proporcional con *padding*.
3. Redimensionamiento proporcional con *CenterCrop*.

La columna izquierda mostrará la fotografía RGB y la derecha su máscara correspondiente.

Observa cuidadosamente las diferencias entre las tres estrategias.

Presta especial atención a:

- La forma y proporciones del animal.
- La presencia de bordes agregados.
- Las regiones eliminadas mediante el recorte.
- La correspondencia entre fotografía y máscara.
- La conservación de las etiquetas de segmentación.

---

## 📊 Resultado · Comparación de estrategias

Al finalizar, habrás generado tres pares de imágenes y máscaras con dimensiones de **256 × 256 píxeles**.

| Estrategia | Conserva la relación de aspecto | Agrega bordes | Puede eliminar contenido |
|---|---|---|---|
| `Resize` directo | No necesariamente | No | No, pero puede deformar |
| `LongestMaxSize` + `PadIfNeeded` | Sí | Sí | No |
| `SmallestMaxSize` + `CenterCrop` | Sí | No | Sí |

Las tres estrategias permiten obtener imágenes con dimensiones uniformes, pero **no conservan la información original de la misma manera**.

La elección dependerá de las características del dataset y de los requisitos del modelo.

---

## 🤔 Observa e interpreta

Al finalizar la práctica, responde las siguientes preguntas:

1. ¿Por qué es necesario utilizar dimensiones uniformes al construir lotes de imágenes para entrenar una red neuronal?
2. ¿Qué diferencia existe entre redimensionar directamente una imagen y hacerlo de manera proporcional?
3. ¿Qué ocurre con la relación de aspecto al utilizar `A.Resize()` con dimensiones cuadradas?
4. ¿Qué función cumple `A.LongestMaxSize()` dentro de la estrategia de *padding*?
5. ¿Por qué es necesario agregar bordes después de aplicar `A.LongestMaxSize()`?
6. ¿Qué representa el parámetro `fill_mask=2` utilizado en el notebook?
7. ¿Qué diferencia existe entre `A.LongestMaxSize()` y `A.SmallestMaxSize()`?
8. ¿Qué información podría perderse al utilizar `A.CenterCrop()`?
9. ¿Por qué debemos aplicar las mismas transformaciones geométricas a la fotografía y a su máscara?
10. Si tuvieras que preparar un dataset para entrenar una U-Net, ¿cuál de las tres estrategias seleccionarías y qué características del dataset considerarías para tomar esa decisión?

---

## ✅ Punto de control

Al finalizar esta práctica habrás:

- Incorporado un nuevo notebook al proyecto de Visual Studio Code.
- Recuperado una fotografía y su máscara del Oxford-IIIT Pet Dataset.
- Utilizado Albumentations para aplicar transformaciones geométricas sincronizadas.
- Redimensionado fotografías y máscaras a `256 × 256` píxeles.
- Aplicado redimensionamiento directo mediante `A.Resize()`.
- Conservado la relación de aspecto mediante `A.LongestMaxSize()`.
- Agregado bordes mediante `A.PadIfNeeded()`.
- Utilizado `A.SmallestMaxSize()` y `A.CenterCrop()` para obtener recortes centrales.
- Identificado la diferencia entre deformar, rellenar y recortar una imagen.
- Comparado visualmente los resultados de las tres estrategias.
- Reconocido la importancia de preservar las etiquetas de las máscaras de segmentación.
- Analizado las ventajas y limitaciones de cada estrategia para preparar datos de entrenamiento.

---

## 🏁 ¡Práctica completada!

Has comparado tres formas diferentes de transformar fotografías y máscaras a dimensiones uniformes.

Aunque todas producen resultados de **256 × 256 píxeles**, cada una modifica de manera diferente la información original.

Comprender estas diferencias es fundamental para diseñar un flujo de preprocesamiento adecuado, ya que **la elección de una estrategia de redimensionamiento puede influir en la información que estará disponible para el modelo durante el entrenamiento**.

---

## 📚 Dataset de referencia

Esta práctica utiliza una fotografía y su máscara de segmentación del **Oxford-IIIT Pet Dataset**.

**Referencia:**

Parkhi, O. M., Vedaldi, A., Zisserman, A., & Jawahar, C. V. (2012).

*Cats and Dogs.*

IEEE Conference on Computer Vision and Pattern Recognition (CVPR).

[Consultar el dataset original →](https://www.robots.ox.ac.uk/~vgg/data/pets/)

---

[← Volver a Aumento de datos](../../modulos/03-procesamiento-de-imagenes-y-mascaras/03-02-aumento-de-datos.md)