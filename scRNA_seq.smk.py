# snakemake with scRNA-seq
# 2022-3-13



csv = "/home/luotao/c_elegans/yard/run_cellranger_mkfastq/cellranger-tiny-bcl-simple-1.2.0.csv"


rule matrix_barcode_feature:
    input:
        "matrix_barcode_feature"

# bcl2fastq
rule bcl2fastq_cellrange_mkfastq:
    input:
        "/home/luotao/c_elegans/yard/run_cellranger_mkfastq/cellranger-tiny-bcl-1.2.0/"
    output:
        "output_fastq_out"
    
    shell:
        "cellranger mkfastq --id={output} --run={input} --csv={csv}"
    
rule fastq2matrix_cellrange_count:
    input:
        "output_fastq_out"
        
    output:
        "matrix_barcode_feature"
        
    shell:
    # sample 如果FASTQ目录中有多个样例，则使用——sample参数指定使用哪个样例  
        "cellranger count --id={output}  \
        --fastqs={input} \
        --sample=fastq.gz  \
        --transcriptome=/home/luotao/c_elegans/yard/run_cellranger_count/refdata-gex-GRCh38-2020-A/"






