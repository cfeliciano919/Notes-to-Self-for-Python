def xo(s):
    letters = list(s.lower())
    if letters.count('x') == letters.count('o'):
        return True
    else:
        return False


print(xo('xxxoo'))

def Xand(s):
    l = s.lower()
    return l.count('x') == l.count('o')

print(Xand('xXoo'))
print('aaabb'.count('b'))
