def checkio(number):
    return str(bin(number)).count('1')
print(checkio(1022))