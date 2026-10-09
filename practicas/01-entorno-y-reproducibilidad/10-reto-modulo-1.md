# 🐈 Reto Unidad 1: ¡Encuentra al gato!

Durante esta unidad aprendiste a preparar entornos de desarrollo, trabajar con Jupyter Notebooks, navegar entre archivos y directorios, utilizar Git y GitHub, y ejecutar código en Google Colab.

Ahora es momento de poner a prueba lo aprendido.

En este reto deberás responder **10 preguntas de opción múltiple** relacionadas con los conceptos y herramientas estudiados durante el **Módulo 1 · Entorno de desarrollo y reproducibilidad**.

Pero hay un pequeño detalle: **¡un gato se ha escondido al final del notebook!** 🐈

Para encontrarlo, tendrás que responder correctamente todas las preguntas.

**¿Podrás conseguir que aparezca?**

---

## 🎯 Objetivo

Evaluar e integrar los conocimientos adquiridos durante el Módulo 1 mediante un cuestionario interactivo desarrollado en Jupyter Notebook.

Durante el reto pondrás a prueba tu comprensión de:

- Entornos de Conda y dependencias.
- Archivos `environment.yml`.
- Jupyter Notebooks y kernels.
- Directorios de trabajo y rutas.
- Manejo de archivos con `pathlib`.
- Control de versiones mediante Git.
- Repositorios remotos en GitHub.
- Uso de `.gitignore`.
- Autenticación mediante SSH.
- Google Colab y Google Drive.

---

## 💻 Instrucciones

Para realizar este reto necesitarás:

- Visual Studio Code.
- El notebook del reto.
- El repositorio de GitHub que contiene los módulos necesarios para ejecutarlo.
- Un entorno de ejecución de Python, que puede ser **local o de Google Colab**.

**Notebook del reto:**

[📓 Abrir el notebook «Encuentra al gato»](../../recursos/codigo/01-entorno-y-reproducibilidad/encuentra-al-gato-1.ipynb)

**Repositorio de GitHub:**

[🐙 Consultar el repositorio del reto](https://github.com/bettypau-open-knowledge/del-dataset-a-unet_reto-1.git)

Puedes realizar la actividad utilizando cualquiera de las dos modalidades descritas a continuación.

---

## ☁️ Opción A · Ejecutar el reto en Google Colab

### 1 · Abre el notebook

Abre el notebook del reto en **Visual Studio Code**.

Conéctalo a un runtime de **Google Colab**, utilizando el procedimiento aprendido en las prácticas anteriores.

Comprueba que el kernel seleccionado corresponde al runtime de Colab.

### 2 · Prepara el repositorio

Ejecuta las celdas de preparación del notebook siguiendo sus indicaciones.

Estas instrucciones permiten acceder a los archivos y módulos del repositorio que necesita el cuestionario para funcionar.

> [!NOTE]
> Recuerda que, aunque el notebook se encuentre abierto en VS Code, las instrucciones se ejecutarán en el runtime remoto de Google Colab.

---

## 💻 Opción B · Ejecutar el reto localmente

También puedes realizar este reto utilizando un entorno de Python instalado en tu computadora, sin necesidad de conectarte a Google Colab.

### 1 · Descarga el repositorio

Descarga o clona el repositorio de GitHub proporcionado para esta actividad.

Si decides utilizar Git, puedes ejecutar:

```bash
git clone URL_DEL_REPOSITORIO
```

Abre la carpeta del repositorio en **Visual Studio Code**.

### 2 · Coloca el notebook en la raíz del proyecto

Descarga el notebook del reto y colócalo directamente en la **raíz del repositorio**, al mismo nivel que los demás archivos y directorios principales.

La estructura deberá ser similar a:

```text
repositorio-del-reto/
├── src/
│   └── ...
├── ...
└── encuentra_al_gato.ipynb
```

> [!IMPORTANT]
> El notebook debe encontrarse en la **raíz del proyecto** para que las rutas utilizadas durante su ejecución permitan localizar correctamente los módulos y recursos del repositorio.

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

---

### 6 · Responde las preguntas

Analiza cada pregunta y selecciona la opción que consideres correcta.

Recuerda que el objetivo no es únicamente memorizar comandos, sino comprender:

- Qué problema resuelve cada herramienta.
- Cómo se relacionan los diferentes componentes de un proyecto.
- Cómo se construyen y utilizan las rutas.
- Dónde se encuentran los archivos y dónde se ejecuta el código.
- Cómo organizar y reproducir un flujo de trabajo.

---

### 7 · ¡Encuentra al gato!

Al llegar a la última celda del notebook, comprueba el resultado del reto.

**Si respondiste correctamente todas las preguntas, el gato aparecerá.** 🐈

Si todavía no aparece, revisa tus respuestas y vuelve a intentarlo.

> [!TIP]
> Puedes consultar los materiales y prácticas del Módulo 1 para repasar aquellos conceptos que todavía te generen dudas.

---

## 🤔 Observa e interpreta

Al finalizar el reto, reflexiona:

- ¿Qué preguntas pudiste responder sin consultar tus apuntes?
- ¿Qué conceptos necesitaste repasar?
- ¿Qué diferencias existen entre ejecutar el notebook localmente y utilizar
  Google Colab?
- ¿Por qué es importante seleccionar correctamente el kernel?
- ¿Qué papel desempeñan las rutas para localizar los módulos del proyecto?
- ¿Por qué es importante conservar una estructura de directorios organizada?
- ¿Qué herramientas de esta unidad consideras más importantes para comenzar
  un proyecto de segmentación de imágenes?

---

## ✅ Punto de control

Al finalizar este reto habrás:

- preparado un entorno para ejecutar un notebook interactivo;
- utilizado un kernel local o remoto;
- trabajado con módulos pertenecientes a un repositorio de GitHub;
- aplicado conocimientos sobre entornos y dependencias;
- recuperado conceptos de directorios de trabajo y rutas;
- identificado las funciones de Git, GitHub y `.gitignore`;
- distinguido entre ejecución local, ejecución remota y almacenamiento
  persistente;
- evaluado tu comprensión de los conceptos fundamentales del Módulo 1.

---

## 🏁 ¡Reto completado!

Si conseguiste que el gato apareciera, significa que respondiste correctamente las **10 preguntas del cuestionario**.

Has concluido las actividades del
**Módulo 1 · Entorno de desarrollo y reproducibilidad**.

Ahora cuentas con las herramientas fundamentales para comenzar a trabajar con proyectos de procesamiento y segmentación de imágenes.

<!--**¡Nos vemos en el siguiente módulo!**-->