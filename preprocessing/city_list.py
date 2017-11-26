import sys  
sys.path.append("..")
from dataStructure import GeneralTool

fi=open(GeneralTool.getDataPath('business_int_str_city.txt'),'r',encoding='utf8')
dict_city={}
error=0
for line in fi:  
    line = line.strip()
    try:
        index,iid,city = line.split('\t')  
        try:
            dict_city[city].append(int(index))
        except:
            dict_city[city]=[int(index)]
            #print(city,index)
    except:
        error+=1
fi.close()
#print(error)
#print(len(dict_city))
fo=open(GeneralTool.getDataPath('business_city_int.txt'),'w',encoding='utf8')
for city, ilist in dict_city.items():
    if(len(ilist)>=5):
        fo.write(city+'\t'+str(ilist).strip('[]')+'\n')
        #print(len(ilist))
fo.close()
