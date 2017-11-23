import numpy as np
import sys
sys.path.append("..")
from dataStructure import GeneralTool

def import_uvec(uvec,u_index):
    fu=open(GeneralTool.getDataPath(uvec),'r')
    for i in range(u_index+1):
        line=next(fu)
    temp=(line.split('\t')[:-1])
    user_vec=[float(i) for i in temp]
    fu.close  
    return user_vec

def import_ivec(ivec,i_index):
    fi=open(GeneralTool.getDataPath(ivec),'r')
    for i in range(i_index+1):
        line=next(fi)
    temp=(line.split('\t')[:-1])
    item_vec=[float(i) for i in temp]
    fi.close  
    return item_vec

def get_bias(bias):
    fb=open(GeneralTool.getDataPath(bias),'r')
    return float(fb.read())
def calculate_rating(user_vec,item_vec,g_bias=3.71361140936):
    return np.dot(user_vec,item_vec)+g_bias

if __name__ == "__main__":
    user_vec=import_uvec('user_vector30000.txt',0)
    item_vec=import_ivec('item_vector30000.txt',0)
    print(user_vec)
    print(len(user_vec))
    print(item_vec)
    print(len(item_vec))
    print(get_bias('global_bias.txt'))
    print(calculate_rating(user_vec,item_vec))
