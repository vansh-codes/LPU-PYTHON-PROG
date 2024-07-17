##l1=[1,2,3,4,5]
##l2=[5,6,7,8,9,4]

l1=list(map(int,input("Enter list1 : ").split(" ")))
l2=list(map(int,input("Enter list2 : ").split(" ")))

def common(l1,l2):
    l=[]
    for i in l1:
        if i in l2:
            l=l+[i]

    for i in l:
        print(i,end=" ")


if len(l1)<=len(l2):
    common(l1,l2)
else:
    common(l2,l1)

