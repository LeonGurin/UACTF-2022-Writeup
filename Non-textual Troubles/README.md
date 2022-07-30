**Non-textual Troubles**

After messing up the implementation, I have decided that this is a feature and not a flaw.

Note: Intended solution uses Python 3

Author: Javad

___

Knowing that the cipher was using a seed, it was easy to get the right numbers to `xor` the plaintext with.

In my code the `l` list holds the seed xorkeys for each letter encoded.

```python
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
```

The flag turns out to be:
> UACTF{b4d_h4b175_l34d_70_py7h0n2}
