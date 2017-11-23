# -*- coding: UTF-8 -*-
'''
Created on 2017-11-23

@author: Chen Zhongxing
'''
import sys
sys.path.append("..")
from _overlapped import NULL
from dataStructure import GeneralTool
class BusinessQuery(object):
    '''
    classdocs
    '''
    def __init__(self, file_path):
        '''
        Constructor
        '''
        self.path = file_path
        self.cityIndex = 4
    def getBusinessById (self, businessid):
        a = []
        dict1 = {}
        data = open(self.path, 'r', encoding="utf8")
        for line in data:
            a.append(line.split('\t'))
        for i in range(0, len(a)):
            dict1[a[i][0]] = a[i][1:]
        if businessid in dict1.keys():
            return(dict1[businessid])
        else:
#             print('wrong')
            return(NULL)
        data.close()
    def getBusinessIdByCity(self, city):
        data = open(self.path, 'r', encoding="utf8")
        result=[]
        for line in data:
            splitData = line.split('\t')
            if(splitData[self.cityIndex]==city):
                result.append(splitData[0])
#                 print(splitData[0]+" "+splitData[self.cityIndex])
        data.close()
        return result       
if __name__ == '__main__':
#     id=input()
    id = "mLwM-h2YhXl2NCgdS84_Bw"
    city = "Charlotte"
    path = 'business_full_data.txt'
    path = GeneralTool.getDataPath(path)
#     id="12312"
    b = BusinessQuery(path)
    print(b.getBusinessById(id))
    result=b.getBusinessIdByCity(city)
    for city in result:
        print(city)
