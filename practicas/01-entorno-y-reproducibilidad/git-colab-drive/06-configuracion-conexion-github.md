# 🔐 Configuración de la conexión SSH con GitHub

Para trabajar con repositorios remotos necesitamos un mecanismo que permita a GitHub reconocer de forma segura nuestra computadora.

En esta práctica configurarás una conexión mediante **SSH (Secure Shell)**.
Para ello, generarás un par de claves: una **clave privada**, que permanecerá en tu computadora, y una **clave pública**, que agregarás a tu cuenta de
GitHub. Después, configurarás SSH para utilizar esta clave y comprobarás que la autenticación funciona correctamente.

---

## 🎯 Objetivo

Configurar la autenticación mediante **SSH** entre una computadora con Windows y GitHub, utilizando un par de claves pública y privada, y verificar que la conexión se haya establecido correctamente.

---

## 💻 Instrucciones

Realiza los siguientes pasos desde **PowerShell**.

Durante la práctica generarás archivos dentro del directorio `.ssh` de tu usuario y agregarás una clave pública a tu cuenta de GitHub.

> [!IMPORTANT]
> Durante este procedimiento se generarán dos claves:
>
> - 🔐 **Clave privada** → permanece únicamente en tu computadora.
> - 🔓 **Clave pública** → se agrega a tu cuenta de GitHub.
>
> **La clave privada nunca debe compartirse ni publicarse.**

---

### 1 · Comprueba el directorio `.ssh`

Las claves SSH normalmente se almacenan dentro del directorio:

```text
~/.ssh
```

En **PowerShell**, comprueba si ya existe:

```powershell
Get-ChildItem ~/.ssh
```

Si PowerShell indica que el directorio no existe, créalo:

```powershell
New-Item -ItemType Directory -Path "$HOME/.ssh"
```

> [!IMPORTANT]
> Si `.ssh` ya existe, no es necesario volver a crearlo.
> Tampoco elimines las claves que ya se encuentren dentro de este directorio.

---

### 2 · Genera una clave SSH

Crea un nuevo par de claves utilizando el algoritmo **Ed25519**:

```powershell
ssh-keygen -t ed25519 -C "correo@ejemplo.com" -f "$HOME/.ssh/id_ed25519_github"
```

La opción:

```text
-C "correo@ejemplo.com"
```

agrega un comentario a la clave que ayuda a **identificarla**.

Para mantener una identificación consistente con tu cuenta de GitHub, puedes utilizar el correo asociado a la cuenta.

Si activaste:

**Settings → Emails → Keep my email addresses private**

también puedes utilizar la dirección `noreply` proporcionada por GitHub:

```powershell
ssh-keygen -t ed25519 -C "ID+usuario@users.noreply.github.com" -f "$HOME/.ssh/id_ed25519_github"
```

> [!NOTE]
> El correo utilizado con `-C` funciona como una **etiqueta o comentario de
> identificación de la clave**. No es una contraseña ni es lo que autentica
> la conexión con GitHub.

Durante la creación de la clave aparecerá:

```text
Enter passphrase (empty for no passphrase):
```

Escribe una contraseña (*passphrase*) para proteger tu clave privada y presiona **Enter**.

Después se solicitará confirmarla:

```text
Enter same passphrase again:
```

Escribe nuevamente la misma contraseña.

Al finalizar se crearán dos archivos:

```text
id_ed25519_github
id_ed25519_github.pub
```

| Archivo | Tipo | ¿Se comparte? |
|---|---|:---:|
| `id_ed25519_github` | 🔐 Clave privada | 🚫 **Nunca** |
| `id_ed25519_github.pub` | 🔓 Clave pública | ✅ Sí |

---

### 3 · Muestra y copia la clave pública

Para mostrar el contenido de la clave pública ejecuta:

```powershell
Get-Content ~/.ssh/id_ed25519_github.pub
```

La salida tendrá una estructura similar a:

```text
ssh-ed25519 AAAA... correo@ejemplo.com
```

Copia **toda la línea**.

> [!WARNING]
> Verifica que estás copiando el contenido del archivo terminado en `.pub`.
> La clave privada `id_ed25519_github` nunca debe compartirse.

---

### 4 · Agrega la clave pública a GitHub

En tu cuenta de GitHub:

1. Abre **Settings**.
2. Selecciona **SSH and GPG keys**.
3. Selecciona **New SSH key**.
4. En **Title**, escribe un nombre que permita identificar la computadora,
   por ejemplo:

   ```text
   Laptop Windows
   ```

5. En **Key type**, conserva:

   ```text
   Authentication Key
   ```

6. En **Key**, pega la línea completa que copiaste de:

   ```text
   id_ed25519_github.pub
   ```

7. Selecciona **Add SSH key**.

De esta forma, GitHub tendrá la **clave pública**, mientras que la clave privada permanecerá almacenada únicamente en tu computadora.

---

### 5 · Configura qué clave utilizar con GitHub

Ahora indicaremos a SSH qué clave privada debe utilizar cuando se conecte con GitHub.

Abre el archivo de configuración SSH desde PowerShell:

```powershell
code $HOME\.ssh\config
```

Si el archivo todavía no existe, code abrirá en VS Code un archivo para guardarlo en la posición $HOME\.ssh, una vez modificado, se debe guardar.

Agrega:

```text
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_github
    IdentitiesOnly yes
```

Guarda el archivo y ciérralo.

Esta configuración indica que cuando SSH intente conectarse con:

```text
github.com
```

deberá utilizar la clave privada:

```text
~/.ssh/id_ed25519_github
```

> [!IMPORTANT]
> `IdentityFile` debe apuntar a la **clave privada**:
>
> ```text
> id_ed25519_github
> ```
>
> y no al archivo de clave pública:
>
> ```text
> id_ed25519_github.pub
> ```

---

### 6 · Verifica la conexión con GitHub

Desde PowerShell ejecuta:

```powershell
ssh -T git@github.com
```

La primera vez que te conectes a GitHub desde esta computadora puede aparecer un mensaje solicitando confirmar la identidad del servidor.

Después de verificar que se trata de GitHub, escribe:

```text
yes
```

Si protegiste tu clave con una *passphrase*, también puede solicitarla.

Cuando la autenticación sea correcta, aparecerá un mensaje similar a:

```text
Hi usuario! You've successfully authenticated, but GitHub does not provide shell access.
```

Esto confirma que GitHub pudo autenticar la conexión mediante tu clave SSH.

---

## 🤔 Observa e interpreta

Al finalizar la configuración, identifica:

- ¿qué archivo corresponde a la **clave privada**?
- ¿qué archivo corresponde a la **clave pública**?
- ¿cuál de las dos claves se agregó a GitHub?
- ¿cuál permanece únicamente en tu computadora?
- ¿qué función cumple el archivo `~/.ssh/config`?
- ¿qué comprueba el comando `ssh -T git@github.com`?

---

## ✅ Punto de control

Al finalizar esta práctica habrás:

- identificado el directorio utilizado para almacenar las claves SSH;
- generado un par de claves pública y privada;
- protegido la clave privada mediante una *passphrase*;
- agregado una clave pública a tu cuenta de GitHub;
- configurado la clave que SSH utilizará para conectarse con GitHub;
- comprobado la autenticación mediante SSH.

> [!IMPORTANT]
> Recuerda que la **clave pública puede compartirse**, pero la **clave privada debe permanecer siempre protegida en tu computadora**.

---

[← Volver a Git, Github, Google Colab y Google Drive](../../../modulos/01-entorno-y-reproducibilidad/01-03-git-colab-drive.md)