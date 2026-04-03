print(range(3))  # range(0, 3)
print(list(range(3)))  # [0, 1, 2]
print(range(1, 46))  # range(1, 46)
print(list(range(1, 46)))  # [1, 2, 3, 4, ... 45]
print(list(range(1, 46, 5)))  # [1, 6, 11, 16, 21, 26, 31, 36, 41]
print(list(range(5, 1, -1)))  # [5,4,3,2]

dan = 1
for n in list(range(1, 10)):
    print(f"{dan} * {n} = {dan * n}")

for i in list(range(1, 10)):
    for n in list(range(1, 10)):
        print(f"{i} * {n} = {i * n}")
    print("\n")

i = 0
while i < 3:  # i가 3보다 작은 동안 실행
    print(f"i = {i}")
    i += 1

# print(f"while end i = {i}")
# print("end")

# while i < 10:  # 1 ~ 10
#     print(f"i={i}")
#     i += 1
#     if i == 2:
#         break

ns = [5, 15, 6, 20, 7, 25]

for n in ns:
    if n < 10:
        continue
    print(n)
