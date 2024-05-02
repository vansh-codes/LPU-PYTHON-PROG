d={1:'a', 2:'b' , 3:'c', 4:'d'}
d[5]='e'               #Adding in the dictionary  dict_name[key]=value
print(d)

del d[2]               #Deletion in the dictionary  dict_name[key]
print(d)

d[1]='z'               #Updating in the dictionary dict_name[key]=new_value
print(d)

l=[(1,2),(3,4)]        #Entering pair values which can be converted into dictionary
print(dict(l))

l1=[1,2,3,4]
l2=['a','b','c','d']
d1=dict(zip(l1,l2))    #creates pairs of l1 & l2 which can be converted into dict
print(d1)
