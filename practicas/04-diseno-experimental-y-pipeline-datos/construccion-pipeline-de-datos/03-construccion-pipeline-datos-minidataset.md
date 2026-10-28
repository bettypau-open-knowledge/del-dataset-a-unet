# 🔄 Construcción del pipeline de datos del minidataset con PyTorch

En la práctica anterior, **[Diseño de los conjuntos experimentales del minidataset](../diseno-conjuntos-experimentales/01-diseno-conjuntos-experimentales-minidataset.md)**, aprendimos a organizar nuestras imágenes en conjuntos de entrenamiento (*train*), validación (*validation*) y prueba (*test*).

Utilizamos una partición aleatoria estratificada por raza y generamos dos configuraciones experimentales: **70/15/15 y 80/10/10**.

También comprobamos que las particiones conservaran los identificadores originales y que cada fotografía permaneciera asociada con su máscara de segmentación.

Ahora que tenemos nuestros conjuntos experimentales definidos, debemos resolver una nueva pregunta:

**¿Cómo podemos recuperar, transformar y organizar estas imágenes y máscaras para utilizarlas durante el entrenamiento y la evaluación de un modelo de Deep Learning?**

En esta práctica construiremos un **pipeline de datos mediante PyTorch**, utilizando las clases `Dataset` y `DataLoader`.

Nuestro pipeline permitirá:

1. Recuperar las particiones experimentales que generamos anteriormente.
2. Localizar y leer las fotografías y máscaras del minidataset.
3. Aplicar transformaciones mediante Albumentations.
4. Convertir las imágenes y máscaras a tensores de PyTorch.
5. Organizar las muestras en lotes (*batches*).
6. Verificar las dimensiones, tipos de datos, etiquetas y correspondencia visual entre imágenes y máscaras.

Además, aprenderemos a aplicar **data augmentation exclusivamente al conjunto de entrenamiento**, manteniendo un procesamiento determinista para validación y prueba.

---

## 🎯 Objetivo

Construir y verificar un pipeline de datos para segmentación de imágenes mediante PyTorch, reutilizando los conjuntos experimentales del minidataset y aplicando transformaciones adecuadas a fotografías y máscaras.

Al finalizar, serás capaz de:

- Recuperar particiones experimentales previamente definidas.
- Configurar transformaciones mediante Albumentations.
- Diferenciar el procesamiento de entrenamiento del utilizado en validación y prueba.
- Implementar una clase personalizada que herede de `torch.utils.data.Dataset`.
- Comprender los métodos `__init__()`, `__len__()` y `__getitem__()`.
- Convertir imágenes y máscaras a tensores con dimensiones y tipos adecuados.
- Crear objetos `DataLoader` para organizar las muestras en lotes.
- Configurar `batch_size`, `shuffle` y `num_workers`.
- Inspeccionar y visualizar las muestras recuperadas por el pipeline.
- Verificar que las imágenes y máscaras conserven su correspondencia espacial.

---

## 📦 Repositorio de la práctica

Para esta actividad **continuaremos utilizando el repositorio de la práctica anterior**:

**[Abrir repositorio del minidataset en GitHub →](https://github.com/bettypau-open-knowledge/del-dataset-a-unet_conjuntos-experimentales-minidataset)**

No es necesario descargar nuevamente el minidataset ni crear otro proyecto.

Únicamente deberás incorporar el notebook proporcionado:


[pipeline_de_datos.ipynb](../../../recursos/codigo/04-diseno-experimental-y-pipeline-datos/pipeline_de_datos.ipynb)


dentro del directorio `notebooks/` del proyecto que ya tienes en Visual Studio Code.

> [!IMPORTANT]
> Esta práctica utiliza los archivos CSV generados durante **Diseño de los conjuntos experimentales del minidataset**.
>
> Antes de comenzar, comprueba que completaste aquella práctica y que los archivos `split_70_15_15.csv` y `split_80_10_10.csv` se encuentran disponibles.
>
> **No volveremos a ejecutar `train_test_split()`**, porque las particiones experimentales ya están definidas.

---

## 📁 Organización del proyecto

La estructura relevante del proyecto deberá quedar de la siguiente manera:

```text
del-dataset-a-unet_conjuntos-experimentales-minidataset/
├── config/
│   └── dataset.json
├── data/
│   ├── manifests/
│   │   └── manifest.csv
│   ├── raw/
│   │   ├── images/
│   │   │   ├── chihuahua/
│   │   │   ├── Maine_Coon/
│   │   │   ├── Siamese/
│   │   │   └── Sphynx/
│   │   └── list.txt
│   └── splits/
│       ├── split_70_15_15.csv
│       └── split_80_10_10.csv
└── notebooks/
    ├── conjuntos_experimentales.ipynb
    └── pipeline_de_datos.ipynb
```

| Archivo | Función |
|---|---|
| `config/dataset.json` | Contiene la configuración de las rutas del proyecto. |
| `data/manifests/manifest.csv` | Registra las muestras del minidataset y sus archivos asociados. |
| `data/raw/images/` | Almacena las fotografías y máscaras originales. |
| `data/splits/split_70_15_15.csv` | Contiene la primera configuración experimental. |
| `data/splits/split_80_10_10.csv` | Contiene la segunda configuración experimental. |
| `notebooks/conjuntos_experimentales.ipynb` | Notebook utilizado para construir las particiones. |
| `notebooks/pipeline_de_datos.ipynb` | Notebook que utilizaremos para construir el pipeline de datos. |

> [!NOTE]
> No debes modificar ni reorganizar los archivos originales del minidataset.
>
> El pipeline recuperará las fotografías y máscaras mediante las rutas registradas en los archivos CSV.

---

## 💻 Requisitos

Para realizar la práctica necesitarás Visual Studio Code, un entorno de Python compatible con Jupyter Notebooks y las siguientes bibliotecas:

| Biblioteca | Función |
|---|---|
| `pathlib` | Construcción y manejo de rutas. |
| `json` | Lectura del archivo de configuración. |
| `numpy` | Manipulación de arreglos y conversión de tipos. |
| `pandas` | Lectura y filtrado de las particiones experimentales. |
| `opencv-python` | Lectura de fotografías y máscaras. |
| `albumentations` (2.x) | Transformaciones geométricas y fotométricas. |
| `torch` | Construcción y manipulación de tensores. |
| `matplotlib` | Visualización de imágenes, máscaras y lotes. |

`pathlib` y `json` forman parte de la biblioteca estándar de Python.

---

## 💻 Instrucciones

### 1 · Abre el proyecto de la práctica anterior

Abre en Visual Studio Code la carpeta principal del repositorio del minidataset.

Comprueba que se encuentren disponibles los archivos:

```text
config/dataset.json
data/splits/split_70_15_15.csv
data/splits/split_80_10_10.csv
```

### 2 · Incorpora el notebook

Coloca el archivo proporcionado `pipeline_de_datos.ipynb` dentro de `notebooks/`.

Abre el notebook y selecciona el kernel correspondiente al entorno de Python del taller.

### 3 · Verifica el directorio de trabajo

El notebook utiliza:

```python
PROYECTO = Path("..").resolve()
```

Esta instrucción considera que el directorio de trabajo de Python es `notebooks/`.

> [!IMPORTANT]
> Si el directorio de trabajo es diferente, las rutas podrían construirse incorrectamente.
>
> Comprueba la ubicación desde la que se ejecuta el notebook antes de continuar.

### 4 · Ejecuta las actividades

Ejecuta las celdas en el orden indicado.

Durante la práctica inspeccionaremos tanto las salidas de texto como las visualizaciones de fotografías, máscaras y lotes.

---

## 🧪 Actividades de la práctica

### 1 · Importar las bibliotecas necesarias

Comenzaremos importando las bibliotecas que utilizaremos para recuperar, transformar y organizar las muestras.

En particular, importaremos las clases:

```python
from torch.utils.data import Dataset, DataLoader
```

Estas clases cumplen funciones diferentes:

- **`Dataset`:** define cómo recuperar y preparar una muestra individual.
- **`DataLoader`:** solicita muestras al Dataset y las organiza en lotes.

Ambas serán necesarias para construir nuestro pipeline.

---

### 2 · Recuperar la configuración del proyecto

Leeremos el archivo:

```text
config/dataset.json
```

Mediante `pathlib` y `json`, recuperaremos las rutas necesarias para localizar las fotografías, el manifest y los archivos de partición.

El notebook utiliza la configuración existente para construir las rutas del proyecto.

**Considera:** ¿qué ventajas tiene recuperar las rutas desde un archivo de configuración en lugar de escribirlas manualmente en diferentes celdas?

---

### 3 · Recuperar los conjuntos experimentales

Comenzaremos utilizando la configuración **70/15/15** generada durante la práctica anterior.

El notebook recupera:

```python
splits = pd.read_csv(
    DIRECTORIO_SPLITS / "split_70_15_15.csv"
)
```

Después, separa los registros según la columna `split`:

```python
train_df = splits[splits["split"] == "train"].reset_index(drop=True)

val_df = splits[splits["split"] == "validation"].reset_index(drop=True)

test_df = splits[splits["split"] == "test"].reset_index(drop=True)
```

Obtendremos tres DataFrames, uno por cada conjunto experimental.

> [!IMPORTANT]
> En esta etapa no estamos generando nuevas particiones.
>
> Únicamente recuperamos las asignaciones que ya habíamos establecido y guardado en archivos CSV.

**Considera:** ¿por qué es importante conservar los mismos conjuntos experimentales durante las diferentes etapas de desarrollo de un modelo?

---

### 4 · Definir los pipelines de Albumentations

Ahora estableceremos las transformaciones que aplicaremos a las fotografías y máscaras.

Comenzaremos definiendo un procesamiento común para los tres conjuntos experimentales.

**Procesamiento común**

Utilizaremos:

- `A.LongestMaxSize()`: redimensiona proporcionalmente la imagen, conservando su relación de aspecto.
- `A.PadIfNeeded()`: completa las dimensiones hasta obtener imágenes y máscaras de **256 × 256 píxeles**.

El procesamiento utiliza interpolación bilineal para las fotografías y vecino más cercano para las máscaras.

Para las regiones agregadas mediante *padding*, se utiliza:

```python
fill=0
fill_mask=2
```

El valor `0` produce bordes negros en la fotografía.

El valor `2` corresponde a la etiqueta de fondo de las máscaras originales del Oxford-IIIT Pet Dataset.

**Aumento de datos para entrenamiento**

Además del procesamiento común, aplicaremos cuatro transformaciones aleatorias:

| Transformación | Probabilidad |
|---|---:|
| Rotación de hasta ±20° | 50 % |
| Volteo horizontal | 50 % |
| Modificación de brillo | 50 % |
| Modificación de contraste | 50 % |

Cada transformación realiza su propia decisión aleatoria.

Las transformaciones geométricas se aplican de manera sincronizada a fotografía y máscara, mientras que los cambios de brillo y contraste afectan únicamente a la fotografía.

**Procesamiento para validación y prueba**

En estos conjuntos utilizaremos únicamente las transformaciones comunes de redimensionamiento y *padding*.

No aplicaremos aumentos aleatorios.

> [!NOTE]
> Una probabilidad de aplicación del 50 % no significa que una transformación se ejecutará exactamente en la mitad de las muestras.
>
> Cada vez que se solicita una muestra, se realiza una decisión aleatoria independiente.

**Considera:** ¿por qué es importante utilizar un procesamiento determinista para los conjuntos de validación y prueba?

---

### 5 · Implementar la clase `PetSegmentationDataset`

Construiremos una clase personalizada que herede de `Dataset`.

```python
class PetSegmentationDataset(Dataset):
    ...
```

Nuestra clase implementará tres métodos fundamentales.

**`__init__()` — Inicialización**

Se ejecuta cuando creamos el objeto.

Almacena el DataFrame correspondiente, el directorio de imágenes y el pipeline de transformaciones.

**`__len__()` — Longitud**

Devuelve el número de muestras disponibles en el Dataset.

Esto permite conocer cuántos registros contiene cada conjunto experimental.

**`__getitem__()` — Recuperación de una muestra**

Se ejecuta cuando solicitamos una muestra mediante su índice.

Este método:

1. Recupera una fila del DataFrame.
2. Construye las rutas de la fotografía y su máscara.
3. Lee ambos archivos mediante OpenCV.
4. Convierte la fotografía de BGR a RGB.
5. Aplica las transformaciones sincronizadas.
6. Convierte los datos a los tipos adecuados.
7. Construye los tensores de PyTorch.
8. Devuelve la fotografía y su máscara.

Al finalizar, cada muestra tendrá los siguientes formatos:

| Elemento | Tipo | Dimensiones |
|---|---|---|
| Fotografía | `torch.float32` | `(3, 256, 256)` |
| Máscara | `torch.int64` | `(256, 256)` |

Los valores de la fotografía estarán escalados al intervalo `[0, 1]`.

Las etiquetas originales de la máscara se convertirán de:

```text
1, 2, 3
```

a:

```text
0, 1, 2
```

Por lo tanto, las clases utilizadas serán:

| Etiqueta original | Etiqueta nueva | Región |
|---|---|---|
| 1 | 0 | Animal |
| 2 | 1 | Fondo |
| 3 | 2 | Contorno |

> [!IMPORTANT]
> Las máscaras contienen etiquetas categóricas, por lo que no deben normalizarse como si fueran fotografías.
>
> La conversión de etiquetas permite trabajar con clases numeradas desde cero, conservando su significado.

---

### 6 · Crear los tres objetos `Dataset`

Una vez implementada la clase, construiremos tres objetos:

```python
train_dataset
val_dataset
test_dataset
```

Cada objeto utilizará el DataFrame correspondiente a su conjunto experimental.

Sin embargo, los pipelines de transformación serán diferentes:

| Dataset | Transformaciones |
|---|---|
| `train_dataset` | Procesamiento común + data augmentation |
| `val_dataset` | Procesamiento común |
| `test_dataset` | Procesamiento común |

Después, utilizaremos `len()` para consultar la cantidad de muestras de cada Dataset.

**Considera:** ¿por qué podemos utilizar una misma clase `Dataset` para los tres conjuntos, aunque sus transformaciones sean diferentes?

---

### 7 · Recuperar una muestra y verificar los tensores

Solicitaremos una muestra mediante:

```python
imagen, mascara = train_dataset[0]
```

Esta instrucción llama internamente al método `__getitem__(0)`.

Después, inspeccionaremos:

- Las dimensiones de la fotografía.
- Las dimensiones de la máscara.
- Los tipos de datos.
- El intervalo de valores de la fotografía.
- Las etiquetas presentes en la máscara.

Utilizaremos instrucciones `assert` para comprobar que:

- La fotografía sea de tipo `torch.float32`.
- La máscara sea de tipo `torch.int64`.
- Los valores de la fotografía estén entre `0` y `1`.
- Las etiquetas de la máscara pertenezcan al conjunto `{0, 1, 2}`.

**Considera:** ¿por qué es necesario verificar las dimensiones y los tipos antes de entregar los datos a una red neuronal?

---

### 8 · Visualizar una fotografía y su máscara

Ahora visualizaremos la muestra recuperada mediante Matplotlib.

La fotografía se encuentra en formato:

```text
(C, H, W)
```

Sin embargo, `imshow()` espera que una imagen RGB tenga sus dimensiones organizadas como:

```text
(H, W, C)
```

Por ello, utilizaremos:

```python
imagen.permute(1, 2, 0)
```

La máscara se visualizará mediante un mapa de colores discreto para distinguir las tres clases.

Observa que la fotografía y su máscara conservan su correspondencia espacial.

---

### 9 · Comparar data augmentation y procesamiento determinista

En esta actividad visualizaremos tres resultados:

1. Primera recuperación de una muestra de entrenamiento.
2. Segunda recuperación de esa misma muestra de entrenamiento.
3. Recuperación de una muestra de validación.

Las dos primeras llamadas utilizan el mismo índice de entrenamiento, pero pueden producir resultados diferentes debido a las transformaciones aleatorias.

En cambio, el conjunto de validación utiliza únicamente el procesamiento determinista.

> [!NOTE]
> Como las transformaciones de entrenamiento son aleatorias, dos ejecuciones pueden producir resultados diferentes, aunque también podrían coincidir ocasionalmente.
>
> La ausencia de diferencias visibles en una ejecución no significa necesariamente que el pipeline de aumento de datos esté desactivado.

**Considera:** ¿qué diferencia existe entre modificar aleatoriamente una muestra de entrenamiento y cambiar la asignación de una muestra a otro conjunto experimental?

---

### 10 · Crear los objetos `DataLoader`

Ahora utilizaremos `DataLoader` para organizar las muestras en lotes.

El notebook utiliza:

```python
BATCH_SIZE = 4
```

Crearemos tres objetos:

```python
train_loader
val_loader
test_loader
```

Con la siguiente configuración:

| Parámetro | Entrenamiento | Validación | Prueba |
|---|---|---|---|
| `batch_size` | 4 | 4 | 4 |
| `shuffle` | `True` | `False` | `False` |
| `num_workers` | 0 | 0 | 0 |

**`batch_size=4`**

Cada lote contendrá hasta cuatro muestras.

Si el número total de muestras no es múltiplo de cuatro, el último lote podrá contener menos elementos.

**`shuffle=True`**

Permite reordenar las muestras al crear cada iteración del conjunto de entrenamiento.

No modifica las asignaciones a *train*, *validation* o *test*.

**`num_workers=0`**

La carga de datos se realiza en el proceso principal.

Esta configuración resulta adecuada para comenzar a trabajar con DataLoader en notebooks, especialmente en Windows.

Después, utilizaremos `len()` para consultar cuántos lotes contiene cada DataLoader.

---

### 11 · Recuperar e inspeccionar un batch

Solicitaremos el primer lote de entrenamiento mediante:

```python
imagenes, mascaras = next(iter(train_loader))
```

Al utilizar `batch_size=4`, esperamos obtener tensores con las siguientes dimensiones para un lote completo:

| Elemento | Dimensiones |
|---|---|
| Imágenes | `(4, 3, 256, 256)` |
| Máscaras | `(4, 256, 256)` |

En este caso:

- `4` representa el número de muestras del lote.
- `3` representa los canales RGB.
- `256 × 256` representa las dimensiones espaciales.

También comprobaremos que:

- Los tensores tengan el número correcto de dimensiones.
- Las imágenes y máscaras contengan la misma cantidad de muestras.
- Las fotografías sean de tipo `float32`.
- Las máscaras sean de tipo `int64`.
- Las etiquetas de segmentación pertenezcan a `{0, 1, 2}`.

---

### 12 · Visualizar las muestras de un batch

Finalmente, visualizaremos todas las fotografías y máscaras del lote recuperado.

La figura mostrará dos columnas:

- **Izquierda:** fotografía RGB.
- **Derecha:** máscara de segmentación.

Cada fila corresponderá a una muestra del lote.

Esta visualización permitirá comprobar que:

- Las fotografías se recuperan correctamente.
- Las máscaras corresponden a sus respectivas imágenes.
- Las transformaciones geométricas mantienen la alineación espacial.
- Las etiquetas de segmentación se conservan.
- Las dimensiones son consistentes entre las muestras.

> [!IMPORTANT]
> Antes de entrenar una U-Net, es fundamental inspeccionar visualmente los lotes.
>
> Un pipeline puede ejecutarse sin errores de Python y, aun así, contener problemas de correspondencia entre imágenes y máscaras que afecten el entrenamiento.

---

## 📊 Resultados esperados

Al finalizar la práctica, habrás construido tres objetos `Dataset` y tres objetos `DataLoader`.

| Conjunto | Dataset | DataLoader | Transformaciones |
|---|---|---|---|
| Entrenamiento | `train_dataset` | `train_loader` | Procesamiento + augmentation |
| Validación | `val_dataset` | `val_loader` | Procesamiento determinista |
| Prueba | `test_dataset` | `test_loader` | Procesamiento determinista |

Cada muestra contendrá una fotografía RGB y su máscara de segmentación.

Las fotografías estarán representadas como tensores `float32` con dimensiones `(3, 256, 256)` y valores en `[0, 1]`.

Las máscaras estarán representadas como tensores `int64` con dimensiones `(256, 256)` y etiquetas `0`, `1` y `2`.

Los DataLoader permitirán agrupar estas muestras en lotes para su utilización posterior.

---

## 🧩 Punto de control

Antes de finalizar, realiza las siguientes actividades:

**1 · Cambiar la configuración experimental**

Modifica la carga del CSV para utilizar:

```text
split_80_10_10.csv
```

Ejecuta nuevamente el notebook desde la celda de carga de particiones.

**2 · Comparar los conjuntos**

Compara la cantidad de muestras y lotes obtenidos con las configuraciones 70/15/15 y 80/10/10.

**3 · Comprobar el aumento de datos**

Ejecuta dos veces la celda de visualización de entrenamiento.

Observa si las transformaciones producen resultados diferentes y explica por qué pueden cambiar entre ejecuciones.

**4 · Verificar las máscaras**

Comprueba que las máscaras continúen utilizando únicamente las etiquetas enteras:

```text
0, 1, 2
```

**5 · Explicar el procesamiento de evaluación**

Explica por qué no aplicamos rotaciones, volteos, cambios de brillo ni modificaciones de contraste aleatorios a los conjuntos de validación y prueba.

**Resultado esperado:** tres objetos Dataset y tres DataLoader con fotografías y máscaras alineadas, dimensiones y tipos correctos, y aumento de datos exclusivo para entrenamiento.

---

## 🤔 Observa e interpreta

Al finalizar la práctica, responde las siguientes preguntas:

1. ¿Cuál es la diferencia entre las funciones de `Dataset` y `DataLoader`?
2. ¿Por qué recuperamos las particiones desde un archivo CSV en lugar de volver a dividir el dataset?
3. ¿Qué función cumple cada uno de los métodos `__init__()`, `__len__()` y `__getitem__()`?
4. ¿Por qué debemos aplicar las transformaciones geométricas de manera sincronizada a las fotografías y sus máscaras?
5. ¿Por qué utilizamos `fill_mask=2` antes de convertir las etiquetas de segmentación?
6. ¿Por qué las fotografías se convierten a `float32` y las máscaras a `int64`?
7. ¿Qué diferencia existe entre las dimensiones `(H, W, C)` y `(C, H, W)`?
8. ¿Qué controla el parámetro `batch_size` y qué sucede cuando el número de muestras no es múltiplo del tamaño de lote?
9. ¿Qué diferencia existe entre utilizar `shuffle=True` y `shuffle=False`?
10. ¿Por qué es importante verificar visualmente los lotes antes de comenzar el entrenamiento de un modelo?

---

## ✅ Punto de control final

Al finalizar esta práctica habrás:

- Recuperado el proyecto del minidataset utilizado anteriormente.
- Incorporado el notebook `pipeline_de_datos.ipynb` dentro de `notebooks/`.
- Reutilizado el archivo `dataset.json`.
- Recuperado los conjuntos experimentales desde los CSV.
- Definido transformaciones comunes para imágenes y máscaras.
- Aplicado data augmentation únicamente al conjunto de entrenamiento.
- Conservado la relación de aspecto mediante redimensionamiento y padding.
- Implementado una clase personalizada que hereda de `Dataset`.
- Comprendido los métodos `__init__()`, `__len__()` y `__getitem__()`.
- Convertido fotografías y máscaras a tensores de PyTorch.
- Verificado dimensiones, tipos de datos y etiquetas de segmentación.
- Visualizado fotografías y máscaras recuperadas mediante Dataset.
- Creado tres objetos DataLoader.
- Configurado `batch_size`, `shuffle` y `num_workers`.
- Recuperado y verificado un lote de imágenes y máscaras.
- Visualizado las muestras de un lote completo.
- Comparado los resultados de las configuraciones 70/15/15 y 80/10/10.
- Comprobado que el pipeline mantiene la correspondencia entre fotografías y máscaras.

---

## 🏁 ¡Práctica completada!

Has construido un pipeline de datos para segmentación de imágenes utilizando PyTorch.

Ahora nuestro proyecto cuenta con los mecanismos necesarios para **recuperar, transformar, convertir y organizar las fotografías y máscaras en lotes**, conservando las particiones experimentales definidas anteriormente.

También hemos comprobado que las transformaciones aleatorias se aplican exclusivamente durante el entrenamiento y que los datos mantienen dimensiones, tipos y etiquetas adecuados.

**Este pipeline será la conexión entre nuestro dataset y el modelo U-Net que construiremos posteriormente.**

---

## 📚 Dataset de referencia

Esta práctica utiliza una selección reducida y reorganizada del **Oxford-IIIT Pet Dataset**, preparada con fines didácticos.

**Referencia:**

Parkhi, O. M., Vedaldi, A., Zisserman, A., & Jawahar, C. V. (2012).

*Cats and Dogs.*

IEEE Conference on Computer Vision and Pattern Recognition (CVPR).

[Consultar el dataset original →](https://www.robots.ox.ac.uk/~vgg/data/pets/)

---

## 🔗 Enlaces

[**Abrir repositorio del minidataset →**](https://github.com/bettypau-open-knowledge/del-dataset-a-unet_conjuntos-experimentales-minidataset)

[← Volver a Construcción del pipeline de datos](../../../modulos/04-diseno-experimental-y-pipeline-datos/04-02-construccion-pipeline-datos.md)