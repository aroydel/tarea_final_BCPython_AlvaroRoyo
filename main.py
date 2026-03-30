#!/usr/bin/env python3

import re
import sys
from rich.console import Console
from rich.table import Table

def main():

    # Comprobar que se pasa la ruta al SAM
    if len(sys.argv) < 2:
        print("Uso: uv run main.py <archivo.sam>")
        sys.exit(1)

    sam_path = sys.argv[1]

    console = Console()

    total = 0
    count_60 = 0

    with open(sam_path, "r") as f:
        for line in f:
            if line.startswith("@"):
                continue

            cols = re.split(r"\t", line.strip())
            if len(cols) < 5:
                continue

            mapq = int(cols[4])

            total += 1
            if mapq == 60:
                count_60 += 1

    percent = (count_60 / total) * 100 if total > 0 else 0

    # Crear tabla con Rich
    table = Table(title="Resumen de Calidad de Alineamiento (MAPQ)")
    table.add_column("Métrica", style="cyan")
    table.add_column("Valor", style="bold white")

    table.add_row("Total de lecturas alineadas", str(total))
    table.add_row("Lecturas con MAPQ = 60", str(count_60))
    table.add_row("Porcentaje MAPQ=60", f"{percent:.2f}%")

    # Mostrar en consola
    console.print(table)

if __name__ == "__main__":
    main()
