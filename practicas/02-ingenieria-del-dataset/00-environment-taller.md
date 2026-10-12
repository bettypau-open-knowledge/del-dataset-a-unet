# 🐍 Configuración del entorno local del taller

A partir de esta unidad utilizaremos un entorno de Python con las bibliotecas necesarias para trabajar con datasets, procesar imágenes y desarrollar modelos de segmentación mediante Deep Learning.

Para facilitar la configuración del entorno, se proporciona el archivo [`environment_taller.yml`](../../recursos/codigo/02-ingenieria-del-dataset/environment_taller.yml), que contiene las dependencias generales que utilizaremos durante el resto del taller.

Además, instalaremos **PyTorch**, **TorchVision** y **MONAI**, bibliotecas que emplearemos posteriormente para construir y entrenar modelos de segmentación.

> [!NOTE]
> Esta configuración es necesaria únicamente si deseas ejecutar las prácticas **localmente**.
>
> Si utilizas Google Colab, trabajarás con el entorno remoto proporcionado por la plataforma y seguirás las instrucciones de instalación correspondientes a cada notebook.

---

## 🎯 Objetivo

Crear y configurar un entorno de Conda para las siguientes unidades del taller, instalar las bibliotecas necesarias para trabajar con Deep Learning y comprobar que se encuentran disponibles en el entorno seleccionado.

---

## 💻 Instrucciones

Para realizar esta actividad necesitarás:

- Miniconda o Anaconda instalado y configurado.
- Visual Studio Code.
- Acceso a Internet.
- El archivo `environment_taller.yml`.

**Archivo de configuración:**

[📄 Descargar `environment_taller.yml` →](../../recursos/codigo/02-ingenieria-del-dataset/environment_taller.yml)

---

### 1 · Crea el entorno de Conda

Descarga el archivo `environment_taller.yml` y guárdalo en una carpeta de tu computadora.

Abre una terminal de Conda y navega hasta el directorio donde se encuentra el archivo.

Ejecuta:

```bash
conda env create -f environment_taller.yml
```

Conda utilizará las instrucciones del archivo para crear el entorno e instalar las dependencias especificadas.

> [!NOTE]
> La creación del entorno puede tardar algunos minutos, dependiendo de las bibliotecas que deban instalarse y de la velocidad de conexión.

---

### 2 · Activa el entorno

Una vez finalizada la instalación, activa el entorno utilizando el nombre definido dentro de `environment_taller.yml`:

```bash
conda activate taller-unet
```

Comprueba que el entorno se encuentre activo:

```bash
conda info --envs
```

El entorno activo aparecerá identificado con un asterisco (`*`).

---

### 3 · Instala PyTorch y TorchVision

**PyTorch** es una biblioteca de Deep Learning que utilizaremos para construir, entrenar y evaluar redes neuronales.

**TorchVision** proporciona herramientas y componentes relacionados con visión por computadora.

En esta actividad utilizaremos una instalación de PyTorch orientada a **CPU**, sin requerir una tarjeta gráfica dedicada.

La instrucción de instalación puede variar dependiendo del sistema operativo.

Para obtener el comando correspondiente:

1. Ingresa a la página oficial de PyTorch:

   [**PyTorch · Get Started →**](https://pytorch.org/get-started/locally/)

2. En el configurador de instalación selecciona:

   | Opción | Selección |
   |---|---|
   | PyTorch Build | Stable |
   | Your OS | Windows, Linux o Mac, según corresponda |
   | Package | Pip |
   | Language | Python |
   | Compute Platform | CPU, cuando esté disponible |

3. Copia la instrucción de instalación proporcionada por la página.

4. Ejecútala en la terminal, asegurándote de que el entorno de Conda del taller continúe activo.

Por ejemplo, en macOS la instalación puede realizarse mediante:

```bash
python -m pip install torch torchvision
```

> [!IMPORTANT]
> En Windows y Linux, utiliza la instrucción específica para **CPU** que proporcione la página oficial.
>
> Esta puede incluir una opción `--index-url` para descargar las versiones correspondientes a CPU.
>
> No selecciones una instalación CUDA o ROCm para esta actividad.

---

### 4 · Instala MONAI

**MONAI** (*Medical Open Network for AI*) es un framework basado en PyTorch que proporciona herramientas especializadas para el desarrollo de aplicaciones de Deep Learning, particularmente en procesamiento y análisis de imágenes médicas (puedes consultar su documentación [**aquí →**](https://monai.readthedocs.io/en/stable/)).

Con el entorno del taller activo, ejecuta:

```bash
conda install -c conda-forge monai
```

Conda buscará e instalará MONAI y resolverá las dependencias necesarias.

> [!NOTE]
> Durante la instalación, revisa los cambios propuestos por Conda antes de confirmarlos.
>
> Si Conda propone reemplazar o modificar significativamente la instalación de PyTorch, no confirmes todavía la operación y consulta al instructor.

---

## ✅ Comprueba la instalación

### 5 · Verifica PyTorch y TorchVision

Ejecuta:

```bash
python -c "import torch; print(torch.__version__)"
```

Después:

```bash
python -c "import torchvision; print(torchvision.__version__)"
```

Ambas instrucciones deberán mostrar las versiones instaladas sin producir errores de importación.

---

### 6 · Verifica MONAI

Ejecuta:

```bash
python -c "import monai; print(monai.__version__)"
```

Si la instalación se realizó correctamente, aparecerá la versión de MONAI disponible en el entorno.

> [!NOTE]
> Pueden aparecer advertencias de funciones próximas a quedar obsoletas, pero puedes continuar si no existe ningún mensaje de error.

---

### 7 · Comprueba el dispositivo de ejecución

Finalmente, ejecuta:

```bash
python -c "import torch; print(torch.device('cpu'))"
```

La salida esperada es:

```text
cpu
```

> [!NOTE]
> Esta instrucción construye un objeto que representa el dispositivo CPU.
> No comprueba por sí sola que la instalación de PyTorch sea exclusivamente
> para CPU.

---

> [!IMPORTANT]
> Antes de ejecutar los notebooks de las próximas prácticas, recuerda seleccionar en Visual Studio Code el **kernel correspondiente al entorno del taller**.
>
> De esta forma, las celdas utilizarán las bibliotecas instaladas en el entorno correcto.

---
[← Volver al módulo](../../modulos/02-ingenieria-del-dataset/02-01-exploracion-de-un-dataset.md)