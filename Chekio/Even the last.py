def checkio(array):
    summ=0
    if len(array) > 0:
        for i in range(0,len(array),2):
            summ+=array[i]
        summ*=array[-1]
    return summ

print(checkio([]))