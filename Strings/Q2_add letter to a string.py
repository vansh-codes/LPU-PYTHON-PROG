str=input("Enter string : ")
c=input("Enter character : ")
for i in range(len(str)+1):
    print(str[:i] + c + str[i::])
