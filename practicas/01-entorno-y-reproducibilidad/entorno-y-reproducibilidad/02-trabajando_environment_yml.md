# 📄 Trabajando con `environment.yml`

Hasta ahora hemos creado entornos indicando sus características directamente desde la terminal. Con Conda también podemos **describir un entorno en un archivo** llamado `environment.yml`. De esta manera, las dependencias y configuraciones necesarias quedan registradas y pueden utilizarse posteriormente para reconstruir el entorno.

---

## 👀 Ejemplo guiado

A continuación de presenta un ejemplo de uso de environment.yml. Es necesario que se utilice el mismo entorno en todos los ejercicios y que los pasos se sigan en el orden en que están establecidos.

### 1. Crear `environment.yml`

Crea un archivo llamado:

```text
environment.yml
```

y agrega el siguiente contenido:

```yaml
name: entorno-demo

channels:
  - conda-forge
  - defaults

dependencies:
  - python=3.11
  - matplotlib
```

> [!IMPORTANT]
> Verifica que la identación sea con espacios, no con tabuladores.

### 🔎 ¿Qué estamos declarando?

El archivo anterior describe tres elementos principales:

```text
environment.yml
│
├── name
│   └── entorno-demo
│
├── channels
│   └── conda-forge
│   └── defaults
│
└── dependencies
    ├── python=3.11
    ├── matplotlib
```

- **`name`** define el nombre que tendrá el entorno.
- **`channels`** indica dónde buscará Conda los paquetes.
- **`dependencies`** contiene los paquetes que deberán instalarse en el entorno.
- **`python=3.11`** indica además una versión específica de Python.

---

### 2. Crear el entorno

Abre una terminal **en la carpeta** donde se encuentra `environment.yml` y ejecuta:

```bash
conda env create -f environment.yml
```

Conda leerá el archivo y creará el entorno con las características que acabamos de declarar.

---

### 3. Activar el entorno

Una vez finalizada la creación, activa el entorno:

```bash
conda activate entorno-demo
```

---

### 4. Comprobar el entorno

Comprueba primero la versión de Python:

```bash
python --version
```

Después, consulta los paquetes instalados:

```bash
conda list
```

---

### 5. Actualizar el entorno a partir de `environment.yml`

Agrega `numpy` y `pandas` a la lista de dependencias de `environment.yml` y elimina `matplotlib`:

```yaml
name: entorno-demo

channels:
  - conda-forge
  - defaults

dependencies:
  - python=3.11
  - numpy
  - pandas
```

Guarda el archivo y ejecuta en la terminal:

```bash
conda env update -f environment.yml
```

Podemos verificar directamente que ambos paquetes se encuentran disponibles:

```bash
python -c "import numpy; import pandas; print('Entorno listo')"
```

Si el comando se ejecuta sin errores, Python ha podido importar ambos paquetes desde el entorno que acabamos de crear.

Verifica si `matplotlib` está enlistada en el entorno utilizando `conda list`.

---

### 6. Actualizar el entorno a partir de `environment.yml` y `--prune`

Elimina `pandas` en la lista de dependencias de `environment.yml`:

```yaml
name: entorno-demo

channels:
  - conda-forge
  - defaults

dependencies:
  - python=3.11
  - numpy
```

Guarda el archivo y ejecuta en la terminal:

```bash
conda env update -f environment.yml --prune
```

Verifica si `matplotlib` y `pandas` están listadas en el entorno utilizando `conda list`.

---

### 7. Exportar un entorno

Ejecuta en la terminal:

```bash
conda env export > environment_2.yml
```

Revisa el archivo `environment_2.yml`.

---

## ✅ Punto de control

Al finalizar estos ejercicios habrás practicado:

- reconocer la estructura básica de un archivo `environment.yml`;
- declarar el nombre, los canales y las dependencias de un entorno;
- crear un entorno a partir de un archivo YAML;
- activar el entorno;
- comprobar que sus dependencias están disponibles;
- actualizar el entorno a partir de su archivo `environment.yml`
- exportar el entorno.

---

[← Volver a Entorno y reproducibilidad](../../../modulos/01-entorno-y-reproducibilidad/01-01-entorno-y-reproducibilidad.md)