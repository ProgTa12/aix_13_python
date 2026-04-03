# # 2차원 리스트
# arr = [1,2,3] # 1차원
# arr2 = [[1,2], [3,4], [5,6]] # 2차원
# arr2[0]
# arr2[0][0]
# arr2[행][열]
# print(arr2)

arr2 = ['*']*10
print(arr2)

arr3 = []
arr3.append(['*']*10)
arr3.append(['*']*10)
arr3.append(['*']*10)
arr3[0][0] = "3"
arr3[1][1] = "1"
arr3[1][3] = "4"
for a in arr3:
    print(" ".join(a))