import random
urc = int(input("Enter a number of your choice between 1 to 10:\n"))
friend = int(input("Enter same number for your friend:\n"))
my = 0
             
randNo = random.randint(1,3)
if randNo == 1:
    my += 10
    print("Add 10 for me")
elif randNo == 2:
    my += 14
    print("Add 14 for me")
elif randNo == 3:
    my += 30
    print("Add 30 for me")

total = urc + friend + my

print("Add all the values and donate half")
print("Return the number to your friend")

donate = (total/2)
left = donate - friend

print("You are left with",left)
