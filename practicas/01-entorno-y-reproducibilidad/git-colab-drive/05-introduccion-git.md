# 🌱 Introducción a Git

Git permite registrar los cambios realizados en los archivos de un proyecto y conservar un historial de sus diferentes versiones.

En esta práctica crearás un repositorio Git local y modificarás un archivo de
texto varias veces. Cada cambio se registrará mediante un *commit* para,
posteriormente, explorar el historial y recuperar una versión anterior del archivo.

---

## 🎯 Objetivo

Familiarizarse con el flujo básico de trabajo de Git y reconocer cómo los cambios de un archivo pasan del **directorio de trabajo** al **staging area** antes de almacenarse como un *commit* en el repositorio local.

También utilizarás el historial de Git para consultar y recuperar una versión anterior de un archivo.

---

## 💻 Instrucciones

### 1 · Crea una carpeta para la práctica

Crea una nueva carpeta llamada:

```text
introduccion-git
```

Ábrela como proyecto en **Visual Studio Code**.

La carpeta comenzará vacía:

```text
introduccion-git/
```

Abre la terminal integrada de VS Code y comprueba que te encuentras dentro de esta carpeta.

---

### 2 · Inicializa el repositorio

Inicializa un repositorio Git:

```bash
git init
```

Consulta su estado:

```bash
git status
```

> [!NOTE]
> `git init` convierte la carpeta actual en un **repositorio Git local**.
> A partir de este momento, Git podrá comenzar a registrar el historial de los archivos del proyecto.

---

### 3 · Crea `texto.txt`

Desde el explorador de archivos de VS Code crea:

```text
texto.txt
```

Déjalo vacío por el momento.

Consulta nuevamente el estado del repositorio:

```bash
git status
```

Observa cómo aparece `texto.txt`.

---

### 4 · Agrega el archivo al staging area

Selecciona `texto.txt` para incluirlo en el próximo *commit*:

```bash
git add texto.txt
```

Consulta nuevamente:

```bash
git status
```

Compara esta salida con la que obtuviste antes de ejecutar `git add`.

---

### 5 · Registra la primera versión

Crea el primer *commit*:

```bash
git commit -m "Creación de texto.txt"
```

Este *commit* representa la primera versión registrada del archivo.

---

### 6 · Agrega el primer mensaje

Abre `texto.txt` y escribe:

```text
¡Hola mundo!
```

Guarda el archivo.

Agrega el cambio al staging area:

```bash
git add texto.txt
```

Registra esta nueva versión:

```bash
git commit -m "Agrega saludo Hola mundo"
```

---

### 7 · Modifica nuevamente el archivo

Reemplaza el contenido de `texto.txt` por:

```text
¡Bye bye!
```

Guarda el archivo y consulta el estado del repositorio:

```bash
git status
```

Agrega la modificación:

```bash
git add texto.txt
```

Registra la nueva versión:

```bash
git commit -m "Cambia saludo a Bye bye"
```

Finalmente, consulta nuevamente:

```bash
git status
```

> [!TIP]
> Si todos los cambios fueron registrados correctamente, `git status` deberá indicar que no existen cambios pendientes en el directorio de trabajo.

---

## 🕘 Explora el historial del archivo

Hasta este momento, `texto.txt` ha tenido diferentes versiones:

```text
archivo vacío
      ↓
¡Hola mundo!
      ↓
¡Bye bye!
```

Git conserva este historial.

### 8 · Consulta los commits de `texto.txt`

Ejecuta:

```bash
git log --oneline -- texto.txt
```

Obtendrás una lista similar a:

```text
a1b2c3d Cambia saludo a Bye bye
e4f5g6h Agrega saludo Hola mundo
i7j8k9l Creación de texto.txt
```

> [!NOTE]
> Los identificadores de los commits serán diferentes en cada repositorio.
> Utiliza los que aparezcan en tu propia terminal.

Localiza el commit:

```text
Agrega saludo Hola mundo
```

y copia su identificador.

En los siguientes pasos lo representaremos como:

```text
ID
```

---

### 9 · Consulta una versión anterior

Antes de modificar el archivo actual, observa cómo era `texto.txt` en ese commit.

Sustituye `ID` por el identificador que copiaste:

```bash
git show ID:texto.txt
```

La terminal deberá mostrar el contenido que tenía `texto.txt` en ese momento del historial.

También puedes explorar los commits y los cambios desde **Source Control** en Visual Studio Code.

> [!IMPORTANT]
> `git show` permite **consultar** el contenido almacenado en un commit sin modificar todavía el archivo de tu directorio de trabajo.

---

## ⏪ Recupera una versión anterior

### 10 · Restaura la versión con `¡Hola mundo!`

Utiliza el mismo identificador para recuperar la versión de `texto.txt`
correspondiente al commit **Agrega saludo Hola mundo**:

```bash
git restore --source=ID texto.txt
```

Abre `texto.txt` y observa su contenido.

Después consulta:

```bash
git status
```

### 🤔 Observa

Aunque recuperaste una versión almacenada anteriormente, Git indica que `texto.txt` tiene cambios pendientes.

¿Por qué?

El historial **no retrocedió**. `git restore --source=ID` tomó el contenido de `texto.txt` almacenado en aquel commit y lo colocó nuevamente en tu **directorio de trabajo**.

---

### 11 · Examina el cambio

Consulta las diferencias desde la terminal:

```bash
git diff
```

Observa qué contenido fue eliminado y cuál fue agregado.

También puedes visualizar esta comparación desde **Source Control** en VS Code, lo que puede resultar más cómodo para identificar gráficamente las modificaciones.

---

### 12 · Registra la versión recuperada

Agrega `texto.txt` al staging area:

```bash
git add texto.txt
```

Registra el cambio:

```bash
git commit -m "Recupera versión Hola mundo"
```

---

### 13 · Consulta nuevamente el historial

Ejecuta:

```bash
git log --oneline -- texto.txt
```

Ahora deberás observar un nuevo commit al inicio del historial:

```text
... Recupera versión Hola mundo
... Cambia saludo a Bye bye
... Agrega saludo Hola mundo
... Creación de texto.txt
```

Observa que el commit **Cambia saludo a Bye bye** continúa formando parte del historial.

La recuperación de una versión anterior **no eliminó los commits posteriores**: creó un nuevo cambio a partir del contenido almacenado previamente.

---

## 🤔 Observa e interpreta

A partir de lo realizado durante la práctica, reflexiona:

- ¿Qué mostró `git status` inmediatamente después de crear `texto.txt`?
- ¿Qué cambió después de ejecutar `git add texto.txt`?
- ¿Qué función cumple el **staging area** antes de realizar un commit?
- ¿Qué información permite consultar `git log`?
- ¿Qué diferencia observaste entre `git show` y `git restore`?
- Después de ejecutar `git restore --source=ID texto.txt`, ¿por qué apareció nuevamente una modificación en `git status`?
- ¿Se eliminó del historial la versión que contenía `¡Bye bye!`?
- ¿Qué ventaja tiene conservar las versiones anteriores en lugar de reemplazarlas definitivamente?

---

## ✅ Punto de control

Al finalizar esta práctica habrás practicado:

- inicializar un repositorio Git local;
- consultar el estado del repositorio;
- identificar un archivo nuevo o modificado;
- agregar cambios al staging area;
- registrar versiones mediante commits;
- consultar el historial de un archivo;
- inspeccionar el contenido de una versión anterior;
- comparar cambios entre el directorio de trabajo y la versión registrada;
- recuperar el contenido de una versión anterior;
- registrar la recuperación como un nuevo commit.

> [!TIP]
> Utiliza `git status` con frecuencia mientras trabajas con Git. Es una de las formas más sencillas de identificar **dónde se encuentran tus cambios antes de realizar la siguiente operación**.

---

[← Volver a Git, Github, Google Colab y Google Drive](../../../modulos/01-entorno-y-reproducibilidad/01-03-git-colab-drive.md)