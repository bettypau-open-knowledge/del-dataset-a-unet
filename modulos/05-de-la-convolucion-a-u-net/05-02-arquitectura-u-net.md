# 5.2 · Arquitectura U-Net

En el tema anterior estudiamos los fundamentos de las **redes neuronales convolucionales (CNN)** y aprendimos cómo las operaciones de convolución permiten extraer características visuales de una imagen.

Analizamos cómo los kernels, canales, stride y padding determinan las dimensiones de los mapas de características, y cómo operaciones como ReLU, Max Pooling y las convoluciones transpuestas transforman los tensores a medida que avanzan por una red neuronal.

Ahora utilizaremos estos conocimientos para comprender una de las arquitecturas más utilizadas en segmentación semántica de imágenes: **U-Net**.

A diferencia de una red diseñada únicamente para clasificar una imagen completa, un modelo de segmentación debe identificar las regiones de interés y determinar **a qué clase pertenece cada píxel**.

Esto nos plantea una pregunta fundamental:

**¿Cómo puede una red neuronal comprender qué aparece en una imagen y, al mismo tiempo, conservar la información espacial necesaria para localizarlo píxel por píxel?**

Para responderla, estudiaremos la arquitectura **encoder–decoder**, que organiza el procesamiento de una imagen en dos etapas complementarias.

Comenzaremos con el **encoder (codificador)**, encargado de extraer características mediante operaciones convolucionales. A medida que avanzamos por sus diferentes niveles, disminuye progresivamente la resolución espacial de los mapas de características y, en la configuración que estudiaremos, aumenta el número de canales.

Esto permite construir representaciones cada vez más abstractas: desde características locales, como bordes y texturas, hasta patrones y estructuras visuales más complejas.

Posteriormente, conoceremos el **bottleneck o cuello de botella**, que conecta el encoder con el decoder y contiene las representaciones más profundas de la arquitectura.

Después estudiaremos el **decoder (decodificador)**, encargado de construir la representación de salida a partir de las características extraídas. Mediante operaciones de *upsampling* o convoluciones transpuestas, incrementa progresivamente la resolución espacial de los mapas de características.

Para comprender este recorrido, analizaremos un ejemplo en el que una imagen RGB de entrada tiene dimensiones `(3, 256, 256)` y los mapas de características evolucionan de la siguiente manera:

| Etapa | Dimensiones `(C, H, W)` |
|---|---|
| Entrada | `(3, 256, 256)` |
| Encoder · Nivel 1 | `(64, 256, 256)` |
| Encoder · Nivel 2 | `(128, 128, 128)` |
| Encoder · Nivel 3 | `(256, 64, 64)` |
| Bottleneck | `(512, 32, 32)` |
| Decoder · Nivel 1 | `(256, 64, 64)` |
| Decoder · Nivel 2 | `(128, 128, 128)` |
| Decoder · Nivel 3 | `(64, 256, 256)` |
| Salida binaria | `(1, 256, 256)` |

Este ejemplo nos permitirá observar cómo el encoder reduce la resolución espacial mientras construye representaciones con más canales, y cómo el decoder recupera progresivamente la resolución necesaria para generar una predicción por píxel.

Sin embargo, recuperar las dimensiones espaciales no significa recuperar automáticamente toda la información que se perdió durante las operaciones de reducción.

Por ello, estudiaremos uno de los componentes característicos de U-Net: las **skip connections o conexiones de salto**.

Estas conexiones permiten transferir directamente mapas de características desde determinados niveles del encoder hacia los niveles correspondientes del decoder, sin hacerlos pasar por todas las capas intermedias.

Su propósito es reutilizar información espacial de mayor resolución y combinarla con las representaciones más profundas del decoder, favoreciendo una localización más precisa de las regiones y sus contornos.

Para integrar esta información, U-Net utiliza la **concatenación de mapas de características**.

Analizaremos cómo `torch.cat()` permite unir tensores a lo largo de la dimensión de canales (`dim=1`), conservando el tamaño del batch y las dimensiones espaciales.

Por ejemplo, si tenemos dos tensores:

```python
X_skip.shape = (4, 64, 128, 128)
X_up.shape   = (4, 64, 128, 128)
```

Su concatenación produce:

```python
X_concat = torch.cat([X_skip, X_up], dim=1)

# Resultado:
# (4, 128, 128, 128)
```

Observaremos que la concatenación **aumenta el número de canales**, pero no suma los valores de los tensores ni modifica sus dimensiones espaciales.

También distinguiremos la concatenación de la suma elemento a elemento, utilizada en otras arquitecturas, y comprenderemos por qué ambas operaciones tienen requisitos y efectos diferentes.

Después analizaremos qué sucede con los mapas concatenados: nuevas capas convolucionales permiten combinar las características recibidas desde el encoder y el decoder, generando representaciones que integran información espacial y semántica.

Finalmente, estudiaremos la **capa de salida de U-Net**, encargada de transformar los últimos mapas de características del decoder en una predicción de segmentación.

Para ello, conoceremos el uso de una **convolución de `1 × 1`**, que combina los canales de cada posición espacial sin modificar la altura ni la anchura del tensor.

Por ejemplo, si el último bloque del decoder produce un tensor:

```text
(4, 64, 256, 256)
```

Una capa:

```python
nn.Conv2d(
    in_channels=64,
    out_channels=1,
    kernel_size=1
)
```

produce:

```text
(4, 1, 256, 256)
```

Cada valor de salida corresponde a un **logit**, es decir, una puntuación sin normalizar que posteriormente puede transformarse en una probabilidad.

En este caso, la capa contiene **65 parámetros entrenables**: 64 pesos y un sesgo.

A partir de esta operación, distinguiremos dos configuraciones de segmentación.

**Segmentación binaria**

Cuando necesitamos distinguir entre dos clases, como objeto y fondo, podemos utilizar un único canal de salida.

Estudiaremos cómo la función **Sigmoid** transforma los logits en valores entre `0` y `1`, que pueden interpretarse como probabilidades de pertenencia a la clase positiva.

Posteriormente, aplicaremos un umbral, por ejemplo `0.5`, para obtener una máscara binaria con valores `0` y `1`.

**Segmentación multiclase**

Cuando necesitamos distinguir entre más de dos clases mutuamente excluyentes, utilizaremos una capa de salida con tantos canales como clases tenga el problema.

Por ejemplo, para tres clases:

```python
nn.Conv2d(
    in_channels=64,
    out_channels=3,
    kernel_size=1
)
```

La salida tendrá dimensiones:

```text
(4, 3, 256, 256)
```

Estudiaremos cómo **Softmax** permite obtener probabilidades por clase para cada píxel y cómo `argmax(dim=1)` selecciona la clase con mayor puntuación, generando una máscara de etiquetas.

También relacionaremos ambas configuraciones con sus funciones de pérdida habituales:

| Característica | Binaria | Multiclase |
|---|---|---|
| Canales de salida | 1 | `K` |
| Activación para probabilidades | Sigmoid | Softmax |
| Predicción final | Umbral | Argmax |
| Función de pérdida habitual | `BCEWithLogitsLoss` | `CrossEntropyLoss` |

> [!IMPORTANT]
> Las funciones `BCEWithLogitsLoss` y `CrossEntropyLoss` reciben directamente los **logits**, sin aplicar previamente Sigmoid o Softmax.
>
> Estas activaciones pueden utilizarse posteriormente para obtener probabilidades e interpretar las predicciones.

Al finalizar este tema comprenderemos que **U-Net no dibuja directamente una máscara**, sino que aprende a transformar una imagen en puntuaciones por clase para cada posición espacial.

La combinación del encoder, el decoder, las conexiones de salto y la capa de salida permite construir una arquitectura capaz de integrar características visuales profundas con información espacial, un requisito fundamental para la segmentación semántica.

### 📽️ Presentación

[**Ver presentación del tema →**](../../recursos/presentaciones/05-02-arquitectura-u-net.pdf)

---

## 🧪 Prácticas

1. [Arquitectura U-Net →](../../recursos/codigo/05-de-la-convolucion-a-u-net/arquitectura-u-net.ipynb)


---
<!---
## ➡️ Siguiente etapa

Una vez comprendida la arquitectura U-Net, podremos comenzar a implementar sus componentes mediante PyTorch.

Utilizaremos los conocimientos sobre convoluciones, bloques de procesamiento, conexiones de salto y capas de salida para construir un modelo de segmentación y conectarlo con el pipeline de datos desarrollado en el módulo anterior.
--->
---

[← Volver al repositorio principal del taller](https://github.com/bettypau-open-knowledge/del-dataset-a-unet)