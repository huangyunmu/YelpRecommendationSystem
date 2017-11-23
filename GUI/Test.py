# -*- coding: UTF-8 -*-
'''
Created on 2017/11/23
@author: andyh
'''
import os
import sys
sys.path.append("..")
from dataStructure import BusinessQuery
from dataStructure import GeneralTool
if __name__=='__main__':
    id="mLwM-h2YhXl2NCgdS84_Bw"
    filePath="business_full_data.txt"
    filePath=GeneralTool.getDataPath((filePath))
    print(filePath)
    bb=BusinessQuery.BusinessQuery(filePath)
    print(bb.getBusinessById(id))
#     print(os.getcwd())
#     print(os.path.pardir)
  
