import collections
a = []
dict1 = {}
data1 = open('data/business_rest.txt', 'r')
for line in data1:
    a.append(line.split('\t'))
for i in range(0, len(a)):
    dict1[a[i][0]] = i
data1.close()
'''for key in dict1.keys():
    print('key=%s, value=%s' % (key, dict1[key]))'''
# data1_out = open('business_int_to_string.txt', 'w')
# for i in range(0, len(a)):
#     data1_out.write(str(i) + '\t' + str(a[i][0]) + '\n')
# data1_out.close()
# 
# data1_out = open('business_string_to_int.txt', 'w')
# order_dict1 = collections.OrderedDict(sorted(dict1.items()))
# for(k, v) in order_dict1.items():
#     data1_out.write(str(k) + '\t' + str(v) + '\n')
# data1_out.close()

b = []
dict2 = {}
data2 = open('data/user_rest.txt', 'r')
for line in data2:
    b.append(line.strip('\n'))
for i in range(0, len(b)):
    dict2[b[i]] = i
# data2_out = open('user_int_to_string.txt', 'w')
# for i in range(0, len(a)):
#     data2_out.write(str(i) + '\t' + str(a[i][0]) + '\n')
# data2_out.close()
# 
# data2_out = open('user_string_to_int.txt', 'w')
# order_dict2 = collections.OrderedDict(sorted(dict2.items()))
# for(k, v) in order_dict2.items():
#     data2_out.write(str(k) + '\t' + str(v) + '\n')
# data2_out.close()
# data2.close()

'''
for key in dict2.keys():
    print('key=%s, value=%s' % (key, dict2[key])) 
'''
 
c = []
data3 = open('data/review_rest.txt', 'r')
for line in data3:
    c.append(line.split('\t'))
 
# fi = open('data/final.txt', 'w')
# for i in range(0, len(c)):
#     c[i][0] = dict2[c[i][0]]
#     c[i][1] = dict1[c[i][1]]
#     fi.write(str(c[i][0]) + '\t' + str(c[i][1]) + '\t' + str(c[i][2]) + '\t' + str(c[i][3]))
# fi.close()
    
fi = open('data/final_part.txt', 'w')
for i in range(0, len(c)):
    c[i][0] = dict2[c[i][0]]
    c[i][1] = dict1[c[i][1]]
    if(c[i][0]<30000 and c[i][1]<30000):
        fi.write(str(c[i][0]) + '\t' + str(c[i][1]) + '\t' + str(c[i][2]) + '\t' + str(c[i][3]))
fi.close()

