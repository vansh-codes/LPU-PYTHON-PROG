#GP of series :
#1 + 1/2 + 1/3 + ..... + 1/n
n=int(input("Enternum :"))
def geosum(n):
    if n==0:
        return 1
    else:
        return 1/pow(n,1)+geosum(n-1)

print("{:.6f}".format(geosum(n)-1))
