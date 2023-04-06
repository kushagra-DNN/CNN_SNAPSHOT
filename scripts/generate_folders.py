import os 


## generate folders for x axis train set
os.mkdir("x")
for i in range(0,360):
    os.mkdir("\\x\\ds" + str(i+1) + str("\\") + str("train"))
    for i in range(0,1):
        os.mkdir("\\x\\ds" + str(i+1) + str("\\") + str("train") + str("\\") + str("active")) ## for x axis train active class png images
        os.mkdir("\\x\\ds" + str(i+1) + str("\\") + str("train") + str("\\") + str("I"))  ## for x axis train inactive class png images

## generate folders for x axis test set
for i in range(0,360):
    os.mkdir("\\x\\ds" + str(i+1) + str("\\") + str("test"))
    for i in range(0,1):
        os.mkdir("\\x\\ds" + str(i+1) + str("\\") + str("test") + str("\\") + str("active")) ## for x axis test active class png images
        os.mkdir("\\x\\ds" + str(i+1) + str("\\") + str("test") + str("\\") + str("I"))  ## for x axis test inactive class png images


## generate folders for y axis train set
os.mkdir("y")
for i in range(0,360):
    os.mkdir("\\y\\ds" + str(i+1) + str("\\") + str("train"))
    for i in range(0,1):
        os.mkdir("\\y\\ds" + str(i+1) + str("\\") + str("train") + str("\\") + str("active")) ## for y axis train active class png images
        os.mkdir("\\y\\ds" + str(i+1) + str("\\") + str("train") + str("\\") + str("I"))  ## for y axis train inactive class png images

## generate folders for y axis test set
for i in range(0,360):
    os.mkdir("\\y\\ds" + str(i+1) + str("\\") + str("test"))
    for i in range(0,1):
        os.mkdir("\\y\\ds" + str(i+1) + str("\\") + str("test") + str("\\") + str("active")) ## for y axis test active class png images
        os.mkdir("\\y\\ds" + str(i+1) + str("\\") + str("test") + str("\\") + str("I"))  ## for y axis test inactive class png images


## generate folders for z axis train set
os.mkdir("z")
for i in range(0,360):
    os.mkdir("\\z\\ds" + str(i+1) + str("\\") + str("train"))
    for i in range(0,1):
        os.mkdir("\\z\\ds" + str(i+1) + str("\\") + str("train") + str("\\") + str("active")) ## for z axis train active class png images
        os.mkdir("\\z\\ds" + str(i+1) + str("\\") + str("train") + str("\\") + str("I"))  ## for z axis train inactive class png images

## generate folders for z axis test set
for i in range(0,360):
    os.mkdir("\\z\\ds" + str(i+1) + str("\\") + str("test"))
    for i in range(0,1):
        os.mkdir("\\z\\ds" + str(i+1) + str("\\") + str("test") + str("\\") + str("active")) ## for z axis test active class png images
        os.mkdir("\\z\\ds" + str(i+1) + str("\\") + str("test") + str("\\") + str("I"))  ## for z axis test inactive class png images

