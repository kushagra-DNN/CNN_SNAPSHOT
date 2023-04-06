import os, sys, glob
import os.path
from rdkit import *
from rdkit import Chem
from rdkit.Chem import AllChem
import pandas as pd 
import numpy as np
import argparse
import sys
import sys, getopt

print ('smiles_to_pdb.py -i <InputSmilesfile> -o <pdbfilelocation>')
print ("-i is train/active/inactive/pi or test/active/inactive/pi smiles file and -o is directory where pdbfiles will be generated" )
print ("change -i for train/test actives/inactives/pi")

def main(argv):
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    for opt, arg in opts:
      if opt == '-h':
         print ('smiles_to_pdb.py -i <InputSmilesfile> -o <pdbfilelocation>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         InputSmilesfile = arg
      elif opt in ("-o", "--ofile"):
         pdbfilelocation = arg
                  
    data = pd.read_csv(InputSmilesfile,header=None)
    os.chdir(pdbfilelocation)

    data.columns = ['a']
    data['a'] = data['a'].astype(str)
    k1=data['a']
    k1=k1.astype(str)


    for i in range(0,len(data)):
      mol=Chem.MolFromSmiles(k1[i])
      mol2=Chem.AddHs(mol)
      AllChem.EmbedMolecule(mol2)
      AllChem.EmbedMolecule(mol2,randomSeed=0xf00d)
      x = AllChem.EmbedMolecule(mol2,useRandomCoords=True)
      AllChem.MMFFOptimizeMolecule(mol2)
      AllChem.MolToPDBFile(mol2, str(i+1) + '.pdb')
  
if __name__ == "__main__":
    main(sys.argv[1:])
