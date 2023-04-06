# CNN_SNAPSHOT

Code for our paper: Identification of Potential Aldose Reductase Inhibitors using Convolutional Neural Networks based Insilico Screening

### Step 1: Installation
- git clone https://github.com/kushagra-DNN/CNN_SNAPSHOT.git <br>
- cd CNN_SNAPSHOT <br>
- conda env create -f environment.yaml -n CNN_SNAPSHOT <br>
- conda activate CNN_SNAPSHOT <br>
- python setup.py install <br>

#### Step 2: Generate folders
For generating folders for training/test set actives,inactives and putative inactives, run **python generate_folders.py** file
This will create folders across all axis. The dataset will be distributed across this format:
```
x/
  ds1/
    train\ 
      active\
      I\
    test\ 
      active\
      I\
  ...
y/
  ds1/
    train\ 
      active\
      I\
    test\ 
      active\
      I\
  ...
z/
  ds1/
    train\ 
      active\
      I\
    test\ 
      active\
      I\
  ...
```

#### Step 3: Convert molecular canonical SMILES to PDB files
Run:<br>
```
python smiles_to_pdb.py --ifile [InputSmilesfile] --ofile [pdbfilelocation] --mfile [MaybridgeSmilesfile] --mofile [MaybridgepdbfilePath]
```

#### Step 4: Convert PDB to PNG (Snapshots of 3D rotated molecules)
Create PNG files for all sets of training sets active, inactive and putative inactives for both training and testing set 
Run:<br>
```
python pdb_to_png.py --ifile [Train_Test_pdbfilelocation] --ofile [Train_Test_ImageFileOutput] --mfile [Maybridge_pdbfilelocation] --mofile [Maybridge_ImageFileOutputPath]
```
Note: The PNG files generated should be directed to the correct file location as mentioned in the step 2  

#### Step 5: Training the CNN model using the prepared dataset 
Run:<br>
```
python CNNSnapshot.py --Afile [Path_To_Particular_Axis_Directory]
```

#### Step 6: CNN model prediction on the Maybridge image (Snapshots of 3D rotated molecules) PNG files
Run:<br>
```
python Predictions.py --Afile [Path_To_Particular_Axis_Directory] --Tfile [TrainingImageFilesPath] --Mfile [MaybridgeImageFilePath] --Mofile [PredictionsResultPath] 
```

