x=int(input("N : "))
try:
    if x>10:
        raise ValueError
    else:
        print("X is less than 10")
except ValueError:
    print("Incorrect Value")
