# Módulo 3 · Procesamiento de imágenes y máscaras

Una vez que hemos explorado, organizado y analizado nuestro dataset, el siguiente paso consiste en comprender cómo se representan las imágenes digitales y qué operaciones podemos aplicar para prepararlas antes de utilizarlas en un modelo de segmentación.

En este módulo abordaremos el **procesamiento de imágenes y máscaras**, comenzando por los fundamentos de la representación digital de imágenes y las transformaciones básicas, y continuando con el tratamiento de máscaras de segmentación, las operaciones morfológicas y las técnicas de aumento de datos.

El objetivo es desarrollar los conocimientos y habilidades necesarios para **leer, representar y transformar imágenes y máscaras de manera adecuada, preservando la información relevante para las siguientes etapas del proyecto**.

## 📚 Temas de la unidad

1. **Fundamentos y procesamiento básico:** representación de imágenes digitales, píxeles, resolución espacial, canales, profundidad de bits, matrices y tensores, redimensionamiento, interpolación, conversión de tipos y normalización.
2. **Aumento de datos:** representación y procesamiento de máscaras de segmentación, operaciones morfológicas y transformaciones geométricas y fotométricas para el aumento de datos.

---

# 3.1 · Fundamentos y procesamiento básico

Antes de aplicar transformaciones a nuestras imágenes, es importante comprender **cómo se representa una imagen digital, qué información contiene cada píxel y cómo se organizan sus valores en estructuras de datos que podemos manipular mediante Python**.

En esta sección estudiaremos los conceptos de **píxel, resolución espacial, canales y profundidad de bits**, así como la representación de imágenes en escala de grises y RGB mediante **matrices y tensores**. También distinguiremos entre los formatos HWC (alto, ancho, canales) y CHW (canales, alto, ancho), utilizados habitualmente en diferentes bibliotecas de procesamiento de imágenes y Deep Learning.

Posteriormente, abordaremos el **redimensionamiento (*resize*) y los métodos de interpolación**, analizando cómo estas operaciones modifican el número de píxeles y pueden afectar la relación de aspecto y la apariencia de una imagen. Compararemos los métodos de vecino más cercano, interpolación bilineal e interpolación bicúbica.

Finalmente, estudiaremos la diferencia entre **conversión de tipos de datos, escalado de intensidades y estandarización**, reconociendo que son operaciones distintas y que las transformaciones de intensidad utilizadas en las fotografías no deben aplicarse indiscriminadamente a las etiquetas categóricas de las máscaras de segmentación.

Estos conceptos nos permitirán comprender cómo preparar las imágenes de entrada para un modelo de segmentación, identificando las implicaciones de cada transformación sobre su representación y contenido.

### 📽️ Presentación

[**Ver presentación del tema →**](../../recursos/presentaciones/03-01-fundamentos-y-procesamiento-basico.pdf)

---

## 🧪 Práctica

1. [Procesamiento básico de imágenes →](../../practicas/03-procesamiento-de-imagenes-y-mascaras/01-procesamiento-basico-imagenes.md)

---

## ➡️ Siguiente tema

[Aumento de datos →](./03-02-aumento-de-datos.md)

---

[← Volver al índice de módulos](../modulos.md)

[← Volver a la portada del taller](../../README.md)