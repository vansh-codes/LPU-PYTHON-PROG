import pickle
import sys
s1={'id':1221,"Name":"Ritesh","ROllno":52}
s2={'id':1222,"Name":"Ritesh2","ROllno":53}
s3={'id':1223,"Name":"Ritesh3","ROllno":54}
db=[s1,s2,s3]

f=open("BinWrite.dat","wb")
pickle.dump(db,f)
f.close()
f=open("BinWrite.dat","rb")
f1=pickle.load(f)
for i in f1:
    print(i.values())
print("Size : ",sys.getsizeof(f1))
f.close()
