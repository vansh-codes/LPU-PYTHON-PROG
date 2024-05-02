f=open("aSearch.txt","r")
for i in f.readlines():
    x=i.split(" ")
    t="#".join(x)
    print(t)
f.close()

