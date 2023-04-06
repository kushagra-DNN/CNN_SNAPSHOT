from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPool2D , Flatten
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.models import Model
from keras.layers import Input,Conv2D,MaxPooling2D,Activation, Dropout, Flatten, Dense
from keras.layers.merge import concatenate
from keras.callbacks import ReduceLROnPlateau,EarlyStopping,ModelCheckpoint,CSVLogger
from keras.utils import plot_model
import pickle
import tensorflow as tf
import keras
import os
import numpy as np
import random as python_random
import pandas as pd
from matplotlib import pyplot
import itertools  
import pickle
python_random.seed(10)


print ('Predictions.py -a <ChooseAxis> -t <TrainingImageFilesPath> -m <MaybridgeImageFilePath> -mo <PredictionsResultPath>')

def main(argv):
    opts, args = getopt.getopt(argv,"hi:o:",["Afile=", "Tfile=", "Mfile=", "Mofile="])

    for opt, arg in opts:
      if opt == '-h':
         print ('Predictions.py -a <ChooseAxis> -t <TrainingImageFilesPath> -m <MaybridgeImageFilePath> -mo <PredictionsResultPath>')
         sys.exit()
      elif opt in ("-a", "--Afile"):
         ChooseAxis = arg
      elif opt in ("-t", "--Tfile"):
         TrainingImageFilesPath = arg
      elif opt in ("-m", "--Mfile"):
         MaybridgeImageFilePath = arg
      elif opt in ("-mo", "--Mofile"):
         PredictionsResultPath = arg
         
         
    train_datagen = ImageDataGenerator( rescale=1./255 ,shear_range=0.2,zoom_range=0.2,width_shift_range = 0.2,height_shift_range = 0.2)
    validation_datagen = ImageDataGenerator( rescale=1./255 ,shear_range=0.2,zoom_range=0.2,width_shift_range = 0.2,height_shift_range = 0.2)


    for i in range(0,360):
        model1=tf.keras.models.load_model(ChooseAxis + str("\\ds") + str(i+1) + str("\\hdf)" + str(i+1) + str(".h5"))
        
        train_generator = train_datagen.flow_from_directory(
          ChooseAxis + str("\\ds") + str(i+1) + str("\\") + str("train"),  ## training image file location
          target_size=(200,200),
          batch_size=32,
          class_mode='binary')  
                  
        validation_generator =validation_datagen.flow_from_directory(
          MaybridgeImageFilePath + str(i+1), ## maybridge image file directory for prediction         
          target_size=(200, 200),
          color_mode="rgb",
          batch_size=32,
          class_mode=None,
          shuffle=False )  

        filenames = validation_generator.filenames
        nb_samples = len(filenames)
        print(filenames)

        predict = model1.predict_generator(validation_generator)
        from sklearn.metrics import confusion_matrix

        predicted_class_indices=np.argmax(predict,axis=1)

        labels = (train_generator.class_indices)

        labels = dict((v,k) for k,v in labels.items())
        predictions = [labels[k] for k in predicted_class_indices]


        results=pd.DataFrame({"Filename":filenames, "Predictions":predictions})
        
        results.to_csv(PredictionsResultPath + str(i+1) + str(".csv") )


if __name__ == "__main__":
    main(sys.argv[1:])