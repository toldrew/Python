def min(*args, **kwargs):
    key = kwargs.get("key", None)
    print(key)
    for i in args:
        if i<min: min=i
    return min


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    print(key)
    max=0
    for i in args:
        if i < max: max = i
    return max

#print(max([1, 2, 0, 3, 4]))
print(min("hello"))
print(max(2.2, 5.6, 5.9, key=int))
print(min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]))