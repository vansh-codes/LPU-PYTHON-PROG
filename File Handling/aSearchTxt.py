##f=open("aSearch.txt","w")
##f.write("Hello this is Python Programming \n How can we remove the line which contains a in it. \n Okay nice! \n Good!")
##f.close()

f=open("aSearch.txt","r")
f1=open("aLine.txt","w")
for i in f.readlines():
    if 'a' not in i:
        f1.write(i+'\n')
f.close()
f1.close()
