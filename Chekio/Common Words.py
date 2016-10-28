def common_words(first, second):
    first = first.split(',')
    second = second.split(',')
    words =[]
    for i in first:
        if i in second: words.append(i)
    words.sort()
    return ', '.join(words)

print(common_words("hello,world", "hello,earth"))
print(common_words("one,two,three", "four,five,six"))
print(common_words("one,two,three", "four,five,one,two,six,three"))