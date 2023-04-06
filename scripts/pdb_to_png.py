from pymol import cmd
import os
import argparse
import sys
import sys, getopt

######## generation of Training/testing set active/inactives/PI PNG files  #####

print ('pdb_to_png.py -i <Train_Test_pdbfilelocation> -o <Train_Test_ImageFileOutput> -m <Maybridge_pdbfilelocation> -mo <Maybridge_ImageFileOutputPath>')

def main(argv):
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])

    for opt, arg in opts:
      if opt == '-h':
         print ('pdb_to_png.py -i <Train_Test_pdbfilelocation> -o <Train_Test_ImageFileOutput> -m <Maybridge_pdbfilelocation> -mo <Maybridge_ImageFileOutputPath>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         Train_Test_pdbfilelocation = arg
      elif opt in ("-o", "--ofile"):
         Train_Test_ImageFileOutputPath = arg

      elif opt in ("-m", "--mfile"):
         Maybridge_pdbfilelocation = arg
      elif opt in ("-mo", "--mofile"):
         Maybridge_ImageFileOutputPath = arg

    os.chdir(Train_Test_pdbfilelocation)
    from glob import glob
    lst = glob("*.pdb")
    lst.sort()

    a=0
    for i in range(360):
      a=a+1
      os.mkdir(Train_Test_ImageFileOutputPath + str(a))
      for j in range(len(lst)):
       cmd.load(lst[j],"mov",multiplex =1)
       cmd.color("gray","elem c*")
       cmd.color("white","elem h*")
       cmd.rotate("y", a)   # x axis at 15
       cmd.set('ray_opaque_background', 3200)
       cmd.png(Train_Test_ImageFileOutputPath + str(a) + "\\" + str(lst[j]) ,width=200, height=200)
       
######## generation of Maybridge PNG files  #####

    os.chdir(Maybridge_pdbfilelocation)
    from glob import glob
    lst = glob("*.pdb")
    lst.sort()

    a=0
    for i in range(360):
      a=a+1
      os.mkdir(Maybridge_ImageFileOutputPath + str(a))
      for j in range(len(lst)):
       cmd.load(lst[j],"mov",multiplex =1)
       cmd.color("gray","elem c*")
       cmd.color("white","elem h*")
       cmd.rotate("y", a)   # x axis at 15
       cmd.set('ray_opaque_background', 3200)
       cmd.png(Maybridge_ImageFileOutputPath + str(a) + "\\" + str(lst[j]) ,width=200, height=200)


if __name__ == "__main__":
    main(sys.argv[1:])
