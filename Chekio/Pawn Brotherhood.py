def safe_pawns(pawns):
    n=0
    for i in pawns:
        if chr(ord(i[0])-1)+str(int(i[1])-1) in pawns or chr(ord(i[0])+1)+str(int(i[1])-1) in pawns: n +=1
    return n

print (safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
print(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}))