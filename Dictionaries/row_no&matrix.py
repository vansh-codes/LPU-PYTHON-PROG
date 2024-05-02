n=int(input())  #no of rows
d={}
for i in range(1,n+1):
    d.update({i:tuple(map(int,input().split(",")))})
print(d)
