# 📊 Análisis exploratorio del minidataset

En la práctica [Inventario y configuración del minidataset](../inventario-y-configuracion-del-dataset/03-inventario-y-configuracion-de-minidataset.md) construimos un inventario estructurado (*manifest*) de nuestro minidataset de Oxford-IIIT Pet, recuperando información sobre las imágenes, sus categorías, dimensiones y anotaciones.

Ahora utilizaremos ese inventario para realizar un **análisis exploratorio de datos (EDA, *Exploratory Data Analysis*)**, con el propósito de comprender las características y la composición del conjunto de datos antes de utilizarlo para entrenar un modelo de segmentación.

A través de estadísticas descriptivas y representaciones gráficas, estudiaremos cómo se distribuyen las muestras entre categorías, qué tamaños y proporciones presentan las imágenes y cuánto espacio ocupan los animales dentro de sus respectivas máscaras de segmentación.

Este análisis nos permitirá identificar patrones, diferencias entre muestras y posibles desequilibrios que podrían influir en las siguientes etapas del proyecto.

---

## 🎯 Objetivo

Realizar un análisis exploratorio del minidataset de Oxford-IIIT Pet mediante el uso de `pandas`, `NumPy` y herramientas de visualización de datos.

Analizar la distribución de imágenes por especie y raza, las dimensiones y relaciones de aspecto de las fotografías, así como la distribución de píxeles correspondientes al animal, fondo y contorno en las máscaras de segmentación.

Interpretar los resultados obtenidos para reconocer características relevantes del dataset y su posible influencia en el procesamiento de imágenes y entrenamiento de modelos.

---

## 📦 Repositorio de la práctica

Los archivos necesarios para realizar esta actividad se encuentran en el siguiente repositorio:

**[🐱🐶 Acceder al repositorio de Análisis exploratorio del minidataset →](https://github.com/bettypau-open-knowledge/del-dataset-a-unet_analisis-exploratorio-minidataset)**

El repositorio de la práctica está organizado alrededor de:

- El **minidataset didáctico** de Oxford-IIIT Pet, con fotografías y máscaras de segmentación.
- El notebook `inventario.ipynb`, que permite generar el inventario estructurado y el archivo de configuración.
- El notebook `analisis_exploratorio.ipynb`, donde se desarrolla el análisis exploratorio.
- Un `README.md` con información adicional sobre el proyecto.

> [!NOTE]
> Los archivos `data/manifests/manifest.csv` y `config/dataset.json` se generan al ejecutar `inventario.ipynb`. Por lo tanto, deben estar disponibles antes de iniciar el análisis exploratorio.

> [!IMPORTANT]
> Esta práctica utiliza una selección reducida y reorganizada del Oxford-IIIT Pet Dataset original.
>
> Su propósito es aprender a explorar, describir e interpretar las características de un dataset. Los resultados obtenidos corresponden al minidataset utilizado y no deben generalizarse automáticamente al conjunto original.

---

## 📁 Organización del proyecto

Para realizar el análisis utilizaremos los archivos del minidataset y la información registrada en el manifest.

La estructura de referencia es:

```text
proyecto/
├── config/
│   └── dataset.json
├── data/
│   ├── raw/
│   │   ├── list.txt
│   │   └── images/
│   │       ├── ...
│   │       └── ...
│   └── manifests/
│       └── manifest.csv
└── notebooks/
    └── analisis_exploratorio.ipynb
```

Las fotografías y máscaras se encuentran dentro de `data/raw/`, mientras que el inventario estructurado está almacenado en `data/manifests/manifest.csv`.

El notebook utilizará esta información para recuperar los metadatos de las muestras y acceder a las máscaras cuando sea necesario analizar sus píxeles.

> [!NOTE]
> La estructura mostrada es una referencia de organización del proyecto. Comprueba las rutas de los archivos disponibles en el repositorio antes de ejecutar el notebook.

---

## 💻 Instrucciones

### 1 · Prepara el proyecto

Accede al repositorio de la práctica y descarga o clona su contenido.

Si trabajarás localmente, abre el proyecto en Visual Studio Code y selecciona el entorno de Python utilizado durante el taller.

Si utilizarás Google Colab, prepara el acceso a los archivos del proyecto siguiendo las instrucciones del repositorio.

### 2 · Genera el manifest y el archivo de configuración

Antes de comenzar el análisis exploratorio, es necesario contar con el inventario estructurado y el archivo de configuración del minidataset.

Para generarlos, localiza y abre el notebook:

```text
notebooks/inventario.ipynb
```

Ejecuta sus celdas en orden, siguiendo las instrucciones correspondientes.

Este notebook, desarrollado durante la práctica anterior, permite recuperar los metadatos de las imágenes y sus anotaciones, validar la información disponible y generar los siguientes archivos:

| Archivo | Descripción |
|---|---|
| `data/manifests/manifest.csv` | Inventario estructurado con la información de las muestras válidas del minidataset. |
| `config/dataset.json` | Archivo de configuración que centraliza las rutas necesarias para localizar los datos y el inventario. |

Al finalizar, verifica que ambos archivos se hayan generado correctamente y que se encuentren en las rutas correspondientes.

> [!IMPORTANT]
> **Este paso es indispensable para continuar con la práctica.**
>
> El notebook de análisis exploratorio utiliza la información del `manifest.csv` para recuperar las características de las imágenes y localizar sus archivos asociados.
>
> Por lo tanto, si todavía no has ejecutado `inventario.ipynb`, debes hacerlo antes de continuar.

### 3 · Abre el notebook de análisis exploratorio

Una vez generados el manifest y el archivo de configuración, localiza el notebook:

```text
notebooks/analisis_exploratorio.ipynb
```

Ábrelo y ejecuta las celdas progresivamente, siguiendo las explicaciones, instrucciones y observaciones de cada sección.

Durante su ejecución, utilizarás la información del inventario para realizar cálculos estadísticos y generar visualizaciones de las características del minidataset.

> [!IMPORTANT]
> Antes de ejecutar el análisis, comprueba que el notebook puede localizar correctamente:
>
> - El archivo `config/dataset.json`.
> - El inventario `data/manifests/manifest.csv`.
> - Las fotografías y máscaras de segmentación.
>
> Recuerda que las rutas relativas dependen del directorio de trabajo desde el que se ejecuta Python.

---

## 🧪 Actividades de la práctica

### 1 · Carga y exploración del manifest

Comenzaremos cargando el inventario estructurado mediante `pandas`.

Exploraremos las primeras filas, las columnas disponibles y los tipos de datos registrados.

También recuperaremos información general sobre el número de muestras y las categorías presentes.

Esta etapa nos permitirá identificar qué características podemos estudiar directamente desde el inventario y cuáles requieren consultar los archivos originales.

### 2 · Distribución de imágenes por categoría

Analizaremos cómo se distribuyen las imágenes entre las distintas especies y razas del minidataset.

Construiremos representaciones gráficas para observar:

- Número de imágenes por especie.
- Número de imágenes por raza.
- Distribución de razas dentro de cada especie.
- Posibles diferencias en la cantidad de muestras entre categorías.

Utilizaremos gráficos de barras y una representación jerárquica para visualizar la composición del conjunto de datos.

El propósito será identificar si las categorías están equilibradas o si algunas tienen mayor representación que otras.

### 3 · Análisis de las dimensiones de las imágenes

Estudiaremos las dimensiones espaciales de las fotografías.

A partir de los campos `width` y `height` del manifest, analizaremos:

- Ancho de las imágenes, en píxeles.
- Alto de las imágenes, en píxeles.
- Relación entre ancho y alto.
- Variabilidad de las resoluciones del conjunto de datos.

Utilizaremos un diagrama de dispersión para representar las dimensiones de las fotografías.

Esto nos permitirá identificar si las imágenes presentan tamaños similares o si existe una variabilidad importante que debamos considerar durante el preprocesamiento.

### 4 · Análisis de la relación de aspecto

La **relación de aspecto (*aspect ratio*)** describe la proporción entre el ancho y el alto de una imagen:

$$
r=\frac{W}{H}
$$

Donde:

- $W$ representa el ancho de la imagen.
- $H$ representa el alto de la imagen.
- $r$ representa su relación de aspecto.

Analizaremos la distribución de estos valores mediante un histograma.

Esto permitirá identificar fotografías aproximadamente cuadradas, horizontales y verticales, así como comprender por qué el cambio de tamaño de las imágenes debe realizarse cuidadosamente.

### 5 · Análisis de las máscaras de segmentación

Hasta ahora hemos estudiado características de las fotografías y sus etiquetas.

En esta etapa exploraremos el contenido de las **máscaras de segmentación**.

Las máscaras del Oxford-IIIT Pet Dataset utilizan tres valores para representar distintas regiones:

| Valor | Región |
|---|---|
| `1` | Animal (*foreground*) |
| `2` | Fondo (*background*) |
| `3` | Contorno (*boundary*) |

Contaremos los píxeles correspondientes a cada región y calcularemos su proporción respecto al total de píxeles de la máscara.

Por ejemplo, la proporción de píxeles correspondientes al animal se calcula mediante:

$$
p_{\text{animal}}=
\frac{N_{\text{animal}}}{N_{\text{total}}}
$$

Donde:

- $N_{\text{animal}}$ es el número de píxeles etiquetados como animal.
- $N_{\text{total}}$ es el número total de píxeles de la máscara.

Para expresar el resultado como porcentaje:

$$
P_{\text{animal}}=p_{\text{animal}}\times100
$$

Este análisis permitirá estudiar qué proporción de cada imagen corresponde al objeto que queremos segmentar.

### 6 · Distribución de la proporción de píxeles del animal

Una vez calculada la proporción de píxeles del animal para cada máscara, analizaremos cómo se distribuye esta característica entre las muestras.

Utilizaremos un histograma para identificar:

- Imágenes donde el animal ocupa una pequeña proporción del espacio.
- Imágenes donde el animal ocupa gran parte de la fotografía.
- Valores frecuentes y variabilidad de la proporción de píxeles del animal.

Este análisis es relevante porque, aunque todas las imágenes pertenezcan a una tarea de segmentación de animales, el tamaño relativo del objeto puede variar considerablemente.

### 7 · Composición de las máscaras

Representaremos la distribución de píxeles de animal, fondo y contorno.

Utilizaremos gráficos de barras apiladas para observar la composición de máscaras individuales y un gráfico circular para representar la distribución global de píxeles del minidataset.

Esto permitirá distinguir entre dos perspectivas:

- **Composición individual:** cómo se distribuyen los píxeles dentro de cada máscara.
- **Composición global:** qué proporción del total de píxeles analizados corresponde a cada región.

> [!NOTE]
> La composición global considera conjuntamente los píxeles de todas las máscaras. Por tanto, las imágenes con mayor resolución aportan más píxeles al cálculo que las imágenes pequeñas.
>
> Esto no es equivalente a calcular el promedio de los porcentajes individuales de las máscaras.

### 8 · Distribución del tamaño del animal

Finalmente, compararemos dos características relacionadas con el tamaño del objeto segmentado:

- **Tamaño absoluto:** número de píxeles etiquetados como animal.
- **Tamaño relativo:** porcentaje de píxeles de la máscara que corresponde al animal.

Utilizaremos gráficos de violín para observar la distribución de ambas variables.

Esta comparación nos permitirá comprender por qué dos animales pueden ocupar un número similar de píxeles, pero representar porcentajes diferentes de sus respectivas imágenes.

También discutiremos la importancia de distinguir entre tamaño absoluto y relativo al analizar datasets con resoluciones variables.

---

## 📋 Resultado 1 · Caracterización de las muestras

El primer resultado será una descripción estadística de las características del minidataset.

A partir del manifest y de las máscaras de segmentación, habremos estudiado:

| Característica | Información obtenida |
|---|---|
| Especie | Distribución de imágenes entre gatos y perros. |
| Raza | Número de imágenes por categoría. |
| Ancho | Dimensión horizontal de las fotografías. |
| Alto | Dimensión vertical de las fotografías. |
| Relación de aspecto | Proporción entre ancho y alto. |
| Píxeles del animal | Tamaño absoluto de la región segmentada. |
| Porcentaje del animal | Tamaño relativo del objeto dentro de la imagen. |
| Píxeles del fondo | Cantidad de píxeles etiquetados como fondo. |
| Píxeles del contorno | Cantidad de píxeles correspondientes al borde del objeto. |

Esta información complementa el inventario construido en la práctica anterior y proporciona una visión más completa de la composición del dataset.

---

## 📈 Resultado 2 · Visualizaciones del dataset

El segundo resultado será un conjunto de representaciones gráficas que permitirán interpretar las características del minidataset.

Entre ellas se encuentran:

| Visualización | Propósito |
|---|---|
| Gráfico de barras por especie y raza | Comparar la cantidad de muestras por categoría. |
| Gráfico jerárquico de categorías | Observar la composición de especies y razas. |
| Diagrama de dispersión ancho–alto | Examinar la variabilidad de las dimensiones. |
| Histograma de relación de aspecto | Identificar formatos de imagen frecuentes. |
| Histograma de porcentaje del animal | Estudiar el tamaño relativo del objeto segmentado. |
| Barras apiladas de máscaras | Comparar las regiones de animal, fondo y contorno. |
| Gráfico circular de píxeles | Visualizar la composición global de las máscaras. |
| Gráficos de violín | Comparar distribuciones del tamaño absoluto y relativo del animal. |

> [!TIP]
> Una visualización no debe interpretarse únicamente por su apariencia.
>
> Antes de obtener conclusiones, identifica qué variable se representa, cuáles son sus unidades, qué significa cada eje y si los valores corresponden a cantidades absolutas, proporciones o porcentajes.

---

## 🤔 Observa e interpreta

Al finalizar la práctica, reflexiona sobre las siguientes preguntas:

1. ¿Todas las especies y razas tienen la misma cantidad de imágenes? ¿Qué consecuencias podría tener una distribución desequilibrada?
2. ¿Las fotografías presentan dimensiones similares o existe una variabilidad importante en su resolución?
3. ¿Qué diferencias observas entre las distribuciones del ancho, alto y relación de aspecto?
4. ¿Por qué conocer las dimensiones originales de las imágenes resulta importante antes de aplicar operaciones de *resize*?
5. ¿Todas las máscaras presentan proporciones similares de píxeles correspondientes al animal?
6. ¿Qué diferencia existe entre analizar el número absoluto de píxeles del animal y analizar su porcentaje respecto al total?
7. ¿Por qué la distribución global de píxeles puede ser diferente del promedio de las proporciones individuales?
8. ¿Qué características identificadas durante el análisis exploratorio podrían influir en el entrenamiento de un modelo U-Net?
9. ¿Qué información adicional necesitaríamos para evaluar si el minidataset es adecuado para entrenar y evaluar un modelo de segmentación?

---

## ✅ Punto de control

Al finalizar esta práctica habrás:

- Cargado y explorado un inventario estructurado mediante `pandas`.
- Identificado la distribución de imágenes por especie y raza.
- Analizado las dimensiones y relaciones de aspecto de las fotografías.
- Interpretado diagramas de dispersión, histogramas y gráficos de distribución.
- Recuperado información sobre las regiones etiquetadas en las máscaras de segmentación.
- Calculado cantidades y proporciones de píxeles correspondientes al animal, fondo y contorno.
- Comparado el tamaño absoluto y relativo de los objetos segmentados.
- Identificado características del dataset relevantes para las siguientes etapas de procesamiento y entrenamiento.

---

## 📚 Dataset de referencia

Esta práctica utiliza una versión reducida y reorganizada del **Oxford-IIIT Pet Dataset**.

**Referencia:**

Parkhi, O. M., Vedaldi, A., Zisserman, A., & Jawahar, C. V. (2012).

*Cats and Dogs.*

IEEE Conference on Computer Vision and Pattern Recognition (CVPR).

[Consultar el dataset original →](https://www.robots.ox.ac.uk/~vgg/data/pets/)

---

[← Volver a Análisis exploratorio del dataset](../../../modulos/02-ingenieria-del-dataset/02-03-analisis-exploratorio-del-dataset.md)