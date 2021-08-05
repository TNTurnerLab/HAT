<p align="center">
  <img width="300" height="300" src=https://github.com/TNTurnerLab/HAT/blob/main/doc/logo/small_logo_test_2.png>
</p>


Hare And Tortoise, HAT, are two _de novo_ variant callers developed by the Turner Lab.  Hare, as seen in Ng et al. 2021,  uses the software Parabricks, v3.0.0, by NVIDIA, that leverages GPUs to accelerate variant calling, specically for Haplotyecaller GATK 4.1.0 and DeepVariant v.10.0.  Tortoise uses freely avaiable, open source versions of the these variant callers.  We then use GLnexus to form family level joint-genotyped files to be run through our custom _de novo_ variant filter.

### Hare

Hare can be found [here](https://github.com/TNTurnerLab/GPU_accelerated_de_novo_workflow)

### Tortoise

The link to Tortoise can be found [here](https://github.com/TNTurnerLab/Tortoise).  Below you can find the comparison of the two workflows run on WGS 30x NA12878 sample from the 1000 Genomes Project and two monozygtoic twins, labelled here as twin 1 and twin 2.  Further details about these three samples can be found in Ng et. al.  

NA12878

![NA12878](https://github.com/TNTurnerLab/HAT/blob/main/doc/GPU_vs_CPU_NA12878.png)

Twin 1

![twin1](https://github.com/TNTurnerLab/HAT/blob/main/doc/GPU_vs_CPU_twin1.png)

Twin 2

![twin2](https://github.com/TNTurnerLab/HAT/blob/main/doc/GPU_vs_CPU_twin2.png)
