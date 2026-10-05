# 📓 Introducción a Notebooks en VS Code

Los **Jupyter Notebooks** permiten combinar celdas de código, texto y resultados dentro de un mismo documento. A diferencia de un programa de Python que se ejecuta de principio a fin, en un notebook es posible ejecutar las celdas individualmente y en diferente orden.

En esta práctica utilizarás el archivo
[`notebook_vscode.ipynb`](../../../recursos/codigo/01-entorno-y-reproducibilidad/notebook_vscode.ipynb) para familiarizarte con la ejecución de notebooks en **Visual Studio Code**, explorar el estado del kernel y observar qué ocurre cuando las celdas no se ejecutan en el orden en que aparecen.

---

## 🎯 Objetivo

Familiarizarse con la ejecución de Jupyter Notebooks en Visual Studio Code, identificar el entorno utilizado como kernel y reconocer cómo el **orden de ejecución de las celdas** puede modificar el estado y los resultados de un notebook.

---

## 💻 Instrucciones

### 1 · Prepara el entorno

Antes de ejecutar el notebook, asegúrate de utilizar un **entorno de Python que tenga instalado el paquete `ipykernel`**.

Activa el entorno que utilizarás:

```bash
conda activate nombre-del-entorno
```

Si `ipykernel` no está instalado, puedes instalarlo desde Conda con:

```bash
conda install ipykernel
```

Una vez instalado, verifica desde la terminal que `ipykernel` puede importarse correctamente:

```bash
python -c "import ipykernel; print(ipykernel.__version__)"
```

Si la instalación es correcta, la terminal mostrará la versión de `ipykernel` disponible en el entorno.

> [!IMPORTANT]
> Ejecuta estos comandos **después de activar el entorno que utilizarás con el notebook**. De esta forma, `ipykernel` se instalará y verificará en ese entorno y no accidentalmente en otro.

---

### 2 · Abre el notebook y selecciona el kernel

Abre el archivo:

[`notebook_vscode.ipynb`](./notebook_vscode.ipynb)

Antes de ejecutar cualquier celda, utiliza **Select Kernel** para seleccionar el entorno de Python que preparaste en el paso anterior.

> [!NOTE]
> El **kernel** es el proceso que ejecuta el código del notebook y mantiene su estado durante la sesión. Por ello, es importante comprobar qué entorno de Python está utilizando antes de comenzar a ejecutar las celdas.

---

### 3 · Explora los controles del notebook

Utiliza el contenido incluido en el notebook para experimentar con los siguientes controles de VS Code:

| Botón | Experimenta con... |
|---|---|
| **▶ Run All** | Ejecutar todas las celdas del notebook en orden. |
| **↻ Restart** | Reiniciar el kernel y observar qué ocurre con las variables que estaban en memoria. |
| **Clear All Outputs** | Eliminar las salidas visibles y comprobar si las variables continúan disponibles. |
| **Jupyter Variables** | Observar qué variables existen en la memoria del kernel conforme ejecutas diferentes celdas. |
| **Select Kernel** | Identificar y seleccionar el entorno de Python que utilizará el notebook. |

> [!IMPORTANT]
> **Reiniciar el kernel** y **borrar las salidas** son acciones diferentes.
>
> - **Restart** → limpia la **memoria** del kernel.
> - **Clear All Outputs** → limpia las **salidas visibles** del notebook.

---

### 4 · Experimenta con el orden de ejecución

El archivo `notebook_vscode.ipynb` contiene un pequeño ejemplo preparado para experimentar con el **orden de ejecución de las celdas**.

Prueba diferentes secuencias:

1. Reinicia el kernel.
2. Ejecuta las celdas en el orden en que aparecen.
3. Observa los resultados.
4. Reinicia nuevamente el kernel.
5. Ejecuta las mismas celdas en un **orden diferente**.
6. Compara los resultados.

Mientras realizas las pruebas, observa también **Jupyter Variables** para identificar cómo cambia el estado del kernel.

---

## 🤔 Observa e interpreta

Durante las pruebas, reflexiona sobre las siguientes preguntas:

- ¿El orden en el que aparecen las celdas determina necesariamente el orden
  en que fueron ejecutadas?
- ¿Qué ocurre si una celda utiliza una variable que todavía no ha sido creada en el kernel?
- ¿Qué ocurre con las variables después de reiniciar el kernel?
- ¿Borrar las salidas elimina también las variables almacenadas en memoria?
- ¿Por qué un notebook puede producir resultados diferentes dependiendo del orden en que se ejecutaron sus celdas?

---

## ✅ Punto de control

Al finalizar esta práctica habrás experimentado con:

- preparar un entorno para ejecutar Jupyter Notebooks;
- verificar la instalación de `ipykernel`;
- seleccionar el entorno que utilizará el notebook como kernel;
- ejecutar una o todas las celdas;
- reiniciar el kernel;
- limpiar las salidas del notebook;
- consultar las variables disponibles en memoria;
- modificar el orden de ejecución de las celdas;
- reconocer la diferencia entre el **orden visual de las celdas** y el **estado de ejecución del notebook**.

> [!TIP]
> Cuando quieras comprobar que un notebook puede ejecutarse de forma reproducible, reinicia el kernel y ejecuta nuevamente todas las celdas desde el principio.

---

[← Volver a Directorio de trabajo y tipos de rutas](../../../modulos/01-entorno-y-reproducibilidad/01-02-directorio-trabajo-y-tipos-rutas.md)