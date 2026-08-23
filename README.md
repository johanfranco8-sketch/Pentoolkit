# Pentoolkit

Toolkit educativo para auditorías de seguridad autorizadas en sistemas propios o con permiso escrito.

## Estructura

- `pentoolkit/main.py`: punto de entrada y menú.
- `pentoolkit/modules/reconnaissance.py`: reconocimiento autorizado con Nmap y Sublist3r.
- `pentoolkit/modules/host_auditing.py`: revisión local de intentos fallidos y procesos.
- `pentoolkit/modules/network_auditing.py`: resumen local de conexiones activas.
- `pentoolkit/core/runner.py`: ejecución segura de comandos externos.

## Instalación

Se requiere Python 3.10 o superior y, según la función utilizada, Nmap, Sublist3r y herramientas del sistema.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m pentoolkit.main
```

## 🚀 Cómo usarlo

Guarda el archivo como `pentoolkit.py`.

Dale permisos de ejecución:

```bash
chmod +x pentoolkit.py
```

Ejecútalo:

```bash
python3 pentoolkit.py
```

Navega por el menú y selecciona la herramienta que quieras usar.

> Nota: en la estructura modular actual, el punto de entrada recomendado es `python3 -m pentoolkit.main`. Ejecuta herramientas de red únicamente contra sistemas propios o con autorización explícita.

## 🔧 Pasos para crear alias

### 1. Abrir tu archivo de configuración de shell

Si usas Bash (por defecto en Kali):

```bash
nano ~/.bashrc
```

Si usas Zsh:

```bash
nano ~/.zshrc
```

### 2. Agregar alias personalizados

Dentro del archivo, al final, añade líneas como estas:

```bash
# Alias para Pentoolkit
alias pentoolkit="python3 ~/pentest-scripts/pentoolkit.py"

# Alias para escaneo rápido de puertos
alias quickscan="python3 ~/pentest-scripts/reconnaissance/nmap_scan.py"

# Alias para ver procesos sospechosos
alias suspicious="bash ~/pentest-scripts/monitoring/suspicious_processes.sh"
```

### 3. Guardar y recargar configuración

Después de editar, guarda con `CTRL+O`, sal con `CTRL+X` y recarga:

```bash
source ~/.bashrc
```

En Zsh, recarga con:

```bash
source ~/.zshrc
```

### 4. Usar tus alias

Ahora puedes ejecutar directamente:

```bash
pentoolkit
quickscan
suspicious
```

### 📌 Tip avanzado

Si quieres tener todos tus scripts accesibles con un solo alias, puedes crear uno que liste y ejecute:

```bash
alias pentools="cd ~/pentest-scripts && ls"
```

Al escribir `pentools`, entrarás a tu carpeta y verás todos los scripts disponibles.

> Usa estos alias únicamente con herramientas y objetivos autorizados. Revisa las rutas de los scripts antes de ejecutarlos.

## Uso responsable

Ejecuta escaneos únicamente contra activos propios o cubiertos por una autorización explícita y documentada. Define alcance, fechas, técnicas permitidas y contactos de emergencia antes de realizar una prueba. No uses este proyecto para evadir controles, acceder a cuentas, interrumpir servicios o analizar terceros sin autorización.

## Limitaciones

Las funciones de red ejecutan herramientas externas y sus resultados dependen de las utilidades instaladas y de los permisos del sistema. El módulo de logs y procesos está diseñado para auditoría local.
