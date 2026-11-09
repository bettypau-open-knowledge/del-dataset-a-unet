# 6.2 · Entrenamiento, evaluación y análisis de resultados

En el tema anterior estudiamos los fundamentos del entrenamiento de redes neuronales, comprendiendo cómo las funciones de pérdida, la retropropagación y los optimizadores permiten actualizar los parámetros de un modelo.

Ahora debemos responder una pregunta fundamental:

**¿Podemos afirmar que nuestro modelo segmentará correctamente imágenes nuevas únicamente porque su pérdida de entrenamiento disminuye?**

Para responderla, estudiaremos cómo **evaluar el aprendizaje de una red neuronal y analizar su capacidad de generalización**.

Comenzaremos distinguiendo los procesos de **entrenamiento y validación**, identificando sus objetivos y las operaciones que se realizan en cada uno. Comprenderemos por qué la validación permite observar el comportamiento del modelo sobre datos que no utiliza para actualizar sus parámetros.

Posteriormente, analizaremos las **curvas de aprendizaje**, que representan la evolución de las pérdidas de entrenamiento y validación a lo largo de las épocas. Aprenderemos a reconocer comportamientos asociados con el subajuste, el aprendizaje favorable y el sobreajuste, así como posibles acciones para mejorar el entrenamiento.

También estudiaremos el uso de **checkpoints**, que permiten conservar y recuperar el estado de un modelo. Distinguiremos entre guardar la última época, conservar el modelo con mejor resultado de validación y almacenar la información necesaria para reanudar el entrenamiento.

Finalmente, abordaremos la **evaluación cuantitativa de la segmentación binaria**. A partir de la matriz de confusión y sus cuatro componentes —verdaderos positivos (TP), verdaderos negativos (TN), falsos positivos (FP) y falsos negativos (FN)—, conoceremos las principales métricas utilizadas para medir el desempeño:

- **Precision y Recall:** permiten analizar los errores de clasificación y la capacidad para detectar los píxeles de interés.
- **Dice/F1 e IoU:** cuantifican la coincidencia entre las máscaras predichas y las reales.
- **Accuracy y Specificity:** proporcionan información complementaria sobre la clasificación de los píxeles.

Comprenderemos que **ninguna métrica describe por sí sola todos los aspectos del desempeño de un modelo** y que la interpretación de los resultados debe complementarse con la revisión visual de las máscaras.

Al finalizar este tema, contaremos con los fundamentos necesarios para **monitorear el entrenamiento, seleccionar un modelo y evaluar sus predicciones de segmentación**, distinguiendo entre aprender sobre los datos de entrenamiento y generalizar a imágenes no utilizadas durante el aprendizaje.

### 📽️ Presentación

[**Ver presentación del tema →**](../../recursos/presentaciones/06-02-entrenamiento-evaluacion-analisis.pdf)

---

## 🧪 Prácticas

En las actividades prácticas aplicaremos los conceptos estudiados para:

- Registrar y comparar las pérdidas de entrenamiento y validación.
- Visualizar e interpretar curvas de aprendizaje.
- Identificar posibles comportamientos de subajuste y sobreajuste.
- Guardar y recuperar checkpoints del modelo.
- Calcular TP, TN, FP y FN a partir de máscaras binarias.
- Obtener métricas como Precision, Recall, Dice/F1, IoU, Accuracy y Specificity.
- Comparar las máscaras reales y predichas para interpretar los resultados.

---

[← Volver al repositorio principal del taller](https://github.com/bettypau-open-knowledge/del-dataset-a-unet)