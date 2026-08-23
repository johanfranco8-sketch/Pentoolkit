"""Ejecución controlada de herramientas del sistema."""

from __future__ import annotations

import shutil
import subprocess
from collections.abc import Sequence


def run_command(command: Sequence[str]) -> int:
    if not command:
        raise ValueError("El comando no puede estar vacío")
    if shutil.which(command[0]) is None:
        raise FileNotFoundError(f"No se encontró la herramienta: {command[0]}")
    result = subprocess.run(list(command), check=False)
    return result.returncode
