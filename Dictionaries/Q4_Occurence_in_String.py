s=input("Enter string : ")
main={}
for i in s:
    if i in main:
        continue
    else:
        c=s.count(i)
        #d={i:c}
        main.update({i:c})
print(main)
