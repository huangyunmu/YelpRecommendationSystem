#@Author: ZHAO Fanyue
import sys
sys.path.append("..")
from dataStructure import GeneralTool
class Converter:
    def __init__(self):
        # self.inInt = inInt
        self.something = "tt"

    def getBusinessStr(self, inInt, path="business_int_to_string.txt"):
        self.path = GeneralTool.getDataPath(path)
        data = open(self.path,'r')
        for line in data:
            temp=line.split('\t')

            if (int(temp[0]) == inInt):
                #print(temp[1])
                data.close()
                return temp[1]
    
    def getBusinessInt(self, inStr,path="business_string_to_int.txt"):
        self.path = GeneralTool.getDataPath(path)
        data = open(self.path,'r')
        for line in data:
            temp=line.split('\t')

            if (str(temp[0]) == inStr):
                #print(temp[1])
                data.close()
                return int(temp[1])

    def getUserStr(self, inInt,path='user_int_to_string.txt'):
        self.path = GeneralTool.getDataPath(path)
        data = open(self.path,'r')
        for line in data:
            temp=line.split('\t')

            if (int(temp[0]) == inInt):
                #print(temp[1])
                data.close()
                return temp[1]

    def getUserInt(self, inStr,path='user_string_to_int.txt'):
        self.path = GeneralTool.getDataPath(path)
        data = open(self.path,'r')
        for line in data:
            temp=line.split('\t')

            if (str(temp[0]) == inStr):
                #print(temp[1])
                data.close()
                return int(temp[1])

        
        
##
##t = Converter();
##gg=t.getBusinessStr(5,"business_int_to_string.txt")
##print("Something")
##print(gg)
        
        
        
