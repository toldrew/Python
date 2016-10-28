def checkio(data):

    def su(lst):
        nonlocal s
        s += lst[0]

        if len(lst) > 1:
            su (lst[1:])
    s = 0
    su(data)
    return s

print(checkio([1, 2, 3]))