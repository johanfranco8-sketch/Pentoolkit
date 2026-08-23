"""Auditoría de señales locales del sistema."""

from __future__ import annotations

from pathlib import Path

from pentoolkit.core.runner import run_command


def failed_logins() -> None:
    log_file = Path(input("Ruta del log local: ").strip())
    try:
        with log_file.open(encoding="utf-8", errors="replace") as handle:
            for line in handle:
                if "Failed password" in line:
                    print(line.strip())
    except (FileNotFoundError, PermissionError) as exc:
        print(f"No se pudo leer el archivo: {exc}")


def suspicious_processes() -> None:
    run_command(["ps", "-U", "root", "-u", "root", "u"])
