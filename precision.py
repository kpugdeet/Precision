from keras.datasets import cifar10

(xTrain, yTrain), (xTest, yTest) = cifar10.load_data()

print xTrain.shape
print yTrain.shape
print xTest.shape
print yTest.shape

