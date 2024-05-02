#.keys()      prints all keys
#.values()    prints all values
#.copy()      returns a copy
#.update()    updates by the specified key,value pair
#.setdefault  returns value of specified keys, if keys do not exist then insert the key with the specified value
#.popitem()   deletes last element and returns
#.pop()       deletes specified element , takes 1 argument
#.get()       prints value of the specified key
#.items()     prints list consisting of tuple of key,value pair


menu={"Name":"Price",
      "Bread":10.0 ,
      "Pasta":30.0 ,
      "Rice":100.0 ,
      "Oils":200.0 ,
      "Soups":50.0 }

menu1={"Name":"Price",
      "Bread":10.0 ,
      "Pasta":30.0 ,
      "Rice":100.0 ,
      "Oils":200.0 ,
      "Soups":50.0 }

print(menu.keys())
print(menu.values())
menu1.clear()
print(menu1)
print(menu.copy())       #creates another dictionary with different memory location whereas d1=d
                         #is called aliasing and it stores in the same memory location
print(menu.popitem())
print("Pop : ",menu.pop("Rice"))
print(menu.items())
print(sorted(menu.items()))
menu.update({"Bread":20})
print(menu)
print(menu.setdefault("Bread"))
print(menu.fromkeys([1,2,3]))

