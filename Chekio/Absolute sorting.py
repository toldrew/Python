def checkio(numbers_array):
    dic={}
    arr=[]
    for i in numbers_array:
        dic[abs(i)]=i
        arr.append(abs(i))
    arr.sort()
    numbers=[]
    for i in arr:
        numbers.append(dic[i])
    return numbers
print(checkio((-20, -5, 10, 15)))