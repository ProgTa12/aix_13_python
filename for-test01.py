import random

#로또추출방법
nums = list(range(1,46))
print('nums',nums)

mylotto = []

for a in [1,2,3,4,5,6]:
    r = random.randint(0,len(nums)-1)
    mylotto.append(nums[r])
    nums.pop(r)

mylotto.sort()
print('mylotto', mylotto)