def left_join(phrases):
    s = ','.join(phrases).replace('right','left')
    return s

print(left_join(("left", "right", "left", "stop")))
print(left_join(("bright aright", "ok")))
print(left_join(("enough", "jokes")))
print(left_join(("brightness wright",)))