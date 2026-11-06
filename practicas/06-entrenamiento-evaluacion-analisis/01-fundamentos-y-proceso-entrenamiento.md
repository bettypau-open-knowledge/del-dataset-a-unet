# 🧠 Entrenamiento de una Mini U-Net con el Oxford-IIIT Pet Dataset

En las prácticas anteriores aprendimos a organizar el Oxford-IIIT Pet Dataset, construir un inventario de sus fotografías y máscaras, generar particiones experimentales reproducibles e implementar un pipeline de datos mediante PyTorch.

Posteriormente, estudiamos los fundamentos de las redes neuronales convolucionales y la arquitectura U-Net, comprendiendo cómo sus componentes permiten extraer características visuales y producir predicciones de segmentación.

Ahora que contamos con los datos preparados y conocemos la arquitectura, debemos resolver una nueva pregunta:

**¿Cómo podemos entrenar una U-Net para que aprenda a identificar las regiones correspondientes a los animales en nuestras fotografías?**

En esta práctica entrenaremos una **Mini U-Net para segmentación binaria**, utilizando el proyecto del Oxford-IIIT Pet Dataset que hemos desarrollado a lo largo del taller.

Para ello, incorporaremos tres módulos de Python que nos permitirán separar las responsabilidades del proyecto:

- `dataset.py`: recuperación y preparación de fotografías y máscaras.
- `transforms.py`: definición de los pipelines de transformación.
- `models.py`: implementación de la arquitectura Mini U-Net.

Después utilizaremos el notebook `entrenamiento_mini_u-net.ipynb` para integrar estos componentes, configurar el entrenamiento y ejecutar las operaciones que permiten actualizar los parámetros de la red neuronal.

También aprenderemos a guardar y recuperar **checkpoints**, calcular la pérdida de validación y visualizar las máscaras predichas por el modelo.

---

## 🎯 Objetivo

Implementar y ejecutar el proceso de entrenamiento de una Mini U-Net para segmentación binaria de imágenes del Oxford-IIIT Pet Dataset, utilizando PyTorch y los conjuntos experimentales preparados anteriormente.

Al finalizar, serás capaz de:

- Organizar el código de un proyecto de Deep Learning mediante módulos de Python.
- Importar clases y funciones desde el directorio `src/`.
- Reutilizar los archivos de configuración y particiones experimentales existentes.
- Preparar fotografías y máscaras para segmentación binaria.
- Construir objetos `Dataset` y `DataLoader` utilizando módulos externos.
- Instanciar una arquitectura Mini U-Net.
- Seleccionar un dispositivo de entrenamiento compatible con PyTorch.
- Configurar una función de pérdida y un optimizador.
- Ejecutar el forward pass y comprobar las dimensiones de salida.
- Implementar un ciclo de entrenamiento por épocas y batches.
- Calcular gradientes mediante backpropagation.
- Actualizar los parámetros del modelo mediante un optimizador.
- Guardar y recuperar checkpoints.
- Calcular la pérdida sobre el conjunto de validación.
- Generar probabilidades y máscaras binarias a partir de los logits.
- Visualizar y comparar las predicciones con las máscaras reales.

---

## 📁 Organización del proyecto

Continuaremos utilizando el proyecto desarrollado en la práctica **Construcción del pipeline de datos del Oxford-IIIT Pet Dataset**.

No es necesario descargar nuevamente el dataset, crear otro repositorio ni generar nuevas particiones experimentales.

En esta ocasión incorporaremos una carpeta llamada `src/` en la raíz del proyecto y un nuevo notebook dentro de `notebooks/`.

La estructura relevante será:

```text
proyecto/
├── config/
│   └── dataset.json
├── data/
│   ├── raw/
│   │   └── ...
│   ├── manifests/
│   │   └── manifest.csv
│   └── splits/
│       ├── split_70_15_15.csv
│       └── split_80_10_10.csv
├── notebooks/
│   ├── ...
│   ├── pipeline_de_datos_oxford.ipynb
│   └── entrenamiento_mini_u-net.ipynb
├── src/
│   ├── dataset.py
│   ├── models.py
│   └── transforms.py
└── outputs/
    └── checkpoints/
```

El directorio `outputs/checkpoints/` se creará automáticamente durante la ejecución del notebook.

| Archivo | Función |
|---|---|
| `config/dataset.json` | Contiene las rutas y la configuración del proyecto. |
| `data/manifests/manifest.csv` | Registra las fotografías y máscaras del dataset. |
| `data/splits/` | Almacena las particiones experimentales previamente generadas. |
| `src/dataset.py` | Implementa la clase `PetSegmentationDataset`. |
| `src/models.py` | Define los bloques convolucionales y la arquitectura `MiniUNet`. |
| `src/transforms.py` | Contiene los pipelines de entrenamiento y evaluación. |
| `notebooks/entrenamiento_mini_u-net.ipynb` | Integra los componentes y ejecuta el entrenamiento. |
| `outputs/checkpoints/` | Almacena los estados guardados del entrenamiento. |

> [!IMPORTANT]
> La carpeta `src/` debe colocarse en la **raíz del proyecto**, al mismo nivel que `data/`, `config/` y `notebooks/`.
>
> No debes colocar los archivos `.py` dentro de `notebooks/`, porque el notebook está preparado para importarlos desde `src/`.

---

## 💻 Requisitos

Para realizar esta práctica necesitarás Visual Studio Code, un entorno de Python compatible con Jupyter Notebooks y las bibliotecas utilizadas durante el taller.

| Biblioteca | Función |
|---|---|
| `torch` | Definición, entrenamiento y evaluación de Mini U-Net. |
| `numpy` | Manipulación de arreglos y máscaras. |
| `pandas` | Recuperación de particiones experimentales. |
| `opencv-python` | Lectura y conversión de fotografías y máscaras. |
| `albumentations` (2.x) | Transformaciones geométricas y fotométricas. |
| `matplotlib` | Visualización de predicciones. |
| `pathlib` | Construcción de rutas del proyecto. |
| `json` | Lectura y actualización de la configuración. |

`pathlib` y `json` forman parte de la biblioteca estándar de Python.

> [!NOTE]
> Utilizaremos el entorno de Python configurado durante las prácticas anteriores.
>
> No es necesario crear un entorno nuevo si las dependencias ya se encuentran instaladas.

---

## 💻 Preparación de la práctica

### 1 · Recupera el proyecto anterior

Abre en Visual Studio Code el proyecto del Oxford-IIIT Pet Dataset.

Comprueba que estén disponibles:

```text
config/dataset.json
data/manifests/manifest.csv
data/splits/split_70_15_15.csv
data/splits/split_80_10_10.csv
```

Estos archivos permitirán recuperar los datos y las particiones experimentales sin repetir las etapas de preparación.

### 2 · Incorpora la carpeta `src/`

En la raíz del proyecto, incorpora la carpeta llamada:

```text
src/
```

Puedes encontrar la carpeta [aquí →](../../recursos/codigo/06-entrenamiento-evaluacion-analisis/06-01-fundamentos-y-proceso-entrenamiento/)

Dentro encontrarás los tres archivos proporcionados:

```text
src/
├── __init__.py
├── dataset.py
├── models.py
└── transforms.py
```

No modifiques sus nombres.

### 3 · Incorpora el notebook

Descarga el notebook `entrenamiento_mini_u-net.ipynb` [aquí →](../../recursos/codigo/06-entrenamiento-evaluacion-analisis/06-01-fundamentos-y-proceso-entrenamiento/notebooks/entrenamiento_mini_u-net.ipynb)

Coloca el archivo proporcionado dentro de `notebooks/`.

Abre el notebook y selecciona el kernel correspondiente al entorno del taller.

### 4 · Verifica el directorio de trabajo

El notebook utiliza:

```python
PROJECT_ROOT = Path("..").resolve()
```

Esta instrucción considera que el directorio de trabajo de Python es `notebooks/`.

Comprueba que `PROJECT_ROOT` corresponda a la raíz del proyecto antes de ejecutar las siguientes celdas.

---

## 🧪 Actividades de la práctica

### 1 · Incorporar los módulos del proyecto

Comenzaremos organizando el código en módulos independientes.

Hasta ahora hemos trabajado principalmente con notebooks, pero a medida que un proyecto crece resulta conveniente separar las definiciones reutilizables de las actividades de experimentación.

En esta práctica utilizaremos tres módulos.

**`dataset.py`**

Contiene la clase `PetSegmentationDataset`, encargada de recuperar fotografías y máscaras, aplicar transformaciones y convertir los datos a tensores.

**`transforms.py`**

Define las funciones:

```python
get_train_transform(tamano)
get_val_transform(tamano)
```

Estas funciones construyen los pipelines de transformación para entrenamiento y evaluación.

**`models.py`**

Contiene las clases:

```python
DoubleConv
MiniUNet
```

La primera implementa un bloque de dos convoluciones y la segunda define la arquitectura de segmentación.

**Considera:** ¿qué ventajas ofrece separar estas definiciones del notebook que ejecuta el entrenamiento?

---

### 2 · Configurar las rutas de importación

El notebook comienza incorporando la raíz del proyecto a las rutas de búsqueda de Python.

```python
import sys
from pathlib import Path

PROJECT_ROOT = Path("..").resolve()

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
```

Esto permite importar los módulos ubicados dentro de `src/`.

Después utilizaremos:

```python
from src.models import MiniUNet
from src.dataset import PetSegmentationDataset
from src.transforms import (
    get_train_transform,
    get_val_transform
)
```

Observa que estamos importando clases y funciones que se encuentran definidas en archivos externos.

> [!NOTE]
> El notebook no necesita contener nuevamente la implementación completa de Mini U-Net ni de los pipelines de transformación.
>
> Estas definiciones se recuperan directamente desde los módulos de Python.

---

### 3 · Establecer la configuración del entrenamiento

Definiremos cuatro parámetros iniciales:

```python
TAMANO_IMAGEN = 256
BATCH_SIZE = 4
SPLIT_FILE = "split_70_15_15.csv"
NUM_EPOCHS = 5
```

| Parámetro | Valor | Función |
|---|---|---|
| `TAMANO_IMAGEN` | 256 | Dimensión espacial de entrada. |
| `BATCH_SIZE` | 4 | Número máximo de muestras por batch. |
| `SPLIT_FILE` | 70/15/15 | Configuración experimental seleccionada. |
| `NUM_EPOCHS` | 5 | Número de recorridos del conjunto de entrenamiento. |

Utilizaremos esta configuración inicial para observar el funcionamiento del ciclo de entrenamiento.

> [!IMPORTANT]
> Cinco épocas constituyen una configuración didáctica inicial.
>
> No debemos asumir que el modelo habrá alcanzado su mejor desempeño al finalizar este número de épocas.

---

### 4 · Recuperar la configuración y las particiones

Leeremos el archivo `dataset.json` para recuperar las rutas utilizadas por el proyecto.

El notebook utiliza las claves:

```python
config["manifest"]["path"]
config["dataset"]["root"]
config["splits"]["path"]
```

Después, recuperaremos la configuración experimental seleccionada mediante:

```python
splits = pd.read_csv(
    DIRECTORIO_SPLITS / SPLIT_FILE
)
```

Separaremos los registros en:

```python
train_df
val_df
test_df
```

Cada DataFrame contendrá las muestras asignadas al conjunto correspondiente.

> [!IMPORTANT]
> No volveremos a ejecutar `train_test_split()`.
>
> El entrenamiento utilizará las particiones experimentales generadas y guardadas durante las prácticas anteriores.

---

### 5 · Preparar las máscaras para segmentación binaria

En las prácticas anteriores trabajamos con las tres etiquetas originales del Oxford-IIIT Pet Dataset:

| Etiqueta original | Región |
|---|---|
| 1 | Animal |
| 2 | Fondo |
| 3 | Contorno |

En esta práctica utilizaremos una **segmentación binaria**, por lo que distinguiremos únicamente entre animal y no animal.

El módulo `dataset.py` realiza la conversión mediante:

```python
mascara_binaria = (mascara == 1).astype(np.uint8)
```

Obtendremos:

| Etiqueta binaria | Región |
|---|---|
| 1 | Animal |
| 0 | Fondo y contorno |

Esta conversión se realiza antes de aplicar las transformaciones.

Posteriormente, las máscaras se convertirán a tensores `float32` y se añadirá una dimensión de canal.

**Dimensiones esperadas:**

| Elemento | Dimensiones |
|---|---|
| Fotografía | `(3, 256, 256)` |
| Máscara binaria | `(1, 256, 256)` |

> [!IMPORTANT]
> En esta práctica las máscaras tienen un solo canal y contienen valores `0` y `1`.
>
> Esta representación es diferente de la segmentación multiclase que utilizamos anteriormente y es compatible con `BCEWithLogitsLoss`.

---

### 6 · Recuperar los pipelines de transformación

El módulo `transforms.py` define dos funciones.

**`get_train_transform()`**

Aplica:

- Redimensionamiento proporcional mediante `LongestMaxSize`.
- Padding hasta alcanzar `256 × 256`.
- Rotación aleatoria de hasta ±20°.
- Volteo horizontal aleatorio.
- Modificación aleatoria de brillo.
- Modificación aleatoria de contraste.

**`get_val_transform()`**

Aplica únicamente:

- Redimensionamiento proporcional.
- Padding hasta alcanzar `256 × 256`.

El pipeline de entrenamiento incorpora aumento de datos, mientras que el de validación y prueba utiliza un procesamiento determinista.

También observarás que el padding utiliza:

```python
fill_mask=0
```

Esto se debe a que ahora trabajamos con máscaras binarias, donde el valor `0` representa el fondo.

**Considera:** ¿por qué en la práctica anterior utilizábamos `fill_mask=2` y ahora utilizamos `fill_mask=0`?

---

### 7 · Construir los objetos Dataset y DataLoader

Utilizaremos la clase `PetSegmentationDataset` para crear:

```python
train_dataset
val_dataset
test_dataset
```

Después construiremos los DataLoader:

```python
train_loader
val_loader
test_loader
```

La configuración será:

| Parámetro | Train | Validation | Test |
|---|---|---|---|
| `batch_size` | 4 | 4 | 4 |
| `shuffle` | `True` | `False` | `False` |
| `num_workers` | 0 | 0 | 0 |

Comprobaremos cuántas muestras y batches contiene cada conjunto.

Observa que ahora recuperamos las clases y transformaciones desde módulos externos, pero seguimos utilizando los conceptos de `Dataset` y `DataLoader` que estudiamos anteriormente.

---

### 8 · Seleccionar el dispositivo de entrenamiento

Antes de instanciar el modelo, seleccionaremos el dispositivo de ejecución.

El notebook utiliza:

```python
DEVICE = torch.device(
    "cuda" if torch.cuda.is_available()
    else "mps" if torch.backends.mps.is_available()
    else "cpu"
)
```

Esta configuración permite utilizar:

- **CUDA:** cuando existe una GPU NVIDIA compatible.
- **MPS:** cuando está disponible la aceleración mediante Apple Silicon.
- **CPU:** cuando no se dispone de los aceleradores anteriores.

Posteriormente, enviaremos el modelo al dispositivo seleccionado.

> [!NOTE]
> La disponibilidad de un acelerador depende del equipo, la instalación de PyTorch y la compatibilidad del entorno.
>
> El entrenamiento también puede ejecutarse mediante CPU, aunque el tiempo requerido puede ser mayor.

---

### 9 · Instanciar Mini U-Net

Utilizaremos la clase `MiniUNet` definida en `models.py`.

La arquitectura contiene:

- Dos bloques convolucionales en el encoder.
- Operaciones de Max Pooling para reducir la resolución espacial.
- Un bottleneck.
- Dos niveles de decoder.
- Convoluciones transpuestas para recuperar la resolución.
- Skip connections mediante concatenación.
- Una convolución final de `1 × 1`.

La instanciación será:

```python
modelo = MiniUNet(
    in_channels=3,
    num_classes=1
).to(DEVICE)
```

El modelo recibirá fotografías RGB y producirá un canal de salida para segmentación binaria.

Su estructura general será:

```text
Imagen RGB
    ↓
Encoder
    ↓
Bottleneck
    ↓
Decoder + Skip Connections
    ↓
Convolución 1 × 1
    ↓
Logits de segmentación
```

> [!IMPORTANT]
> La salida de Mini U-Net contiene **logits**, no probabilidades.
>
> No aplicaremos Sigmoid dentro del modelo porque utilizaremos `BCEWithLogitsLoss`.

---

### 10 · Configurar la función de pérdida y el optimizador

Para entrenar Mini U-Net utilizaremos:

**Función de pérdida**

```python
criterio = nn.BCEWithLogitsLoss()
```

Esta función compara los logits del modelo con las máscaras binarias reales.

**Optimizador**

```python
optimizer = torch.optim.Adam(
    modelo.parameters(),
    lr=1e-3
)
```

Adam utilizará los gradientes calculados mediante backpropagation para actualizar los parámetros entrenables.

El learning rate inicial será:

\[
\eta = 0.001
\]

**Considera:** ¿cuál es la diferencia entre calcular la pérdida y actualizar los parámetros del modelo?

---

### 11 · Verificar las dimensiones de entrada y salida

Antes de comenzar el entrenamiento, recuperaremos un batch:

```python
data, target = next(iter(train_loader))
```

Comprobaremos sus dimensiones y los valores presentes en las máscaras.

Para un batch completo de cuatro muestras esperamos:

| Elemento | Dimensiones |
|---|---|
| Imágenes | `(4, 3, 256, 256)` |
| Máscaras | `(4, 1, 256, 256)` |

Después, realizaremos un forward pass con una imagen:

```python
with torch.no_grad():
    logits = modelo(data[:1].to(DEVICE))
```

La salida esperada será:

```text
(1, 1, 256, 256)
```

> [!NOTE]
> `torch.no_grad()` permite ejecutar el modelo sin registrar operaciones para el cálculo de gradientes.
>
> En esta actividad lo utilizaremos únicamente para comprobar la salida antes de entrenar.

---

### 12 · Preparar el directorio de checkpoints

Antes de iniciar el entrenamiento, configuraremos un directorio para almacenar los estados del modelo.

El notebook utiliza:

```text
outputs/checkpoints/
```

Si el directorio no existe, se creará automáticamente.

También se agregará al archivo `dataset.json` una entrada con la ruta de los checkpoints:

```json
{
    "checkpoints": {
        "path": "outputs/checkpoints"
    }
}
```

Esta entrada se incorpora a la configuración existente, sin sustituir las demás secciones.

**Considera:** ¿qué ventajas ofrece registrar las rutas de salida dentro del archivo de configuración del proyecto?

---

### 13 · Ejecutar el ciclo de entrenamiento

Ahora realizaremos la actividad principal de la práctica.

Entrenaremos Mini U-Net durante cinco épocas.

Para cada época, el notebook:

1. Activa el modo de entrenamiento mediante `modelo.train()`.
2. Recorre los batches de `train_loader`.
3. Mueve las imágenes y máscaras al dispositivo.
4. Reinicia los gradientes.
5. Calcula las predicciones mediante el forward pass.
6. Calcula la pérdida.
7. Ejecuta backpropagation.
8. Actualiza los parámetros.
9. Acumula la pérdida para calcular el promedio de la época.

La secuencia fundamental será:

```python
optimizer.zero_grad()

logits = modelo(data)

loss = criterio(logits, target)

loss.backward()

optimizer.step()
```

Observa que cada instrucción cumple una función diferente:

| Instrucción | Función |
|---|---|
| `optimizer.zero_grad()` | Reinicia los gradientes acumulados. |
| `modelo(data)` | Calcula los logits. |
| `criterio(logits, target)` | Calcula la pérdida. |
| `loss.backward()` | Calcula los gradientes. |
| `optimizer.step()` | Actualiza los parámetros. |

Al finalizar cada época, el notebook calculará la pérdida promedio de entrenamiento y mostrará un resultado similar a:

```text
Epoch [1/5] Train Loss: ...
Epoch [2/5] Train Loss: ...
Epoch [3/5] Train Loss: ...
Epoch [4/5] Train Loss: ...
Epoch [5/5] Train Loss: ...
```

Los valores dependerán del entrenamiento realizado.

> [!IMPORTANT]
> Una disminución de la pérdida de entrenamiento indica que el modelo está reduciendo el error medido sobre los datos utilizados para aprender.
>
> Sin embargo, esto no garantiza que tenga un buen desempeño sobre imágenes que no utilizó durante el entrenamiento.

---

### 14 · Guardar checkpoints

Al finalizar cada época, el notebook guardará un checkpoint mediante `torch.save()`.

Los archivos tendrán nombres como:

```text
miniunet_checkpoint_epoch_1.pth
miniunet_checkpoint_epoch_2.pth
miniunet_checkpoint_epoch_3.pth
miniunet_checkpoint_epoch_4.pth
miniunet_checkpoint_epoch_5.pth
```

Cada checkpoint contendrá:

- Número de época.
- Estado de los parámetros del modelo.
- Estado del optimizador.
- Valor de la pérdida del último batch de esa época.

Esto permitirá recuperar los parámetros aprendidos sin tener que repetir necesariamente todo el entrenamiento.

**Considera:** ¿qué diferencia existe entre guardar únicamente los pesos del modelo y guardar también el estado del optimizador?

---

### 15 · Recuperar un checkpoint

Después del entrenamiento, cargaremos el checkpoint correspondiente a la quinta época.

El notebook utiliza:

```python
checkpoint = torch.load(
    ruta_checkpoint,
    map_location=DEVICE,
    weights_only=True
)
```

Posteriormente, recuperaremos los parámetros del modelo:

```python
modelo.load_state_dict(
    checkpoint["model_state_dict"]
)
```

También recuperaremos el estado del optimizador:

```python
optimizer.load_state_dict(
    checkpoint["optimizer_state_dict"]
)
```

> [!NOTE]
> Recuperar los pesos permite utilizar el modelo entrenado para evaluación o inferencia.
>
> Si deseamos continuar el entrenamiento, también resulta importante recuperar el estado del optimizador y considerar la época desde la cual reanudaremos el proceso.

---

### 16 · Calcular la pérdida de validación

Una vez recuperado el modelo entrenado, calcularemos su pérdida sobre el conjunto de validación.

Para ello utilizaremos:

```python
modelo.eval()
```

y:

```python
with torch.no_grad():
    ...
```

Estas instrucciones permiten ejecutar la evaluación sin realizar actualizaciones de los parámetros.

Durante la validación:

1. Recuperaremos los batches de `val_loader`.
2. Moveremos los datos al dispositivo.
3. Calcularemos los logits.
4. Calcularemos la pérdida mediante `BCEWithLogitsLoss`.
5. Acumularemos los resultados.
6. Obtendremos la pérdida promedio del conjunto.

El notebook mostrará:

```text
Validation Loss: ...
```

**Considera:** ¿por qué durante la validación no utilizamos `loss.backward()` ni `optimizer.step()`?

---

### 17 · Generar una predicción de segmentación

Finalmente, utilizaremos una fotografía del conjunto de prueba para observar cómo se comporta Mini U-Net.

Seleccionaremos una muestra aleatoria de `test_dataset`.

Después, agregaremos la dimensión de batch y realizaremos una inferencia mediante:

```python
modelo.eval()

with torch.no_grad():
    logits = modelo(entrada)
```

La salida del modelo contiene logits.

Para obtener probabilidades utilizaremos:

```python
probabilidades = torch.sigmoid(logits)
```

Después, aplicaremos un umbral de `0.5`:

```python
prediccion = (
    probabilidades >= 0.5
).float()
```

Obtendremos una máscara binaria donde:

- `1` representa los píxeles predichos como animal.
- `0` representa los píxeles predichos como fondo.

> [!IMPORTANT]
> Las probabilidades y las máscaras binarias no son lo mismo.
>
> Las probabilidades representan valores continuos entre `0` y `1`, mientras que la máscara final contiene únicamente las etiquetas `0` y `1`.

---

### 18 · Visualizar los resultados

La última actividad consistirá en comparar visualmente las predicciones del modelo con las anotaciones reales.

El notebook genera una figura con cuatro representaciones:

| Visualización | Descripción |
|---|---|
| Imagen | Fotografía utilizada como entrada. |
| Máscara real | Anotación binaria correspondiente a la fotografía. |
| Probabilidades | Mapa de probabilidades producido mediante Sigmoid. |
| Predicción binaria | Máscara obtenida al aplicar el umbral de 0.5. |

Observa las diferencias entre la máscara real y la predicción.

Presta especial atención a:

- Regiones del animal que no fueron identificadas.
- Píxeles del fondo clasificados incorrectamente como animal.
- Contornos que no coinciden con la anotación.
- Regiones con probabilidades cercanas al umbral.
- Posibles efectos de las transformaciones y del entrenamiento limitado.

> [!NOTE]
> En esta práctica realizaremos una inspección visual inicial sobre una muestra del conjunto de prueba.
>
> Esta visualización no sustituye una evaluación cuantitativa del desempeño sobre todo el conjunto.

---

## 📊 Resultados esperados

Al finalizar, el proyecto contará con una implementación modular de Mini U-Net y los componentes necesarios para ejecutar su entrenamiento.

| Componente | Resultado |
|---|---|
| `src/dataset.py` | Dataset para segmentación binaria. |
| `src/transforms.py` | Pipelines de entrenamiento y evaluación. |
| `src/models.py` | Arquitectura Mini U-Net. |
| `train_loader` | Lotes de entrenamiento con aumento de datos. |
| `val_loader` | Lotes de validación con procesamiento determinista. |
| `test_loader` | Lotes de prueba con procesamiento determinista. |
| Modelo | Mini U-Net con tres canales de entrada y uno de salida. |
| Función de pérdida | `BCEWithLogitsLoss`. |
| Optimizador | Adam con learning rate de `0.001`. |
| Entrenamiento | Cinco épocas iniciales. |
| Checkpoints | Archivos `.pth` guardados por época. |
| Validación | Pérdida promedio sobre el conjunto de validación. |
| Inferencia | Probabilidades y máscara binaria de una muestra. |

---

## 🧩 Punto de control

Antes de finalizar, realiza las siguientes actividades:

**1 · Verificar la estructura del proyecto**

Comprueba que los archivos `dataset.py`, `models.py` y `transforms.py` se encuentren dentro de `src/` y que el notebook pueda importarlos correctamente.

**2 · Inspeccionar las dimensiones**

Verifica que un batch completo de cuatro fotografías tenga dimensiones:

```text
(4, 3, 256, 256)
```

y que las máscaras correspondientes tengan dimensiones:

```text
(4, 1, 256, 256)
```

**3 · Identificar las operaciones de entrenamiento**

Localiza las instrucciones responsables del forward pass, el cálculo de pérdida, backpropagation y la actualización de parámetros.

Explica qué sucede en cada una.

**4 · Comprobar los checkpoints**

Verifica que se hayan generado los archivos correspondientes a las cinco épocas de entrenamiento.

**5 · Interpretar la pérdida**

Observa los valores de pérdida reportados durante el entrenamiento y el valor obtenido durante la validación.

Explica qué información proporciona cada uno.

**6 · Analizar la predicción**

Compara visualmente la máscara real con la predicción binaria.

Identifica al menos una región donde coincidan y, si existen, regiones donde difieran.

**Resultado esperado:** una Mini U-Net entrenada durante cinco épocas, con checkpoints guardados, pérdida de validación calculada y una predicción binaria visualizada.

---

## 🤔 Observa e interpreta

Al finalizar la práctica, responde las siguientes preguntas:

1. ¿Qué ventajas ofrece organizar el código en módulos dentro de `src/` en lugar de mantener todas las definiciones dentro de un notebook?
2. ¿Por qué convertimos las máscaras originales del Oxford-IIIT Pet Dataset a una representación binaria?
3. ¿Qué diferencia existe entre los pipelines de entrenamiento y validación?
4. ¿Por qué Mini U-Net utiliza `num_classes=1` para este problema de segmentación binaria?
5. ¿Por qué utilizamos `BCEWithLogitsLoss` sin aplicar previamente Sigmoid?
6. ¿Qué función cumplen `optimizer.zero_grad()`, `loss.backward()` y `optimizer.step()`?
7. ¿Qué diferencia existe entre un batch, una iteración y una época?
8. ¿Qué información contiene un checkpoint y por qué puede ser útil recuperar el estado del optimizador?
9. ¿Por qué utilizamos `modelo.eval()` y `torch.no_grad()` durante la validación y la inferencia?
10. ¿Qué diferencias existen entre los logits, las probabilidades y la máscara binaria generada por Mini U-Net?

---

## ✅ Punto de control final

Al finalizar esta práctica habrás:

- Reutilizado el proyecto del Oxford-IIIT Pet Dataset.
- Incorporado una carpeta `src/` en la raíz del proyecto.
- Agregado los módulos `dataset.py`, `models.py` y `transforms.py`.
- Incorporado el notebook `entrenamiento_mini_u-net.ipynb`.
- Importado clases y funciones desde módulos externos.
- Recuperado las particiones experimentales existentes.
- Convertido las máscaras originales a segmentación binaria.
- Construido objetos Dataset y DataLoader.
- Seleccionado el dispositivo de entrenamiento.
- Instanciado una arquitectura Mini U-Net.
- Configurado `BCEWithLogitsLoss` y Adam.
- Verificado las dimensiones de entrada y salida.
- Ejecutado el ciclo de entrenamiento durante cinco épocas.
- Calculado gradientes mediante backpropagation.
- Actualizado los parámetros del modelo.
- Guardado checkpoints por época.
- Recuperado los estados del modelo y del optimizador.
- Calculado la pérdida sobre el conjunto de validación.
- Generado probabilidades mediante Sigmoid.
- Aplicado un umbral para obtener una máscara binaria.
- Visualizado y comparado las predicciones con las máscaras reales.

---

## 🏁 ¡Práctica completada!

Has integrado los principales componentes necesarios para entrenar una red neuronal de segmentación utilizando PyTorch.

Nuestro proyecto ahora cuenta con una arquitectura Mini U-Net, un pipeline de datos reutilizable, una función de pérdida, un optimizador y un ciclo de entrenamiento que permite actualizar los parámetros del modelo.

También aprendimos a guardar y recuperar checkpoints, calcular la pérdida de validación y transformar los logits en predicciones binarias.

**Con esta práctica hemos conectado el dataset, el modelo y el proceso de aprendizaje.**

En las siguientes actividades profundizaremos en la evaluación del desempeño y el análisis de los errores de segmentación.

---

## 📚 Dataset de referencia

**Oxford-IIIT Pet Dataset**

Parkhi, O. M., Vedaldi, A., Zisserman, A., & Jawahar, C. V. (2012).

*Cats and Dogs.*

IEEE Conference on Computer Vision and Pattern Recognition (CVPR).

[Consultar el dataset original →](https://www.robots.ox.ac.uk/~vgg/data/pets/)

---

## 🔗 Enlaces

[**← Volver al repositorio principal del taller**](https://github.com/bettypau-open-knowledge/del-dataset-a-unet)