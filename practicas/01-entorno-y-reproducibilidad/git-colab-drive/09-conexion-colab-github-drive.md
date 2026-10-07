# 🔗 Conexión entre Google Colab, GitHub y Google Drive

Hasta ahora hemos trabajado por separado con **rutas y directorios**, **Git y GitHub** y **Google Colab**. En esta práctica integraremos estos conceptos para construir un flujo de trabajo en la nube.

Utilizaremos **Google Colab** como entorno de ejecución, clonaremos desde **GitHub** un proyecto que contiene código y datos de ejemplo y conectaremos **Google Drive** para almacenar los resultados que queremos conservar.

Durante la práctica retomaremos lo aprendido sobre **directorios de trabajo y rutas** para navegar por el sistema de archivos de Colab y localizar los recursos del proyecto. También utilizaremos lo aprendido sobre **Git** para obtener un repositorio remoto y trabajar con su contenido desde Colab.

La práctica se realizará utilizando el notebook:

[`connect_colab_github_drive.ipynb`](../../../recursos/codigo/01-entorno-y-reproducibilidad/connect_colab_github_drive.ipynb)

y el repositorio:

`https://github.com/bettypau-open-knowledge/del-dataset-a-unet_colab-github.git`

---

## 🎯 Objetivo

Integrar **Google Colab, GitHub y Google Drive** en un flujo de trabajo que permita obtener código y datos desde un repositorio, ejecutarlos en un entorno remoto y guardar de forma persistente los resultados generados.

---

## 💻 Instrucciones

Abre en Visual Studio Code el notebook:

[`connect_colab_github_drive.ipynb`](../../../recursos/codigo/01-entorno-y-reproducibilidad/connect_colab_github_drive.ipynb)

Conecta el notebook a un runtime de **Google Colab**, como realizaste en la práctica anterior.

Ejecuta las celdas progresivamente y observa qué ocurre en cada sección.

> [!IMPORTANT]
> No ejecutes únicamente **Run All** al comenzar.
>
> En esta práctica interesa observar cómo cambia el sistema de archivos conforme conectamos diferentes recursos y construimos las rutas que utilizaremos.

---

### 1 · Identifica el entorno de ejecución

Comienza ejecutando las primeras celdas del notebook.

Comprueba:

- si el código se está ejecutando en Google Colab;
- qué versión de Python está utilizando el runtime.

Antes de continuar, confirma que el notebook indique que se está ejecutando en **Google Colab**.

---

### 2 · Identifica el directorio de trabajo

Ejecuta la sección:

**¿En qué directorio estoy ejecutando?**

Observa el resultado obtenido mediante `Path.cwd()` y compáralo con el obtenido utilizando el comando `pwd`.

> [!NOTE]
> Aunque el notebook se encuentre abierto en VS Code, el código se está ejecutando en el sistema de archivos del runtime de Google Colab.
>
> Por ello, las rutas que utilizaremos corresponden al **entorno remoto** y no al sistema de archivos de nuestra computadora.

---

### 3 · Explora el sistema de archivos de Colab

Continúa con la sección que permite consultar los archivos y directorios disponibles en el directorio de trabajo.

Observa las diferentes formas utilizadas en el notebook para explorar el sistema de archivos:

- `Path.cwd()`;
- `Path.iterdir()`;
- `.is_dir()`;
- `.name`;
- comandos del sistema Linux;
- navegación entre directorios.

Utiliza las celdas preparadas para entrar en un directorio y regresar posteriormente al directorio padre.

### 🤔 Observa

Relaciona esta parte con lo aprendido anteriormente sobre:

```text
.
```

y:

```text
..
```

Recuerda:

- `.` representa el **directorio actual**;
- `..` representa el **directorio padre**.

---

### 4 · Revisa los recursos del runtime

Ejecuta la sección:

**Revisar el hardware del runtime**

Observa la información disponible sobre:

- CPU;
- número de procesadores lógicos;
- memoria RAM;
- GPU, cuando esté disponible.

El notebook utiliza tanto Python como comandos del sistema Linux para consultar esta información.

> [!NOTE]
> Los recursos pertenecen al **runtime de Google Colab**.
>
> No corresponden necesariamente al hardware de la computadora desde la que estás utilizando VS Code.

---

## 💾 Conecta Google Drive

### 5 · Monta Google Drive

Ejecuta la sección:

**Conectar con Google Drive**

Google solicitará autorización para permitir que el runtime de Colab acceda a tu Drive.

Completa el proceso de autorización.

Después, observa la ruta utilizada por el notebook para acceder a:

```text
MyDrive
```

y explora algunos de los archivos y directorios disponibles.

> [!IMPORTANT]
> Al montar Google Drive estamos incorporando otro espacio de almacenamiento al sistema de archivos que puede consultar el runtime.
>
> A partir de ese momento podremos construir rutas hacia nuestros archivos de Drive utilizando las mismas ideas de `pathlib` que utilizamos anteriormente.

---

## 🐙 Conecta GitHub

### 6 · Identifica el repositorio que utilizarás

En esta práctica trabajaremos con el repositorio:

`https://github.com/bettypau-open-knowledge/del-dataset-a-unet_colab-github.git`

El notebook contiene las instrucciones necesarias para clonarlo dentro del runtime de Google Colab.

Antes de ejecutar la sección correspondiente, observa la ruta definida para el proyecto.

---

### 7 · Clona el repositorio

Ejecuta la sección:

**Clonar un repositorio de GitHub en Colab**

La primera vez que ejecutes esta sección, Git descargará una copia del repositorio dentro del runtime.

Si el repositorio ya se encuentra disponible en la ubicación esperada, el notebook comprobará su existencia y actualizará su contenido.

Relaciona este proceso con los comandos de Git estudiados anteriormente.

> [!NOTE]
> En esta práctica utilizamos la dirección **HTTPS** de un repositorio público para clonarlo en Colab.
>
> La clave SSH configurada anteriormente pertenece a nuestra computadora
> local y no se encuentra automáticamente disponible dentro de un nuevo
> runtime de Colab.

---

### 8 · Explora el proyecto clonado

Una vez obtenido el repositorio, utiliza las siguientes celdas para explorar su estructura.

Identifica:

- los archivos del proyecto;
- sus subdirectorios;
- la carpeta `data/`;
- la carpeta `src/`;
- los archivos que utilizará posteriormente el notebook.

Observa nuevamente cómo las rutas permiten navegar desde la raíz del proyecto hacia sus diferentes recursos.

---

## 🧩 Utiliza el código del repositorio

### 9 · Prepara el acceso a los módulos del proyecto

Continúa con la sección:

**Ejecutar código del repositorio clonado**

Primero observa las rutas disponibles para Python.

Después, ejecuta las celdas que incorporan la raíz del proyecto clonado a las rutas desde las que Python puede localizar módulos.

> [!NOTE]
> Clonar un repositorio hace que sus archivos estén disponibles en el sistema de archivos, pero Python también necesita saber dónde buscar los módulos que queremos importar.

---

### 10 · Construye las rutas del proyecto

El notebook define rutas para acceder a diferentes partes del repositorio.

Observa cómo se construyen progresivamente las rutas hacia:

```text
proyecto
└── data
    ├── images
    └── text
```

Relaciona esta sección con la práctica anterior de `pathlib`.

En lugar de escribir manualmente una ruta completa para cada archivo, partimos de una ruta conocida y construimos las demás utilizando sus componentes.

---

### 11 · Ejecuta código del repositorio

Ejecuta las celdas que importan funciones desde `src/`.

Utiliza esas funciones para:

- leer el archivo de texto incluido en el repositorio;
- cargar la imagen de ejemplo;
- convertir la imagen a escala de grises.

### 🔎 Observa

En este punto estás utilizando conjuntamente:

```text
GitHub
   ↓
repositorio clonado
   ↓
código + datos
   ↓
Google Colab
   ↓
ejecución
```

El código y los datos utilizados proceden del **repositorio de GitHub**, pero las instrucciones se están ejecutando utilizando los recursos del **runtime de Colab**.

---

## 📁 Guarda los resultados en Google Drive

### 12 · Define el directorio de resultados

Continúa con la sección:

**Guardar datos en Google Drive**

El notebook construirá una ruta dentro de `MyDrive` destinada a los ejercicios del taller y, dentro de ella, otra carpeta para los resultados de esta práctica.

Observa nuevamente cómo se utilizan objetos `Path` para construir estas rutas.

---

### 13 · Crea los directorios necesarios

Ejecuta la sección correspondiente a la creación de directorios.

El notebook creará las carpetas necesarias únicamente cuando no existan.

Después, observa la ruta resultante.

---

### 14 · Guarda el resultado

Finalmente, ejecuta la celda que guarda en Google Drive la imagen convertida a escala de grises.

Comprueba desde tu Google Drive que se haya creado el archivo:

```text
Ejercicios_taller_del_dataset_a_unet/
└── Resultados_practica_colab_github_drive/
    └── imagen_grises.png
```

Abre la imagen y verifica el resultado.

---

## 🔄 ¿Qué ocurrió durante la práctica?

El flujo completo que acabas de realizar puede representarse como:

```text
                    GitHub
                       │
                       │ git clone
                       ▼
              ┌─────────────────┐
              │  Google Colab   │
              │                 │
              │ código + datos  │
              │       ↓         │
              │   ejecución     │
              │       ↓         │
              │   resultado     │
              └────────┬────────┘
                       │
                       │ guardar
                       ▼
                 Google Drive
                  persistente
```

Cada herramienta cumple una función diferente:

| Herramienta | Función en esta práctica |
|---|---|
| **VS Code** | Interfaz desde la que trabajamos con el notebook. |
| **GitHub** | Aloja el repositorio con el código y los datos de ejemplo. |
| **Git** | Permite obtener y actualizar el repositorio dentro del runtime. |
| **Google Colab** | Proporciona el entorno remoto donde se ejecuta el código. |
| **Google Drive** | Almacena de forma persistente los resultados que queremos conservar. |
| **`pathlib`** | Permite construir y navegar las rutas entre los diferentes archivos y directorios. |

> [!IMPORTANT]
> El almacenamiento del runtime de Colab es **temporal**.
>
> Si la sesión termina, los archivos almacenados únicamente dentro del runtime pueden desaparecer. Por ello, los resultados que queremos conservar se guardan en **Google Drive**.

---

## 🤔 Observa e interpreta

A partir de lo realizado durante la práctica, reflexiona:

- ¿Cuál fue el directorio de trabajo inicial del runtime?
- ¿Qué diferencia existe entre el sistema de archivos de tu computadora y el sistema de archivos de Colab?
- ¿Qué ocurrió con el sistema de archivos después de montar Google Drive?
- ¿En qué ubicación se clonó el repositorio de GitHub?
- ¿Por qué utilizamos rutas para acceder a `data/`, `src/` y sus archivos?
- ¿De dónde proviene el código que ejecutamos?
- ¿Dónde se ejecuta ese código?
- ¿Dónde se almacenó finalmente la imagen procesada?
- ¿Qué información desaparecería al terminar el runtime?
- ¿Qué información permanecerá disponible después de finalizar la sesión?

---

## ✅ Punto de control

Al finalizar esta práctica habrás integrado:

- la identificación del directorio de trabajo;
- la navegación por directorios y archivos;
- la construcción de rutas mediante `pathlib`;
- la exploración de un sistema de archivos remoto;
- la conexión de Google Drive con un runtime de Colab;
- el uso de Git para obtener un repositorio desde GitHub;
- la exploración de la estructura de un proyecto clonado;
- la importación y ejecución de código perteneciente al proyecto;
- el acceso a datos mediante rutas;
- el procesamiento de información en Google Colab;
- el almacenamiento persistente de resultados en Google Drive.

> [!TIP]
> Al trabajar en la nube, pregúntate siempre:
>
> **¿Dónde está mi código? ¿Dónde están mis datos? ¿Dónde se ejecuta el código y dónde se guardarán los resultados?**
>
> Distinguir estas cuatro cosas ayuda a construir flujos de trabajo más claros y reproducibles.

---

[← Volver a Git, Github, Google Colab y Google Drive](../../../modulos/01-entorno-y-reproducibilidad/01-03-git-colab-drive.md)