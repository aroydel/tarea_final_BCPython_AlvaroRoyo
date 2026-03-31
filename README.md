# tarea_final_BCPython_AlvaroRoyo
Repositorio para la entrega de la tarea final del Curso de Biología Computacional del CSIC. Autor: Álvaro Royo.

# Analisis de Calidad de Alineamiento (MAPQ) – Proyecto Final

Este proyecto implementa un flujo completo para analizar ficheros SAM y obtener estadísticas de calidad de alineamiento (MAPQ) utilizando Python, uv, Rich, Nextflow DSL2 y un scripten bash main.sh.

## Objetivo del Proyecto

A partir de un fichero SAM, el script:
1. Ignora líneas de cabecera (@)
2. Extrae los valores de MAPQ
3. Cuenta el total de lecturas alineadas
4. Cuenta cuántas lecturas tienen MAPQ = 60
5. Calcula el porcentaje correspondiente
6. Muestra los resultados formateados con Rich
7. Guarda la misma tabla en mapq_result.txt

## Estructura del Proyecto

main.py
main.nf
main.sh
pyproject.toml
uv.lock
README.md
results/

## Dependencias
tener python y conda instalados
recomendado crear un conda environment limpio y activarlo:

conda create --name <environment-name>
conda activate environment-name

intalar Nextflow y uv en ese environment:

conda install -c bioconda nextflow
conda install -c conda-forge uv

sincronizar uc para respetar las dependencias (en nuestro caso "Rich")

uv sync

## Ejecución del pipeline

chmod +x main.sh
./main.sh

