# Pentoolkit

Toolkit educativo para auditorías de seguridad autorizadas en sistemas propios o con permiso escrito.

## Implementación del menú categorizado

El menú categorizado fue agregado correctamente en la rama `feature/categorized-menu`.

### Archivos incluidos

- `pentoolkit/categorized_menu.py`.
- `README.md` actualizado.

### Organización de herramientas

#### Reconocimiento

- Escaneo Nmap.
- Enumeración de subdominios.

#### Vulnerabilidades

- Escaneo mediante Nmap NSE.

#### Monitoreo

- Intentos de inicio de sesión fallidos.
- Procesos del sistema.
- Conexiones activas.

## Ejecución

```bash
python3 -m pentoolkit.categorized_menu
```

Los escaneos deben ejecutarse únicamente contra activos propios o cubiertos por autorización explícita y documentada.
