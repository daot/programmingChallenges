eod = input("encode (e) or decode (d): ").upper()
uin = input("input > ").upper()
key = input("key > ").upper()

key = ''.join(sorted(set(key), key=key.index))

alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
clean = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '

i = 0
while i < len(key):
    alph = alph.replace(key[i], '')
    i += 1
key = key + alph

if(eod == 'E'):
    for i in uin:
        print(clean[key.index(str(i))], end='')
if(eod == 'D'):
    for i in uin:
        print(key[clean.index(str(i))], end='')
