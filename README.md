<p align="center">
  <img width="300" height="300" src=https://github.com/TNTurnerLab/HAT/blob/main/doc/logo/small_logo_test_2.png>
</p>


Hare And Tortoise, HAT, are two _de novo_ variant callers developed by the Tychele N. Turner Lab at Washington University in St. Louis Medical School.  Hare, as seen in [Ng et al. 2022](https://doi.org/10.1002/humu.24455),  uses the software Parabricks, v4.0.0-1, by NVIDIA, that leverages GPUs to accelerate variant calling, specifically for Haplotyecaller GATK 4.2.0 and DeepVariant v1.4.0.  Tortoise uses freely available, open source versions of the these variant callers.  We then use GLnexus to form family level joint-genotyped files to be run through our custom _de novo_ variant filter.

## Hare

The original code used for Ng et al. (Hare v1.0) can be found [here.](https://github.com/TNTurnerLab/GPU_accelerated_de_novo_workflow)

The updated Hare, v1.2, workflow can be found [here.](https://github.com/TNTurnerLab/Hare).  This workflow is effective for WGS and WES data only.  

## Tortoise

The link to Tortoise can be found [here](https://github.com/TNTurnerLab/Tortoise).  Below you can find the comparison of the two workflows run on WGS 30x NA12878 sample from the 1000 Genomes Project and two monozygotic twins, labelled here as twin 1 and twin 2.  Further details about these three samples can be found in Ng et. al.  This workflow is effect for WGS, WES and PacBio data.

## Acorn

If you would like to do some followup statistics on the output from HAT, you can install the R package acorn, [found here.](https://github.com/TNTurnerLab/acorn)  To prep the output from HAT, you can run squirrel.py found here in this repo.

## Hare vs Tortoise comparisons

### NA12878

![NA12878](https://github.com/TNTurnerLab/HAT/blob/main/doc/hare1.0_vs_tortoise_1.1_NA12878.png)

### Twin 1

![twin1](https://github.com/TNTurnerLab/HAT/blob/main/doc/hare1.0_vs_tortoise1.1_twin1.png)

### Twin 2

![twin2](https://github.com/TNTurnerLab/HAT/blob/main/doc/hare1.0_vs_tortoise1.1_twin2.png)



