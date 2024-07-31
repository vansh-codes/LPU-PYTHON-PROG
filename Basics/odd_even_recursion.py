def check(x):
    if x<3:
        return x
    else:
        return check(x-2)
y=check(int(input()))

if y==2:
    print('even')
else:
    print('odd')

