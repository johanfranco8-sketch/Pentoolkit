# Pentoolkit

Toolkit educativo para auditorías de seguridad autorizadas en sistemas propios o con permiso escrito.

## Estructura

- `pentoolkit.py`: menú independiente con historial de resultados.
- `pentoolkit/main.py`: punto de entrada modular.
- `pentoolkit/modules/`: módulos de reconocimiento, auditoría local y red.
- `pentoolkit/core/`: componentes centrales.
- `logs/`: resultados locales generados durante las ejecuciones; no debe publicarse si contiene información sensible.

## Instalación

### Linux (Bash/Kali)

Debes ejecutar los comandos desde la carpeta raíz del repositorio, es decir, la carpeta que contiene `requirements.txt` y el directorio `pentoolkit/`.

```bash
git clone https://github.com/johanfranco8-sketch/Pentoolkit.git
cd Pentoolkit

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

Comprueba que estás en la ubicación correcta:

```bash
pwd
ls
test -f requirements.txt && echo "requirements.txt encontrado"
test -d pentoolkit && echo "paquete pentoolkit encontrado"
which python3
python3 -c 'import sys; print(sys.executable)'
```

> Si `pip` muestra `No such file or directory: requirements.txt`, estás en una carpeta incorrecta o el archivo no existe en tu copia local. Ejecuta `pwd` y `ls`, y vuelve a entrar en la raíz del repositorio con `cd`.

## Ejecución en Linux

Menú modular:

```bash
python3 -m pentoolkit.main
```

Archivo independiente:

```bash
chmod +x pentoolkit.py
python3 pentoolkit.py
```

> Si aparece `ModuleNotFoundError: No module named 'pentoolkit'`, verifica que el entorno esté activado, que estés en la raíz del repositorio y que exista el directorio `pentoolkit/`. El comando `python3 -m pentoolkit.main` debe ejecutarse desde esa raíz.

## Instalación en Windows

En PowerShell, abre la carpeta raíz del repositorio:

```powershell
git clone https://github.com/johanfranco8-sketch/Pentoolkit.git
Set-Location Pentoolkit

py -m venv .venv
.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
```

Ejecuta el menú modular:

```powershell
py -m pentoolkit.main
```

O el archivo independiente:

```powershell
py pentoolkit.py
```

Si PowerShell bloquea la activación durante la sesión actual:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

## Herramientas externas

Las funciones de reconocimiento requieren que `nmap` y, para enumeración de subdominios, `sublist3r` estén instalados y disponibles en `PATH`. Las funciones locales pueden usar `ps`, `ss` o `netstat` según el sistema.

## Historial de resultados

El archivo `pentoolkit.py` guarda los resultados en:

```text
logs/<categoría>/<YYYY-MM-DD>/<herramienta>_<HHMMSS>.txt
```

Los registros pueden contener direcciones IP, nombres de host, rutas y otra información sensible. Revísalos antes de compartirlos o subirlos a GitHub.

## Alias de shell

Los alias de Bash/Zsh solo funcionarán si las rutas apuntan a tu copia local real. Por ejemplo, desde una instalación en `~/Pentoolkit`:

```bash
alias pentoolkit="python3 ~/Pentoolkit/pentoolkit.py"
alias pentools="cd ~/Pentoolkit && ls"
```

Recarga Bash con:

```bash
source ~/.bashrc
```

Recarga Zsh con:

```bash
source ~/.zshrc
```

## Uso responsable

Ejecuta escaneos únicamente contra activos propios o cubiertos por una autorización explícita y documentada. Define alcance, fechas, técnicas permitidas y contactos de emergencia antes de realizar una prueba. No uses este proyecto para evadir controles, acceder a cuentas, interrumpir servicios o analizar terceros sin autorización.
