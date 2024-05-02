#to print names in the given list
'''l=['Aman','Raj','Ravi','Aman','Atul']
def hello():
    for i in l:
        print("Hello",i)
        
hello()'''

#to give as many input as we want in the function
def hello(*n):
    for i in n:
        print("Hello",i)
hello('Aman','Raj','Ravi','Aman','Atul','Raju')
