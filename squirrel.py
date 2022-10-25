import os
from argparse import ArgumentParser

parser = ArgumentParser(description='Grab info for filter')
parser.add_argument('-p','--path',help='Path to out folder',required=True)
args = parser.parse_args()
if args.path.endswith('/'):
    pathway=args.path[:-1]
files=os.listdir(args.path)
holdme=[]
with open('combined_dnv_information.txt','w') as out:
    out.write('SAMPLE\tCHROM\tPOS_B38\tREFERENCE\tALTERNATE\tID\n')
    for file in files:
        vcfpath=pathway+'/'+file+'/'+file+'.glnexus.family.combined_intersection_filtered_gq_20_depth_10_position.vcf' 
        with open(vcfpath) as input:
            
            sample=vcfpath.split('/')[-1].split('.')[0]
            for line in input:
                if not line.startswith("#"):
                    out.write(sample+'\t')
                    data=line.strip().split('\t')
                    out.write(data[0]+'\t'+data[1]+'\t'+data[3]+'\t'+data[4]+'\t'+data[2]+'\n')
                    