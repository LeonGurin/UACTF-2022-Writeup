**Peter works at Bendigo** 

Peter: "Welcome to Bendigo, I am Peter. How may I help you today?" Albert: "Hey! I have my bank card here, but I cannot seem to be able to read the credit card numbers on it as some of them are scratched off. I was wondering if you could tell me what they were if I could confirm my identity to you." Peter: "Ohh, unfortunatly I cannot do that. You are going to have to order a new credit card. If you requested one now, it should arrive by 2nd of August. Would you like me to do this for you?" Albert: "Hmm, unfortuately I need it sooner than that. I'll see if I can remember it in the mean time. THANKS PETER..." Peter: "See you!"

![img1](https://github.com/LeonGurin/UACTF-2022-Writeup/blob/main/Peter%20works%20at%20Bendigo/leaked.png)

The flag is the bankcard number wrapped in UACTF{...}.

Author: Lachlan

___
First I looked up how credit card numbers are validated and found my answers in `StackOverflow` [discussion](https://stackoverflow.com/questions/40688156/python-credit-card-validation).

I tried just replacing the `X`-ed out numbers with using a script that incremented them from 0 but it gave me a lot more valid numbers than I expected which were not asociated with the right card. 

I looked again at the prompt and realised that the card was a `Bendigo` card which means its first 6 numbers are out there in the world known as the `Issuer identification number`.

After finding them: `519244`, and running my final version of the script again:

```python
# this portion is from the stackoverflow thread, credit to: [Refah Mahaboob Shaik]
def validator(n):
    validatelist=[]
    for i in n:
        validatelist.append(int(i))
    for i in range(0,len(n),2):
        validatelist[i] = validatelist[i]*2
        if validatelist[i] >= 10:
            validatelist[i] = validatelist[i]//10 + validatelist[i]%10
    if sum(validatelist)%10 == 0:
        print(n)
second = 0
third = 0
while True:
    f = "519244668" + str(second) + "125" + str(third) + "57"
    if (len(f) == 16):
        validator(f)
    third += 1
    if third == 10:
        third = 0
        second += 1
        if second == 10:
            break
# 5192446687125957
```

gave me only those numbers to try out:

```
5192446680125657
5192446681125557
5192446682125457
5192446683125357
5192446684125257
5192446685125157
5192446686125057
5192446687125957
5192446688125857
5192446689125757
```

Trying them one by one finally got me the flag with:

> UACTF{5192446687125957}