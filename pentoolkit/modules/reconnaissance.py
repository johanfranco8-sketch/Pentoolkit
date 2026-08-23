"""Reconocimiento autorizado de dominios e infraestructura."""

from __future__ import annotations

from pathlib import Path

from pentoolkit.core.runner import run_command


def run_nmap() -> None:
    target = input("Objetivo autorizado (IP/dominio): ").strip()
    options = input("Opciones Nmap, separadas por espacios: ").split()
    if not target:
        print("El objetivo no puede estar vacío.")
        return
    run_command(["nmap", *options, target])


def subdomain_enum() -> None:
    target = input("Dominio autorizado: ").strip()
    if not target:
        print("El dominio no puede estar vacío.")
        return
    output = Path("subdomains.txt")
    run_command(["sublist3r", "-d", target, "-o", str(output)])
    print(f"Subdominios guardados en {output}")


def vuln_scan() -> None:
    target = input("IP o dominio autorizado: ").strip()
    if not target:
        print("El objetivo no puede estar vacío.")
        return
    run_command(["nmap", "-sV", "--script=vuln", target])
