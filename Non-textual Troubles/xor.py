from random import seed, randrange
seed(True, version=2)
cipher = 'aÁh»öo:¥ì6Ñ×kT:4¡9ÐEÍ'
l = list()
for char in range(0,48):
        B = randrange(256)
        l.append(B)
A = 0
index = 0
for i in l:
    try: 
        while chr(A ^ i) != cipher[index]:
            A += 1
        print(chr(A),end='')
        index += 1
        A = 0
    except:
        print("")
        break
