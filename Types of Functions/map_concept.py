#map function is not for single value
def sq(x):    
    return x**2

l=[1,2,3,4]
y=list(map(sq,l))     #SYNTAX: list(map(func,value)) #value should be a list
print(y)

#by anonymous function method(lambda method)
#this makes the code shorter
#the same work is done here in 2 lines
y=list(map(lambda x:x**2,[1,2,3]))     #direct list can also be given in the fucntion
print(y)


