"""
Created on Mon Apr  9 16:17:53 2018

@author: kuilong.zhang
"""

import numpy

def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open('testSet.txt', 'r')
    for line in fr.readlines():
        lineArr = line.strip().split()
        #print(lineArr)
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat

def sigmoid(inX):
    return 1.0/(1 + numpy.exp(-inX))

def gradAscent(dataMatIn, classLabels):
    dataMatrix = numpy.mat(dataMatIn)
    labelMat = numpy.mat(classLabels).transpose()
    m,n = numpy.shape(dataMatrix)
    alpha = 0.001
    maxCycles = 500
    weights = numpy.ones((n, 1))
    for k in range(maxCycles):
        h = sigmoid(dataMatrix * weights)
        error = labelMat - h
        weights = weights + alpha * dataMatrix.transpose() * error
    return weights

A, B = loadDataSet()
C = gradAscent(A, B)
print(C)

def stocGradAscent1(dataMatrix, classLabels, numIter = 50):
    m, n = numpy.shape(dataMatrix)
    weights = numpy.ones(n)
    for j in range(numIter):
        dataIndex = range(m)
        for i in range(m):
            alpha = 4 / (1.0 + j + i) + 0.01
            randIndex = int(numpy.random.uniform(0, len(dataIndex)))
            h = sigmoid(sum(dataMatrix[randIndex] * weights))
            error = classLabels[randIndex] - h
            weights = weights + numpy.float64(alpha) * numpy.float64(error) * numpy.float64(dataMatrix[randIndex])
    return weights

my = stocGradAscent1(A, B)
print(my)

def classifyVector(inX, weights):
    prob = sigmoid(sum(inX * weights))
    if prob > 0.5:
        return 1.0
    else:
        return 0.0

def colicTest():
    frTrain = open('horseColicTraining.txt')
    frTest = open('horseColicTest.txt')
    trainingSet = []
    trainingLabels = []
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[21]))
    trainWeights = stocGradAscent1(numpy.array(trainingSet), trainingLabels, 500)
    errorCount = 0
    numTestVec = 0.0
    for line in frTest.readlines():
        numTestVec += 1.0
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        if int(classifyVector(numpy.array(lineArr), trainWeights))!=int(currLine[21]):
            errorCount += 1
    errorRate = (float(errorCount)/numTestVec)
    print("the error rate of this test is: %f" % errorRate)
    return errorRate

def multiTest():
    numTests = 10
    errorSum = 0.0
    for k in range(numTests):
        errorSum += colicTest()
    print('after %d iterations the average error rate is : %f' % (numTests, errorSum/float(numTests)))

multiTest()