import numpy as np
import sys
sys.path.append("..")
from dataStructure import GeneralTool

def import_uvec(uvec_path,u_index):
    fu=open(GeneralTool.getDataPath(uvec_path),'r')
    for i in range(u_index+1):
        line=next(fu)
    temp=(line.split('\t')[:-1])
    user_vec=[float(i) for i in temp]
    fu.close  
    return user_vec

def import_ivec(ivec_path,i_index):
    fi=open(GeneralTool.getDataPath(ivec_path),'r')
    for i in range(i_index+1):
        line=next(fi)
    temp=(line.split('\t')[:-1])
    item_vec=[float(i) for i in temp]
    fi.close  
    return item_vec

def get_bias(bias):
    fb=open(GeneralTool.getDataPath(bias),'r')
    return float(fb.read())
##def construct_item_matrix(path,index):
##    matrix=[]
##    for i in index:
##        matrix.append(import_ivec(path,i))
##    return matrix
        
        
def calculate_rating(user_vec,item_vec,g_bias=3.71361140936):
    return np.dot(user_vec,item_vec)+g_bias

def sort_by_rating(u_index,item_index_list,uvpath='user_vector30000.txt',ivpath='item_vector30000.txt',bias_path='global_bias.txt'):
    _list=[]
    user_vec=import_uvec(uvpath,u_index)
    for i in range(len(item_index_list)):
        item_vec=import_ivec(ivpath,i)
        rating=calculate_rating(user_vec,item_vec,get_bias(bias_path))
        _list.append([item_index_list[i],rating])
    _list=sorted(_list,key=lambda x:x[1],reverse=True)
    result=[[i[0],i[1]] for i in _list]
    #print(result)
    return result

if __name__ == "__main__":
##    user_vec=import_uvec('user_vector30000.txt',0)
##    item_vec=import_ivec('item_vector30000.txt',0)
##    print(user_vec)
##    print(len(user_vec))
##    print(item_vec)
##    print(len(item_vec))
##    print(get_bias('global_bias.txt'))
##    print(calculate_rating(user_vec,item_vec,get_bias('global_bias.txt')))

    t=sort_by_rating(0,range(0,50))

    print(t)
    
