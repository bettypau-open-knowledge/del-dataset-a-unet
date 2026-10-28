# 🧪 Diseño de los conjuntos experimentales del minidataset

En los módulos anteriores aprendimos a organizar un dataset, identificar fotografías y máscaras de segmentación, analizar sus características y aplicar transformaciones para preparar las imágenes antes del entrenamiento.

Ahora debemos resolver una pregunta fundamental:

**¿Cómo podemos organizar nuestros datos para entrenar, validar y evaluar un modelo sin comprometer la confiabilidad de los resultados?**

En esta práctica utilizaremos un **minidataset derivado del Oxford-IIIT Pet Dataset**, que contiene fotografías de perros y gatos, sus máscaras de segmentación y archivos de anotaciones.

Mediante Python y **scikit-learn**, construiremos dos configuraciones de conjuntos experimentales:

- **70/15/15:** 70 % entrenamiento, 15 % validación y 15 % prueba.
- **80/10/10:** 80 % entrenamiento, 10 % validación y 10 % prueba.

En ambos casos utilizaremos una **partición aleatoria estratificada por raza**, con una semilla fija para facilitar la reproducibilidad.

Finalmente, compararemos la distribución de las categorías y comprobaremos que las particiones conserven todos los identificadores originales, sin duplicaciones ni omisiones.

---

## 🎯 Objetivo

Diseñar y verificar conjuntos experimentales reproducibles mediante Python, utilizando particiones aleatorias estratificadas por raza y diferentes proporciones de entrenamiento, validación y prueba.

Al finalizar, serás capaz de:

- Distinguir el propósito de los conjuntos *train*, *validation* y *test*.
- Utilizar `train_test_split()` de scikit-learn.
- Aplicar estratificación mediante una variable categórica.
- Utilizar una semilla fija para obtener particiones reproducibles.
- Comparar las distribuciones de las categorías entre conjuntos.
- Verificar la integridad de las particiones mediante instrucciones `assert`.
- Guardar las asignaciones en archivos CSV sin modificar los archivos originales.

---

## 📦 Repositorio de la práctica

Para esta actividad utilizaremos un repositorio independiente que contiene el minidataset, los archivos de configuración y el notebook.

**[Abrir repositorio de la práctica en GitHub →](https://github.com/bettypau-open-knowledge/del-dataset-a-unet_conjuntos-experimentales-minidataset)**

Puedes obtenerlo mediante **Code → Download ZIP** o clonarlo con Git:

```bash
git clone https://github.com/bettypau-open-knowledge/del-dataset-a-unet_conjuntos-experimentales-minidataset.git
```

> [!IMPORTANT]
> Para esta práctica trabajaremos directamente con la estructura del repositorio proporcionado.
>
> No es necesario copiar las fotografías y máscaras al proyecto utilizado en los módulos anteriores. El minidataset ya se encuentra organizado para realizar las actividades.

---

## 📁 Organización del proyecto

El repositorio contiene la siguiente estructura:

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
│   └── splits/                       # Generado durante la práctica
│       ├── split_70_15_15.csv
│       └── split_80_10_10.csv
└── notebooks/
    └── conjuntos_experimentales.ipynb
```

Dentro de los directorios correspondientes a cada raza se encuentran las fotografías, máscaras y anotaciones individuales.

Los archivos de una misma muestra comparten el mismo nombre base y utilizan extensiones diferentes:

```text
Sphynx_19.jpg    # Fotografía
Sphynx_19.png    # Máscara de segmentación
Sphynx_19.xml    # Anotación
```

### Archivos principales

| Archivo | Función |
|---|---|
| `config/dataset.json` | Administra la configuración de rutas del proyecto. |
| `data/manifests/manifest.csv` | Contiene los registros necesarios para identificar las muestras y localizar sus imágenes y máscaras. |
| `data/raw/` | Almacena los archivos originales del minidataset. |
| `notebooks/conjuntos_experimentales.ipynb` | Contiene las actividades de diseño y verificación de particiones. |
| `data/splits/` | Almacena los CSV generados durante la práctica. |

> [!NOTE]
> Este minidataset contiene únicamente una pequeña selección de imágenes del Oxford-IIIT Pet Dataset original.
>
> Se ha preparado con fines didácticos para estudiar las estrategias de partición. No representa el dataset completo ni está diseñado para obtener evaluaciones representativas del rendimiento de modelos de segmentación.

---

## 💻 Requisitos

Para ejecutar la práctica necesitarás Visual Studio Code, un entorno de Python compatible con Jupyter Notebooks y las siguientes bibliotecas:

| Biblioteca | Uso |
|---|---|
| `pathlib` | Construcción y manipulación de rutas. |
| `json` | Lectura y actualización de la configuración. |
| `pandas` | Lectura del manifest, organización de datos, tablas y exportación a CSV. |
| `scikit-learn` | Construcción de particiones aleatorias estratificadas. |

`pathlib` y `json` forman parte de la biblioteca estándar de Python.

---

## 💻 Instrucciones

### 1 · Abre el repositorio en Visual Studio Code

Descarga o clona el repositorio de la práctica.

Abre la carpeta principal en Visual Studio Code y localiza el archivo:

```text
notebooks/conjuntos_experimentales.ipynb
```

Selecciona el kernel de Python correspondiente al entorno del taller.

### 2 · Revisa los archivos proporcionados

Antes de ejecutar las actividades, identifica:

- El archivo de configuración `dataset.json`.
- El manifest del minidataset.
- Los directorios correspondientes a las cuatro razas.
- Las fotografías y sus máscaras asociadas.

Observa cómo los archivos se relacionan mediante sus identificadores.

### 3 · Ejecuta el notebook

Ejecuta las celdas en el orden indicado.

Durante la práctica, observa las particiones obtenidas, las tablas generadas y los resultados de las verificaciones.

> [!TIP]
> Recuerda que puedes utilizar **Run All** para ejecutar todas las celdas en orden o **Restart Kernel** para reiniciar el estado del notebook y comprobar nuevamente su ejecución.

---

## 🧪 Actividades de la práctica

### 1 · Lectura de la configuración y del manifest

Comenzaremos recuperando la configuración del proyecto y leyendo el archivo `manifest.csv` mediante pandas.

El manifest contiene la información necesaria para identificar cada muestra y localizar su fotografía y máscara correspondiente.

Antes de generar las particiones, observa los identificadores disponibles y la columna `breed`, que utilizaremos como criterio de estratificación.

**Considera:** ¿por qué es preferible construir las particiones a partir de un manifest en lugar de mover manualmente fotografías y máscaras entre carpetas?

---

### 2 · Primera partición: 70/15/15

La primera configuración utilizará las siguientes proporciones:

| Conjunto | Proporción |
|---|---:|
| Train | 70 % |
| Validation | 15 % |
| Test | 15 % |

Utilizaremos `train_test_split()` de scikit-learn para realizar una partición aleatoria estratificada por raza.

La estratificación busca conservar aproximadamente la distribución de las razas entre los conjuntos.

También utilizaremos:

```python
random_state=42
```

Este parámetro permite repetir la partición bajo las mismas condiciones y obtener los mismos resultados.

> [!NOTE]
> Debido al tamaño reducido del minidataset, las proporciones efectivas pueden diferir ligeramente de las solicitadas.
>
> Esto ocurre porque el número de muestras debe ser entero y la estratificación no garantiza distribuciones exactamente idénticas.

**Considera:** ¿qué ventajas ofrece utilizar una semilla fija cuando queremos comparar diferentes experimentos?

---

### 3 · Segunda partición: 80/10/10

Repetiremos el procedimiento utilizando una segunda configuración:

| Conjunto | Proporción |
|---|---:|
| Train | 80 % |
| Validation | 10 % |
| Test | 10 % |

En esta ocasión destinaremos una mayor proporción de las muestras al entrenamiento y reduciremos el tamaño de los conjuntos de validación y prueba.

Observa cómo cambia la cantidad de muestras disponibles en cada conjunto.

**Considera:** ¿qué ventajas y limitaciones podría tener aumentar el tamaño del conjunto de entrenamiento a costa de reducir los conjuntos de validación y prueba?

---

### 4 · Comparación de la distribución de razas

Una vez generadas ambas configuraciones, analizaremos cómo se distribuyen las categorías entre los conjuntos.

Utilizaremos:

```python
pd.crosstab()
```

Esta función permite construir tablas de contingencia para comparar la cantidad de muestras de cada raza asignadas a entrenamiento, validación y prueba.

Observa los resultados obtenidos para las cuatro razas del minidataset:

- Chihuahua.
- Maine Coon.
- Siamese.
- Sphynx.

La estratificación busca mantener aproximadamente la distribución original de las categorías, aunque las cantidades finales pueden variar por el tamaño del dataset y los redondeos necesarios.

**Considera:** ¿por qué puede ser importante conservar la distribución de las categorías cuando diseñamos conjuntos experimentales?

---

### 5 · Verificación de la integridad de las particiones

Después de generar las particiones, debemos comprobar que su organización sea consistente.

Para ello, el notebook utiliza instrucciones `assert` que verifican tres condiciones:

**Condición 1. Identificadores únicos**

No deben existir identificadores `image_id` repetidos dentro de una misma configuración.

**Condición 2. Conservación de las muestras**

Los identificadores presentes en cada configuración deben coincidir exactamente con los identificadores del manifest original.

Esto permite detectar omisiones o registros adicionales.

**Condición 3. Etiquetas válidas**

Cada muestra debe pertenecer a uno de los siguientes conjuntos:

```text
train
validation
test
```

> [!IMPORTANT]
> Estas verificaciones permiten comprobar la consistencia de las asignaciones registradas en los CSV, pero no son suficientes para descartar todas las formas de **data leakage**.
>
> Por ejemplo, podrían existir imágenes casi idénticas o muestras relacionadas con identificadores diferentes.
>
> En esos casos sería necesario incorporar verificaciones adicionales o utilizar una estrategia de partición por grupos.

---

### 6 · Exportación de las particiones a CSV

Finalmente, guardaremos las dos configuraciones dentro del directorio:

```text
data/splits/
```

Se generarán los siguientes archivos:

```text
split_70_15_15.csv
split_80_10_10.csv
```

Cada archivo contendrá cinco columnas:

| Columna | Descripción |
|---|---|
| `image_id` | Identificador único de la muestra. |
| `breed` | Raza correspondiente. |
| `image_path` | Ruta de la fotografía. |
| `mask_path` | Ruta de la máscara. |
| `split` | Conjunto experimental asignado. |

La fotografía y su máscara permanecerán asociadas en la misma fila.

**No moveremos ni duplicaremos los archivos originales.** Únicamente registraremos en los CSV el conjunto al que pertenece cada muestra.

Esto permitirá recuperar las mismas particiones en etapas posteriores del proyecto.

---

## 📊 Resultados esperados

Al finalizar la práctica, tendrás dos configuraciones de conjuntos experimentales guardadas en archivos CSV.

| Característica | Configuración 1 | Configuración 2 |
|---|---|---|
| Proporciones | 70/15/15 | 80/10/10 |
| Estrategia | Aleatoria estratificada | Aleatoria estratificada |
| Variable de estratificación | `breed` | `breed` |
| Semilla | `42` | `42` |
| Archivo de salida | `split_70_15_15.csv` | `split_80_10_10.csv` |

También habrás generado tablas para observar la distribución de razas y ejecutado verificaciones para comprobar la integridad de los identificadores.

---

## 🤔 Observa e interpreta

Al finalizar la práctica, responde las siguientes preguntas:

1. ¿Cuál es la diferencia entre los conjuntos de entrenamiento, validación y prueba?
2. ¿Por qué no debemos evaluar la capacidad de generalización de un modelo utilizando únicamente las imágenes con las que fue entrenado?
3. ¿Qué significa realizar una partición estratificada?
4. ¿Por qué utilizamos la columna `breed` como criterio de estratificación?
5. ¿Qué función cumple el parámetro `random_state=42`?
6. ¿Por qué los porcentajes efectivos pueden diferir ligeramente de las proporciones solicitadas?
7. ¿Qué diferencias observaste entre las distribuciones 70/15/15 y 80/10/10?
8. ¿Qué información podemos obtener mediante una tabla de contingencia generada con `pd.crosstab()`?
9. ¿Qué errores permiten detectar las instrucciones `assert` utilizadas en la práctica?
10. ¿Por qué comprobar que no existen identificadores repetidos no garantiza por sí solo que se haya evitado el *data leakage*?

---

## ✅ Punto de control

Al finalizar esta práctica habrás:

- Descargado o clonado un repositorio independiente con un minidataset organizado.
- Identificado la función del archivo de configuración y del manifest.
- Reconocido la relación entre fotografías, máscaras e identificadores.
- Construido una partición 70/15/15.
- Construido una partición 80/10/10.
- Utilizado `train_test_split()` de scikit-learn.
- Aplicado estratificación mediante la variable `breed`.
- Utilizado una semilla fija para facilitar la reproducibilidad.
- Comparado la distribución de razas mediante tablas de contingencia.
- Verificado la unicidad y conservación de los identificadores.
- Comprobado la validez de las etiquetas de partición.
- Generado dos archivos CSV con las asignaciones experimentales.
- Comprendido la importancia de conservar las particiones para futuros experimentos.
- Identificado limitaciones de estas verificaciones frente al *data leakage*.

---

## 🏁 ¡Práctica completada!

Has construido dos configuraciones de conjuntos experimentales y comprobado que sus asignaciones sean consistentes con el manifest original.

Ahora sabemos que **diseñar una partición experimental no consiste únicamente en distribuir porcentajes de imágenes**, sino también en considerar la composición del dataset, la reproducibilidad de las decisiones y la integridad de las muestras.

Los archivos CSV obtenidos permitirán conservar las asignaciones y utilizarlas posteriormente durante la preparación de los datos para el entrenamiento y la evaluación.

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

[**Abrir repositorio de la práctica →**](https://github.com/bettypau-open-knowledge/del-dataset-a-unet_conjuntos-experimentales-minidataset)

[← Volver a Diseño de los conjuntos experimentales](../../../modulos/04-diseno-experimental-y-pipeline-datos/04-01-diseno-conjuntos-experimentales.md)