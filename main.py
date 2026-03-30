from rich.console import Console
from rich.table import Table
import re

def main():
    console = Console()

    # Pedimos el fichero al usuario (porque no podemos usar sys)
    sam_path = input("Introduce la ruta al archivo SAM: ").strip()

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

    # ==== FORMATO CON RICH ====

    table = Table(title="Resumen de Calidad de Alineamiento (MAPQ)")

    table.add_column("Métrica", justify="left", style="cyan", no_wrap=True)
    table.add_column("Valor", justify="right", style="bold white")

    table.add_row("Total de lecturas alineadas", str(total))
    table.add_row("Lecturas con MAPQ = 60", str(count_60))
    table.add_row("Porcentaje MAPQ=60", f"{percent:.2f}%")

    console.print("\n[bold green]✔ Análisis completado correctamente[/bold green]\n")
    console.print(table)

if __name__ == "__main__":
    main()
