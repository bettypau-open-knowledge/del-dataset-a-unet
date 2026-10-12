# Módulo 2 · Ingeniería del dataset

Antes de entrenar un modelo de segmentación de imágenes, es necesario conocer los datos con los que trabajaremos, comprender cómo están organizados y comprobar que cumplen con las condiciones necesarias para utilizarlos.

En este módulo abordaremos la **ingeniería del dataset**, comenzando por la exploración de sus componentes y estructura, continuando con la construcción de un inventario y su configuración, y finalizando con una auditoría y un análisis exploratorio que nos permitan identificar posibles problemas en los datos.

El objetivo es desarrollar un proceso organizado y reproducible para **conocer, documentar y evaluar un dataset antes de utilizarlo en las siguientes etapas del proyecto**.

<!--
## 📚 Temas de la unidad

1. **Exploración de un dataset de segmentación:** identificación de imágenes, máscaras, etiquetas, metadatos y estructuras de directorios.
2. **Inventario y configuración del dataset:** identificación y registro de los archivos disponibles, sus características y la configuración necesaria para trabajar con ellos.
3. **Auditoría y análisis exploratorio:** revisión de la integridad, consistencia y características de los datos para detectar posibles problemas antes de su procesamiento.
-->
---

# 2.1 · Exploración de un dataset de segmentación

Antes de comenzar a procesar imágenes o entrenar un modelo de segmentación, es importante comprender **qué información contiene un dataset, cómo está organizada y qué relación existe entre sus diferentes componentes**.

En esta sección exploraremos la **anatomía de un dataset de segmentación**, distinguiendo entre **imágenes, máscaras, etiquetas y metadatos**. También analizaremos diferentes **estructuras de directorios y convenciones de nombres**, reconociendo que no todos los datasets se organizan de la misma manera y que es necesario identificar correctamente la correspondencia entre imágenes y máscaras.

Estos conceptos nos permitirán comprender qué información recibe un modelo, de dónde obtiene las respuestas correctas durante el entrenamiento y por qué es importante conocer y documentar la organización de los datos antes de utilizarlos.

### 📽️ Presentación

[**Ver presentación del tema →**](../../recursos/presentaciones/02-ingenieria-del-dataset.pdf)

### Requerimientos

Para poder ejecutar las prácticas de este módulo y de los siguientes de manera local, necesitas crear un entorno de Python con las bibliotecas necesarias para trabajar con datasets, procesar imágenes y desarrollar modelos de segmentación mediante Deep Learning. Puedes crear ese entorno siguiendo estas instrucciones:

[Configuración del entorno local del taller →](../../practicas/02-ingenieria-del-dataset/00-environment-taller.md)

---

## 🧪 Prácticas

1. [Exploración inicial de un dataset de segmentación →](../../practicas/02-ingenieria-del-dataset/exploracion-de-un-dataset/01-exploracion-inicial-de-un-dataset)
2. [Exploración inicial del Oxford-IIIT Pet Dataset →](../../practicas/02-ingenieria-del-dataset/exploracion-de-un-dataset/02-exploracion-inicial-del-oxford-dataset.md)



---
<!--
## ➡️ Siguiente tema

[Inventario y configuración del dataset →](./02-02-inventario-y-configuracion.md)
-->
---

[← Volver al índice de módulos](../modulos.md)

[← Volver a la portada del taller](../../README.md)