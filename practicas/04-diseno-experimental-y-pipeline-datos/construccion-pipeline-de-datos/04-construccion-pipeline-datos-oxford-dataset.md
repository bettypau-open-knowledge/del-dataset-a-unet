# 🔄 Construcción del pipeline de datos del Oxford-IIIT Pet Dataset

En las prácticas anteriores aprendimos a organizar el Oxford-IIIT Pet Dataset, identificar sus fotografías y máscaras, registrar sus características mediante un manifest y construir conjuntos experimentales reproducibles.

En particular, durante la práctica **[Diseño de conjuntos experimentales del Oxford-IIIT Pet Dataset](../diseno-conjuntos-experimentales/02-diseno-conjuntos-experimentales-oxford-dataset.md)**, generamos dos configuraciones de entrenamiento (*train*), validación (*validation*) y prueba (*test*) con proporciones **70/15/15 y 80/10/10**.

Ahora utilizaremos estos resultados para construir el mecanismo que permitirá recuperar y preparar los datos antes de entregarlos a nuestro modelo de segmentación.

**¿Cómo podemos conectar las fotografías y máscaras almacenadas en nuestro proyecto con un modelo de Deep Learning?**

Para resolverlo, construiremos un **pipeline de datos mediante PyTorch**, utilizando las clases `Dataset` y `DataLoader`.

Este pipeline nos permitirá recuperar las particiones existentes, leer fotografías y máscaras, aplicar transformaciones mediante Albumentations, convertir los datos a tensores y organizarlos en lotes (*batches*).

A diferencia de la práctica introductoria realizada con el minidataset, ahora trabajaremos con el **Oxford-IIIT Pet Dataset de nuestro proyecto principal**, aprovechando los archivos que hemos construido a lo largo del taller.

---

## 🎯 Objetivo

Construir y verificar un pipeline de datos para segmentación de imágenes mediante PyTorch, utilizando los archivos de configuración, manifest y particiones experimentales del Oxford-IIIT Pet Dataset.

Al finalizar, serás capaz de:

- Recuperar los conjuntos experimentales previamente definidos.
- Configurar transformaciones mediante Albumentations.
- Aplicar *data augmentation* exclusivamente al conjunto de entrenamiento.
- Implementar una clase personalizada que herede de `torch.utils.data.Dataset`.
- Comprender los métodos `__init__()`, `__len__()` y `__getitem__()`.
- Recuperar fotografías y máscaras mediante las rutas registradas en el proyecto.
- Convertir imágenes y máscaras a tensores con dimensiones y tipos adecuados.
- Crear objetos `DataLoader` para organizar las muestras en lotes.
- Configurar los parámetros `batch_size`, `shuffle` y `num_workers`.
- Inspeccionar y visualizar las muestras y los lotes obtenidos.
- Verificar la correspondencia espacial entre fotografías y máscaras.

---

## 📁 Organización del proyecto

Continuaremos utilizando el proyecto de Visual Studio Code que hemos desarrollado durante el taller.

No es necesario descargar otro repositorio ni volver a obtener el Oxford-IIIT Pet Dataset.

La estructura relevante será:

```text
proyecto/
├── config/
│   └── dataset.json
├── data/
│   ├── raw/
│   │   └── ...
│   ├── manifests/
│   │   └── manifest.csv
│   └── splits/
│       ├── split_70_15_15.csv
│       └── split_80_10_10.csv
└── notebooks/
    ├── ...
    ├── conjuntos_experimentales_oxford.ipynb
    └── pipeline_de_datos_oxford.ipynb
```

El archivo `pipeline_de_datos_oxford.ipynb` será un notebook nuevo que crearás dentro del directorio `notebooks/`.

| Archivo | Función |
|---|---|
| `config/dataset.json` | Contiene la configuración de rutas del proyecto. |
| `data/manifests/manifest.csv` | Registra las muestras y permite localizar fotografías y máscaras. |
| `data/raw/` | Contiene los archivos originales del Oxford-IIIT Pet Dataset. |
| `data/splits/split_70_15_15.csv` | Contiene la primera configuración experimental. |
| `data/splits/split_80_10_10.csv` | Contiene la segunda configuración experimental. |
| `notebooks/conjuntos_experimentales_oxford.ipynb` | Notebook utilizado para generar las particiones. |
| `notebooks/pipeline_de_datos_oxford.ipynb` | Notebook que desarrollarás durante esta práctica. |

> [!IMPORTANT]
> Esta práctica es una continuación del proyecto principal.
>
> No debes mover, renombrar ni duplicar las fotografías y máscaras originales.
>
> Tampoco volveremos a ejecutar `train_test_split()`: utilizaremos las particiones que ya guardamos en archivos CSV.

---

## 💻 Requisitos

Para realizar esta práctica necesitarás Visual Studio Code, el entorno de Python utilizado durante el taller y los archivos generados en las prácticas anteriores.

Utilizaremos las siguientes bibliotecas:

| Biblioteca | Función |
|---|---|
| `pathlib` | Construcción y manejo de rutas. |
| `json` | Lectura del archivo de configuración. |
| `numpy` | Manipulación de arreglos y conversión de tipos. |
| `pandas` | Lectura y filtrado de las particiones experimentales. |
| `opencv-python` | Lectura de fotografías y máscaras. |
| `albumentations` (2.x) | Transformaciones geométricas y fotométricas. |
| `torch` | Construcción de tensores, Dataset y DataLoader. |
| `matplotlib` | Visualización de imágenes, máscaras y lotes. |

`pathlib` y `json` forman parte de la biblioteca estándar de Python.

---

## 💻 Preparación de la práctica

### 1 · Recupera el proyecto anterior

Antes de comenzar, comprueba que tienes disponibles los resultados de las prácticas:

- **[Inventario y configuración del Oxford-IIIT Pet Dataset](../../02-ingenieria-del-dataset/inventario-y-configuracion-del-dataset/04-inventario-y-configuracion-del-oxford-dataset.md)**

- **[Diseño de conjuntos experimentales del Oxford-IIIT Pet Dataset](../../04-diseno-experimental-y-pipeline-datos/diseno-conjuntos-experimentales/02-diseno-conjuntos-experimentales-oxford-dataset.md)**

Verifica que existan:

```text
config/dataset.json
data/manifests/manifest.csv
data/splits/split_70_15_15.csv
data/splits/split_80_10_10.csv
```

Estos archivos serán el punto de partida del pipeline.

### 2 · Crea el notebook

Dentro de `notebooks/`, crea un archivo llamado:

```text
pipeline_de_datos_oxford.ipynb
```

Selecciona el kernel correspondiente al entorno de Python del taller.

### 3 · Prepara las bibliotecas

En la primera celda de código, importa las bibliotecas necesarias:

```python
from pathlib import Path
import json

import numpy as np
import pandas as pd
import cv2
import albumentations as A
import torch
import matplotlib.pyplot as plt

from matplotlib.colors import ListedColormap
from torch.utils.data import Dataset, DataLoader
```

---

## 🧪 Actividades de la práctica

### 1 · Recuperar la configuración del proyecto

Comenzaremos leyendo el archivo `dataset.json` que construimos anteriormente.

Utiliza `pathlib` para localizar el directorio principal y recuperar la configuración mediante `json`.

Si el directorio de trabajo de Python es `notebooks/`, puedes utilizar:

```python
PROYECTO = Path("..").resolve()

ruta_config = PROYECTO / "config" / "dataset.json"

with ruta_config.open("r", encoding="utf-8") as archivo:
    config = json.load(archivo)
```

Después, utiliza las claves existentes en tu configuración para construir las rutas necesarias.

> [!NOTE]
> Comprueba el directorio de trabajo de Python antes de ejecutar las celdas.
>
> Las rutas relativas se interpretan desde el directorio de trabajo, que no necesariamente coincide con la ubicación del notebook.

**Considera:** ¿qué ventajas ofrece utilizar un archivo de configuración para localizar los datos?

---

### 2 · Recuperar los conjuntos experimentales

Comenzaremos utilizando la configuración **70/15/15** generada anteriormente.

Recupera el archivo:

```text
data/splits/split_70_15_15.csv
```

Utiliza pandas para cargarlo:

```python
splits = pd.read_csv(
    ruta_splits / "split_70_15_15.csv"
)
```

Donde `ruta_splits` representa la ruta del directorio de particiones, construida a partir de la configuración del proyecto.

Después, separa los registros correspondientes a cada conjunto:

```python
train_df = splits[
    splits["split"] == "train"
].reset_index(drop=True)

val_df = splits[
    splits["split"] == "validation"
].reset_index(drop=True)

test_df = splits[
    splits["split"] == "test"
].reset_index(drop=True)
```

Comprueba cuántas muestras contiene cada DataFrame.

> [!IMPORTANT]
> Estamos recuperando las particiones experimentales, no generando otras nuevas.
>
> Esto permite conservar las mismas asignaciones durante las siguientes etapas del proyecto.

---

### 3 · Definir las transformaciones comunes

Antes de construir nuestra clase Dataset, definiremos las transformaciones que aplicaremos a las fotografías y máscaras.

Comenzaremos con un procesamiento común para los tres conjuntos experimentales.

Utilizaremos:

- `A.LongestMaxSize()`: redimensiona proporcionalmente las imágenes.
- `A.PadIfNeeded()`: completa las dimensiones mediante bordes.

El tamaño de destino será:

```python
TAMANO = 256
```

Define las transformaciones:

```python
transform_base = [
    A.LongestMaxSize(
        max_size=TAMANO,
        interpolation=cv2.INTER_LINEAR,
        mask_interpolation=cv2.INTER_NEAREST
    ),

    A.PadIfNeeded(
        min_height=TAMANO,
        min_width=TAMANO,
        border_mode=cv2.BORDER_CONSTANT,
        fill=0,
        fill_mask=2,
        position="center"
    )
]
```

La fotografía se redimensionará mediante interpolación bilineal, mientras que la máscara utilizará vecino más cercano para conservar sus etiquetas.

El valor `fill_mask=2` corresponde al fondo en las máscaras originales del Oxford-IIIT Pet Dataset.

**Considera:** ¿por qué debemos utilizar métodos de interpolación diferentes para fotografías y máscaras categóricas?

---

### 4 · Configurar el aumento de datos para entrenamiento

Ahora agregaremos transformaciones aleatorias exclusivamente al conjunto de entrenamiento.

Utilizaremos:

| Transformación | Probabilidad |
|---|---:|
| Rotación de hasta ±20° | 50 % |
| Volteo horizontal | 50 % |
| Modificación de brillo | 50 % |
| Modificación de contraste | 50 % |

Construye dos pipelines:

**Pipeline de entrenamiento**

Debe incluir las transformaciones comunes y las operaciones aleatorias de aumento de datos.

**Pipeline de validación y prueba**

Debe incluir únicamente las transformaciones comunes.

Puedes utilizar `A.Compose()` para agrupar las operaciones.

> [!IMPORTANT]
> Las transformaciones geométricas deben aplicarse de manera sincronizada a fotografías y máscaras.
>
> Los cambios de brillo y contraste deben afectar únicamente a las fotografías.
>
> Las transformaciones aleatorias de entrenamiento no deben utilizarse para modificar las muestras de validación y prueba.

**Considera:** ¿por qué debemos utilizar un procesamiento determinista durante la evaluación?

---

### 5 · Implementar la clase `PetSegmentationDataset`

Construiremos una clase personalizada que herede de `torch.utils.data.Dataset`.

```python
class PetSegmentationDataset(Dataset):
    ...
```

La clase deberá implementar tres métodos.

**`__init__()` — Inicialización**

Recibirá:

- El DataFrame del conjunto experimental.
- La ubicación de los archivos originales.
- El pipeline de transformaciones.

Almacenará estas referencias para utilizarlas posteriormente.

**`__len__()` — Longitud**

Devolverá el número de muestras disponibles.

**`__getitem__()` — Recuperación de una muestra**

Recibirá un índice y realizará las siguientes operaciones:

1. Recuperar la fila correspondiente del DataFrame.
2. Obtener las rutas de la fotografía y su máscara.
3. Leer ambos archivos mediante OpenCV.
4. Convertir la fotografía de BGR a RGB.
5. Aplicar las transformaciones sincronizadas.
6. Convertir la fotografía a `float32` y escalarla a `[0, 1]`.
7. Convertir las etiquetas originales de la máscara a `0`, `1` y `2`.
8. Convertir fotografía y máscara a tensores de PyTorch.
9. Devolver ambos tensores.

> [!NOTE]
> En el proyecto principal, las rutas pueden estar registradas de forma diferente a las del minidataset.
>
> Adapta la construcción de rutas a las columnas de tu `manifest.csv` y de los CSV de partición.
>
> Si las rutas son relativas al proyecto, resuélvelas desde la raíz del proyecto. No debes agregar automáticamente un directorio de imágenes a una ruta que ya lo incluye.

---

### 6 · Convertir fotografías y máscaras a tensores

El método `__getitem__()` deberá devolver dos tensores.

**Fotografía**

- Tipo: `torch.float32`.
- Dimensiones: `(3, 256, 256)`.
- Valores: `[0, 1]`.

**Máscara**

- Tipo: `torch.int64`.
- Dimensiones: `(256, 256)`.
- Etiquetas: `{0, 1, 2}`.

Las etiquetas originales del Oxford-IIIT Pet Dataset se convertirán de la siguiente manera:

| Etiqueta original | Etiqueta nueva | Región |
|---|---|---|
| 1 | 0 | Animal |
| 2 | 1 | Fondo |
| 3 | 2 | Contorno |

Esta conversión permite representar las clases mediante índices enteros consecutivos desde cero.

> [!IMPORTANT]
> No debes dividir las máscaras entre `255` ni aplicarles la normalización de intensidades utilizada para las fotografías.
>
> Las máscaras representan categorías, no intensidades continuas.

---

### 7 · Crear los objetos Dataset

Una vez implementada la clase, crea tres objetos:

```python
train_dataset
val_dataset
test_dataset
```

Cada uno utilizará el DataFrame correspondiente.

| Dataset | Transformaciones |
|---|---|
| `train_dataset` | Procesamiento común + augmentation |
| `val_dataset` | Procesamiento común |
| `test_dataset` | Procesamiento común |

Consulta sus longitudes mediante `len()`.

Comprueba que el número de muestras coincida con el registrado en los CSV.

**Considera:** ¿por qué podemos reutilizar la misma clase Dataset para los tres conjuntos?

---

### 8 · Recuperar una muestra y verificar sus tensores

Solicita una muestra de entrenamiento:

```python
imagen, mascara = train_dataset[0]
```

Inspecciona:

- Dimensiones de la fotografía.
- Dimensiones de la máscara.
- Tipos de datos.
- Valores mínimos y máximos.
- Etiquetas presentes en la máscara.

Utiliza instrucciones `assert` para comprobar:

```python
assert imagen.shape == (3, 256, 256)
assert mascara.shape == (256, 256)

assert imagen.dtype == torch.float32
assert mascara.dtype == torch.int64

assert imagen.min().item() >= 0
assert imagen.max().item() <= 1

assert set(torch.unique(mascara).tolist()).issubset({0, 1, 2})
```

Estas comprobaciones permitirán detectar errores antes de construir los lotes.

---

### 9 · Visualizar una fotografía y su máscara

Utiliza Matplotlib para visualizar la muestra recuperada.

La fotografía se encuentra en formato:

```text
(C, H, W)
```

Para visualizarla mediante `imshow()`, conviértela a:

```text
(H, W, C)
```

Puedes utilizar:

```python
imagen.permute(1, 2, 0)
```

Para representar las tres clases de segmentación, utiliza un mapa de colores discreto.

Por ejemplo:

```python
cmap = ListedColormap([
    "#D0805C",
    "#F7F5F1",
    "#568A80"
])
```

Comprueba visualmente que la fotografía y la máscara se encuentren correctamente alineadas.

---

### 10 · Comparar augmentation y procesamiento determinista

Recupera dos veces una misma muestra del conjunto de entrenamiento:

```python
imagen_1, mascara_1 = train_dataset[0]

imagen_2, mascara_2 = train_dataset[0]
```

Después, recupera una muestra de validación.

Visualiza los tres resultados.

Observa que las dos llamadas al Dataset de entrenamiento pueden producir transformaciones diferentes, aunque se utilice el mismo índice.

En validación, el procesamiento no debe introducir cambios aleatorios.

> [!NOTE]
> Debido a la naturaleza aleatoria de las transformaciones, dos llamadas pueden producir resultados diferentes o coincidir ocasionalmente.
>
> Esto no modifica la pertenencia de la muestra al conjunto experimental.

---

### 11 · Crear los objetos DataLoader

Ahora construiremos los objetos que organizarán las muestras en lotes.

Utilizaremos inicialmente:

```python
BATCH_SIZE = 4
```

Crea los siguientes objetos:

```python
train_loader
val_loader
test_loader
```

Con esta configuración:

| Parámetro | Train | Validation | Test |
|---|---|---|---|
| `batch_size` | 4 | 4 | 4 |
| `shuffle` | `True` | `False` | `False` |
| `num_workers` | 0 | 0 | 0 |

**`batch_size`**

Determina cuántas muestras se agrupan en cada lote.

**`shuffle`**

Controla si se reordena la secuencia de muestras al crear cada iteración.

Utilizaremos `shuffle=True` únicamente en entrenamiento.

**`num_workers`**

Determina cuántos procesos auxiliares se utilizan para cargar las muestras.

Comenzaremos con `num_workers=0` para facilitar la ejecución y depuración en notebooks.

Después, consulta cuántos lotes contiene cada DataLoader.

---

### 12 · Recuperar e inspeccionar un batch

Solicita el primer lote de entrenamiento:

```python
imagenes, mascaras = next(iter(train_loader))
```

Para un lote completo de cuatro muestras, esperamos obtener:

| Elemento | Dimensiones |
|---|---|
| Imágenes | `(4, 3, 256, 256)` |
| Máscaras | `(4, 256, 256)` |

Recuerda que:

- `B` representa el número de muestras.
- `C` representa el número de canales.
- `H` y `W` representan las dimensiones espaciales.

Comprueba los tipos de datos y las etiquetas de las máscaras.

> [!NOTE]
> Si el número de muestras no es múltiplo de `batch_size`, el último lote puede contener menos de cuatro elementos.
>
> Esta situación es normal cuando no se utiliza `drop_last=True`.

---

### 13 · Visualizar las muestras de un batch

Finalmente, visualiza todas las fotografías y máscaras recuperadas en el primer lote.

Organiza la figura en dos columnas:

- **Izquierda:** fotografía RGB.
- **Derecha:** máscara de segmentación.

Cada fila corresponderá a una muestra del lote.

Comprueba que:

- Las fotografías se visualicen correctamente.
- Las máscaras correspondan a sus respectivas imágenes.
- Las transformaciones geométricas conserven la alineación espacial.
- Las etiquetas de segmentación sean válidas.
- Las dimensiones sean consistentes.

> [!IMPORTANT]
> Antes de entrenar una U-Net, es indispensable inspeccionar visualmente los datos.
>
> Un pipeline puede ejecutarse sin errores y, aun así, contener problemas de lectura, transformación o correspondencia entre imágenes y máscaras.

---

## 📊 Resultados esperados

Al finalizar, tu proyecto contará con tres objetos Dataset y tres objetos DataLoader:

| Conjunto | Dataset | DataLoader | Transformaciones |
|---|---|---|---|
| Entrenamiento | `train_dataset` | `train_loader` | Procesamiento + augmentation |
| Validación | `val_dataset` | `val_loader` | Procesamiento determinista |
| Prueba | `test_dataset` | `test_loader` | Procesamiento determinista |

Las fotografías estarán representadas como tensores `float32` con dimensiones `(3, 256, 256)` y valores en `[0, 1]`.

Las máscaras estarán representadas como tensores `int64` con dimensiones `(256, 256)` y etiquetas `0`, `1` y `2`.

Los DataLoader permitirán agrupar estas muestras en lotes para utilizarlas posteriormente durante el entrenamiento y la evaluación.

---

## 🧩 Punto de control

Antes de finalizar, realiza las siguientes actividades:

**1 · Cambiar la configuración experimental**

Modifica la lectura del CSV para utilizar:

```text
split_80_10_10.csv
```

Ejecuta nuevamente las celdas desde la recuperación de las particiones.

**2 · Comparar los conjuntos**

Compara el número de muestras y lotes obtenidos con las configuraciones 70/15/15 y 80/10/10.

**3 · Comprobar el aumento de datos**

Recupera dos veces la misma muestra de entrenamiento y observa los resultados.

Explica por qué pueden producirse imágenes diferentes.

**4 · Verificar las máscaras**

Comprueba que las máscaras transformadas contengan únicamente etiquetas válidas:

```text
0, 1, 2
```

**5 · Inspeccionar los lotes**

Recupera un lote de entrenamiento y comprueba sus dimensiones, tipos y correspondencia visual.

**Resultado esperado:** tres objetos Dataset y tres DataLoader correctamente construidos, con imágenes y máscaras alineadas, dimensiones y tipos adecuados, y aumento de datos exclusivo para entrenamiento.

---

## 🤔 Observa e interpreta

Al finalizar la práctica, responde las siguientes preguntas:

1. ¿Por qué recuperamos las particiones desde archivos CSV en lugar de volver a dividir el Oxford-IIIT Pet Dataset?
2. ¿Qué diferencia existe entre las funciones de `Dataset` y `DataLoader`?
3. ¿Qué función cumple cada uno de los métodos `__init__()`, `__len__()` y `__getitem__()`?
4. ¿Por qué debemos aplicar las transformaciones geométricas de manera sincronizada a fotografías y máscaras?
5. ¿Por qué utilizamos `fill_mask=2` durante el *padding* de las máscaras originales?
6. ¿Por qué convertimos las fotografías a `float32` y las máscaras a `int64`?
7. ¿Qué diferencia existe entre las dimensiones `(H, W, C)` y `(C, H, W)`?
8. ¿Qué controla el parámetro `batch_size` y qué ocurre cuando el número de muestras no es múltiplo de este valor?
9. ¿Qué diferencia existe entre utilizar `shuffle=True` y `shuffle=False`?
10. ¿Por qué es necesario verificar visualmente los lotes antes de comenzar el entrenamiento de una U-Net?

---

## ✅ Punto de control final

Al finalizar esta práctica habrás:

- Recuperado el proyecto principal del Oxford-IIIT Pet Dataset.
- Reutilizado el archivo `dataset.json`.
- Recuperado las particiones experimentales guardadas en CSV.
- Construido un notebook para el pipeline de datos.
- Definido transformaciones comunes mediante Albumentations.
- Aplicado *data augmentation* únicamente al conjunto de entrenamiento.
- Conservado la relación de aspecto mediante redimensionamiento y *padding*.
- Implementado una clase personalizada que hereda de `Dataset`.
- Comprendido los métodos `__init__()`, `__len__()` y `__getitem__()`.
- Convertido fotografías y máscaras a tensores de PyTorch.
- Verificado dimensiones, tipos de datos y etiquetas de segmentación.
- Creado tres objetos Dataset y tres objetos DataLoader.
- Configurado `batch_size`, `shuffle` y `num_workers`.
- Recuperado e inspeccionado lotes de imágenes y máscaras.
- Visualizado las muestras de un lote.
- Comparado las configuraciones experimentales 70/15/15 y 80/10/10.
- Comprobado que el pipeline conserva la correspondencia espacial entre fotografías y máscaras.

---

## 🏁 ¡Práctica completada!

Has construido un pipeline de datos para segmentación de imágenes utilizando el Oxford-IIIT Pet Dataset que has preparado durante el taller.

Ahora nuestro proyecto cuenta con los mecanismos necesarios para **recuperar, transformar, convertir y organizar fotografías y máscaras en lotes**, conservando las particiones experimentales definidas anteriormente.

También hemos comprobado que las transformaciones aleatorias se aplican únicamente durante el entrenamiento y que los datos mantienen dimensiones, tipos y etiquetas adecuados.

**Este pipeline será la conexión entre nuestro dataset y el modelo U-Net que construiremos posteriormente.**

---

## 📚 Dataset de referencia

**Oxford-IIIT Pet Dataset**

Parkhi, O. M., Vedaldi, A., Zisserman, A., & Jawahar, C. V. (2012).

*Cats and Dogs.*

IEEE Conference on Computer Vision and Pattern Recognition (CVPR).

[Consultar el dataset original →](https://www.robots.ox.ac.uk/~vgg/data/pets/)

---

## 🔗 Enlaces

[**← Volver a Inventario y configuración del Oxford Dataset**](./04-inventario-y-configuracion-del-oxford-dataset.md)

[← Volver a Construcción del pipeline de datos](../../../modulos/04-diseno-experimental-y-pipeline-datos/04-02-construccion-pipeline-datos.md)