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


print ('CNNSnapshot.py -a <Path_To_Particular_Axis_Directory>')

def main(argv):
    opts, args = getopt.getopt(argv,"hi:o:",["Afile="])

    for opt, arg in opts:
      if opt == '-h':
         print ('CNNSnapshot.py -a <Path_To_Particular_Axis_Directory>' )
         sys.exit()
      elif opt in ("-a", "--Afile"):
         AxisDirectory = arg
         
         
    train_datagen = ImageDataGenerator( rescale=1./255 ,shear_range=0.2,zoom_range=0.2,width_shift_range = 0.2,height_shift_range = 0.2)
    test_datagen = ImageDataGenerator( rescale=1./255 ,shear_range=0.2,zoom_range=0.2,width_shift_range = 0.2,height_shift_range = 0.2)

    for i in range(0,360):
        os.chdir(AxisDirectory + str("\\ds") + str(i+1)) # change directory to a specific axis 
        train_generator = train_datagen.flow_from_directory(
                  AxisDirectory + str("\\ds") + str(i+1) + str("\\") + str("train"),  
                  target_size=(200,200),
                  batch_size=32,
                  class_mode='categorical')

        test_generator =test_datagen.flow_from_directory(
                  AxisDirectory + str("\\ds") + str(i+1) + str("\\") + str("test"),  
                  target_size=(200,200),
                  batch_size=32,
                  class_mode='categorical')  


        target_names = []
        for key in test_generator.class_indices:
            target_names.append(key)


        def CNN_Snapshot(layer_in, f1, f2_in, f2_out, f3_in, f3_out, f4_out):
            conv1 = Conv2D(f1, (1,1), padding='same', activation='relu', )(layer_in)
            conv3 = Conv2D(f2_in, (1,1), padding='same', activation='relu')(layer_in)
            conv3 = Conv2D(f2_out, (3,3), padding='same', activation='relu',kernel_regularizer =tf.keras.regularizers.l2( l=0.01))(conv3)
            conv5 = Conv2D(f3_in, (1,1), padding='same', activation='relu',kernel_regularizer =tf.keras.regularizers.l2( l=0.01))(layer_in)
            conv5 = Conv2D(f3_out, (5,5), padding='same', activation='relu')(conv5)
            pool = MaxPooling2D((3,3), strides=(1,1), padding='same')(layer_in)
            pool = Conv2D(f4_out, (1,1), padding='same', activation='relu')(pool)
            layer_out = concatenate([conv1, conv3, conv5, pool], axis=-1)
            return layer_out

        visible = Input(shape=(200, 200, 3))
        layer = CNN_Snapshot(visible, 15, 20, 25, 25, 30, 20)

        model = keras.models.Model(inputs=visible, outputs=layer)
        model.summary()


        Model = Sequential()
        Model.add(model)

        Model.add(Flatten())  
        Model.add(Dense(2))
        Model.add(Activation('sigmoid'))
        

        Model.compile(loss='binary_crossentropy',
                     optimizer="adam",
                     metrics=[tf.keras.metrics.AUC(), 
                     tf.keras.metrics.Precision(), 
                     tf.keras.metrics.Recall(),
                     tf.keras.metrics.BinaryAccuracy(),
                     tf.keras.metrics.Accuracy(),
                     tf.keras.metrics.SpecificityAtSensitivity(0.5),
                     tf.keras.metrics.SensitivityAtSpecificity(0.5),
                     tf.keras.metrics.TruePositives(),
                     tf.keras.metrics.TrueNegatives(),
                     tf.keras.metrics.FalsePositives(),
                     tf.keras.metrics.FalseNegatives()                 
                    ])
                     
        csv_logger = CSVLogger(ChooseAxis + str("\\ds") + str(i+1) + str("\\") + str("CSV_") + str(i+1) + str(".csv"),separator=",")

        reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=5, min_lr=0.0001, verbose=1)    

        history = Model.fit_generator(generator=train_generator,epochs=200,validation_data= test_generator,callbacks=[mc,csv_logger,reduce_lr])   
        Model.save(AxisDirectory + str("\\ds") + str(i+1) + str("\\") + str("hdf") + str(i+1) + str(".h5"))

if __name__ == "__main__":
    main(sys.argv[1:]) 
