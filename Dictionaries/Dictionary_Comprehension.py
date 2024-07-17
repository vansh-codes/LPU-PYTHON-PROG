d={i:i*i for i in range(5)}
print(d)

d1={x.lower():x for x in "HEllo WORLD"}
print(d1)

d2={a:b for a in range(5) for b in range(5,10)}     #Error in range of b
print(d2)


