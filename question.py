#188p 도전 문제 1
q = input("입력: ")

if "안녕" in q:
    print("안녕하세요")
elif "몇 시"  in q:
    print("지금은 15시입니다.")
else:
    print(f"{q}")

#------------------------------------------------------------------

#189p 도전 문제 2
num = input("정수를 입력해주세요: ")
num = int(num)
list = [2,3,4,5]

for i in list:
    if num % i == 0:
        print(f"{num}는(은) {i}로 나누어 떨어지는 숫자입니다.")
    else:
        print(f"{num}는(은) {i}로 나누어 떨어지는 숫자가 아닙니다.")

#------------------------------------------------------------------

# 213p 확인문제 1
list_a = [0, 1, 2, 3, 4, 5, 6, 7]

list_a.extend(list_a)   #[0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7]
list_a.append(10)       #[0,1,2,3,4,5,6,7,10]
list_a.insert(3,0)      #[0,1,2,0,3,4,5,6,7]
list_a.remove(3)        #[0,1,2,4,5,6,7]
list_a.pop(3)           #[0,1,2,4,5,6,7]
list_a.clear()          #[]

#------------------------------------------------------------------

# 214p 확인문제 2
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number > 100:
        print("- 100 이상의 수:", number)

#------------------------------------------------------------------

# 214p 확인문제 3
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for num in numbers:
    if num % 2 == 0:
        print(f"{num}는 짝수입니다.")
    else:
        print(f"{num}는 홀수입니다.")

for num in numbers:
    if num // 1 >= 100:
        print(f"{num}는 3자리수입니다.")
    elif num // 1 >= 10:
        print(f"{num}는 2자리수입니다.")
    else: 
        print(f"{num}는 1자리수입니다.")

#------------------------------------------------------------------

# 215p 확인문제 4

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [] ,[]]

for number in numbers:
    output[(number-1) % 3].append(number)

print(output)

#------------------------------------------------------------------

# 215p 확인문제 5

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0, len(numbers) // 2):
    j = i + (i+1)
    print(f"i = {i}, j = {j}")
    numbers[j] = numbers[j] ** 2

print(numbers)