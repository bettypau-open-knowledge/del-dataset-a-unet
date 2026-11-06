# Módulo 6 · Entrenamiento, evaluación y análisis

En los módulos anteriores aprendimos a organizar y preparar un dataset de segmentación de imágenes, diseñar conjuntos experimentales reproducibles y construir un pipeline de datos mediante PyTorch.

Posteriormente, estudiamos los fundamentos de las redes neuronales convolucionales (CNN) y la arquitectura U-Net, comprendiendo cómo sus componentes permiten extraer características visuales, recuperar información espacial y generar predicciones de segmentación por píxel.

Ahora contamos con los elementos necesarios para comprender cómo una red neuronal puede **aprender a producir máscaras de segmentación a partir de las imágenes y anotaciones de nuestro dataset**.

Sin embargo, construir una arquitectura no significa que sus parámetros ya permitan realizar predicciones correctas. Para que el modelo aprenda, necesitamos establecer un procedimiento que permita comparar sus predicciones con las máscaras reales, cuantificar los errores y actualizar progresivamente sus parámetros.

En este módulo estudiaremos el **entrenamiento, la evaluación y el análisis de modelos de segmentación**, utilizando los fundamentos que hemos desarrollado a lo largo del taller.

Comenzaremos con el proceso de entrenamiento, identificando las operaciones que se realizan durante cada iteración y comprendiendo cómo intervienen las funciones de pérdida, la retropropagación y los optimizadores.

Posteriormente, utilizaremos estos conocimientos para entrenar nuestro modelo, evaluar sus predicciones e interpretar los resultados obtenidos.

El propósito es comprender **cómo aprende una red neuronal, cómo podemos medir su desempeño y qué información necesitamos analizar para determinar si está segmentando correctamente las imágenes**.

## 📚 Temas de la unidad

1. **Fundamentos y proceso de entrenamiento:** batch, iteración, época, forward pass, funciones de pérdida para segmentación, backpropagation, acumulación de gradientes, learning rate y optimizadores.
2. **Entrenamiento, evaluación y análisis de resultados:** ejecución del entrenamiento, validación, métricas de segmentación, seguimiento del aprendizaje, evaluación del modelo e interpretación de predicciones y errores.

---

# 6.1 · Fundamentos y proceso de entrenamiento

En el módulo anterior estudiamos la arquitectura U-Net y comprendimos cómo sus componentes permiten transformar una imagen de entrada en una predicción de segmentación.

Analizamos el funcionamiento del encoder, decoder, bottleneck, skip connections y la capa de salida, identificando cómo se generan los logits que representan las predicciones del modelo.

Ahora debemos responder una pregunta fundamental:

**¿Cómo aprende U-Net a producir máscaras cada vez más parecidas a las anotaciones reales y qué operaciones permiten modificar sus parámetros para reducir los errores?**

Para responderla, comenzaremos estudiando el **ciclo de entrenamiento de una red neuronal**, identificando los conceptos que permiten organizar el procesamiento de los datos y las operaciones necesarias para actualizar sus parámetros.

Distinguiremos cuatro conceptos fundamentales:

- **Batch:** conjunto de muestras que se procesan simultáneamente durante una iteración.
- **Iteración:** procesamiento de un batch que, durante el entrenamiento convencional, incluye el cálculo de predicciones, la pérdida, los gradientes y la actualización de parámetros.
- **Época (*epoch*):** recorrido completo del conjunto de entrenamiento.
- **Forward pass:** propagación de las imágenes a través del modelo para obtener predicciones, sin actualizar todavía sus parámetros.

Posteriormente, estudiaremos las operaciones que conforman una iteración de entrenamiento:

1. **Reiniciar los gradientes:** limpiar los valores acumulados de iteraciones anteriores.
2. **Forward pass:** obtener las predicciones del modelo a partir de las imágenes.
3. **Cálculo de la pérdida:** comparar las predicciones con las máscaras reales.
4. **Backward pass:** calcular los gradientes de la pérdida respecto a los parámetros entrenables mediante backpropagation.
5. **Actualización de parámetros:** utilizar un optimizador para modificar los pesos del modelo.

Esta secuencia nos permitirá comprender cómo las predicciones y los errores obtenidos durante cada batch contribuyen al aprendizaje de la red neuronal.

**Función de pérdida y métricas de evaluación**

Estudiaremos la diferencia entre una **función de pérdida (*loss function*)** y una **métrica de evaluación**.

La función de pérdida cuantifica el error de las predicciones y proporciona una señal que permite optimizar los parámetros del modelo.

Por su parte, las métricas permiten medir e interpretar su desempeño mediante criterios que resultan significativos para el problema de segmentación.

Conoceremos métricas como **Dice Score, Intersection over Union (IoU), precisión y recall**, y comprenderemos que no necesariamente deben utilizarse como funciones de pérdida.

**Funciones de pérdida para segmentación**

Posteriormente, estudiaremos diferentes funciones de pérdida utilizadas para entrenar modelos de segmentación de imágenes.

Comenzaremos con **Binary Cross-Entropy (BCE)**, que mide el error de las probabilidades predichas para un problema de clasificación binaria.

También conoceremos **`BCEWithLogitsLoss` de PyTorch**, que combina internamente la transformación Sigmoid con el cálculo de BCE y permite trabajar directamente con los logits del modelo.

Después estudiaremos **Dice Loss**, una función basada en el solapamiento entre la predicción y la máscara real.

Comprenderemos por qué puede resultar útil cuando existen regiones de interés pequeñas o un desequilibrio importante entre el objeto y el fondo.

Posteriormente, conoceremos **Focal Loss**, diseñada para reducir la contribución relativa de ejemplos fáciles y concentrar el aprendizaje en predicciones difíciles.

Finalmente, estudiaremos **Generalized Dice Focal Loss (GDFL)**, que combina dos objetivos complementarios:

- **Generalized Dice Loss:** considera el solapamiento entre clases e incorpora ponderaciones para abordar diferencias en su representación.
- **Focal Loss:** enfatiza las predicciones difíciles durante el aprendizaje.

Compararemos las características, ventajas y limitaciones de estas funciones de pérdida, identificando qué aspectos de la segmentación busca optimizar cada una.

También conoceremos ejemplos de implementación mediante PyTorch y MONAI.

**Backpropagation y cálculo de gradientes**

Una vez comprendido cómo se cuantifica el error, estudiaremos el mecanismo que permite calcular cómo debe modificarse cada parámetro de la red neuronal.

Analizaremos la **retropropagación del error (*backpropagation*)**, mediante la cual se calculan los gradientes de la función de pérdida respecto a los parámetros entrenables.

Comprenderemos que un gradiente indica cómo cambia la pérdida ante una pequeña variación de un parámetro.

En PyTorch, esta operación se realiza mediante:

```python
loss.backward()
```

Estudiaremos cómo los gradientes calculados se almacenan en el atributo `.grad` de los parámetros y por qué es necesario administrarlos correctamente durante el entrenamiento.

**Acumulación de gradientes**

También analizaremos una característica importante de PyTorch: los gradientes se acumulan de manera predeterminada cuando ejecutamos sucesivas llamadas a `loss.backward()`.

Comprenderemos la diferencia entre dos estrategias:

- **Actualización por batch:** calcular gradientes y actualizar los parámetros después de procesar cada lote.
- **Acumulación de gradientes:** procesar varios microbatches, acumular sus contribuciones y actualizar los parámetros una vez completado el grupo.

Conoceremos el uso de:

```python
optimizer.zero_grad()
```

y estudiaremos en qué momento debe ejecutarse para evitar acumulaciones no deseadas o permitir una acumulación controlada.

También comprenderemos por qué la acumulación de gradientes puede resultar útil cuando la memoria disponible no permite procesar simultáneamente un batch grande.

**Optimizadores y learning rate**

Finalmente, estudiaremos los **optimizadores**, componentes encargados de actualizar los parámetros del modelo utilizando los gradientes calculados durante backpropagation.

Comenzaremos con la regla básica del descenso de gradiente:

$$
w_{t+1}=w_t-\eta\frac{\partial\mathcal{L}}{\partial w_t}
$$

Donde:

- $(w_t)$: valor actual del parámetro.
- $(w_{t+1})$: valor actualizado del parámetro.
- $(\eta)$: learning rate o tasa de aprendizaje.
- $(\frac{\partial\mathcal{L}}{\partial w_t})$: gradiente de la pérdida respecto al parámetro.

Analizaremos cómo el **learning rate** determina la magnitud de las actualizaciones y por qué valores demasiado grandes o demasiado pequeños pueden dificultar el entrenamiento.

Posteriormente, compararemos tres optimizadores utilizados en Deep Learning:

- **SGD:** utiliza los gradientes para actualizar los parámetros y puede incorporar momentum.
- **Adam:** combina estimaciones adaptativas de primer y segundo momento de los gradientes.
- **AdamW:** utiliza una estrategia de actualización adaptativa con regularización mediante *weight decay* desacoplado.

Comprenderemos sus principales diferencias y conoceremos cómo se utilizan mediante PyTorch.

Finalmente, integraremos los conceptos estudiados para interpretar el ciclo completo de entrenamiento:

```python
optimizer.zero_grad()

logits = modelo(imagenes)

loss = criterio(logits, mascaras)

loss.backward()

optimizer.step()
```

Esta secuencia nos permitirá distinguir claramente las responsabilidades de cada operación:

- `optimizer.zero_grad()` limpia los gradientes acumulados.
- `modelo(imagenes)` realiza el forward pass.
- `criterio(logits, mascaras)` calcula la pérdida.
- `loss.backward()` calcula los gradientes mediante backpropagation.
- `optimizer.step()` actualiza los parámetros del modelo.

Al finalizar este tema comprenderemos que **el aprendizaje de U-Net es un proceso iterativo en el que las predicciones se comparan con las máscaras reales, los errores se cuantifican mediante una función de pérdida y los parámetros se actualizan utilizando gradientes y un optimizador**.

### 📽️ Presentación

[**Ver presentación del tema →**](../../recursos/presentaciones/06-01-fundamentos-y-proceso-de-entrenamiento.pdf)

---

## 🧪 Prácticas

1. [Entrenamiento de una Mini U-Net con el Oxford-IIIT Pet Dataset →](../../practicas/06-entrenamiento-evaluacion-analisis/01-fundamentos-y-proceso-entrenamiento.md)



---
<!--
## ➡️ Siguiente tema

**Entrenamiento, evaluación y análisis de resultados**

En el siguiente tema utilizaremos los fundamentos del proceso de entrenamiento para ejecutar el aprendizaje de nuestro modelo, registrar su comportamiento y evaluar las predicciones obtenidas.

También estudiaremos cómo interpretar las métricas de segmentación y analizar los resultados para identificar aciertos, errores y posibles oportunidades de mejora.
-->
---

[← Volver al repositorio principal del taller](https://github.com/bettypau-open-knowledge/del-dataset-a-unet)