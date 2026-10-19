# 📊 Análisis exploratorio del Oxford-IIIT Pet Dataset

En la práctica [Inventario y configuración del Oxford-IIIT Pet Dataset](../inventario-y-configuracion-del-dataset/04-inventario-y-configuracion-del-oxford-dataset.md) construimos un **inventario estructurado (*manifest*)** del Oxford-IIIT Pet Dataset original, recuperando información sobre las fotografías, sus categorías, dimensiones y anotaciones.

También creamos un **archivo de configuración JSON** para centralizar las rutas del proyecto y facilitar el acceso a los datos.

Ahora utilizaremos estos recursos para desarrollar un **análisis exploratorio de datos (EDA, *Exploratory Data Analysis*)** que nos permita comprender las características y la composición del dataset.

Estudiaremos cómo se distribuyen las imágenes entre especies y razas, qué dimensiones y relaciones de aspecto presentan las fotografías y cómo se distribuyen los píxeles correspondientes al animal, fondo y contorno dentro de las máscaras de segmentación.

En esta ocasión, **no se proporcionará un notebook con el procedimiento resuelto**. Deberás recuperar y adaptar las herramientas utilizadas en la práctica de análisis exploratorio del minidataset para construir tu propia solución.

---

## 🎯 Objetivo

Desarrollar un análisis exploratorio del Oxford-IIIT Pet Dataset original mediante estadísticas descriptivas y representaciones gráficas, utilizando la información del manifest y las máscaras de segmentación.

Caracterizar la distribución de imágenes por especie y raza, las dimensiones y relaciones de aspecto de las fotografías, así como el tamaño absoluto y relativo de las regiones segmentadas.

Interpretar los resultados para identificar características relevantes del dataset que deban considerarse durante las siguientes etapas de preprocesamiento y entrenamiento de modelos.

---

## 💻 Instrucciones

Para realizar esta actividad necesitarás:

- El Oxford-IIIT Pet Dataset original, descargado durante las prácticas anteriores.
- Los archivos `manifest.csv` y `dataset.json` generados en la Práctica [Inventario y configuración del Oxford-IIIT Pet Dataset](../inventario-y-configuracion-del-dataset/04-inventario-y-configuracion-del-oxford-dataset.md).
- El entorno de Python del taller, si trabajarás localmente.
- Visual Studio Code o Google Colab.
- La práctica de análisis exploratorio del minidataset como material de consulta.

> [!IMPORTANT]
> En esta actividad deberás construir tu propio notebook.
>
> Puedes consultar y reutilizar el código desarrollado anteriormente, pero tendrás que adaptarlo para trabajar con el Oxford-IIIT Pet Dataset original.
>
> **No modifiques ni sobrescribas los archivos originales del dataset.**

---

### 1 · Recupera el proyecto de la práctica anterior

Retoma el proyecto que utilizaste para construir el inventario del Oxford-IIIT Pet Dataset original.

La estructura de referencia es:

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
│   └── manifests/
│       └── manifest.csv
└── notebooks/
    ├── inventario_oxford_pet.ipynb
    └── analisis_exploratorio_oxford_pet.ipynb
```

Comprueba que los archivos `manifest.csv` y `dataset.json` se encuentran disponibles y que corresponden al dataset original.

> [!NOTE]
> El notebook `analisis_exploratorio_oxford_pet.ipynb` se creará durante esta práctica.
>
> Si organizaste el proyecto de manera diferente, puedes conservar tu estructura siempre que las rutas sean consistentes.

---

### 2 · Crea el notebook de análisis exploratorio

Dentro del directorio `notebooks/`, crea un archivo llamado:

```text
analisis_exploratorio_oxford_pet.ipynb
```

Organiza el notebook en secciones que permitan distinguir las diferentes etapas del análisis.

Antes de comenzar, recupera las rutas necesarias para acceder al dataset.

Utiliza el archivo:

```text
config/dataset.json
```

para localizar el manifest y los directorios que contienen las fotografías y máscaras de segmentación.

> [!IMPORTANT]
> Utiliza la información almacenada en el archivo de configuración.
>
> Evita escribir manualmente las rutas completas del dataset en diferentes celdas del notebook.

---

### 3 · Carga y explora el manifest

Utiliza `pandas` para cargar el inventario generado durante la Práctica [Inventario y configuración del Oxford-IIIT Pet Dataset](../inventario-y-configuracion-del-dataset/04-inventario-y-configuracion-del-oxford-dataset.md).

Explora su contenido y recupera información general sobre las muestras registradas.

Como mínimo, identifica:

1. El número total de muestras válidas.
2. Los nombres de las columnas.
3. Los tipos de datos de cada columna.
4. La presencia de valores faltantes.
5. El número de especies y razas representadas.

Recuerda que el manifest contiene información estructurada sobre las fotografías, sus etiquetas de clasificación, dimensiones y rutas de acceso.

**Considera:** ¿qué características puedes analizar directamente desde el manifest y cuáles requieren consultar los archivos originales?

---

### 4 · Analiza la distribución de imágenes por categoría

Utiliza los campos de clasificación del manifest para estudiar cómo se distribuyen las imágenes entre las diferentes especies y razas.

Calcula:

- Número de imágenes por especie.
- Número de imágenes por raza.
- Proporción de imágenes correspondiente a cada especie.
- Distribución de razas dentro de cada especie.

Construye las siguientes visualizaciones:

**a) Gráfico de barras por categoría**

Representa el número de imágenes correspondientes a cada raza.

Organiza las categorías de manera que sea posible identificar cuáles tienen mayor y menor representación.

**b) Gráfico jerárquico de categorías**

Construye una representación que permita observar la distribución de razas dentro de las especies.

Puedes utilizar un gráfico de dona con anillos anidados, como el desarrollado en la práctica anterior.

**Considera:** ¿el dataset contiene cantidades similares de imágenes para todas las razas? ¿Qué implicaciones podría tener una distribución desequilibrada?

---

### 5 · Analiza las dimensiones de las fotografías

Utiliza los campos `width` y `height` del manifest para estudiar las dimensiones espaciales de las imágenes.

Calcula estadísticas descriptivas que permitan identificar:

- Ancho mínimo y máximo.
- Alto mínimo y máximo.
- Valores promedio y medianas.
- Variabilidad de las dimensiones.

Construye un **diagrama de dispersión** que represente:

- Eje horizontal: ancho de la fotografía.
- Eje vertical: alto de la fotografía.

Observa la distribución de los puntos e identifica si existen agrupaciones, valores extremos o diferencias importantes entre las resoluciones.

**Considera:** ¿qué dificultades podrían surgir al utilizar fotografías con dimensiones diferentes para entrenar una red neuronal?

---

### 6 · Calcula y analiza la relación de aspecto

La **relación de aspecto (*aspect ratio*)** describe la proporción entre el ancho y el alto de una imagen:

$$
r=\frac{W}{H}
$$

Donde:

- $W$ representa el ancho de la imagen.
- $H$ representa el alto de la imagen.
- $r$ representa la relación de aspecto.

Calcula este valor para cada fotografía registrada en el manifest.

Después, construye un **histograma** para representar su distribución.

Identifica:

- Imágenes con relación de aspecto cercana a 1.
- Imágenes predominantemente horizontales.
- Imágenes predominantemente verticales.
- Valores extremos de la distribución.

**Considera:** ¿qué sucede con la apariencia de un objeto cuando modificamos el ancho y alto de una imagen sin conservar su relación de aspecto?

---

### 7 · Recupera la información de las máscaras de segmentación

Hasta este punto hemos trabajado principalmente con información almacenada en el manifest.

Ahora necesitaremos acceder a las máscaras de segmentación para estudiar su contenido.

Recuerda que las máscaras del Oxford-IIIT Pet Dataset utilizan tres valores:

| Valor | Región |
|---|---|
| `1` | Animal (*foreground*) |
| `2` | Fondo (*background*) |
| `3` | Contorno (*boundary*) |

Utiliza las rutas registradas en el manifest para localizar las máscaras correspondientes a las muestras.

Para cada máscara, calcula:

- Número total de píxeles.
- Número de píxeles correspondientes al animal.
- Número de píxeles correspondientes al fondo.
- Número de píxeles correspondientes al contorno.

Almacena los resultados en una estructura tabular que permita relacionarlos con las muestras originales.

> [!IMPORTANT]
> Las máscaras contienen etiquetas discretas, no intensidades de color que deban interpretarse como fotografías.
>
> Al leerlas, asegúrate de conservar los valores originales de las etiquetas.
>
> No es necesario modificar ni redimensionar las máscaras para realizar este análisis.

**Considera:** ¿cómo puedes verificar que la suma de los píxeles de las tres regiones coincide con el número total de píxeles de la máscara?

---

### 8 · Calcula la proporción de píxeles de cada región

A partir de los conteos obtenidos, calcula la proporción de píxeles correspondientes a cada región.

Para el animal:

$$
p_{\text{animal}}=
\frac{N_{\text{animal}}}{N_{\text{total}}}
$$

Para el fondo:

$$
p_{\text{fondo}}=
\frac{N_{\text{fondo}}}{N_{\text{total}}}
$$

Para el contorno:

$$
p_{\text{contorno}}=
\frac{N_{\text{contorno}}}{N_{\text{total}}}
$$

Donde $N_{\text{total}}$ representa el número total de píxeles de la máscara.

Comprueba que:

$$
p_{\text{animal}}+
p_{\text{fondo}}+
p_{\text{contorno}}=1
$$

Para expresar los resultados como porcentajes, multiplica cada proporción por 100.

**Considera:** ¿por qué resulta útil calcular porcentajes en lugar de comparar únicamente cantidades absolutas de píxeles?

---

### 9 · Analiza la distribución del porcentaje de píxeles del animal

Utiliza los porcentajes calculados para estudiar cuánto espacio ocupa el animal dentro de las fotografías.

Construye un **histograma** que represente la distribución del porcentaje de píxeles correspondientes al animal.

Identifica:

- Los porcentajes más frecuentes.
- La variabilidad de la distribución.
- Las imágenes donde el animal ocupa una proporción pequeña.
- Las imágenes donde el animal ocupa una proporción grande.

**Considera:** ¿qué implicaciones podría tener para un modelo de segmentación que algunos animales ocupen una proporción muy pequeña de la imagen?

---

### 10 · Representa la composición de las máscaras

Construye visualizaciones que permitan comparar las proporciones de animal, fondo y contorno.

**a) Gráfico de barras apiladas**

Selecciona un conjunto de máscaras y representa la proporción de cada región mediante barras apiladas.

Cada barra deberá corresponder a una máscara y mostrar cómo se distribuyen sus píxeles.

**b) Gráfico circular de composición global**

Calcula el número total de píxeles correspondientes a cada región considerando todas las máscaras analizadas.

Representa la distribución global mediante un gráfico circular.

> [!NOTE]
> La composición global no es necesariamente equivalente al promedio de las proporciones individuales.
>
> Si las máscaras tienen diferentes dimensiones, aquellas con mayor número de píxeles contribuyen más al cálculo global.

**Considera:** ¿qué información aporta el gráfico global que no puede observarse directamente en las barras de máscaras individuales?

---

### 11 · Analiza el tamaño absoluto y relativo del animal

Hasta ahora hemos calculado tanto el número de píxeles del animal como su porcentaje respecto al total de la imagen.

Estas variables describen características diferentes:

- **Tamaño absoluto:** cantidad de píxeles etiquetados como animal.
- **Tamaño relativo:** proporción de la máscara correspondiente al animal.

Construye dos **gráficos de violín**:

1. Distribución del número absoluto de píxeles del animal.
2. Distribución del porcentaje de píxeles del animal.

Compara la forma y dispersión de ambas distribuciones.

**Considera:** ¿pueden dos imágenes contener animales con un número similar de píxeles, pero porcentajes diferentes? Explica por qué.

---

### 12 · Organiza e interpreta los resultados

Una vez generadas las estadísticas y visualizaciones, revisa los resultados obtenidos.

Organiza tu notebook para que cada etapa incluya:

1. Una breve explicación de la característica analizada.
2. El código utilizado para realizar los cálculos.
3. La visualización correspondiente, cuando aplique.
4. Una interpretación de los resultados.

No es suficiente generar gráficos: debes explicar qué información proporcionan y qué características del dataset permiten identificar.

> [!TIP]
> Utiliza celdas Markdown dentro del notebook para documentar tus observaciones.
>
> Procura que los títulos de las gráficas, etiquetas de los ejes y unidades sean claros.
>
> Distingue entre cantidades absolutas, proporciones y porcentajes.

---

## 📋 Resultado 1 · Caracterización estadística del dataset

El primer resultado de la práctica será una descripción estadística de las principales características del Oxford-IIIT Pet Dataset.

Como mínimo, deberás haber analizado:

| Característica | Información obtenida |
|---|---|
| Número de muestras | Cantidad de registros válidos disponibles. |
| Especies | Distribución de fotografías entre gatos y perros. |
| Razas | Número de imágenes por categoría. |
| Ancho | Dimensión horizontal de las fotografías. |
| Alto | Dimensión vertical de las fotografías. |
| Relación de aspecto | Proporción entre ancho y alto. |
| Píxeles del animal | Tamaño absoluto de la región segmentada. |
| Porcentaje del animal | Tamaño relativo del objeto. |
| Píxeles del fondo | Cantidad y proporción de píxeles etiquetados como fondo. |
| Píxeles del contorno | Cantidad y proporción de píxeles correspondientes al borde. |

---

## 📈 Resultado 2 · Visualizaciones del dataset

El segundo resultado será un conjunto de representaciones gráficas construidas a partir de los datos analizados.

| Visualización | Propósito |
|---|---|
| Gráfico de barras por raza | Comparar la cantidad de muestras por categoría. |
| Gráfico jerárquico de especies y razas | Observar la composición de las categorías. |
| Diagrama de dispersión ancho–alto | Analizar la variabilidad de las dimensiones. |
| Histograma de relación de aspecto | Identificar los formatos de imagen frecuentes. |
| Histograma de porcentaje del animal | Estudiar el tamaño relativo de los objetos. |
| Gráfico de barras apiladas | Comparar la composición de máscaras individuales. |
| Gráfico circular de píxeles | Representar la composición global de las máscaras. |
| Gráficos de violín | Analizar el tamaño absoluto y relativo del animal. |

Cada visualización deberá acompañarse de una interpretación que explique qué características del dataset permite identificar.

---

## 🤔 Observa e interpreta

Al finalizar la práctica, responde las siguientes preguntas:

1. ¿Qué ventajas ofrece utilizar el manifest en lugar de recorrer nuevamente todos los directorios para recuperar la información de clasificación y dimensiones?
2. ¿Todas las especies y razas tienen cantidades similares de imágenes?
3. ¿Qué diferencias existen entre las dimensiones de las fotografías?
4. ¿Por qué resulta importante conocer la distribución de relaciones de aspecto antes de aplicar operaciones de *resize*?
5. ¿Qué tan variable es el porcentaje de píxeles correspondientes al animal?
6. ¿Qué diferencia existe entre el tamaño absoluto y relativo de un objeto segmentado?
7. ¿Por qué la distribución global de píxeles puede ser diferente del promedio de las proporciones individuales?
8. ¿Qué características del dataset podrían influir en el preprocesamiento de las fotografías y máscaras?
9. ¿Qué información adicional sería necesaria para determinar si el dataset presenta problemas de calidad que no pueden identificarse mediante estadísticas descriptivas?
10. ¿Cómo podrían aprovecharse los resultados de este análisis durante el entrenamiento de un modelo U-Net?

---

## ✅ Punto de control

Al finalizar esta práctica habrás:

- Recuperado el proyecto y los archivos generados durante la Práctica 4.
- Creado un notebook propio para realizar el análisis exploratorio.
- Utilizado `dataset.json` para localizar el manifest y los archivos del dataset.
- Cargado y explorado el inventario estructurado mediante `pandas`.
- Analizado la distribución de imágenes por especie y raza.
- Calculado estadísticas descriptivas de las dimensiones de las fotografías.
- Estudiado la distribución de relaciones de aspecto.
- Recuperado y procesado las máscaras de segmentación.
- Calculado cantidades y proporciones de píxeles correspondientes al animal, fondo y contorno.
- Construido histogramas, diagramas de dispersión, gráficos apilados y gráficos de violín.
- Documentado e interpretado los resultados obtenidos.
- Identificado características relevantes para las siguientes etapas de preprocesamiento y entrenamiento.

---

## 📚 Dataset de referencia

**Oxford-IIIT Pet Dataset**

Parkhi, O. M., Vedaldi, A., Zisserman, A., & Jawahar, C. V. (2012).

*Cats and Dogs.*

IEEE Conference on Computer Vision and Pattern Recognition (CVPR).

[Consultar el dataset original →](https://www.robots.ox.ac.uk/~vgg/data/pets/)

---

[← Volver a Análisis exploratorio del dataset](../../../modulos/02-ingenieria-del-dataset/02-03-analisis-exploratorio-del-dataset.md)