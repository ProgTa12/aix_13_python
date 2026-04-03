#댄동회원관리
names = ['홍', '김', '박']
print(names[0])   #김
print(names[1:2]) #김
print(names[1:])  #김 박
n = names[1:]
names[1] = '이'
print(names)
print(names[0][1:]) # [이 박][0] -> 김
print(n[0]) # 김

arr = [ [1,2,3], [4,5,6]]
print(arr[0]) #[1,2,3]
print(arr[1]) #[4,5,6]
print(arr[0][1]) # 2

a = [10,20,30]
b = [40,50,60]
print(a+b)
print(a*3)
print(f"홍길동의 길이 = {len("홍길동")}")
print(len(a+b))
print(len(a*3))