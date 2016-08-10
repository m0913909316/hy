# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 17:03:44 2016

@author: Liu Hsiao Yun
"""
import random
from numpy import *
import matplotlib.pyplot as plt
#-----------------------------------------------------------------------------
def distance(x1,y1,x2,y2):  
    return sqrt(power(x1 - x2, 2) + power(y1 - y2, 2))

def cen_dis(size,mindis,center,dataSet):
    for i in range(size):
        for j in range(3):
            if mindis[i] > distance(center[j][0],center[j][1],dataSet[i][0],dataSet[i][1]) :
                mindis[i] = distance(center[j][0],center[j][1],dataSet[i][0],dataSet[i][1])
                temp = j
        index.append(temp)

def newcen(cluster):
    size = len(cluster)
    x = 0
    y = 0
    for i in range(size):
        x = x + cluster[i][0]
        y = y + cluster[i][1]
    if size == 0:
        size += 1

    x = x / size
    y = y / size
    
    return [x,y]
    
def showCluster(dataSet,k,center,index):  
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    # draw all samples  
    for i in range(size):  
        markIndex = index[i]
        plt.plot(dataSet[i][0], dataSet[i][1], mark[markIndex])  
    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']  
    # draw the centroids  
    for i in range(3):  
       plt.plot(center[i][0], center[i][1], mark[i], markersize = 15)  
    plt.show()   
#-----------------------------------------------------------------------------
dataSet = []  
indexCen = []
center = []
mindis = []
index = []
cluster_0 = []
cluster_1 = []
cluster_2 = []
#-----------------------------------------------------------------------------
user_input = input('Please input 3 index of the center <0-149,以空白間隔> :')
b = []
a = user_input.split(' ')
b.append(a)
indexCen.append(int(b[0][0]))
indexCen.append(int(b[0][1]))
indexCen.append(int(b[0][2]))
#-----------------------------------------------------------------------------

for round in range(6):
    fileIn = open('C:/Users/USER/Desktop/python/iris.txt')
    
    if round == 0:
        for line in fileIn.readlines():  
            lineArr = line.strip().split(',')
            dataSet.append([float(lineArr[0]),float(lineArr[1])])
    elif round == 1:
        for line in fileIn.readlines():  
            lineArr = line.strip().split(',')
            dataSet.append([float(lineArr[0]),float(lineArr[2])])
    elif round == 2:
        for line in fileIn.readlines():  
            lineArr = line.strip().split(',')
            dataSet.append([float(lineArr[0]),float(lineArr[3])])
    elif round == 3:
        for line in fileIn.readlines():  
            lineArr = line.strip().split(',')
            dataSet.append([float(lineArr[1]),float(lineArr[2])])
    elif round == 4:
        for line in fileIn.readlines():  
            lineArr = line.strip().split(',')
            dataSet.append([float(lineArr[1]),float(lineArr[3])])
    elif round == 5:
        for line in fileIn.readlines():  
            lineArr = line.strip().split(',')
            dataSet.append([float(lineArr[2]),float(lineArr[3])])
          
    size = len(dataSet)
    #隨機找3個中心點
#    for i in range(3):
#        if round == 0:                                      
#            indexCen.append(random.randint(0,size))
#            print(indexCen)
#        center.append(dataSet[indexCen[i]])
      
    for i in range(3):
        center.append(dataSet[indexCen[i]])
    
    while(1):
        for i in range(size):
            mindis.append(10000)
        
        cen_dis(size,mindis,center,dataSet)
        
        for i in range(size):
            if index[i] == 0:
                cluster_0.append(dataSet[i])
            elif index[i] == 1:
                cluster_1.append(dataSet[i])
            elif index[i] == 2:
                cluster_2.append(dataSet[i])
    
        c0 = newcen(cluster_0)
        c1 = newcen(cluster_1)
        c2 = newcen(cluster_2)
            
        if abs(center[0][0] - c0[0] < 0.0001) and abs(center[0][1] - c0[1] < 0.0001):
            if abs(center[1][0] - c1[0] < 0.0001) and abs(center[1][1] - c1[1] < 0.0001):
                if abs(center[2][0] - c2[0] < 0.0001) and abs(center[2][1] - c2[1] < 0.0001):
                    break
              
        center[0] = newcen(cluster_0)
        center[1] = newcen(cluster_1)
        center[2] = newcen(cluster_2)
         
        cluster_0[:] = []
        cluster_1[:] = []
        cluster_2[:] = []
        mindis[:] = []
        index[:] = []
        
    showCluster(dataSet,3,center,index)
    #每一round完 將data 清空
    dataSet[:] = []    
    cluster_0[:] = []
    cluster_1[:] = []
    cluster_2[:] = []
    mindis[:] = []
    index[:] = []
    center[:] = []
