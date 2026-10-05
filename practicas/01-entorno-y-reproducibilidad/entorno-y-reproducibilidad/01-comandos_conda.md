# 🧰 Comandos esenciales de Conda

En esta sección encontrarás una referencia rápida de los comandos de **Conda**
que se utilizan con mayor frecuencia al manejar entornos.

Puedes consultar esta guía mientras realizas los ejercicios.

---

## 📌 Cheat sheet

La siguiente infografía resume los comandos esenciales para crear, consultar,
activar, desactivar y administrar entornos con Conda.

![Cheat sheet de comandos esenciales de Conda](../../../assets/imagenes/modulo_01/1_conda_cheat_sheet.png)

> [!TIP]
> No es necesario memorizar todos los comandos. Utiliza esta guía como
> referencia mientras trabajas con tus entornos.

---

# 🧪 Ejercicios

Los siguientes ejercicios te permitirán practicar progresivamente los
comandos esenciales de Conda.

## Ejercicio 1 · Verificar Conda

### 🎯 Objetivo

Comprobar que Conda está instalado correctamente y consultar información básica de la instalación.

### 💻 Instrucciones

Consulta la versión instalada de Conda:

```bash
conda --version
```

Ahora consulta información sobre tu instalación:

```bash
conda info
```

**🔎 Interpretando `conda info`**

La salida contiene muchos datos, pero por ahora nos interesa identificar ocho campos principales:
| Campo | ¿Qué nos dice? |
|---|---|
| `active environment` | 🌱 El entorno que se encuentra activo actualmente. |
| `conda version` | 📦 La versión de Conda instalada. |
| `python version` | 🐍 La versión de Python con la que se está ejecutando Conda. |
| `solver` | 🧩 El mecanismo que Conda utiliza para encontrar una combinación compatible de paquetes y versiones. |
| `base environment` | 🏠 La ubicación del entorno `base` y, normalmente, de la instalación principal de Conda. |
| `channel URLs` | 🌐 Los canales que Conda consulta para buscar y descargar paquetes. |
| `envs directories` | 📁 Los directorios en los que Conda puede crear y localizar entornos. |
| `platform` | 💻 Identifica el sistema operativo y la arquitectura para los que Conda busca paquetes compatibles. |

Consulta los entornos disponibles:

```bash
conda env list
```


## Ejercicio 2 · Crear un entorno

### 🎯 Objetivo

Crear un nuevo entorno de Conda con una versión específica de Python.

### 💻 Instrucciones

Consulta los entornos disponibles:

```bash
conda env list
```

Crea un entorno llamado `mi-entorno` con una version de python 3.11:

```bash
conda create --name mi-entorno python=3.11
```

Cuando Conda solicite confirmación, escribe:

```text
y
```

### 🔎 Comprueba

Consulta de nuevo los entornos disponibles:

```bash
conda env list
```

Localiza `mi-entorno` en la lista.

---

## Ejercicio 3 · Activar el entorno

### 🎯 Objetivo

Activar el entorno que acabas de crear.

### 💻 Instrucciones

Verifica que no hay un entorno activo en la terminal:

```bash
conda info
```

Activa el entorno `mi-entorno`:

```bash
conda activate mi-entorno
```

### 🔎 Comprueba

Observa el inicio de la línea de comandos.

Deberías encontrar el nombre del entorno activo:

```text
(mi-entorno)
```

También puedes comprobarlo con:

```bash
conda info
```

## Ejercicio 4 · Consultar los paquetes instalados

### 🎯 Objetivo

Explorar los paquetes disponibles dentro del entorno.

### 💻 Instrucciones

Con `mi-entorno` activo, ejecuta:

```bash
conda list
```
**🔎 Interpretando `conda list`**

| Campo | ¿Qué nos dice? |
|---|---|
| `Name` | 📦 Indica el nombre del paquete disponible en el entorno. |
| `Version` | 🔢 Muestra la versión instalada del paquete. |
| `Build` | 🧱 Identifica la variante específica del paquete que Conda instaló. Dos paquetes pueden tener la misma versión, pero diferentes *builds*. |
| `Channel` | 🌐 Indica el canal de Conda desde el cual se obtuvo, por ejemplo `conda-forge`. |


## Ejercicio 5 · Instalar paquetes

### 🎯 Objetivo

Buscar si un paquete existe en los canales de conda, si es así, instalarlo.

### 💻 Instrucciones

Busca el paquete numpy en los canales de conda:

```bash
conda search numpy
```

¿Encuentras varias versiones? No te preocupes, podemos dejar que conda resuelva la versión:

```bash
conda install numpy
```

También puedes elegir la opción que necesitas agregandola al comando:

```bash
conda install numpy=2.4.6
```

Verifica que numpy fue instalado utilizando la lista de los paquetes del entorno:

```bash
conda list
```

Elimina numpy:

```bash
conda remove -y numpy
```

Verifica que numpy haya desaparecido en la lista de paquetes instalados:

```bash
conda list
```

## Ejercicio 6 · Desactivar el entorno

### 🎯 Objetivo

Salir del entorno activo.

### 💻 Instrucciones

```bash
conda deactivate
```

### 🔎 Comprueba

El indicador:

```text
(mi-entorno)
```

deberá desaparecer de la línea de comandos.

---

## Ejercicio 7 · Eliminar el entorno

### 🎯 Objetivo

Eliminar un entorno que ya no necesitamos.

> [!IMPORTANT]
> Antes de eliminar un entorno, asegúrate de que no se encuentre activo.

Comprueba tus entornos:

```bash
conda env list
```

Elimina `mi-entorno`:

```bash
conda env remove --name mi-entorno
```

Finalmente, vuelve a consultar los entornos disponibles:

```bash
conda env list
```

### 🔎 Comprueba

`mi-entorno` ya no deberá aparecer en la lista.

---

## ✅ Punto de control

Al finalizar estos ejercicios habrás practicado:

- consultar la instalación de Conda;
- listar los entornos disponibles;
- crear un entorno;
- activar y desactivar un entorno;
- consultar sus paquetes;
- instalar y remover paquetes;
- eliminar un entorno.

> [!TIP]
> Si no recuerdas algún comando, vuelve al **cheat sheet** al inicio de esta página.

---

[← Volver a Entorno y reproducibilidad](../../../modulos/01-entorno-y-reproducibilidad/01-01-entorno-y-reproducibilidad.md)