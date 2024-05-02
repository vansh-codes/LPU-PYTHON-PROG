#All string methods
s="ba5c"
print(all(s))
print(any(s))
print(len(s))
print(list(s))
print(max(s))
print(min(s))
print(sorted(s))


#Methods
print("----LIST----")
l=[1,2,3]
l1=["a","b","a"]
l.append(4)
l.append(l1)
print("Appended : ",l)
l.extend(l1)       #used to add list into a list
print("Extended: ",l)
l.insert(4,5)
print("insert : ",l)
l.remove(4)
print("remove : ",l)
print("popped el: ",l.pop(3))
print("pop : ",l)
l.clear()
print("clear: ",l)
print("--------")
l=[1,2,3,5,4]
print("count : ",l1.count("a"))
print("Index : ",l.index(2))
l.sort()
print("sorted : ",l)
l.reverse()
print("reversed : ",l)
l.copy()
print(l)

