t=(1,2,3,[3,4,[1,2,3,4]],5)
print(id(t))
t[3][1]=6
t[3][2][0]=24
print(t)
print(id(t))
