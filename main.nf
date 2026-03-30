nextflow.enable.dsl=2

params.ruta   = params.ruta   ?: null
params.outdir = params.outdir ?: "results"

workflow {

    if (params.ruta == null)
        exit 1, "ERROR: Debes pasar la ruta con --ruta"

    Channel
        .value(params.ruta)
        .set { ch_ruta }

    analysis(ch_ruta)
}

process analysis {

    publishDir params.outdir, mode: 'copy'

    input:
    val ruta

    output:
    path "mapq_result.txt"

    script:
    """
    echo "Procesando archivo: $ruta"
    uv run ${projectDir}/main.py "$ruta" | tee mapq_result.txt
    """
}
