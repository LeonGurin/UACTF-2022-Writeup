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
