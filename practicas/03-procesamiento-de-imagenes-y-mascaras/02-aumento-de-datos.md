# 🔄 Aumento de datos con Albumentations

En la práctica anterior aprendimos a leer, visualizar y transformar imágenes digitales mediante Python. También estudiamos las diferencias entre las fotografías y las máscaras de segmentación, reconociendo que ambas requieren un tratamiento adecuado para preservar su información.

Ahora utilizaremos **Albumentations**, una biblioteca especializada en transformaciones y aumento de datos (*data augmentation*) para tareas de visión por computadora.

Durante esta práctica aplicaremos transformaciones geométricas y fotométricas a una fotografía del Oxford-IIIT Pet Dataset, observando cómo cambian sus resultados cuando se ejecutan de manera aleatoria.

Posteriormente, construiremos un **pipeline de aumento de datos** y lo aplicaremos conjuntamente a una fotografía y su máscara de segmentación, comprobando que las transformaciones geométricas mantienen la correspondencia espacial entre ambas, mientras que las fotométricas modifican únicamente la imagen.

---

## 🎯 Objetivo

Aplicar técnicas de aumento de datos mediante Albumentations, utilizando transformaciones geométricas y fotométricas sobre imágenes digitales.

Comprender el funcionamiento de las probabilidades de aplicación de las transformaciones, construir pipelines mediante `A.Compose()` y generar diferentes versiones de una misma fotografía.

Aplicar transformaciones sincronizadas a pares imagen–máscara, identificando la importancia de conservar la correspondencia espacial y los valores categóricos de las anotaciones de segmentación.

---

## 📁 Organización del proyecto

Para esta práctica **continuaremos trabajando con el mismo proyecto de Visual Studio Code utilizado en la práctica anterior**.

No es necesario crear un proyecto nuevo ni duplicar los archivos de imagen.

Únicamente deberás incorporar el notebook [`aumento_datos.ipynb`](../../recursos/codigo/03-procesamiento-de-imagenes-y-mascaras/aumento_datos.ipynb) dentro del directorio `notebooks/`.

La estructura del proyecto deberá quedar de la siguiente manera:

```text
proyecto/
├── data/
│   └── raw/
│       ├── Sphynx_176.jpg
│       └── Sphynx_176.png
└── notebooks/
    ├── procesamiento_imagenes.ipynb
    └── aumento_datos.ipynb
```

| Archivo | Descripción |
|---|---|
| `Sphynx_176.jpg` | Fotografía original que utilizaremos para aplicar las transformaciones. |
| `Sphynx_176.png` | Máscara de segmentación correspondiente a la fotografía. |
| `procesamiento_imagenes.ipynb` | Notebook de la práctica anterior. |
| [`aumento_datos.ipynb`](../../recursos/codigo/03-procesamiento-de-imagenes-y-mascaras/aumento_datos.ipynb) | Notebook de esta práctica, dedicado al aumento de datos. |

> [!IMPORTANT]
> Conserva los archivos de la práctica anterior en sus ubicaciones originales.
>
> El nuevo notebook debe colocarse dentro de `notebooks/`, junto a `procesamiento_imagenes.ipynb`.
>
> **No modifiques ni sobrescribas la fotografía o su máscara original.**

---

## 💻 Instrucciones

Para realizar esta práctica necesitarás:

- Visual Studio Code con soporte para Jupyter Notebooks.
- El proyecto utilizado durante la práctica de procesamiento básico de imágenes.
- El entorno de Python configurado para el taller.
- El notebook [`aumento_datos.ipynb`](../../recursos/codigo/03-procesamiento-de-imagenes-y-mascaras/aumento_datos.ipynb).
- Los archivos `Sphynx_176.jpg` y `Sphynx_176.png`.

### 1 · Abre el proyecto de la práctica anterior

Abre en **Visual Studio Code** la carpeta del proyecto que utilizaste para realizar las actividades de procesamiento básico de imágenes.

Comprueba que los directorios `data/raw/` y `notebooks/` se encuentren disponibles.

Verifica también que la fotografía y su máscara continúen almacenadas dentro de `data/raw/`.

### 2 · Incorpora el nuevo notebook

Coloca el archivo:

```text
aumento_datos.ipynb
```

dentro del directorio:

```text
notebooks/
```

Abre el notebook en Visual Studio Code y selecciona el kernel correspondiente al entorno de Python del taller.

### 3 · Comprueba las dependencias

El notebook utiliza las siguientes bibliotecas:

| Biblioteca | Función |
|---|---|
| `pathlib` | Construcción y manipulación de rutas. |
| `albumentations` | Aplicación de transformaciones y aumento de datos. |
| `cv2` (OpenCV) | Lectura de imágenes y máscaras. |
| `numpy` | Manipulación de arreglos multidimensionales. |
| `matplotlib` | Visualización de imágenes y resultados. |

Comprueba que todas se encuentren disponibles en el entorno seleccionado.

### 4 · Verifica las rutas

Al inicio del notebook se definen las rutas de acceso a los archivos:

```python
PROYECTO = Path("..")
DATA = PROYECTO / "data"
RAW = DATA / "raw"

ruta_imagen_gato = RAW / "Sphynx_176.jpg"
ruta_imagen_mascara = RAW / "Sphynx_176.png"
```

Estas rutas consideran que el directorio de trabajo de Python es `notebooks/`.

Comprueba que ambas rutas permitan localizar correctamente los archivos.

> [!NOTE]
> Las rutas relativas se interpretan desde el directorio de trabajo de Python.
>
> Si ejecutas el notebook desde otra ubicación, deberás ajustar las rutas o establecer el directorio de trabajo correspondiente.

---

## 🧪 Actividades de la práctica

### 1 · Lectura y visualización de la imagen y su máscara

Comenzaremos leyendo la fotografía mediante OpenCV y convirtiéndola del formato BGR a RGB.

También recuperaremos la máscara de segmentación en escala de grises.

Visualizaremos ambos archivos para comprobar que corresponden a la misma muestra y que pueden utilizarse durante las siguientes actividades.

**Considera:** ¿por qué es necesario conservar la correspondencia entre una fotografía y su máscara al aplicar técnicas de aumento de datos?

---

### 2 · Definición de transformaciones individuales

Utilizaremos Albumentations para definir tres transformaciones:

**a) Volteo horizontal**

Mediante `A.HorizontalFlip()` invertiremos horizontalmente la fotografía.

**b) Rotación aleatoria**

Mediante `A.Rotate()` aplicaremos rotaciones aleatorias dentro de un intervalo de −30° a 30°.

También utilizaremos un modo de borde constante para rellenar las regiones que puedan quedar fuera de la imagen original.

**c) Modificación de brillo y contraste**

Mediante `A.RandomBrightnessContrast()` modificaremos aleatoriamente las intensidades de la fotografía.

En esta primera actividad, las transformaciones se configurarán con:

```python
p=1.0
```

Esto significa que cada transformación se aplicará siempre que sea ejecutada.

> [!NOTE]
> Aunque una transformación tenga `p=1.0`, algunos de sus parámetros internos pueden seguir siendo aleatorios.
>
> Por ejemplo, una rotación configurada con un intervalo de ángulos puede producir resultados diferentes en ejecuciones sucesivas.

---

### 3 · Aplicación y visualización de transformaciones

Aplicaremos individualmente las tres transformaciones a la fotografía.

Después, construiremos una visualización que permita comparar:

- Imagen original.
- Imagen con volteo horizontal.
- Imagen rotada.
- Imagen con modificaciones de brillo y contraste.

Ejecuta varias veces las celdas de transformación y visualización.

Observa especialmente los resultados de la rotación y de las modificaciones de brillo y contraste.

**Considera:** ¿por qué algunas transformaciones producen resultados diferentes cada vez que se ejecutan, incluso cuando su probabilidad de aplicación es del 100 %?

---

### 4 · Construcción de un pipeline mediante `A.Compose()`

Hasta ahora hemos aplicado las transformaciones de manera independiente.

Ahora utilizaremos `A.Compose()` para agruparlas dentro de un mismo **pipeline de aumento de datos**.

El pipeline incluirá:

- Volteo horizontal.
- Rotación aleatoria.
- Modificación de brillo y contraste.

Cada transformación tendrá una probabilidad de aplicación de:

```python
p=0.5
```

Mientras que el pipeline completo se configurará con:

```python
p=1.0
```

Observa la diferencia entre la probabilidad asignada a cada transformación y la probabilidad de ejecución del pipeline completo.

> [!IMPORTANT]
> Que el pipeline tenga `p=1.0` no significa que todas las transformaciones incluidas deban aplicarse.
>
> Cada operación conserva su propia probabilidad de ejecución.
>
> Por lo tanto, una misma imagen puede recibir diferentes combinaciones de transformaciones en ejecuciones sucesivas.

**Considera:** ¿qué diferencia existe entre definir una transformación con `p=0.5` y configurar el pipeline completo con `p=0.5`?

---

### 5 · Generación de diferentes versiones de una imagen

Aplicaremos repetidamente el pipeline sobre la misma fotografía.

Generaremos cuatro versiones transformadas y las visualizaremos junto a la imagen original.

Observa las diferencias entre los resultados.

Identifica cuáles transformaciones parecen haberse aplicado en cada versión y cuáles no.

**Considera:** ¿por qué un pipeline con transformaciones probabilísticas permite generar diferentes versiones de una misma fotografía sin modificar el archivo original?

---

### 6 · Aplicación sincronizada a imagen y máscara

Finalmente, utilizaremos el mismo pipeline para transformar conjuntamente la fotografía y su máscara de segmentación.

En lugar de proporcionar únicamente la imagen, utilizaremos ambos argumentos:

```python
resultado = transform(
    image=imagen_rgb,
    mask=mascara
)
```

Después, recuperaremos:

```python
imagen_aumentada = resultado["image"]
mascara_aumentada = resultado["mask"]
```

Visualizaremos los resultados para comprobar cómo se aplican las transformaciones.

Presta atención a las diferencias entre los dos tipos de operaciones:

- **Transformaciones geométricas:** se aplican de manera sincronizada a la imagen y a la máscara.
- **Transformaciones fotométricas:** se aplican únicamente a la fotografía.

En particular, observa qué ocurre cuando se aplica una rotación y cómo se mantiene la correspondencia entre la posición del animal y su región etiquetada.

> [!IMPORTANT]
> Las máscaras de segmentación contienen etiquetas categóricas.
>
> Albumentations permite aplicar transformaciones espaciales sincronizadas a la imagen y a su máscara, utilizando el tratamiento de interpolación correspondiente a cada una.
>
> En el notebook, la rotación utiliza `fill_mask=2` para rellenar con la etiqueta de fondo las regiones nuevas de la máscara que aparecen fuera de la imagen original.

**Considera:** ¿qué sucedería si la fotografía y su máscara recibieran rotaciones aleatorias independientes?

---

## 🤔 Observa e interpreta

Al finalizar la práctica, responde las siguientes preguntas:

1. ¿Qué diferencia existe entre una transformación geométrica y una fotométrica?
2. ¿Qué significa configurar una transformación con `p=1.0`?
3. ¿Por qué una rotación puede producir resultados diferentes aunque tenga una probabilidad de aplicación del 100 %?
4. ¿Qué ventajas ofrece utilizar `A.Compose()` en lugar de aplicar las transformaciones de manera independiente?
5. ¿Qué diferencia existe entre la probabilidad de ejecución de una transformación y la probabilidad del pipeline completo?
6. ¿Por qué podemos obtener varias versiones diferentes de una misma fotografía utilizando el mismo pipeline?
7. ¿Qué transformaciones deben aplicarse de manera sincronizada a una fotografía y su máscara?
8. ¿Por qué los cambios de brillo y contraste no deben aplicarse a las máscaras categóricas?
9. ¿Qué problemas podrían surgir si una imagen y su máscara reciben transformaciones geométricas independientes?
10. ¿Cómo podría contribuir el aumento de datos a mejorar la capacidad de generalización de un modelo de segmentación?

---

## ✅ Punto de control

Al finalizar esta práctica habrás:

- Recuperado el proyecto de Visual Studio Code utilizado en la práctica anterior.
- Incorporado un nuevo notebook dentro del directorio `notebooks/`.
- Leído y visualizado una fotografía y su máscara de segmentación.
- Utilizado Albumentations para definir transformaciones geométricas y fotométricas.
- Aplicado volteos horizontales, rotaciones y modificaciones de brillo y contraste.
- Comprendido el funcionamiento del parámetro `p`.
- Construido un pipeline mediante `A.Compose()`.
- Generado diferentes versiones de una fotografía mediante transformaciones probabilísticas.
- Aplicado un pipeline conjuntamente a una fotografía y su máscara.
- Identificado la importancia de sincronizar las transformaciones geométricas.
- Reconocido por qué las transformaciones fotométricas deben aplicarse únicamente a las fotografías.

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