#FABIONNIC SERIES :)
n=int(input("Enter number of terms : "))
def fab(n):
    if n<=1:
        return n
    else:
        return (fab(n-1)+fab(n-2))

for i in range(n):
    print(fab(i),end=" ")
