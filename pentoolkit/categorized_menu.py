"""Menú categorizado para las funciones de auditoría autorizada."""

from __future__ import annotations

import sys

from pentoolkit.modules.host_auditing import failed_logins, suspicious_processes
from pentoolkit.modules.network_auditing import active_connections
from pentoolkit.modules.reconnaissance import run_nmap, subdomain_enum, vuln_scan


def _run_action(action) -> None:
    try:
        action()
    except (FileNotFoundError, ValueError) as exc:
        print(f"Error: {exc}")


def reconnaissance_menu() -> None:
    while True:
        print("\n--- Reconocimiento ---")
        print("1. Escaneo Nmap")
        print("2. Enumeración de subdominios")
        print("0. Volver al menú principal")
        choice = input("Selecciona una opción: ").strip()
        if choice == "1":
            _run_action(run_nmap)
        elif choice == "2":
            _run_action(subdomain_enum)
        elif choice == "0":
            return
        else:
            print("Opción inválida.")


def vulnerability_menu() -> None:
    while True:
        print("\n--- Vulnerabilidades ---")
        print("1. Escaneo de vulnerabilidades con Nmap NSE")
        print("0. Volver al menú principal")
        choice = input("Selecciona una opción: ").strip()
        if choice == "1":
            _run_action(vuln_scan)
        elif choice == "0":
            return
        else:
            print("Opción inválida.")


def monitoring_menu() -> None:
    while True:
        print("\n--- Monitoreo ---")
        print("1. Intentos de login fallidos")
        print("2. Procesos del sistema")
        print("3. Conexiones activas")
        print("0. Volver al menú principal")
        choice = input("Selecciona una opción: ").strip()
        if choice == "1":
            _run_action(failed_logins)
        elif choice == "2":
            _run_action(suspicious_processes)
        elif choice == "3":
            _run_action(active_connections)
        elif choice == "0":
            return
        else:
            print("Opción inválida.")


def main_menu() -> None:
    while True:
        print("\n=== Pentoolkit ===")
        print("1. Reconocimiento")
        print("2. Vulnerabilidades")
        print("3. Monitoreo")
        print("0. Salir")
        choice = input("Selecciona una categoría: ").strip()
        if choice == "1":
            reconnaissance_menu()
        elif choice == "2":
            vulnerability_menu()
        elif choice == "3":
            monitoring_menu()
        elif choice == "0":
            print("Saliendo...")
            sys.exit(0)
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main_menu()
