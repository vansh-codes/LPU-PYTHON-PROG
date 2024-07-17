#break statement
x=1
while x<10:
    if x>5:
        break
    print(x)
    x=x+1

#continue statement
print("------------------")
for x in range(1,10):
    if x%2==0:
        continue
    print(x)
