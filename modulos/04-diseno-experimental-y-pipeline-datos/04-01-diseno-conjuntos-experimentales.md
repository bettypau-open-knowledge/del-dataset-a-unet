# Módulo 4 · Diseño experimental y pipeline de datos

Una vez que hemos explorado y organizado nuestro dataset, comprendido cómo se representan las imágenes digitales y aprendido a aplicar diferentes transformaciones a imágenes y máscaras, el siguiente paso consiste en preparar los datos para entrenar y evaluar nuestro modelo de segmentación.

Sin embargo, antes de comenzar el entrenamiento, es necesario definir qué muestras utilizaremos para aprender, cuáles emplearemos para ajustar el modelo y cuáles reservaremos para evaluar su capacidad de generalización.

En este módulo abordaremos el **diseño experimental y la construcción del pipeline de datos**, comenzando por la organización de los conjuntos de entrenamiento, validación y prueba, y continuando con la preparación de los mecanismos que permitirán proporcionar imágenes y máscaras al modelo de manera organizada y reproducible.

El objetivo es establecer un procedimiento que permita **preparar, separar y utilizar los datos de forma consistente, evitando problemas que puedan comprometer la interpretación de los resultados experimentales**.

## 📚 Temas de la unidad

1. **Diseño de los conjuntos experimentales:** propósito de los conjuntos de entrenamiento, validación y prueba; proporciones de partición; estrategias de separación de muestras y prevención de *data leakage*.
2. **Construcción del pipeline de datos:** organización de los procedimientos necesarios para cargar, transformar y proporcionar imágenes y máscaras al modelo durante el entrenamiento y la evaluación.

---

# 4.1 · Diseño de los conjuntos experimentales

En los módulos anteriores aprendimos a identificar imágenes y máscaras, registrar sus características, analizar su contenido y aplicar transformaciones para prepararlas antes del entrenamiento.

Pero ahora debemos responder una pregunta fundamental:

**¿Podemos entrenar un modelo utilizando todas las imágenes disponibles y después evaluar su rendimiento con esas mismas imágenes?**

Aunque técnicamente sería posible calcular métricas sobre los datos utilizados durante el entrenamiento, estos resultados no proporcionarían una estimación independiente de la capacidad del modelo para trabajar con imágenes nuevas.

Por esta razón, en esta sección estudiaremos el propósito de los tres conjuntos experimentales: **entrenamiento (*train*), validación (*validation*) y prueba (*test*)**.

Comprenderemos cómo se utilizan durante el desarrollo de un modelo, por qué cumplen funciones diferentes y cómo la información del conjunto de validación puede influir indirectamente en las decisiones de diseño, mientras que el conjunto de prueba debe permanecer reservado para la evaluación final.

También analizaremos diferentes **proporciones de partición**, reconociendo que no existe una distribución universalmente óptima y que su elección depende de las características del dataset y del problema que queremos resolver.

Posteriormente, conoceremos distintas **estrategias de separación de datos**, entre ellas:

- **Holdout aleatorio:** división aleatoria del dataset en conjuntos independientes.
- **Holdout estratificado:** partición que busca conservar las proporciones de las categorías.
- **Partición por grupos:** separación que mantiene juntas las muestras relacionadas, como imágenes de un mismo paciente, animal o escena.
- **K-Fold Cross-Validation:** evaluación mediante diferentes particiones de entrenamiento y validación.
- **Stratified K-Fold:** validación cruzada que procura conservar las proporciones de las clases.
- **Group K-Fold:** validación cruzada que evita compartir grupos entre entrenamiento y validación.
- **Stratified Group K-Fold:** combinación de separación por grupos y conservación aproximada de las proporciones de clases.

Finalmente, abordaremos uno de los problemas más importantes del diseño experimental: el **data leakage**, que ocurre cuando información que no debería estar disponible durante el entrenamiento o la selección del modelo termina influyendo en el proceso y puede provocar una evaluación artificialmente optimista.

Estudiaremos diferentes escenarios, como utilizar una misma imagen para entrenar y evaluar, distribuir imágenes casi idénticas entre conjuntos diferentes o separar incorrectamente muestras relacionadas.

También retomaremos el concepto de **data augmentation**, reconociendo que las variantes generadas a partir de una misma imagen original no deben distribuirse entre los conjuntos de entrenamiento y evaluación.

Estos conocimientos nos permitirán comprender por qué **una partición experimental adecuada es indispensable para obtener resultados confiables y evaluar de manera justa la capacidad de generalización de un modelo de segmentación**.

### 📽️ Presentación

[**Ver presentación del tema →**](../../recursos/presentaciones/04-01-diseno-conjuntos-experimentales.pdf)

> [!IMPORTANT]
> La separación del dataset debe realizarse **antes de aplicar transformaciones aleatorias de aumento de datos** que puedan generar variantes relacionadas.
>
> De esta manera evitamos que diferentes versiones de una misma imagen original terminen distribuidas entre entrenamiento, validación y prueba, comprometiendo la interpretación del rendimiento del modelo.

---

## 🧪 Prácticas

1. [Diseño de los conjuntos experimentales del minidataset →](../../practicas/04-diseno-experimental-y-pipeline-datos/diseno-conjuntos-experimentales/01-diseno-conjuntos-experimentales-minidataset.md)
2. [Diseño de conjuntos experimentales del Oxford-IIIT Pet Dataset →](../../practicas/04-diseno-experimental-y-pipeline-datos/diseno-conjuntos-experimentales/02-diseno-conjuntos-experimentales-oxford-dataset.md)


---

## ➡️ Siguiente tema

[Construcción del pipeline de datos →](./04-02-construccion-pipeline-datos.md)

---

[← Volver al índice de módulos](../modulos.md)

[← Volver a la portada del taller](../../README.md)