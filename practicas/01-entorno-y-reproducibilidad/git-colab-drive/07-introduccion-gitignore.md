# 🙈 Introducción a `.gitignore`

No todos los archivos que forman parte de nuestro espacio de trabajo deben almacenarse en el historial de Git ni publicarse en GitHub.

El archivo `.gitignore` permite indicar a Git qué archivos o directorios debe **ignorar**, evitando que sean incluidos accidentalmente en los commits.

En esta práctica retomarás el repositorio creado en la práctica **[Introducción a Git](../../../practicas/01-entorno-y-reproducibilidad/git-colab-drive/05-introduccion-git.md)**, agregarás un archivo que no queremos versionar y configurarás `.gitignore` para excluirlo. Finalmente, publicarás el repositorio en GitHub y comprobarás qué archivos fueron incluidos.

---

## 🎯 Objetivo

Utilizar un archivo `.gitignore` para excluir archivos del control de versiones y comprobar que únicamente los archivos versionados forman parte del repositorio publicado en GitHub.

---

## 💻 Instrucciones

Utiliza el repositorio local creado durante la práctica
**Introducción a Git**.

Al comenzar, el proyecto deberá contener al menos:

```text
introduccion-git/
└── texto.txt
```

Abre nuevamente esta carpeta en **Visual Studio Code**.

---

### 1 · Comprueba el estado del repositorio

Abre la terminal integrada de VS Code y ejecuta:

```bash
git status
```

Antes de continuar, comprueba que no existan cambios pendientes.

Puedes consultar también el historial:

```bash
git log --oneline
```

Deberás encontrar los commits realizados durante la práctica anterior.

---

### 2 · Crea un archivo que no queremos versionar

En la raíz del proyecto crea un archivo llamado:

```text
archivo_no_versionable.txt
```

Puedes escribir dentro cualquier mensaje, por ejemplo:

```text
Este archivo no debe formar parte del repositorio.
```

Guarda el archivo.

La estructura será ahora:

```text
introduccion-git/
├── texto.txt
└── archivo_no_versionable.txt
```

Consulta el estado:

```bash
git status
```

### 🔎 Observa

Git detecta `archivo_no_versionable.txt` como un archivo nuevo que todavía no está siendo versionado.

Por el momento, **no ejecutes `git add`**.

---

### 3 · Crea `.gitignore`

En la raíz del proyecto crea un nuevo archivo llamado:

```text
.gitignore
```

La estructura será:

```text
introduccion-git/
├── texto.txt
├── archivo_no_versionable.txt
└── .gitignore
```

Dentro de `.gitignore` agrega:

```gitignore
archivo_no_versionable.txt
```

Guarda el archivo.

---

### 4 · Comprueba qué ocurrió

Consulta nuevamente:

```bash
git status
```

Observa los archivos que Git muestra.

`archivo_no_versionable.txt` ya no deberá aparecer como archivo pendiente de versionar.

En cambio, `.gitignore` sí aparecerá como un archivo nuevo.

> [!IMPORTANT]
> `.gitignore` **sí debe versionarse**.
>
> De esta forma, las reglas que indican qué debe ignorar Git también forman parte del proyecto y pueden compartirse con otras personas que utilicen el repositorio.

---

### 5 · Comprueba que Git está ignorando el archivo

Puedes pedir a Git que indique qué regla está provocando que el archivo sea ignorado:

```bash
git check-ignore -v archivo_no_versionable.txt
```

La salida mostrará la regla de `.gitignore` que coincide con el archivo.

> [!TIP]
> `git check-ignore` resulta útil cuando quieres comprobar por qué determinado archivo no aparece en `git status`.

---

### 6 · Agrega `.gitignore` al staging area

Agrega el archivo:

```bash
git add .gitignore
```

Consulta el estado:

```bash
git status
```

Observa que `.gitignore` se encuentra preparado para el siguiente commit, mientras que `archivo_no_versionable.txt` continúa fuera del control de versiones.

---

### 7 · Registra el cambio

Crea un nuevo commit:

```bash
git commit -m "Agrega archivo gitignore"
```

Comprueba nuevamente:

```bash
git status
```

Si no existen otros cambios pendientes, Git indicará que el directorio de trabajo está limpio.

---

## 🌐 Publica el repositorio en GitHub

Hasta este momento hemos trabajado con un **repositorio local**.

Ahora crearemos un repositorio remoto en GitHub y conectaremos ambos repositorios.

### 8 · Crea el repositorio en GitHub

En GitHub, crea un nuevo repositorio.

Puedes utilizar como nombre:

```text
introduccion-git
```

Para esta práctica, crea el repositorio **vacío**.

No agregues desde GitHub:

- `README`;
- `.gitignore`;
- licencia.

Estos archivos no son necesarios para realizar esta práctica y ya contamos con un repositorio Git local que contiene su propio historial.

Crea el repositorio.

---

### 9 · Copia la dirección SSH del repositorio

En la página del nuevo repositorio, selecciona:

**Code → SSH**

Copia la dirección SSH.

Tendrá una estructura similar a:

```text
git@github.com:usuario/introduccion-git.git
```

> [!NOTE]
> En la práctica de configuración SSH se preparó la autenticación entre esta computadora y GitHub. Ahora utilizaremos esa conexión para trabajar con el repositorio remoto.

---

### 10 · Agrega el repositorio remoto

Regresa a la terminal de VS Code.

Agrega el repositorio de GitHub como remoto con el nombre `origin`:

```bash
git remote add origin git@github.com:usuario/introduccion-git.git
```

Sustituye la dirección del ejemplo por la dirección SSH que copiaste desde tu propio repositorio.

Comprueba la configuración:

```bash
git remote -v
```

Deberás observar el remoto `origin` asociado con la dirección de GitHub.

---

### 11 · Comprueba el nombre de la rama

Consulta la rama actual:

```bash
git branch --show-current
```

Si la rama ya se llama:

```text
main
```

continúa con el siguiente paso.

Si tiene otro nombre y quieres utilizar `main`, puedes renombrarla:

```bash
git branch -M main
```

---

### 12 · Publica el repositorio

Envía el historial del repositorio local a GitHub:

```bash
git push -u origin main
```

La opción `-u` establece la relación entre la rama local `main` y la rama remota correspondiente.

Después de esta primera publicación, normalmente podrás enviar nuevos commits con:

```bash
git push
```

---

## 🔎 Comprueba el resultado en GitHub

### 13 · Revisa los archivos publicados

Actualiza la página del repositorio en GitHub.

Comprueba que aparece:

```text
texto.txt
```

y también:

```text
.gitignore
```

Ahora busca:

```text
archivo_no_versionable.txt
```

Este archivo **no deberá aparecer en GitHub**.

Sin embargo, si revisas la carpeta del proyecto en tu computadora, el archivo seguirá existiendo.

> [!IMPORTANT]
> `.gitignore` **no elimina archivos de la computadora**.
>
> Únicamente indica a Git qué archivos no debe comenzar a versionar cuando coinciden con sus reglas.

---

## 🤔 Observa e interpreta

A partir de lo realizado durante la práctica, reflexiona:

- ¿Qué ocurrió en `git status` después de crear `archivo_no_versionable.txt`?
- ¿Qué cambió después de agregar su nombre a `.gitignore`?
- ¿Por qué `.gitignore` sí debe formar parte del repositorio?
- ¿El archivo ignorado desapareció de tu computadora?
- ¿El archivo ignorado apareció en GitHub?
- ¿Qué relación existe entre el repositorio local y el repositorio remoto?
- ¿Qué función cumple `git push`?
- ¿Por qué puede ser importante definir qué archivos deben ignorarse antes de comenzar a trabajar con datasets, modelos o resultados grandes?

---

## ✅ Punto de control

Al finalizar esta práctica habrás practicado:

- crear un archivo `.gitignore`;
- definir una regla para ignorar un archivo;
- comprobar el efecto de `.gitignore` mediante `git status`;
- identificar qué regla ignora un archivo mediante `git check-ignore`;
- versionar y registrar `.gitignore`;
- crear un repositorio remoto en GitHub;
- conectar un repositorio local con un repositorio remoto;
- publicar commits mediante `git push`;
- comprobar qué archivos forman parte del repositorio publicado.

> [!TIP]
> Antes de ejecutar `git add`, utiliza:
>
> ```bash
> git status
> ```
>
> para revisar qué archivos está detectando Git. Esto ayuda a evitar que archivos que no deberían versionarse lleguen accidentalmente al repositorio.

---

[← Volver a Git, Github, Google Colab y Google Drive](../../../modulos/01-entorno-y-reproducibilidad/01-03-git-colab-drive.md)