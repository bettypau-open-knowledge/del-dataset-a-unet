# ☁️ Introducción a Google Colab desde VS Code

Hasta ahora hemos ejecutado nuestros Jupyter Notebooks utilizando un entorno de Python instalado en nuestra computadora. Sin embargo, un notebook también puede ejecutarse utilizando recursos de cómputo que se encuentran en la nube.

**Google Colab** proporciona entornos temporales de ejecución en servidores remotos, con acceso a recursos como **CPU, GPU o TPU**.

Mediante la extensión de Google Colab para Visual Studio Code podemos mantener el notebook abierto y editarlo desde **VS Code**, pero utilizar un servidor de **Google Colab como kernel para ejecutar sus celdas**.

En esta práctica utilizarás el notebook [`vscode-colab.ipynb`](../../../recursos/codigo/01-entorno-y-reproducibilidad/vscode-colab.ipynb para establecer una conexión con Google Colab, comprobar dónde se está ejecutando el código y aprender a desconectar el runtime cuando termines de utilizarlo.

---

## 🎯 Objetivo

Conectar un Jupyter Notebook abierto en **Visual Studio Code** con un entorno de ejecución de **Google Colab**, identificar dónde se ejecuta el código y reconocer la diferencia entre trabajar con un kernel local y uno remoto.

---

## 💻 Instrucciones

Para realizar esta práctica necesitarás:

- Visual Studio Code;
- la extensión de **Google Colab** instalada en VS Code;
- una cuenta de Google con acceso a Google Colab;
- el archivo `vscode-colab.ipynb`.

Abre en VS Code el notebook:

[`vscode-colab.ipynb`](../../../recursos/codigo/01-entorno-y-reproducibilidad/vscode-colab.ipynb)

---

## 🔗 ¿Cómo se conecta VS Code con Google Colab?

Cuando trabajamos con un notebook podemos distinguir dos elementos:

```text
┌──────────────────────────┐
│         VS Code          │
│                          │
│   vscode-colab.ipynb     │
│   código + celdas        │
└────────────┬─────────────┘
             │
             │ conexión
             ▼
┌──────────────────────────┐
│      Google Colab        │
│                          │
│   runtime remoto         │
│   Python + CPU/GPU/TPU   │
└──────────────────────────┘
```

**VS Code** funciona como la interfaz desde la que abrimos, editamos y ejecutamos las celdas del notebook.

**Google Colab** proporciona el entorno remoto en el que se ejecutan las instrucciones.

> [!IMPORTANT]
> Abrir el notebook en VS Code no significa que el código necesariamente se
> esté ejecutando en nuestra computadora.
>
> El **kernel seleccionado** determina qué entorno ejecutará el código.

---

### 1 · Selecciona Google Colab como fuente del kernel

Con `vscode-colab.ipynb` abierto, selecciona:

```text
Select Kernel
```

En el menú que aparece, elige:

```text
Select Another Kernel...
```

Después selecciona:

```text
Colab
```

Esto permitirá utilizar un entorno de Google Colab como kernel del notebook.

---

### 2 · Crea un nuevo servidor de Colab

Para crear un nuevo entorno de ejecución selecciona:

```text
+ New Colab Server
```

VS Code solicitará la información necesaria para crear la instancia.

Si es necesario, inicia sesión con tu cuenta de Google y autoriza la conexión con Google Colab.

---

### 3 · Selecciona los recursos de cómputo

Selecciona el tipo de recurso que utilizará la instancia.

Dependiendo de la disponibilidad de Google Colab, pueden aparecer opciones como:

```text
CPU
GPU
TPU
```

Para esta práctica es suficiente utilizar:

```text
CPU
```

> [!NOTE]
> Las opciones disponibles dependen de los recursos y límites asociados a tu cuenta de Google Colab. Los runtimes con aceleradores como GPU o TPU pueden tener límites de disponibilidad y tiempo de uso.

---

### 4 · Configura la instancia

Continúa con las opciones mostradas por la extensión.

Selecciona las características de la instancia y asigna un nombre que permita identificarla, por ejemplo:

```text
practica-colab
```

Después selecciona el kernel de Python.

Espera hasta que el botón que anteriormente mostraba:

```text
Select Kernel
```

muestre la información correspondiente al entorno de Colab seleccionado.

Esto indica que el notebook está conectado al runtime remoto.

---

## 🔎 Comprueba dónde se ejecuta el notebook

### 5 · Ejecuta la celda de comprobación

El notebook contiene la siguiente celda:

```python
import sys

IN_COLAB = "google.colab" in sys.modules

if IN_COLAB:
    print("Ejecutando en Google Colab")
else:
    print("Ejecutando en un entorno local")

print(f"Versión de Python: {sys.version}")
```

Ejecuta la celda.

Si el notebook está conectado correctamente al runtime de Google Colab, deberás obtener:

```text
Ejecutando en Google Colab
```

También aparecerá la versión de Python disponible en el entorno remoto.

### 🤔 Observa

El archivo continúa abierto dentro de **VS Code**, pero Python se está ejecutando en un servidor de **Google Colab**.

Esto permite distinguir entre:

| Elemento | Función |
|---|---|
| **VS Code** | Interfaz desde la que editamos y trabajamos con el notebook. |
| **Notebook `.ipynb`** | Contiene las celdas de código, texto y resultados. |
| **Kernel** | Ejecuta las instrucciones del notebook. |
| **Google Colab** | Proporciona el entorno remoto y sus recursos de cómputo. |

---

## 🔄 Utiliza el runtime en otro notebook

### 6 · Observa los servidores disponibles

Mientras la instancia permanezca activa, puedes abrir otro notebook en VS Code y seleccionar nuevamente:

```text
Select Kernel → Colab
```

La instancia de Colab que ya tienes asignada puede aparecer entre los servidores disponibles.

Esto permite utilizar el mismo runtime remoto con otros notebooks durante la sesión.

> [!IMPORTANT]
> Utilizar el mismo runtime significa utilizar el mismo **entorno de ejecución**.
>
> Los notebooks siguen siendo archivos independientes.

---

## 🔌 Desconecta Google Colab

### 7 · Elimina el servidor cuando termines

Cuando hayas terminado de trabajar, desconecta la instancia de Google Colab para evitar mantener recursos de ejecución activos innecesariamente.

Desde el menú del notebook, selecciona:

```text
Colab
```

Después:

```text
Remove Server
```

y selecciona la instancia que deseas desconectar.

> [!IMPORTANT]
> Acostúmbrate a desconectar los runtimes de Google Colab cuando termines de utilizarlos, especialmente cuando hayas solicitado recursos como GPU o TPU.

---

### 8 · Comprueba las sesiones desde Google Colab

También puedes revisar las sesiones activas desde la interfaz web de Google Colab.

Desde VS Code selecciona:

```text
Colab → Open Colab Web
```

En Google Colab, abre un notebook y consulta:

```text
Runtime → Manage sessions
```

Desde ahí puedes revisar y finalizar las sesiones que continúen activas.

---

## 🤔 Observa e interpreta

A partir de lo realizado durante la práctica, reflexiona:

- ¿Dónde se encuentra abierto el notebook?
- ¿Dónde se ejecuta Python cuando seleccionas un runtime de Google Colab?
- ¿Qué elemento determina dónde se ejecutarán las celdas?
- ¿Qué diferencia existe entre utilizar un kernel local y un kernel de Colab?
- ¿La versión de Python del runtime de Colab tiene que ser necesariamente la
  misma que la de tu entorno local?
- ¿Qué ocurre con la ejecución cuando desconectas el servidor de Colab?
- ¿Por qué es importante finalizar una instancia cuando ya no la utilizamos?

---

## ✅ Punto de control

Al finalizar esta práctica habrás practicado:

- abrir un Jupyter Notebook en Visual Studio Code;
- seleccionar Google Colab como fuente del kernel;
- crear un runtime remoto de Google Colab;
- seleccionar los recursos de cómputo de una instancia;
- ejecutar código de un notebook de VS Code en Google Colab;
- identificar si Python se está ejecutando localmente o en Colab;
- distinguir entre el notebook, el kernel y el entorno de ejecución;
- reutilizar un runtime de Colab durante una sesión;
- desconectar una instancia cuando terminas de utilizarla.

> [!TIP]
> Antes de comenzar a ejecutar un notebook, comprueba siempre **qué kernel está seleccionado**. El mismo archivo `.ipynb` puede ejecutar su código utilizando entornos diferentes.

---

[← Volver a Git, Github, Google Colab y Google Drive](../../../modulos/01-entorno-y-reproducibilidad/01-03-git-colab-drive.md)