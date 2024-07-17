'''x=10
def t1():
    global x
    x=20

def t2():
    x=30
    
print(x)    #gives value 10 bcoz func is called afterwards
t1()'''

'''x=10
def t1():
    global x
    x=20

def t2():
    x=30
    
t1()
print(x)'''    #gives value 20 bcoz func is called then x printed

'''x=10
def t1():
    global x
    x=20

def t2():
    x=30
    
t2()    #gives the value 10 bcoz x in t2 is not global i.e x has value 30 in the function only
print(x)'''

'''x=10
def t1():
    global x
    x=20

def t2():
    x=30
    print(x)

t2()       #gives x=30 bcoz printed inside the def func
print(x)'''   #gives x=10 bcoz printed outside func

x=10
def t1():
    global x
    x=20

def t2():
    x=30
    
print(x)    #x=10 bcoz printed before calling
t1()        #this makes x=20
t2()
print(x)       #hence this prints x=20





