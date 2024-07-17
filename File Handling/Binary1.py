import pickle
d={1:'a',2:'b',3:'c'}
f=open("Binary1.dat","wb")
pickle.dump(d,f)
f.close()
