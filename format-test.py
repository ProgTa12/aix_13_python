#구구단출력 - 3단
# 3 * 1 = 3
# 3 * 2 = 6
# dan = input("단 입력: ")
# print("{} * {} = {}".format(dan,1,dan*1))
# print("{} * {} = {:5s}".format(dan,1,dan*1))

print("헬러 python 프로그래밍".upper)
a = """
    헬로 파이썬 프로그래밍
"""
print(a.strip())
print("안녕123".isalnum())
print("abc abc programming".find("bc"))    # 1
print("abc abc programming".find("bc", 2)) # 5
print("abc abc programming".find("bc", 6)) # -1

a = "안녕하세요"
print("안녕" in a) #True
print("잘자" in a) #False

b = "홍,김,박,감".split(",")
print(b)
b = "100,200,300,400".split(",")
print(b)
print(type(b[0]))       #str형
print(type(int(b[0])))  #int형

#합과 평균
total = 0
mean = 0

total = int(b[0]) + int(b[1]) + int(b[2]) + int(b[3])
mean = total / 4.0

print("total = ", total)
print("Average = ", mean)
#다른 표현
print("total = {}, Average = {}".format(total, mean))

print(f"total={total}")
print(f"Average={mean}")

#구구단 3단
dan = 3
print(f"{dan} * {1} = {dan * 1}")
print(f"{dan} * {2} = {dan * 2}")
print(f"{dan} * {3} = {dan * 3}")

#생년을 입력받아 나이를 계산해서 출력하기
year = input("태어난해 4자리를 입력하세요: ")
age = 2026-int(year)
print(f"당신은 {age}살 입니다.")