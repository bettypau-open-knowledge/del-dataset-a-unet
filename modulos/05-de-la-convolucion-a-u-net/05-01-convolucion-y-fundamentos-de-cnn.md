# Módulo 5 · De la convolución a U-Net

En los módulos anteriores aprendimos a organizar y preparar un dataset de segmentación de imágenes, diseñar conjuntos experimentales reproducibles y construir un pipeline de datos mediante PyTorch.

Ahora contamos con fotografías y máscaras organizadas en tensores, preparados para utilizarse durante el entrenamiento y la evaluación de un modelo de Deep Learning.

Sin embargo, todavía debemos comprender **cómo una red neuronal procesa estos tensores, identifica características visuales y transforma la información de entrada en una predicción de segmentación**.

En este módulo estudiaremos los fundamentos de las **redes neuronales convolucionales (CNN)** y su aplicación en la arquitectura U-Net.

Comenzaremos analizando las operaciones que permiten extraer características de las imágenes y comprenderemos cómo se relacionan las dimensiones espaciales, los canales y los parámetros entrenables de una red neuronal.

Posteriormente, utilizaremos estos conocimientos para estudiar la arquitectura U-Net, identificando los componentes que permiten combinar información de diferentes niveles de representación y producir predicciones de segmentación.

El propósito es comprender **cómo se construye y funciona una red neuronal capaz de transformar imágenes en mapas de segmentación**, antes de implementar nuestro propio modelo.

## 📚 Temas de la unidad

1. **Convolución y fundamentos de las CNN:** kernels, mapas de características, canales, stride, padding, dilation, parámetros entrenables, normalización, funciones de activación, pooling, dropout y convolución transpuesta.
2. **Arquitectura U-Net:** estructura encoder-decoder, bottleneck, conexiones de salto (*skip connections*), recuperación de la resolución espacial y generación de mapas de segmentación.

---

# 5.1 · Convolución y fundamentos de las CNN

En el módulo anterior construimos un pipeline que nos permite recuperar fotografías y máscaras, aplicar transformaciones y organizar las muestras en lotes de tensores.

Ahora debemos responder una pregunta fundamental:

**Tenemos un tensor de imágenes y otro de máscaras. ¿Qué operaciones debe realizar una red neuronal para transformar el primero en una predicción con la estructura espacial del segundo?**

Para responderla, comenzaremos estudiando la **convolución**, una de las operaciones fundamentales de las redes neuronales convolucionales.

Analizaremos cómo un **kernel o filtro** recorre una imagen, realiza operaciones sobre regiones locales y produce un **mapa de características (*feature map*)**. Mediante ejemplos visuales y cálculos manuales, observaremos cómo se obtienen los valores de salida y por qué diferentes filtros pueden responder a distintos patrones visuales, como bordes, texturas y formas.

Posteriormente, estudiaremos los principales elementos que determinan el comportamiento de una capa convolucional:

- **Weights (*kernel*):** parámetros aprendibles que determinan cómo se combinan los valores de entrada.
- **Bias:** término adicional aprendible que puede incorporarse a la salida de la convolución.
- **Stride:** desplazamiento del kernel sobre la imagen.
- **Padding:** incorporación de bordes que permite controlar las dimensiones espaciales de salida.
- **Dilation:** separación entre los elementos del kernel que permite ampliar su campo receptivo.

También analizaremos la relación entre los **canales de entrada, filtros de salida y canales de salida**, comprendiendo cómo una capa convolucional procesa simultáneamente múltiples canales y genera diferentes mapas de características.

A partir de estos conceptos, aprenderemos a calcular las dimensiones espaciales de salida y el número de parámetros entrenables de una capa convolucional.

Distinguiremos especialmente entre el número de parámetros y el costo computacional de procesar imágenes, observando que **aumentar la resolución espacial o el tamaño del batch no incrementa, por sí mismo, el número de parámetros de una misma capa `Conv2d`**, aunque sí puede incrementar las operaciones y la memoria necesarias.

Después estudiaremos diferentes mecanismos utilizados para transformar, regularizar y organizar las representaciones aprendidas por una CNN.

**Normalización**

Conoceremos dos estrategias:

- **Batch Normalization:** normaliza las activaciones utilizando estadísticas calculadas por canal a partir del batch y las dimensiones espaciales durante el entrenamiento.
- **Group Normalization:** organiza los canales en grupos y calcula estadísticas de normalización dentro de cada grupo, sin depender de las estadísticas de otras imágenes del batch.

Compararemos sus características y comprenderemos por qué el tamaño del batch puede influir en la elección de una estrategia de normalización.

**Funciones de activación y pooling**

Estudiaremos la función de activación **ReLU**, que introduce no linealidad al conservar los valores positivos y convertir los negativos en cero.

También conoceremos **Max Pooling**, una operación que selecciona los valores máximos de regiones locales para reducir las dimensiones espaciales de los mapas de características.

Comprenderemos cómo estas operaciones participan en la construcción de representaciones visuales progresivamente más complejas.

**Dropout**

Analizaremos Dropout como una técnica de regularización que desactiva aleatoriamente activaciones durante el entrenamiento para reducir el riesgo de sobreajuste.

Distinguiremos su comportamiento durante entrenamiento y evaluación, y conoceremos la diferencia entre `Dropout` y `Dropout2d` en redes convolucionales.

Finalmente, estudiaremos **`ConvTranspose2d`**, una operación que permite generar mapas de características con mayor resolución espacial.

Comprenderemos cómo se calculan sus dimensiones de salida y qué función cumplen los parámetros `stride`, `padding` y `output_padding`.

También identificaremos por qué una convolución transpuesta **no representa la operación inversa de una convolución convencional**, aunque puede utilizarse para aumentar la resolución espacial de las representaciones.

Estos conocimientos nos permitirán comprender las operaciones fundamentales que utilizaremos posteriormente para construir la arquitectura U-Net, en la que necesitaremos tanto extraer características como recuperar información espacial para generar máscaras de segmentación.

### 📽️ Presentación

[**Ver presentación del tema →**](../../recursos/presentaciones/05-01-convolucion-y-fundamentos-de-las-CNN.pdf)

---

## 🧪 Prácticas

1. [Introducción CNN →](https://github.com/bettypau-open-knowledge/del-dataset-a-unet_introduccion_cnn.git)

---

## ➡️ Siguiente tema

[Arquitectura U-Net →](./05-02-arquitectura-u-net.md)

---

[← Volver al repositorio principal del taller](https://github.com/bettypau-open-knowledge/del-dataset-a-unet)