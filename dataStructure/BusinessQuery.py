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
if __name__ == '__main__':
#     id=input()
    id = "mLwM-h2YhXl2NCgdS84_Bw"
    path = 'business_rest.txt'
    path = GeneralTool.getDataPath(path)
#     id="12312"
    b = BusinessQuery(path)
    print(b.getBusinessById(id))
    
