def verify_anagrams(first_word, second_word):
    s_w=[]
    for i in second_word.lower():
        if i != ' ': s_w.append(i)
    n = 0
    l = len(s_w)
    for i in first_word.lower():
        if i not in s_w and i != ' ': return False
        elif i != ' ':
            n += 1
            del (s_w[s_w.index(i)])
    if n < l: return False
    else: return True

print(verify_anagrams("Kings Lead Hat", "Talking Heads"))
print(verify_anagrams("Hamlet", "Amleth"))
print(verify_anagrams("Kyoto", "Tokyo"))