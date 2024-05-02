'''
split()
strip()        -  lstrip() & rstrip()
join()
just()         - ljust() & rjust()   #just means justified
startswith()
endswith()
'''

s="  Hello World "
s1=''
s2='2,3,4,5'
l1=['a','b','c','d']
l2=[1,2,3,4]
print(s.split())
print(s2.split(','))    #splits every time it finds comma
print(list(map(str,s2.split(','))))
print(list(map(int,s2.split(','))))
print(s.strip())        #strip also removes trailing left spaces
print(s.lstrip())   
print(s.rstrip())
print("Join : ",s.join(l1))       #cannot join l2 bcoz it only join strings not int
print("Join : ",s1.join(l1))
print(s.startswith("Hello"))
print(s.endswith("World"))

print("".join(map(str,["2","3","a"])))
#to take multiple inputs in a single line
n=input("Enter : ").split()
for i in n:
    print(i)

