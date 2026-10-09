# 1.3 · Git, Github, Google Colab y Google Drive

Hasta ahora hemos preparado un entorno de trabajo y organizado los archivos que forman parte de un proyecto. El siguiente paso es aprender a **registrar sus cambios, compartir el código y trabajar con recursos que pueden encontrarse fuera de nuestra computadora**.

En esta sección utilizaremos **Git** para llevar el control de versiones de un proyecto y **GitHub** para alojar y compartir repositorios de forma remota. También exploraremos **Google Colab** como entorno para ejecutar notebooks en la nube y **Google Drive** como espacio de almacenamiento persistente para nuestros archivos y datos.

De esta forma, distinguiremos dónde se encuentra el **código**, dónde se almacenan los **datos** y dónde se realiza la **ejecución**, tanto al trabajar localmente como en la nube.

### 📽️ Presentación

[**Ver presentación del tema →**](../../recursos/presentaciones/01-03-git-github-colab.pdf)

---

## 👤 Configuración de la identidad en Git

Antes de comenzar a registrar cambios, Git necesita saber **quién es el autor de los commits**.

Para ello se configuran dos datos:

- `user.name` → nombre que aparecerá como autor de los commits;
- `user.email` → correo asociado a los commits.

> [!IMPORTANT]
> Esta configuración identifica al **autor de los commits**.
> No es el mecanismo utilizado para iniciar sesión o autenticarse con GitHub.

### Configuración global

Si deseas utilizar la misma identidad en **todos los repositorios de tu usuario en esta computadora**, ejecuta:

```powershell
git config --global user.name "Nombre"
git config --global user.email "correo@ejemplo.com"
```

La opción `--global` indica que esta configuración se utilizará de forma predeterminada en los repositorios de tu usuario.

### Configuración para un repositorio específico

También es posible utilizar una identidad diferente únicamente en el repositorio actual.

Desde la carpeta del repositorio ejecuta:

```powershell
git config user.name "Nombre"
git config user.email "correo@ejemplo.com"
```

La configuración local del repositorio tendrá prioridad sobre la configuración global.

### ¿Qué correo utilizar?

Puedes utilizar el correo asociado a tu cuenta de GitHub.

Si prefieres **no mostrar públicamente tu dirección de correo personal** en los commits, GitHub proporciona una dirección de correo privada de tipo `noreply`.

Para utilizarla:

1. Abre **GitHub**.
2. Ve a **Settings**.
3. Selecciona **Emails**.
4. Activa:

   **Keep my email addresses private**

GitHub mostrará la dirección privada que puedes utilizar para tus commits.

Tendrá un formato similar a:

```text
ID+usuario@users.noreply.github.com
```

Utiliza **exactamente la dirección que GitHub muestre en tu configuración**.

Después puedes configurarla en Git:

```powershell
git config --global user.email "ID+usuario@users.noreply.github.com"
```

> [!TIP]
> Utilizar el correo `noreply` permite asociar los commits con tu cuenta de GitHub sin publicar tu dirección de correo personal.

### Comprueba la configuración

Para consultar la configuración global de Git:

```powershell
git config --global --list
```

Busca las entradas correspondientes a:

```text
user.name=Nombre
user.email=correo
```

También puedes consultar cada valor individualmente:

```powershell
git config --global user.name
git config --global user.email
```

---

## 📦 ¿Qué versionar?

No todos los archivos de un proyecto necesitan formar parte del repositorio.

Git resulta especialmente útil para conservar los archivos necesarios para **comprender, modificar y reproducir el proyecto**. Sin embargo, algunos archivos pueden ser demasiado grandes, generarse automáticamente o contener información que no debe publicarse.

Consideremos una estructura de proyecto como la siguiente:

```text
proyecto/
├── data/
├── notebooks/
├── src/
├── configs/
├── models/
├── results/
├── environment.yml
├── README.md
└── .gitignore
```

¿Qué elementos conviene versionar?

| Elemento del proyecto | ¿Versionar? | ¿Por qué? |
|---|:---:|---|
| `src/` | ✅ **Sí** | Contiene el **código fuente** necesario para ejecutar y reproducir el proyecto. |
| `notebooks/` | ✅ **Sí** | Conserva los notebooks utilizados para exploración, experimentación y análisis. |
| `configs/` | ✅ **Sí** | Guarda parámetros y archivos de configuración necesarios para reproducir experimentos. |
| `environment.yml` | ✅ **Sí** | Permite reconstruir el **entorno de trabajo y sus dependencias**. |
| `README.md` | ✅ **Sí** | Documenta el proyecto, su estructura y las instrucciones para utilizarlo. |
| `.gitignore` | ✅ **Sí** | Indica qué archivos o directorios Git debe ignorar. |
| `data/` → archivos pequeños de ejemplo | 🟡 **Depende** | Pueden incluirse cuando son necesarios para demostrar, probar o comprender el funcionamiento del proyecto. |
| `data/` → datasets grandes | ❌ **No** | Pueden ocupar varios GB y hacer que el repositorio sea innecesariamente pesado. |
| `models/` → modelos pequeños necesarios | 🟡 **Depende** | Pueden conservarse cuando son pequeños y necesarios para utilizar o demostrar el proyecto. |
| `models/` → checkpoints o pesos grandes | ❌ **Generalmente no** | Los modelos entrenados pueden ocupar cientos de MB o varios GB. |
| `results/` → métricas, tablas o resultados pequeños | 🟡 **Depende** | Pueden conservarse cuando documentan resultados importantes del experimento. |
| `results/` → salidas masivas | ❌ **Generalmente no** | Predicciones, imágenes generadas y resultados intermedios pueden ocupar mucho espacio. |
| archivos temporales o caché | ❌ **No** | Se generan automáticamente y no son necesarios para reproducir el proyecto. |
| archivos del sistema (`.DS_Store`, etc.) | ❌ **No** | Son archivos generados por el sistema operativo y no forman parte del proyecto. |
| credenciales, contraseñas, API keys o tokens | 🚫 **Nunca** | Contienen información sensible que no debe almacenarse en Git ni publicarse en GitHub. |

> [!TIP]
> Antes de agregar un archivo al repositorio, pregúntate:
>
> **¿Este archivo es necesario para comprender, ejecutar o reproducir el proyecto?**
>
> Si la respuesta es **sí**, probablemente conviene versionarlo.
>
> Si es un archivo **grande, generado automáticamente, temporal o sensible**, probablemente no debe formar parte del repositorio.

### Una regla importante

No siempre es necesario ignorar una carpeta completa.

Por ejemplo, `data/`, `models/` y `results/` pueden contener algunos archivos que sí queremos conservar y otros que no. La decisión depende del **contenido** y del propósito que tenga dentro del proyecto.

Para indicar a Git qué archivos no queremos versionar podemos utilizar un archivo llamado:

```text
.gitignore
```

---

## 🧪 Prácticas

1. [Introducción a Introducción a Git →](../../practicas/01-entorno-y-reproducibilidad/git-colab-drive/05-introduccion-git.md)
2. [Configuración de la conexión SSH con GitHub →](../../practicas/01-entorno-y-reproducibilidad/git-colab-drive/06-configuracion-conexion-github.md)
3. [Introducción a .gitignore →](../../practicas/01-entorno-y-reproducibilidad/git-colab-drive/07-introduccion-gitignore.md)
4. [Introducción a Google Colab desde VS Code →](../../practicas/01-entorno-y-reproducibilidad/git-colab-drive/08-introduccion-vscode-colab.md)
5. [Conexión entre Google Colab, GitHub y Google Drive →](../../practicas/01-entorno-y-reproducibilidad/git-colab-drive/09-conexion-colab-github-drive.md)
---

## ➡️ Completa el reto del módulo

[Encuentra al gato →](../../practicas/01-entorno-y-reproducibilidad/10-reto-modulo-1.md)

---
[← Volver a página anterior](./01-02-directorio-trabajo-y-tipos-rutas.md)

[← Volver al índice de módulos](../modulos.md)

[← Volver a la portada del taller](../../README.md)