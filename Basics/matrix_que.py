#UNIT 2 - Lesson 5 Q4
#Write a program to find the transpose of the given matrix in the below program
##Matrix before transposition: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
##Matrix after transposition: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
##
##m=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
##for i in m:
##    print()
##    for j in i:
##        print(j,end=' ')

m=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print("Matrix before transposition: ",m)
m1=[]
for j in range(len(m[0])):
    m1=m1+[[]]
    for i in m:
        m1[j]=m1[j]+[i[j]]

print("Matrix after transposition: ",end=' ')
print(m1)