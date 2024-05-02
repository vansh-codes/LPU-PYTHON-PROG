menu={"Name":"Price",
      "Bread":10.0 ,
      "Pasta":30.0 ,
      "Rice":100.0 ,
      "Oils":200.0 ,
      "Soups":50.0
      }
print("Welcome to LPU GENERAL STORE")
#Loop to print dict
#for i in menu:
#   print(i,menu[i])
while True:
    for key,values in menu.items():
        print("{:10}   :    {:>4}".format(key,values))   # > right justify , < left justify , ^ centre
    print()
    print("1. Update")
    print("2. Add")
    print("3. Delete")
    print("4. Exit")
    choice=input("Enter your choice : ")
    if choice=="1":
        item=input("Enter item name : ")
        update=input("Enter new price : ")
        update=float(update)
        menu[item]=update
        print(menu)
    elif choice=="2":
        item_name=input("Enter item name : ")
        price=float(input("Enter price : "))
        menu[item_name]=price
        print(menu)
    elif choice=="3":
        x=input("Enter item name : ")
        del menu[x]
        print(menu)
        print("Item deleted from the record")
    elif choice=="4":
        print("Exit")
        break
    else:
        print("Invalid Input")
