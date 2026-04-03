def power(item) :
    return item * item

list1 = [1,2,3]
r1 = map(power, list1)

list2 = '10,20,30'.split(',')
print(list2)

list3 = [int(i) for i in list2]
print(list3)

def to_int(c):
    return int(c)

r2 = map(to_int, list2)
print(list(r2))

#짝수만 추출
list4 = [i for i in list1 if i % 2 == 0]
# list4 = []
# for i in list1:
#     if i % 2 == 0:
#         list4.append(i)

def only_even(i):
    return i % 2 == 0

list4 = filter(only_even, list1)

print(type(list4))
print(list(list4))

names = '홍길동, 김길동, 박길동'.split(',')
#김씨만 추출
def only_kim(i):
    return i.strip()[0] == '김' 

kims = list(filter(only_kim, names))
print(kims)

power = lambda x : x * x
print(power(3))

print(list(map(power, [1,3,5])))