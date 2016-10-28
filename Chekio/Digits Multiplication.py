def checkio(number):
    number=str(number)
    p=1
    for i in number:
        if i != '0': p*=int(i)
    return p
print(checkio(1111))