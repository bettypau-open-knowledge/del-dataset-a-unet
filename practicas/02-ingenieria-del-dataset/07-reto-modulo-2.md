# 🐈 Reto Unidad 2: ¡Encuentra al gato!

Durante esta unidad aprendiste a explorar la estructura de un dataset de segmentación, identificar la correspondencia entre imágenes y máscaras, construir inventarios estructurados y utilizar archivos de configuración para organizar la información del proyecto.

También realizamos análisis exploratorios para estudiar las dimensiones de las fotografías, la distribución de sus resoluciones y las proporciones de píxeles correspondientes a diferentes regiones de las máscaras de segmentación.

Ahora es momento de poner a prueba lo aprendido.

En este reto deberás responder **10 preguntas de opción múltiple** relacionadas con los conceptos y procedimientos estudiados durante el **Módulo 2 · Ingeniería y auditoría del dataset**.

Pero hay un pequeño detalle: **¡un gato se ha escondido al final del notebook!** 🐈

Para encontrarlo, tendrás que responder correctamente todas las preguntas.

**¿Podrás conseguir que aparezca?**

---

## 🎯 Objetivo

Evaluar e integrar los conocimientos adquiridos durante el Módulo 2 mediante un cuestionario interactivo desarrollado en Jupyter Notebook.

Durante el reto pondrás a prueba tu comprensión de:

- Estructura de un dataset de segmentación supervisada.
- Función de las imágenes y máscaras de segmentación.
- Exploración de directorios mediante `pathlib`.
- Correspondencia entre imágenes y anotaciones.
- Construcción y utilidad de un *manifest*.
- Organización de metadatos y rutas.
- Archivos de configuración del dataset.
- Dimensiones y resolución de imágenes.
- Interpretación de distribuciones e histogramas.
- Proporciones de píxeles de primer plano y fondo.
- Inspección visual y detección de errores en las anotaciones.

---

## 💻 Instrucciones

Para realizar este reto necesitarás:

- Visual Studio Code.
- El repositorio de GitHub del Reto 2, que incluye el notebook y los módulos necesarios para ejecutarlo.
- Un entorno de ejecución de Python, que puede ser **local o de Google Colab**.

**Repositorio de GitHub:**

[🐙 Consultar el repositorio del Reto 2](https://github.com/bettypau-open-knowledge/del-dataset-a-unet_reto-2/)

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
git clone https://github.com/bettypau-open-knowledge/del-dataset-a-unet_reto-2.git
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
del-dataset-a-unet_reto-2/
├── src/
│   └── ...
├── notebooks/
│   └── encuentra_al_gato_2.ipynb
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

## 🤔 Observa e interpreta

Al finalizar el reto, reflexiona:

- ¿Qué preguntas pudiste responder sin consultar tus apuntes?
- ¿Qué conceptos necesitaste repasar?
- ¿Por qué es importante verificar la correspondencia entre imágenes y máscaras?
- ¿Qué ventajas ofrece utilizar un manifest en lugar de consultar directamente los archivos del dataset?
- ¿Cómo contribuye un archivo de configuración a la organización del proyecto?
- ¿Qué diferencias existen entre las dimensiones de una imagen y el número total de píxeles que contiene?
- ¿Qué información podemos obtener al estudiar la distribución de resoluciones de un dataset?
- ¿Por qué es importante analizar las proporciones de píxeles correspondientes al objeto y al fondo?
- ¿Qué tipos de errores pueden pasar inadvertidos durante una validación automática?
- ¿Cómo contribuyen el inventario y el análisis exploratorio a preparar un dataset para entrenar un modelo de segmentación?

---

## ✅ Punto de control

Al finalizar este reto habrás:

- Preparado un entorno para ejecutar un notebook interactivo.
- Utilizado un kernel local o remoto.
- Trabajado con módulos pertenecientes a un repositorio de GitHub.
- Recuperado conceptos fundamentales sobre datasets de segmentación supervisada.
- Identificado la función de las máscaras y su correspondencia con las fotografías.
- Aplicado conocimientos sobre exploración de archivos mediante `pathlib`.
- Reconocido la utilidad de un manifest y de un archivo de configuración.
- Interpretado información relacionada con dimensiones, resoluciones y cantidades de píxeles.
- Distinguido entre cantidades absolutas y proporciones de píxeles.
- Reconocido la importancia de la inspección visual para identificar errores en las anotaciones.
- Evaluado tu comprensión de los conceptos fundamentales del Módulo 2.

---

## 🏁 ¡Reto completado!

Si conseguiste que el gato apareciera, significa que respondiste correctamente las **10 preguntas del cuestionario**.

Has concluido las actividades del **Módulo 2 · Ingeniería y auditoría del dataset**.

Ahora cuentas con las herramientas necesarias para explorar, organizar y caracterizar un conjunto de imágenes y sus anotaciones, así como para identificar aspectos importantes de su calidad y composición.

Estos conocimientos serán fundamentales para preparar los datos que utilizaremos en las siguientes etapas de nuestro proyecto de segmentación de imágenes.

<!-- ¡Nos vemos en el siguiente módulo! -->