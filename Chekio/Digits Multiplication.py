from functools import reduce
def checkio(n):
    return reduce(lambda a,b:a*b if b!=0 else a,map(int,str(n)),1)
print(checkio(2041))