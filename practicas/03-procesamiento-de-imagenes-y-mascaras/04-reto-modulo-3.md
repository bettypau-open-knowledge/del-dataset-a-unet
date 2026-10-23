# 🐈 Reto Unidad 3: ¡Encuentra al gato!

Durante esta unidad aprendiste cómo se representan las imágenes digitales, cómo manipularlas mediante matrices y tensores, y qué operaciones podemos aplicar para prepararlas antes de entrenar un modelo de segmentación.

También estudiamos los métodos de redimensionamiento e interpolación, las diferencias entre conversión de tipos, escalado y estandarización, y la importancia de utilizar procedimientos adecuados para las máscaras de segmentación.

Finalmente, conocimos las técnicas de **aumento de datos (*data augmentation*)** y utilizamos **Albumentations** para aplicar transformaciones geométricas y fotométricas, conservando la correspondencia entre imágenes y máscaras.

Ahora es momento de poner a prueba lo aprendido.

En este reto deberás responder **10 preguntas de opción múltiple** relacionadas con los conceptos y herramientas estudiados durante el **Módulo 3 · Procesamiento de imágenes y máscaras**.

Pero hay un pequeño detalle: **¡un gato se ha escondido al final del notebook!** 🐈

Para encontrarlo, tendrás que responder correctamente todas las preguntas.

**¿Podrás conseguir que aparezca?**

---

## 🎯 Objetivo

Evaluar e integrar los conocimientos adquiridos durante el Módulo 3 mediante un cuestionario interactivo desarrollado en Jupyter Notebook.

Durante el reto pondrás a prueba tu comprensión de:

- Píxeles, resolución espacial, canales y profundidad de bits.
- Representación de imágenes mediante matrices y tensores.
- Imágenes RGB y en escala de grises.
- Formatos HWC, CHW y BCHW.
- Redimensionamiento y relación de aspecto.
- Métodos de interpolación.
- Conversión de tipos de datos.
- Escalado y estandarización de intensidades.
- Tratamiento de máscaras categóricas.
- Transformaciones geométricas y fotométricas.
- Aumento de datos mediante Albumentations.
- Aplicación sincronizada de transformaciones a imágenes y máscaras.

---

## 💻 Instrucciones

Para realizar este reto necesitarás:

- Visual Studio Code.
- El repositorio de GitHub del Reto 3, que contiene los archivos y módulos necesarios para ejecutar el cuestionario.
- Un entorno de ejecución de Python, que puede ser **local o de Google Colab**.

**Repositorio de GitHub:**

[🐙 Consultar el repositorio del Reto 3](https://github.com/bettypau-open-knowledge/del-dataset-a-unet_reto-3)

El notebook del cuestionario se encuentra dentro del directorio `notebooks/` del repositorio.

Puedes realizar la actividad utilizando cualquiera de las dos modalidades descritas a continuación.

---

## ☁️ Opción A · Ejecutar el reto en Google Colab

### 1 · Abre el repositorio

Descarga o clona el repositorio del reto y abre la carpeta del proyecto en **Visual Studio Code**.

Localiza el notebook del cuestionario dentro del directorio:

```text
notebooks/
```

### 2 · Conecta el notebook a Google Colab

Abre el notebook en Visual Studio Code.

Conéctalo a un runtime de **Google Colab**, utilizando el procedimiento aprendido en las prácticas anteriores.

Comprueba que el kernel seleccionado corresponde al runtime de Colab.

### 3 · Prepara los archivos del reto

Ejecuta las celdas de preparación del notebook siguiendo sus indicaciones.

Estas instrucciones permiten acceder a los archivos y módulos del repositorio que necesita el cuestionario para funcionar.

> [!NOTE]
> Recuerda que, aunque el notebook se encuentre abierto en VS Code, las instrucciones se ejecutarán en el runtime remoto de Google Colab.
>
> Los archivos almacenados localmente no están disponibles automáticamente en ese entorno remoto.

---

## 💻 Opción B · Ejecutar el reto localmente

También puedes realizar este reto utilizando un entorno de Python instalado en tu computadora, sin necesidad de conectarte a Google Colab.

### 1 · Descarga el repositorio

Descarga o clona el repositorio de GitHub proporcionado para esta actividad.

Si decides utilizar Git, puedes ejecutar:

```bash
git clone https://github.com/bettypau-open-knowledge/del-dataset-a-unet_reto-3.git
```

Abre la carpeta del repositorio en **Visual Studio Code**.

### 2 · Localiza el notebook

Dentro del repositorio, localiza el directorio:

```text
notebooks/
```

El notebook del cuestionario ya se encuentra incluido en esta carpeta, por lo que **no es necesario descargarlo ni moverlo a otra ubicación**.

La estructura general será similar a:

```text
del-dataset-a-unet_reto-3/
├── src/
│   └── ...
├── notebooks/
│   └── encuentra-al-gato-3.ipynb
└── ...
```

> [!IMPORTANT]
> Conserva la organización original del repositorio.
>
> Antes de ejecutar el notebook, comprueba que las rutas utilizadas para importar los módulos y acceder a los recursos sean correctas respecto a su ubicación dentro de `notebooks/`.

### 3 · Prepara el entorno de Python

Utiliza un entorno de Conda que tenga instalados los paquetes necesarios para ejecutar el notebook interactivo.

En particular, el entorno debe contar con:

- `ipykernel`: permite utilizar el entorno de Python como kernel de Jupyter.
- `ipywidgets`: permite utilizar los componentes interactivos del cuestionario.

Si todavía no están instalados, activa tu entorno y ejecuta:

```bash
conda install -c conda-forge ipykernel ipywidgets
```

> [!NOTE]
> Si el repositorio requiere otras dependencias, también deberán estar disponibles en el entorno seleccionado.

### 4 · Selecciona el kernel local

Abre el notebook en VS Code.

Selecciona:

```text
Select Kernel
```

y elige el entorno de Python que preparaste.

Comprueba que el kernel seleccionado corresponde al entorno donde instalaste `ipykernel` e `ipywidgets`.

---

## 🐈 ¡Comienza el reto!

### 5 · Ejecuta el notebook

Una vez preparado el entorno, ya sea local o remoto, ejecuta las celdas del notebook siguiendo las instrucciones que aparecen en él.

Lee cuidadosamente cada pregunta antes de responder.

El cuestionario contiene **10 preguntas de opción múltiple**, cada una con tres opciones de respuesta y solamente una respuesta correcta.

Las preguntas evaluarán los conceptos fundamentales de los dos temas principales de la unidad:

1. Fundamentos y procesamiento básico.
2. Aumento de datos.

---

### 6 · Responde las preguntas

Analiza cada pregunta y selecciona la opción que consideres correcta.

Recuerda que el objetivo no es únicamente memorizar definiciones o funciones, sino comprender:

- Cómo se representan las imágenes digitales y qué información contiene cada píxel.
- Cómo se organizan las dimensiones de las imágenes y los tensores.
- Qué sucede cuando modificamos la resolución o relación de aspecto de una fotografía.
- Cómo funcionan los diferentes métodos de interpolación.
- Qué diferencias existen entre convertir tipos de datos, escalar intensidades y estandarizar.
- Por qué las máscaras categóricas requieren un tratamiento diferente al de las fotografías.
- Qué transformaciones deben aplicarse conjuntamente a imágenes y máscaras.
- Cómo funcionan las probabilidades de aplicación de las transformaciones en Albumentations.

---

### 7 · ¡Encuentra al gato!

Al llegar a la última celda del notebook, comprueba el resultado del reto.

**Si respondiste correctamente todas las preguntas, el gato aparecerá.** 🐈

Si todavía no aparece, revisa tus respuestas y vuelve a intentarlo.

> [!TIP]
> Puedes consultar los materiales y prácticas del Módulo 3 para repasar aquellos conceptos que todavía te generen dudas.

---

## 🤔 Observa e interpreta

Al finalizar el reto, reflexiona:

- ¿Qué preguntas pudiste responder sin consultar tus apuntes?
- ¿Qué conceptos necesitaste repasar?
- ¿Por qué es importante conocer las dimensiones, canales y tipos de datos de una imagen?
- ¿Qué diferencias existen entre los formatos HWC y CHW?
- ¿Qué consecuencias puede tener modificar la relación de aspecto de una fotografía?
- ¿Por qué no todos los métodos de interpolación son adecuados para las máscaras de segmentación?
- ¿Qué diferencia existe entre convertir el tipo de dato de una imagen y modificar su rango de intensidades?
- ¿Por qué las transformaciones geométricas deben aplicarse de manera sincronizada a imágenes y máscaras?
- ¿Por qué las transformaciones fotométricas no deben aplicarse a las máscaras categóricas?
- ¿Qué ventajas ofrece utilizar un pipeline de aumento de datos durante el entrenamiento de un modelo de segmentación?

---

## ✅ Punto de control

Al finalizar este reto habrás:

- Preparado un entorno para ejecutar un notebook interactivo.
- Utilizado un kernel local o remoto.
- Trabajado con módulos pertenecientes a un repositorio de GitHub.
- Recuperado conceptos fundamentales de la representación digital de imágenes.
- Identificado las diferencias entre matrices y tensores de imágenes.
- Reconocido la organización de dimensiones en los formatos HWC, CHW y BCHW.
- Aplicado conocimientos sobre redimensionamiento, relación de aspecto e interpolación.
- Distinguido entre conversión de tipos, escalado y estandarización.
- Identificado las operaciones adecuadas para preservar las etiquetas de las máscaras categóricas.
- Diferenciado las transformaciones geométricas de las fotométricas.
- Reconocido la importancia del aumento de datos sincronizado.
- Evaluado tu comprensión de los conceptos fundamentales del Módulo 3.

---

## 🏁 ¡Reto completado!

Si conseguiste que el gato apareciera, significa que respondiste correctamente las **10 preguntas del cuestionario**.

Has concluido las actividades del **Módulo 3 · Procesamiento de imágenes y máscaras**.

Ahora comprendes cómo se representan y transforman las imágenes digitales, qué precauciones debemos tomar al procesar máscaras de segmentación y cómo utilizar técnicas de aumento de datos para generar variaciones de las muestras de entrenamiento.

Estos conocimientos serán fundamentales para construir un flujo de procesamiento adecuado y preparar las imágenes y máscaras que utilizaremos durante el entrenamiento de nuestro modelo U-Net.

<!-- ¡Nos vemos en el siguiente módulo! -->