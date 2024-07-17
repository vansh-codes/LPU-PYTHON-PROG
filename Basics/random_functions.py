import random
x=[1,2,3,4]
y=[1,2]
for i in range(2):
    print("Random: ",random.random())
    print("Randint: ",random.randint(1,10))
    print("Randrange: ",random.randrange(1,10))
    print("Shuffle: ",random.shuffle(y))
    print("Choice: ",random.choice(x))
