# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 15:19:56 2018

@author: kuilong.zhang
"""
import numpy
import math
import getopt
import sys

def loadDataSet():
    postinglist = [
            ['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
            ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
            ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
            ['stop', 'posting', 'stupid', 'worthless', 'garbage'], 
            ['mr', 'licks', 'ate', 'steak', 'how', 'to', 'stop', 'him'],
            ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']
            ]
    classVec = [0, 1, 0, 1, 0, 1]
    return postinglist, classVec

s = loadDataSet()
print(s)

def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

t = createVocabList(loadDataSet()[0])
print('t = ', t)

def setOfWord2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
        else:
            print('the word: %s is not in my vocabulary!' % word)
    return returnVec

mytest = ['zhangkuilong', 'lifei', 'lishun', 'dog']
semytest = set(mytest)
my = setOfWord2Vec(t, semytest)
print(my)
'''
t = setOfWord2Vec(createVocabList(loadDataSet()[0]))
print(t)
'''

def trainNB0(trainMatrix, trainCategory):
    for i in trainMatrix:
        print('********* = ', i)
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    print('numWords = ', numWords)
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    print('sum -= ', sum(trainCategory), pAbusive)
    p0Num = numpy.ones(numWords)
    p1Num = numpy.ones(numWords)
    print('p1Num = ', p1Num)
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
            print('second p1Num = ', p1Num, p1Denom)
        else:
            p0Num += trainMatrix[i] 
            p0Denom += sum(trainMatrix[i])
            
    p1Vect = numpy.log(p1Num / p1Denom)
    p0Vect = numpy.log(p0Num / p0Denom)
    return p0Vect, p1Vect, pAbusive

def classifyNb(vec2Classify, p0Vec, p1Vec, pClass1):

    p1 = sum(vec2Classify * p1Vec) + numpy.log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + numpy.log(1.0 - pClass1)
    if (p1 > p0):
        return 1
    else:
        return 0

def testingNB():
    listOPosts, listClassers = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(setOfWord2Vec(myVocabList, postinDoc))
    p0V, p1V, pAb = trainNB0(trainMat, numpy.array(listClassers))
    testEntry = ['love', 'your', 'mother']
    thisDoc = numpy.array(setOfWord2Vec(myVocabList, testEntry))
    print('testEntry = ', testEntry, 'classified as: ', classifyNb(thisDoc, p0V, p1V, pAb))

if __name__ == "__main__":
    listOPosts, listClassers = loadDataSet()
    print('ZHANGKUILONG = ', listOPosts, listClassers)
    myVocabList = createVocabList(listOPosts)
    print(myVocabList)
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(setOfWord2Vec(myVocabList, postinDoc))
    print('trainMat = ', trainMat)
    
    p0V, p1V, pAb = trainNB0(trainMat, listClassers)
    print(p0V, pAb)
    print(', p1V = ', p1V )
    testingNB()
