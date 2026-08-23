#!/usr/bin/env python3
"""Pentoolkit educativo para auditorías de seguridad autorizadas."""

from __future__ import annotations

import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Sequence

BASE_LOG_DIR = Path("logs")


def log_output(category: str, filename: str, command: Sequence[str]) -> None:
    """Ejecuta una herramienta y guarda stdout/stderr por categoría y fecha."""
    if not category or not filename or not command:
        raise ValueError("Categoría, nombre y comando son obligatorios")
    if shutil.which(command[0]) is None:
        raise FileNotFoundError(f"No se encontró la herramienta: {command[0]}")

    now = datetime.now()
    output_dir = BASE_LOG_DIR / category / now.strftime("%Y-%m-%d")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{filename}_{now.strftime('%H%M%S')}.txt"

    result = subprocess.run(list(command), capture_output=True, text=True, check=False)
    output_file.write_text(
        f"Comando: {' '.join(command)}\n"
        f"Fecha: {now.isoformat(timespec='seconds')}\n"
        f"Código de salida: {result.returncode}\n\n"
        "=== Salida estándar ===\n"
        f"{result.stdout}\n"
        "=== Errores ===\n"
        f"{result.stderr}\n",
        encoding="utf-8",
    )
    print(f"Resultados guardados en {output_file}")


def run_nmap() -> None:
    target = input("Objetivo autorizado (IP/Dominio): ").strip()
    options = input("Opciones Nmap: ").split()
    if target:
        log_output("reconocimiento", "nmap_scan", ["nmap", *options, target])
    else:
        print("El objetivo no puede estar vacío.")


def subdomain_enum() -> None:
    target = input("Dominio autorizado: ").strip()
    if target:
        log_output("reconocimiento", "subdomains", ["sublist3r", "-d", target])
    else:
        print("El dominio no puede estar vacío.")


def vuln_scan() -> None:
    target = input("IP o dominio autorizado: ").strip()
    if target:
        log_output("vulnerabilidades", "vuln_scan", ["nmap", "-sV", "--script=vuln", target])
    else:
        print("El objetivo no puede estar vacío.")


def failed_logins() -> None:
    log_file = Path(input("Ruta del log local: ").strip())
    try:
        with log_file.open(encoding="utf-8", errors="replace") as handle:
            matches = [line.rstrip() for line in handle if "Failed password" in line]
    except (FileNotFoundError, PermissionError) as exc:
        print(f"No se pudo leer el archivo: {exc}")
        return

    now = datetime.now()
    output_dir = BASE_LOG_DIR / "monitoreo" / now.strftime("%Y-%m-%d")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"failed_logins_{now.strftime('%H%M%S')}.txt"
    output_file.write_text(
        f"Archivo analizado: {log_file}\n"
        f"Fecha: {now.isoformat(timespec='seconds')}\n\n"
        + ("\n".join(matches) if matches else "No se encontraron coincidencias.")
        + "\n",
        encoding="utf-8",
    )
    print(f"Resultados guardados en {output_file}")


def suspicious_processes() -> None:
    log_output("monitoreo", "suspicious_processes", ["ps", "-U", "root", "-u", "root", "u"])


def active_connections() -> None:
    tool = "ss" if shutil.which("ss") else "netstat" if shutil.which("netstat") else None
    if tool is None:
        print("No se encontró ss ni netstat.")
        return
    log_output("monitoreo", "active_connections", [tool, "-ntu"])


def safe_action(action) -> None:
    try:
        action()
    except (FileNotFoundError, ValueError) as exc:
        print(f"Error: {exc}")


def reconnaissance_menu() -> None:
    while True:
        print("\n--- Reconocimiento ---")
        print("1. Escaneo Nmap")
        print("2. Enumeración de subdominios")
        print("0. Volver")
        choice = input("Selecciona una opción: ").strip()
        if choice == "1": safe_action(run_nmap)
        elif choice == "2": safe_action(subdomain_enum)
        elif choice == "0": return
        else: print("Opción inválida.")


def vulnerability_menu() -> None:
    while True:
        print("\n--- Vulnerabilidades ---")
        print("1. Escaneo de vulnerabilidades con Nmap NSE")
        print("0. Volver")
        choice = input("Selecciona una opción: ").strip()
        if choice == "1": safe_action(vuln_scan)
        elif choice == "0": return
        else: print("Opción inválida.")


def monitoring_menu() -> None:
    while True:
        print("\n--- Monitoreo ---")
        print("1. Intentos de login fallidos")
        print("2. Procesos del sistema")
        print("3. Conexiones activas")
        print("0. Volver")
        choice = input("Selecciona una opción: ").strip()
        if choice == "1": safe_action(failed_logins)
        elif choice == "2": safe_action(suspicious_processes)
        elif choice == "3": safe_action(active_connections)
        elif choice == "0": return
        else: print("Opción inválida.")


def main_menu() -> None:
    while True:
        print("\n=== Pentoolkit ===")
        print("1. Reconocimiento")
        print("2. Vulnerabilidades")
        print("3. Monitoreo")
        print("0. Salir")
        choice = input("Selecciona una categoría: ").strip()
        if choice == "1": reconnaissance_menu()
        elif choice == "2": vulnerability_menu()
        elif choice == "3": monitoring_menu()
        elif choice == "0":
            print("Saliendo...")
            sys.exit(0)
        else: print("Opción inválida.")


if __name__ == "__main__":
    main_menu()
