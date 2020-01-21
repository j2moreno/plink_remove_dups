# plink_remove_dups
Tool to remove duplicate snps inside of plink binary files bim, bed, and fam. Unlike using plink --list-duplicate-vars and --exlude to get rid of all snps that are duplicated, this tool keeps one copy of duplicated snps and removes the rest. This allows retenation of data without unncessary throwing it away.  

### Requiremnets 
- python 3
- bcftools
- plink 

### How to run

`python plink_remove_dups.py --bfile {plink_prefix} --out {output_prefix}` 
