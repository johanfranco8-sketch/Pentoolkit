"""Auditoría local de conexiones activas."""

from __future__ import annotations

import shutil
import subprocess


def active_connections() -> None:
    if shutil.which("ss"):
        result = subprocess.run(["ss", "-ntu"], capture_output=True, text=True, check=False)
        print(result.stdout)
        return
    if shutil.which("netstat"):
        result = subprocess.run(["netstat", "-ntu"], capture_output=True, text=True, check=False)
        print(result.stdout)
        return
    print("No se encontró ss ni netstat.")
