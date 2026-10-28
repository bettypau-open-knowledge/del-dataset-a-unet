# 4.2 · Construcción del pipeline de datos

En el tema anterior aprendimos a diseñar los conjuntos experimentales de entrenamiento (*train*), validación (*validation*) y prueba (*test*), utilizando estrategias de partición que permiten organizar las muestras de manera reproducible y evitar problemas como el *data leakage*.

Ahora contamos con imágenes, máscaras de segmentación, archivos de configuración y particiones que indican a qué conjunto pertenece cada muestra.

Sin embargo, todavía necesitamos resolver una pregunta:

**¿Cómo podemos recuperar, transformar y organizar nuestras imágenes y máscaras para entregarlas correctamente a un modelo de Deep Learning?**

Para ello construiremos un **pipeline de datos**, es decir, una secuencia organizada de operaciones que permite recuperar las muestras desde su ubicación en disco, aplicar las transformaciones necesarias, convertirlas a tensores y agruparlas en lotes para el entrenamiento o la evaluación.

En esta sección conoceremos los componentes principales de este proceso y aprenderemos cómo implementarlos mediante las herramientas que proporciona **PyTorch**.

Comenzaremos estudiando el recorrido de una muestra a través del pipeline:

1. **Manifest y partición:** identifican las imágenes y máscaras que pertenecen a cada conjunto experimental.
2. **Dataset:** localiza y recupera las fotografías y máscaras correspondientes a cada muestra.
3. **Transformaciones:** aplica las operaciones necesarias de manera sincronizada a la imagen y su máscara.
4. **Conversión a tensores:** prepara los datos en el formato que requiere PyTorch.
5. **DataLoader:** solicita las muestras al Dataset y las organiza en lotes (*batches*).
6. **Modelo U-Net:** recibe los lotes de imágenes para producir predicciones de segmentación.

Posteriormente, estudiaremos la clase **`Dataset`**, que define cómo acceder a una muestra individual y prepararla para su utilización.

Para construir una clase personalizada de segmentación, utilizaremos `torch.utils.data.Dataset` y conoceremos tres métodos fundamentales:

- **`__init__()` — Inicialización:** almacena las referencias y la configuración necesarias para trabajar con el conjunto de datos.
- **`__len__()` — Longitud:** devuelve el número de muestras disponibles.
- **`__getitem__()` — Obtener una muestra:** recupera la información correspondiente a un índice y permite preparar la fotografía y su máscara.

Comprenderemos cómo estos métodos permiten organizar el acceso a las muestras sin necesidad de cargar todas las imágenes en memoria desde el inicio.

Después introduciremos **`DataLoader`**, cuya función consiste en solicitar muestras al Dataset y agruparlas en lotes que puedan utilizarse durante el entrenamiento y la evaluación.

Estudiaremos sus tres parámetros principales:

| Parámetro | Función |
|---|---|
| `batch_size` | Determina cuántas muestras se agrupan en cada lote. |
| `shuffle` | Controla si se reordena la secuencia de muestras al crear cada iteración. |
| `num_workers` | Establece cuántos procesos auxiliares se utilizan para cargar las muestras. |

Mediante ejemplos, observaremos cómo `batch_size` determina la cantidad de lotes generados y por qué el último lote puede contener menos muestras cuando el tamaño del conjunto no es múltiplo del tamaño de lote.

También analizaremos cómo `shuffle` modifica el orden en el que se solicitan las muestras, **sin cambiar su asignación a los conjuntos de entrenamiento, validación o prueba**.

Finalmente, conoceremos el funcionamiento de `num_workers` y su relación con la carga secuencial o paralela de datos, considerando las particularidades de los entornos de ejecución utilizados durante el taller.

A lo largo del tema retomaremos la importancia de conservar la correspondencia espacial entre fotografías y máscaras, así como de verificar las dimensiones de los tensores antes de utilizarlos en un modelo de segmentación.

Por ejemplo, para imágenes RGB y máscaras categóricas, un lote puede representarse mediante:

| Elemento | Dimensiones |
|---|---|
| Imagen individual | `(C, H, W)` |
| Máscara individual | `(H, W)` |
| Lote de imágenes | `(B, C, H, W)` |
| Lote de máscaras | `(B, H, W)` |

Donde `B` representa el tamaño del lote, `C` el número de canales y `H` y `W` las dimensiones espaciales.

Estos conocimientos nos permitirán comprender cómo se conectan las etapas de preparación de datos con el entrenamiento de una red neuronal, y por qué **un pipeline correctamente diseñado es fundamental para trabajar con imágenes y máscaras de manera organizada, consistente y reproducible**.

> [!IMPORTANT]
> Antes de utilizar un pipeline para entrenar un modelo, es necesario comprobar que las imágenes y máscaras se recuperen correctamente, que sus dimensiones sean compatibles y que las etiquetas de segmentación se conserven.
>
> También debemos verificar que las transformaciones geométricas se apliquen de manera sincronizada y que las particiones experimentales definidas anteriormente no se modifiquen accidentalmente.

### 📽️ Presentación

[**Ver presentación del tema →**](../../recursos/presentaciones/04-02-construccion-del-pipeline-de-datos.pdf)

---

## 🧪 Prácticas

1. [Aumento de datos con albumentations →](../../practicas/03-procesamiento-de-imagenes-y-mascaras/02-aumento-de-datos.md)

Las actividades prácticas de este tema estarán orientadas a construir y verificar un pipeline de datos para segmentación de imágenes mediante PyTorch.

Retomaremos los archivos de configuración, el manifest y las particiones experimentales generadas en las prácticas anteriores para desarrollar un procedimiento que permita:

- Recuperar los registros correspondientes a los conjuntos de entrenamiento, validación y prueba.
- Construir una clase personalizada que herede de `torch.utils.data.Dataset`.
- Implementar los métodos `__init__()`, `__len__()` y `__getitem__()`.
- Leer fotografías y máscaras de segmentación desde sus rutas.
- Aplicar transformaciones geométricas sincronizadas a imágenes y máscaras.
- Convertir las imágenes y máscaras a tensores con dimensiones y tipos adecuados.
- Crear objetos `DataLoader` para organizar las muestras en lotes.
- Configurar los parámetros `batch_size`, `shuffle` y `num_workers`.
- Inspeccionar las dimensiones y los tipos de datos de las muestras y los lotes.
- Visualizar fotografías y máscaras recuperadas desde el pipeline para comprobar que se mantienen correctamente asociadas.

> [!IMPORTANT]
> Antes de utilizar un pipeline para entrenar un modelo, es necesario comprobar que las imágenes y máscaras se recuperen correctamente, que sus dimensiones sean compatibles y que las etiquetas de segmentación se conserven.
>
> También debemos verificar que las transformaciones geométricas se apliquen de manera sincronizada y que las particiones experimentales definidas anteriormente no se modifiquen accidentalmente.

El punto de control consistirá en obtener **lotes de imágenes y máscaras correctamente construidos, con dimensiones y tipos verificados, y cuya correspondencia pueda comprobarse visualmente**.

---

## ➡️ Siguiente etapa

Una vez construido y verificado el pipeline, podremos utilizarlo para proporcionar los datos a nuestro modelo de segmentación U-Net durante el entrenamiento y la evaluación.

---

[← Volver al repositorio principal del taller](https://github.com/bettypau-open-knowledge/del-dataset-a-unet)