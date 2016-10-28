CONV_TABLE = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))
def checkio(data):
    if data <= 0: return ''
    ret = ''
    for arab, roman in CONV_TABLE:
        while data >= arab:
            ret += roman
            data -= arab
    return ret

print(checkio(6))
print(checkio(13))
print(checkio(101))
print(checkio(185))
print(checkio(76))
print(checkio(499))
print(checkio(3888))