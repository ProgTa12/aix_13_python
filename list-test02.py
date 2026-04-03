import random

#로또번호생성
mylotto = []


for a in [1,2,3,4,5,6]:
    r = random.randint(1,45)
    if r not in mylotto:
        mylotto.append(r)
    if len(mylotto) == 6:
        break
    

mylotto.sort()
print(mylotto)

