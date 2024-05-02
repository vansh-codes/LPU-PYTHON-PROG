#values as list then print the dictionary in a table format
k=input("Keys : ").split(",")
print("Values : ")
d={}
for i in range(len(k)):
    v=list(map(int,input("Enter values : ").split(",")))
    d[k[i]]=v
print("Dictionary : ",d)   #printing the created dictionary
for row in zip(*([key] + (value) for key,value in sorted(d.items()))):
    print(*row)