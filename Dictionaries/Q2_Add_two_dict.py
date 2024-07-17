#To check if given key exists or not
d1={"a":1,"b":2,"c":3,"d":4}
k=input("Enter key to check : ")
for i in d1:
    if i==k:
        print("Key exists")
        break
    else:
        print("Doesn't exists")

