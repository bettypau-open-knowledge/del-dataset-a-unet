# 2.3 · Análisis exploratorio del dataset

Una vez que hemos construido el **manifest** y centralizado las rutas del dataset mediante un archivo de configuración, contamos con una base organizada para examinar sus características y evaluar la calidad de los datos.

Antes de comenzar el análisis exploratorio, es importante recordar que durante la construcción del inventario realizamos diferentes verificaciones para identificar posibles problemas:

- Imágenes sin máscara y máscaras sin imagen.
- Archivos que no pueden abrirse o decodificarse.
- Extensiones inesperadas y nombres o identificadores duplicados.
- Incompatibilidad de dimensiones entre imagen y máscara.
- Máscaras vacías o con valores no permitidos.

Estas verificaciones permiten detectar **inconsistencias estructurales y errores que pueden identificarse mediante procedimientos automáticos**.

Sin embargo, que una muestra supere estas validaciones no garantiza que sus anotaciones sean correctas. Por ejemplo, un *bounding box* puede encontrarse dentro de los límites de una imagen, pero no señalar realmente la cabeza del animal.

Por ello, complementaremos las verificaciones automáticas con una **inspección visual basada en muestreo aleatorio** y un **análisis estadístico de las características del dataset**.

---

## 🔍 Muestreo aleatorio para inspección visual

La inspección visual permite identificar problemas que no siempre pueden detectarse mediante verificaciones automáticas, como máscaras mal alineadas, anotaciones incorrectas o regiones de interés que no corresponden con el objeto esperado.

Sin embargo, revisar manualmente todas las muestras puede resultar poco práctico cuando trabajamos con datasets grandes.

Una alternativa consiste en seleccionar una **muestra aleatoria** y utilizarla para estimar la proporción de registros que presentan determinado tipo de error.

### 📐 Estimación del tamaño de una muestra representativa

Supongamos que tenemos un dataset con $N$ imágenes y queremos realizar una inspección visual para identificar posibles errores en sus anotaciones.

Aunque podríamos revisar todas las imágenes, cuando el dataset es grande esta tarea puede requerir demasiado tiempo.

Una alternativa consiste en seleccionar una **muestra aleatoria de imágenes** y utilizar los resultados de su inspección para estimar la proporción de errores presentes en el dataset completo.

Pero surge una pregunta importante:

**¿Cuántas imágenes necesitamos inspeccionar para obtener una estimación con un nivel de confianza y un margen de error determinados?**

Para responderla, partiremos de la expresión del **intervalo de confianza para una proporción poblacional**.

#### 1. Intervalo de confianza para una proporción

Supongamos que seleccionamos aleatoriamente $n$ imágenes y encontramos $x$ imágenes con anotaciones incorrectas.

La proporción de errores observada en la muestra es:

$$
\hat{p}=\frac{x}{n}
$$

Donde:

- $N$: número total de imágenes del dataset.
- $n$: número de imágenes seleccionadas para inspección.
- $x$: número de imágenes con errores dentro de la muestra.
- $\hat{p}$: proporción de errores observada en la muestra.
- $p$: proporción real de imágenes con errores en el dataset completo.

Como $\hat{p}$ se calcula a partir de una muestra, generalmente no coincidirá exactamente con la proporción poblacional $p$.

Por ello, utilizamos un **intervalo de confianza**, que expresa un rango de valores plausibles para la proporción poblacional.

Cuando seleccionamos una muestra aleatoria simple sin reemplazo de una población finita, podemos escribir el intervalo aproximado como:

$$ \boxed{
\hat{p} - Z\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}\sqrt{\frac{N-n}{N-1}}\leq p \leq\hat{p}+Z\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}\sqrt{\frac{N-n}{N-1}}
}
$$

Donde $Z$ representa el valor crítico de la distribución normal estándar asociado con el nivel de confianza seleccionado.

El término:

$$
\sqrt{\frac{N-n}{N-1}}
$$

se conoce como **factor de corrección por población finita**.

Este factor considera que estamos seleccionando imágenes de un conjunto limitado, sin reemplazo.

> [!NOTE]
> Esta expresión utiliza una aproximación normal para una proporción, conocida como intervalo de Wald, con corrección por población finita.
>
> Su precisión puede ser limitada cuando la proporción está cerca de 0 o 1 o cuando la muestra es pequeña. La utilizaremos para comprender la deducción del tamaño de muestra.

#### 2. Identificación del margen de error

El intervalo de confianza anterior tiene la forma:

$$
\hat{p}-E\leq p\leq\hat{p}+E
$$

Donde $E$ representa el **margen de error**.

Comparando ambas expresiones, identificamos que:

$$
\boxed{
E=
Z\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
\sqrt{\frac{N-n}{N-1}}
}
$$

Sin embargo, queremos calcular el tamaño de muestra **antes de realizar la inspección**.

Por lo tanto, todavía no conocemos la proporción muestral $\hat{p}$.

Para planificar el muestreo, utilizaremos una proporción esperada de errores, representada por $p_e$.

Así, el margen de error utilizado para determinar el tamaño de muestra queda expresado como:

$$
\boxed{
E=
Z\sqrt{\frac{p_e(1-p_e)}{n}}
\sqrt{\frac{N-n}{N-1}}
}
$$

#### 3. Despeje del tamaño de muestra

Nuestro objetivo es despejar $n$ de la expresión anterior.

**Paso 1. Elevamos ambos lados al cuadrado.**

$$
E^2=
Z^2
\frac{p_e(1-p_e)}{n}
\frac{N-n}{N-1}
$$

Multiplicamos las fracciones:

$$
E^2=
\frac{Z^2p_e(1-p_e)(N-n)}{n(N-1)}
$$

**Paso 2. Multiplicamos ambos lados por $n(N-1)$.**

$$
E^2n(N-1)=Z^2p_e(1-p_e)(N-n)
$$

**Paso 3. Desarrollamos ambos lados de la ecuación.**

$$
E^2nN-E^2n=
Z^2p_e(1-p_e)N-Z^2p_e(1-p_e)n
$$

**Paso 4. Agrupamos los términos que contienen $n$.**

$$
E^2nN-E^2n+Z^2p_e(1-p_e)n=
Z^2p_e(1-p_e)N
$$

**Paso 5. Factorizamos $n$.**

$$
n\left[E^2N-E^2+Z^2p_e(1-p_e)\right] = Z^2p_e(1-p_e)N
$$

**Paso 6. Despejamos $n$.**

$$
n=
\frac{Z^2p_e(1-p_e)N}
{E^2N-E^2+Z^2p_e(1-p_e)}
$$

Reorganizando el denominador:

$$
\boxed{
n=
\frac{Z^2p_e(1-p_e)N}
{E^2(N-1)+Z^2p_e(1-p_e)}
}
$$

Esta es la **fórmula del tamaño de muestra para estimar una proporción en una población finita**, utilizando la aproximación normal.

#### 4. ¿Qué sucede cuando la población es muy grande?

Si el número total de imágenes $N$ es suficientemente grande respecto al tamaño de muestra, el factor de corrección por población finita se aproxima a 1:

$$
\sqrt{\frac{N-n}{N-1}}\approx1
$$

En consecuencia, el margen de error se simplifica a:

$$
E=Z\sqrt{\frac{p_e(1-p_e)}{n}}
$$

Elevando al cuadrado:

$$
E^2=\frac{Z^2p_e(1-p_e)}{n}
$$

Despejando $n$:

$$
\boxed{
n_0=\frac{Z^2p_e(1-p_e)}{E^2}
}
$$

Esta expresión permite calcular el **tamaño de muestra inicial**, sin considerar la corrección por población finita.

Podemos relacionar ambas fórmulas mediante:

$$
\boxed{
n=\frac{Nn_0}{N+n_0-1}
}
$$

Donde:

- $n_0$: tamaño de muestra inicial, sin corrección.
- $n$: tamaño de muestra corregido.
- $N$: número total de imágenes del dataset.

> [!IMPORTANT]
> Cuando conocemos el tamaño del dataset y realizamos un muestreo aleatorio sin reemplazo, podemos utilizar la fórmula con corrección por población finita.
>
> Esta corrección resulta especialmente relevante cuando la muestra representa una fracción considerable del dataset.

---

### 🎯 ¿Cómo seleccionamos los parámetros?

Para calcular el tamaño de muestra necesitamos definir tres valores.

| Parámetro | Símbolo | Descripción |
|---|---|---|
| Nivel de confianza | $1-\alpha$ | Nivel de confianza asociado con el procedimiento de estimación. |
| Margen de error | $E$ | Precisión deseada para estimar la proporción de errores. |
| Proporción esperada de errores | $p_e$ | Proporción de imágenes que suponemos que podrían presentar errores. |

#### Nivel de confianza

El nivel de confianza determina el valor crítico $Z$ de la distribución normal estándar.

| Nivel de confianza | Valor de $Z$ |
|---|---:|
| 90 % | 1.645 |
| 95 % | 1.960 |
| 99 % | 2.576 |

Por ejemplo, utilizar un nivel de confianza del 95 % significa que, si repitiéramos el procedimiento de muestreo muchas veces, aproximadamente el 95 % de los intervalos construidos mediante un método bien calibrado contendrían la proporción poblacional real.

#### Margen de error

El margen de error representa la precisión que deseamos alcanzar.

Por ejemplo:

$$
E=0.05
$$

corresponde a un margen de error de **5 puntos porcentuales**.

Cuanto menor sea el margen de error solicitado, mayor será el tamaño de muestra necesario.

#### Proporción esperada de errores

La proporción esperada $p_e$ representa nuestra estimación previa de la frecuencia de errores en el dataset.

Por ejemplo:

$$
p_e=0.10
$$

significa que esperamos que aproximadamente el 10 % de las imágenes presente algún error.

Podemos obtener este valor a partir de una revisión preliminar o de información previa sobre el dataset.

Si no contamos con información suficiente, podemos utilizar:

$$
p_e=0.5
$$

Este valor maximiza el producto:

$$
p_e(1-p_e)
$$

y, por lo tanto, produce el tamaño de muestra más conservador para la fórmula utilizada.

---

### 🧮 Ejemplo de cálculo

Supongamos que queremos inspeccionar un dataset de **1,000 imágenes** y establecemos los siguientes parámetros:

| Parámetro | Valor |
|---|---:|
| Tamaño de la población ($N$) | 1,000 imágenes |
| Nivel de confianza | 95 % |
| Valor crítico ($Z$) | 1.96 |
| Margen de error ($E$) | 0.05 |
| Proporción esperada de errores ($p_e$) | 0.10 |

**Paso 1. Calculamos el tamaño de muestra inicial.**

$$
n_0=\frac{Z^2p_e(1-p_e)}{E^2}
$$

Sustituyendo:

$$
n_0=\frac{(1.96)^2(0.10)(0.90)}{(0.05)^2}
$$

$$
n_0=138.2976
$$

Sin considerar el tamaño de la población, necesitaríamos inspeccionar aproximadamente **139 imágenes**.

**Paso 2. Aplicamos la corrección por población finita.**

$$
n=\frac{Nn_0}{N+n_0-1}
$$

Sustituyendo:

$$
n=
\frac{(1000)(138.2976)}
{1000+138.2976-1}
$$

$$
n\approx121.60
$$

Redondeando hacia arriba:

$$
\boxed{n=122\text{ imágenes}}
$$

Por lo tanto, bajo los supuestos establecidos, necesitaríamos seleccionar aleatoriamente **122 imágenes de las 1,000 disponibles** para realizar nuestra inspección visual.

> [!NOTE]
> El tamaño de muestra calculado permite planificar la estimación de una proporción con una precisión aproximada, pero no garantiza que se detecten todos los errores.
>
> Tampoco garantiza que cada especie o raza quede suficientemente representada. Si queremos evaluar la calidad de las anotaciones por categoría, debemos considerar un diseño de muestreo apropiado para ese objetivo.

---

### 🧠 Consideraciones para la inspección visual

Una vez determinado el tamaño de muestra, debemos seleccionar las imágenes de manera aleatoria y reproducible.

Para ello, podemos utilizar una semilla aleatoria fija y conservar los identificadores de las imágenes seleccionadas.

También es importante definir previamente **qué consideraremos un error** durante la inspección.

Por ejemplo:

- El *bounding box* no corresponde con la cabeza del animal.
- La máscara no coincide espacialmente con el objeto.
- Existen regiones incorrectamente etiquetadas.
- La anotación presenta inconsistencias visibles.

Si encontramos diferentes tipos de errores, podemos registrar cada uno por separado para facilitar su análisis.

---

## 📊 Análisis estadístico y exploratorio del dataset

Además de revisar la calidad de las anotaciones, necesitamos comprender las características generales de las imágenes y máscaras.

Para ello, utilizaremos la información del manifest y calcularemos estadísticas descriptivas que permitan identificar distribuciones, variabilidad y posibles valores atípicos.

### 🏷️ Distribución de imágenes por categoría

Analizaremos cuántas fotografías pertenecen a cada especie y raza.

Este análisis permitirá identificar:

- Número de imágenes por categoría.
- Proporción de cada categoría respecto al total.
- Diferencias en la cantidad de muestras entre especies y razas.
- Posibles desbalances en la representación de las categorías.

Podemos utilizar gráficas de barras para comparar cantidades y representaciones proporcionales para visualizar la participación de cada categoría dentro del dataset.

### 📐 Dimensiones y tamaño de las imágenes

Estudiaremos las características espaciales de las fotografías mediante:

- Ancho y alto, expresados en píxeles.
- Número total de píxeles por imagen.
- Relación de aspecto (*aspect ratio*).
- Valores mínimos, máximos, media, mediana y dispersión.

El número total de píxeles se calcula como:

$$
N_{\text{píxeles}}=W\times H
$$

Mientras que la relación de aspecto se define como:

$$
r=\frac{W}{H}
$$

Estas características nos ayudarán a identificar diferencias de resolución, imágenes horizontales o verticales y variabilidad dimensional.

La información será útil posteriormente para seleccionar estrategias de redimensionamiento, recorte o relleno durante el procesamiento de imágenes.

### 🎨 Distribución de píxeles en las máscaras

Finalmente, analizaremos la composición de las máscaras de segmentación.

En Oxford-IIIT Pet, las máscaras contienen tres etiquetas:

| Valor | Región |
|---|---|
| `1` | Animal (*foreground*). |
| `2` | Fondo (*background*). |
| `3` | Contorno o región de clasificación ambigua. |

Para cada máscara, calcularemos la cantidad y el porcentaje de píxeles correspondientes a cada región.

La proporción de una clase $c$ puede expresarse como:

$$
P_c=\frac{N_c}{N_{\text{píxeles}}}\times100
$$

Donde $N_c$ representa el número de píxeles pertenecientes a esa clase.

Este análisis permitirá estudiar:

- Porcentaje de la imagen ocupado por el animal.
- Proporciones de animal, fondo y contorno.
- Variabilidad de estas proporciones entre imágenes.
- Distribución global de píxeles por clase.
- Posibles desbalances entre las clases de segmentación.

Utilizaremos histogramas, gráficas de violín, barras apiladas y representaciones proporcionales para examinar estas características desde diferentes perspectivas.

> [!IMPORTANT]
> La distribución de imágenes por especie o raza y la distribución de píxeles por clase de segmentación representan fenómenos diferentes.
>
> Una distribución equilibrada de fotografías entre categorías no implica necesariamente que las clases de segmentación estén balanceadas.

---

## 🧪 Prácticas

1. [Análisis exploratorio del minidataset →](../../practicas/02-ingenieria-del-dataset/analisis-exploratorio-del-dataset/05-analisis-exploratorio-de-minidataset.md)
2. [Análisis exploratorio del Oxford-IIIT Pet Dataset →](../../practicas/02-ingenieria-del-dataset/analisis-exploratorio-del-dataset/06-analisis-exploratorio-del-oxford-dataset.md)

---
## ➡️ Completa el reto del módulo

[Encuentra al gato →](../../practicas/02-ingenieria-del-dataset/07-reto-modulo-2.md)

---
[← Volver a página anterior](./02-02-inventario-y-configuracion-del-dataset.md)

[← Volver al índice de módulos](../modulos.md)

[← Volver a la portada del taller](../../README.md)