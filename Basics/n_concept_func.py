#multi varible star function concept
'''def sum1(*n):      # single * creates a tuple whereas using ** creates a dictionary
    print("Sum: ",sum(n))

sum1(1,2,3)
sum1(1,5)
sum1(8,2)'''

    
'''def fun(*n):
    for i in n:
        print(i,end= '$')
    print()
fun(1,2,3)
fun(1,3,5)'''



#to create a dictionary
def dict1(**n):          #using ** creates a dictionary
    print(n)
    print(type(n))

dict1(a=1,b=2,c=3,d=4)        #calling like a=2 creates a dictionary with a as key and 2 as value