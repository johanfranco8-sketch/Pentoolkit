# Pentoolkit

Toolkit educativo para auditorías de seguridad autorizadas en sistemas propios o con permiso escrito.

## Historial de resultados

Cada ejecución guarda automáticamente stdout, stderr, fecha, comando y código de salida en:

```text
logs/<categoría>/<YYYY-MM-DD>/<herramienta>_<HHMMSS>.txt
```

Categorías actuales: `reconocimiento`, `vulnerabilidades` y `monitoreo`.

## Implementación realizada

El archivo `pentoolkit.py` ahora:

- Guarda automáticamente los resultados de cada ejecución.
- Crea carpetas por categoría y fecha.
- Registra el comando ejecutado, fecha y hora, código de salida, salida estándar y errores producidos.
- Utiliza ejecución de procesos sin `shell=True`.
- Incluye el menú categorizado: Reconocimiento, Vulnerabilidades y Monitoreo.
- Maneja errores cuando faltan herramientas como `nmap`, `sublist3r`, `ss` o `netstat`.

Estructura generada:

```text
logs/
├── reconocimiento/
│   └── YYYY-MM-DD/
├── vulnerabilidades/
│   └── YYYY-MM-DD/
└── monitoreo/
    └── YYYY-MM-DD/
```

Para ejecutarlo desde esa rama:

```bash
git checkout feature/organized-results
chmod +x pentoolkit.py
python3 pentoolkit.py
```

## Uso responsable

Los escaneos deben ejecutarse únicamente contra activos propios o cubiertos por autorización explícita y documentada. Los archivos de `logs/` pueden contener información sensible; no los publiques ni los subas a repositorios sin revisar su contenido.
