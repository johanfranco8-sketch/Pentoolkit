"""Punto de entrada del menú interactivo."""

from __future__ import annotations

import sys

from pentoolkit.modules.host_auditing import failed_logins, suspicious_processes
from pentoolkit.modules.network_auditing import active_connections
from pentoolkit.modules.reconnaissance import run_nmap, subdomain_enum, vuln_scan


def menu() -> None:
    while True:
        print("\n=== Pentoolkit Menu ===")
        print("1. Escaneo Nmap")
        print("2. Enumeración de subdominios")
        print("3. Escaneo de vulnerabilidades")
        print("4. Intentos de login fallidos")
        print("5. Procesos del sistema")
        print("6. Conexiones activas")
        print("0. Salir")
        choice = input("Selecciona una opción: ").strip()
        actions = {"1": run_nmap, "2": subdomain_enum, "3": vuln_scan, "4": failed_logins, "5": suspicious_processes, "6": active_connections}
        if choice == "0":
            print("Saliendo...")
            sys.exit(0)
        action = actions.get(choice)
        if action is None:
            print("Opción inválida, intenta de nuevo.")
            continue
        try:
            action()
        except (FileNotFoundError, ValueError) as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    menu()
