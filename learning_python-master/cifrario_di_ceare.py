import string

def caesar_cypher(text, n):
    text = list(text)
    cod = []
    ret = ''
    for a in text:
        if a.isalpha():
            c = ord(a)
            n = ((n + 26)%26)
            c += n
            if c > 123:
                n = 97 + (c - 123)
                c = n
            d = chr(c)
            ret += d
        else:
            ret += a
    return ret


print caesar_cypher("sopra la panca la capra canta, sotto la panca la capra crepa", 2)
