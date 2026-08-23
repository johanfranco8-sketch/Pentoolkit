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

## Uso responsable

Ejecuta escaneos únicamente contra activos propios o cubiertos por una autorización explícita y documentada. Define alcance, fechas, técnicas permitidas y contactos de emergencia antes de realizar una prueba. No uses este proyecto para evadir controles, acceder a cuentas, interrumpir servicios o analizar terceros sin autorización.

## Limitaciones

Las funciones de red ejecutan herramientas externas y sus resultados dependen de las utilidades instaladas y de los permisos del sistema. El módulo de logs y procesos está diseñado para auditoría local.
