# 🧪 Diseño de conjuntos experimentales del Oxford-IIIT Pet Dataset

En la práctica anterior de diseño de conjuntos experimentales utilizamos un minidataset para aprender a construir particiones de entrenamiento, validación y prueba mediante Python y scikit-learn.

Generamos dos configuraciones, **70/15/15 y 80/10/10**, utilizamos una semilla fija para facilitar la reproducibilidad y verificamos que las muestras estuvieran correctamente distribuidas.

Ahora aplicaremos estos conocimientos al **Oxford-IIIT Pet Dataset que hemos trabajado a lo largo del taller**.

A diferencia de la práctica con el minidataset, en esta ocasión no utilizaremos un repositorio independiente. Continuaremos trabajando en nuestro proyecto de Visual Studio Code, aprovechando los archivos que generamos anteriormente.

En particular, retomaremos el archivo de configuración `dataset.json` y el inventario `manifest.csv` que construimos en la práctica:

**[Inventario y configuración del Oxford-IIIT Pet Dataset](../../02-ingenieria-del-dataset/inventario-y-configuracion-del-dataset/04-inventario-y-configuracion-del-oxford-dataset.md)**

Nuestro propósito será construir y guardar conjuntos experimentales reproducibles que posteriormente podremos utilizar para entrenar y evaluar un modelo de segmentación.

---

## 🎯 Objetivo

Diseñar y verificar los conjuntos de entrenamiento (*train*), validación (*validation*) y prueba (*test*) del Oxford-IIIT Pet Dataset mediante Python, reutilizando el archivo de configuración y el manifest del proyecto.

Al finalizar, serás capaz de:

- Recuperar la configuración y el inventario generados en prácticas anteriores.
- Identificar la variable adecuada para realizar una partición estratificada.
- Generar conjuntos experimentales con proporciones 70/15/15 y 80/10/10.
- Utilizar una semilla fija para obtener particiones reproducibles.
- Comparar la distribución de las categorías entre los conjuntos.
- Verificar que no existan identificadores duplicados u omitidos.
- Mantener asociadas las fotografías y sus máscaras de segmentación.
- Guardar las particiones en archivos CSV para reutilizarlas en las siguientes prácticas.

---

## 📁 Organización del proyecto

Continuaremos utilizando el proyecto de Visual Studio Code que hemos desarrollado durante el taller.

No es necesario crear otro proyecto ni volver a descargar el Oxford-IIIT Pet Dataset.

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
    └── conjuntos_experimentales_oxford.ipynb
```

Los archivos dentro de `data/splits/` se generarán durante esta práctica.

El notebook `conjuntos_experimentales_oxford.ipynb` será un archivo nuevo que crearás dentro de `notebooks/`.

> [!IMPORTANT]
> No debes mover, renombrar ni duplicar las imágenes y máscaras originales.
>
> Las particiones se registrarán mediante archivos CSV que conservarán las rutas de las fotografías y sus máscaras, junto con la asignación del conjunto experimental.

---

## 💻 Requisitos

Para realizar esta práctica necesitarás:

- Visual Studio Code con soporte para Jupyter Notebooks.
- El entorno de Python utilizado durante el taller.
- El Oxford-IIIT Pet Dataset organizado en tu proyecto.
- El archivo `config/dataset.json`.
- El archivo `data/manifests/manifest.csv`.

Utilizaremos las siguientes bibliotecas:

| Biblioteca | Función |
|---|---|
| `pathlib` | Construcción y manejo de rutas. |
| `json` | Lectura de la configuración del proyecto. |
| `pandas` | Lectura del manifest, organización de las particiones y exportación a CSV. |
| `scikit-learn` | Generación de particiones aleatorias estratificadas. |

---

## 💻 Preparación de la práctica

### 1 · Recupera el trabajo anterior

Antes de comenzar, revisa los resultados de la práctica:

**[Inventario y configuración del Oxford-IIIT Pet Dataset](../../02-ingenieria-del-dataset/inventario-y-configuracion-del-dataset/04-inventario-y-configuracion-del-oxford-dataset.md)**

Comprueba que dispones de:

```text
config/dataset.json
data/manifests/manifest.csv
```

El archivo `dataset.json` contiene la configuración necesaria para localizar los directorios y archivos del proyecto.

El archivo `manifest.csv` contiene el inventario de las muestras, incluyendo los identificadores y las rutas que permiten relacionar fotografías y máscaras.

Estos archivos serán el punto de partida de la nueva práctica.

### 2 · Crea el notebook

Dentro de `notebooks/`, crea un archivo llamado:

```text
conjuntos_experimentales_oxford.ipynb
```

Selecciona el kernel correspondiente al entorno de Python del taller.

### 3 · Prepara las bibliotecas

En la primera celda de código, importa las bibliotecas necesarias:

```python
from pathlib import Path
import json

import pandas as pd
from sklearn.model_selection import train_test_split
```

---

## 🧪 Actividades de la práctica

### 1 · Recuperar la configuración del proyecto

Comenzaremos leyendo el archivo `dataset.json` que generamos anteriormente.

Utiliza `pathlib` para localizar el directorio principal del proyecto y construir la ruta del archivo de configuración.

Después, recupera su contenido mediante `json`.

> [!NOTE]
> Recuerda que las rutas relativas dependen del directorio de trabajo desde el cual se ejecuta Python.
>
> Comprueba el directorio de trabajo de tu notebook antes de construir las rutas.

**Punto de comprobación:** debes poder recuperar la configuración del proyecto sin escribir manualmente las rutas de todas las fotografías y máscaras.

---

### 2 · Recuperar el manifest

Utiliza la configuración del proyecto para localizar el archivo `manifest.csv`.

Después, cárgalo mediante pandas:

```python
manifest = pd.read_csv(ruta_manifest)
```

Explora su contenido utilizando:

```python
manifest.head()
manifest.info()
manifest.columns
```

Identifica las columnas que contienen:

- El identificador de cada imagen.
- La categoría o raza de la muestra.
- La ruta de la fotografía.
- La ruta de la máscara de segmentación.

> [!IMPORTANT]
> Utiliza los nombres de columnas definidos en el manifest que construiste anteriormente.
>
> Si son diferentes de los utilizados en el minidataset, adapta las instrucciones del notebook a la estructura real de tu archivo.

**Considera:** ¿por qué es importante utilizar el manifest como fuente de información para construir las particiones?

---

### 3 · Inspeccionar las categorías disponibles

Antes de dividir el dataset, analiza la distribución de las categorías.

Identifica la columna que representa la raza de cada animal y calcula cuántas muestras corresponden a cada categoría.

Puedes utilizar:

```python
manifest[columna_raza].value_counts()
```

Donde `columna_raza` representa el nombre de la columna correspondiente en tu manifest.

Observa si todas las categorías tienen la misma cantidad de muestras.

**Considera:** ¿qué podría ocurrir si realizamos una partición completamente aleatoria sin considerar la distribución de las categorías?

---

### 4 · Generar la partición 70/15/15

Construiremos nuestra primera configuración experimental:

| Conjunto | Proporción |
|---|---:|
| Train | 70 % |
| Validation | 15 % |
| Test | 15 % |

Utilizaremos `train_test_split()` de scikit-learn con estratificación por raza.

Para obtener las tres particiones, podemos realizar dos separaciones consecutivas.

**Primera separación**

Separa el 70 % de las muestras para entrenamiento y reserva el 30 % restante.

**Segunda separación**

Divide el 30 % reservado en dos partes iguales para obtener validación y prueba.

Utiliza una semilla fija:

```python
SEMILLA = 42
```

En ambas separaciones, aplica estratificación utilizando la columna correspondiente a la raza.

> [!TIP]
> Para obtener una distribución 70/15/15 mediante dos llamadas a `train_test_split()`, primero debes reservar el 30 % y después dividir ese subconjunto en dos partes iguales.
>
> Recuerda que las proporciones de la segunda separación se calculan respecto al subconjunto que estás dividiendo.

---

### 5 · Generar la partición 80/10/10

Ahora construiremos una segunda configuración:

| Conjunto | Proporción |
|---|---:|
| Train | 80 % |
| Validation | 10 % |
| Test | 10 % |

Repite el procedimiento anterior, pero esta vez:

1. Reserva el 80 % para entrenamiento.
2. Divide el 20 % restante en dos partes iguales.

Utiliza nuevamente la misma semilla para facilitar la reproducibilidad de cada procedimiento.

**Considera:** ¿qué diferencias existen entre disponer del 70 % y del 80 % de las muestras para entrenamiento?

---

### 6 · Asignar las etiquetas de partición

Una vez obtenidos los tres conjuntos, agrega una columna que indique a cuál pertenece cada muestra.

Utiliza las siguientes etiquetas:

```text
train
validation
test
```

Cada registro deberá conservar la información necesaria para identificar su fotografía y su máscara.

Después, reúne los tres subconjuntos en un solo DataFrame por configuración.

Puedes utilizar:

```python
pd.concat()
```

Al finalizar, tendrás dos DataFrames: uno correspondiente a 70/15/15 y otro a 80/10/10.

---

### 7 · Comparar la distribución de categorías

Utiliza tablas de contingencia para observar cómo se distribuyeron las razas entre los conjuntos.

Puedes emplear:

```python
pd.crosstab(
    particion[columna_raza],
    particion["split"]
)
```

Genera una tabla para cada configuración.

Compara los resultados y observa si las proporciones de las categorías se conservan aproximadamente.

> [!NOTE]
> La estratificación busca mantener una distribución semejante de las categorías, pero no garantiza que las proporciones sean exactamente iguales.
>
> Además, los tamaños finales de los conjuntos pueden presentar pequeñas diferencias debido al redondeo a números enteros.

---

### 8 · Verificar la integridad de las particiones

Antes de guardar los resultados, comprobaremos que las asignaciones sean consistentes.

Utiliza instrucciones `assert` para verificar:

**A. Identificadores únicos**

Cada identificador debe aparecer una sola vez dentro de una configuración.

```python
assert particion[columna_id].is_unique
```

**B. Conservación de las muestras**

Los identificadores presentes en la partición deben coincidir exactamente con los identificadores originales del manifest.

**C. Etiquetas válidas**

La columna `split` debe contener únicamente las etiquetas:

```python
{"train", "validation", "test"}
```

**D. Conjuntos sin identificadores compartidos**

Comprueba que ningún identificador aparezca simultáneamente en entrenamiento, validación o prueba dentro de una misma configuración.

> [!IMPORTANT]
> Estas verificaciones permiten detectar errores de asignación, pero no descartan por sí solas todas las formas de *data leakage*.
>
> Si existen imágenes casi idénticas o muestras relacionadas con identificadores diferentes, sería necesario aplicar verificaciones adicionales o utilizar estrategias de partición por grupos.

---

### 9 · Guardar las particiones en archivos CSV

Crea el directorio:

```text
data/splits/
```

Puedes utilizar `pathlib`:

```python
ruta_splits.mkdir(parents=True, exist_ok=True)
```

Guarda las dos configuraciones mediante `to_csv()`:

```python
particion_70.to_csv(
    ruta_splits / "split_70_15_15.csv",
    index=False
)

particion_80.to_csv(
    ruta_splits / "split_80_10_10.csv",
    index=False
)
```

Los archivos deben conservar, como mínimo, la información necesaria para identificar cada muestra, localizar su fotografía y máscara y conocer el conjunto al que fue asignada.

**Considera:** ¿qué ventajas tiene guardar las particiones en archivos CSV en lugar de generar nuevas divisiones aleatorias cada vez que entrenamos un modelo?

---

### 10 · Recuperar y verificar los archivos guardados

Finalmente, vuelve a cargar los dos CSV generados mediante `pd.read_csv()`.

Comprueba que:

- Los archivos pueden leerse correctamente.
- El número de registros coincide con el manifest original.
- Las etiquetas `train`, `validation` y `test` se conservan.
- Las rutas de fotografías y máscaras siguen asociadas con sus identificadores.
- No existen identificadores duplicados dentro de cada configuración.

Esta última actividad permitirá comprobar que los archivos guardados pueden reutilizarse posteriormente.

---

## 📊 Resultados esperados

Al finalizar la práctica, tu proyecto contará con dos archivos nuevos:

```text
data/
└── splits/
    ├── split_70_15_15.csv
    └── split_80_10_10.csv
```

Cada archivo contendrá la asignación de las muestras a los conjuntos de entrenamiento, validación y prueba.

| Característica | Configuración 1 | Configuración 2 |
|---|---|---|
| Proporciones | 70/15/15 | 80/10/10 |
| Estrategia | Aleatoria estratificada | Aleatoria estratificada |
| Criterio de estratificación | Raza | Raza |
| Semilla | 42 | 42 |
| Fuente de información | `manifest.csv` | `manifest.csv` |
| Archivo de salida | `split_70_15_15.csv` | `split_80_10_10.csv` |

No habremos modificado ni duplicado las fotografías y máscaras originales.

---

## 🤔 Observa e interpreta

Al finalizar la práctica, responde las siguientes preguntas:

1. ¿Qué ventajas tiene recuperar las rutas del proyecto desde `dataset.json` en lugar de escribirlas directamente en el notebook?
2. ¿Por qué utilizamos el archivo `manifest.csv` para generar las particiones?
3. ¿Qué diferencia existe entre una partición aleatoria y una partición aleatoria estratificada?
4. ¿Por qué seleccionamos la raza como criterio de estratificación?
5. ¿Qué función cumple la semilla aleatoria durante la construcción de los conjuntos?
6. ¿Por qué debemos realizar dos separaciones consecutivas para obtener los conjuntos de entrenamiento, validación y prueba mediante `train_test_split()`?
7. ¿Qué diferencias observaste entre las configuraciones 70/15/15 y 80/10/10?
8. ¿Qué errores permiten detectar las verificaciones realizadas mediante `assert`?
9. ¿Por qué es importante conservar la relación entre cada fotografía y su máscara de segmentación?
10. ¿Qué problemas podrían presentarse si generamos nuevas particiones aleatorias cada vez que realizamos un experimento?

---

## ✅ Punto de control

Al finalizar esta práctica habrás:

- Recuperado el proyecto de Oxford-IIIT Pet Dataset utilizado durante el taller.
- Reutilizado el archivo `dataset.json` creado anteriormente.
- Recuperado el inventario `manifest.csv`.
- Identificado los campos necesarios para construir conjuntos experimentales.
- Analizado la distribución de razas.
- Construido una partición estratificada 70/15/15.
- Construido una partición estratificada 80/10/10.
- Utilizado una semilla fija para facilitar la reproducibilidad.
- Comparado las distribuciones mediante tablas de contingencia.
- Verificado que los identificadores sean únicos.
- Comprobado que no existan muestras omitidas.
- Conservado la correspondencia entre fotografías y máscaras.
- Guardado ambas configuraciones en archivos CSV.
- Recuperado y verificado los archivos generados.
- Preparado los conjuntos experimentales para las siguientes etapas del taller.

---

## 🏁 ¡Práctica completada!

Has diseñado los conjuntos experimentales del Oxford-IIIT Pet Dataset utilizando la información que organizaste en prácticas anteriores.

Ahora tu proyecto cuenta con dos configuraciones reproducibles de entrenamiento, validación y prueba.

**Estas particiones serán el punto de partida para construir el pipeline de datos y, posteriormente, entrenar y evaluar nuestro modelo U-Net.**

La siguiente etapa consistirá en utilizar los archivos CSV para recuperar las fotografías y máscaras correspondientes a cada conjunto y preparar su procesamiento mediante las herramientas de Deep Learning.

---

## 📚 Dataset de referencia

**Oxford-IIIT Pet Dataset**

Parkhi, O. M., Vedaldi, A., Zisserman, A., & Jawahar, C. V. (2012).

*Cats and Dogs.*

IEEE Conference on Computer Vision and Pattern Recognition (CVPR).

[Consultar el dataset original →](https://www.robots.ox.ac.uk/~vgg/data/pets/)

---

## 🔗 Enlaces

[← Volver a Diseño de los conjuntos experimentales](../../../modulos/04-diseno-experimental-y-pipeline-datos/04-01-diseno-conjuntos-experimentales.md)
