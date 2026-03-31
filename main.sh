#!/usr/bin/env bash

echo -n "Introduce la ruta al archivo SAM: "
read SAM

nextflow run main.nf --ruta "$SAM"

cat ./results/mapq_result.txt
