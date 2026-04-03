# def print_n_times(n, *values):  # def print_n_times(*values, n)는 오류 발생
#     for i in range(n):
#         for v in values:
#             print(v)
#         print()


# print_n_times(3, "안녕", "즐거운", "파이썬 프로그래밍")
# # print_n_times(3, 10, 30, 50, 70)


# def print_n_times(*values, n=1):
#     for i in range(n):
#         for v in values:
#             print(v)
#         print()


# print_n_times("안녕", "즐거운", "파이썬 프로그래밍", n=3)


# # greeting(이름) -> 출력: 안녕하세요 이름님
# def greeting(name):
#     return "안녕하세요 " + name + "님"


# ans = greeting("홍길동")  # -> 안녕하세요 홍길동님
# print(ans)


# 입력받은 숫자들의 평균계산하는 함수
# def calc_avg(*values):
#     sum = 0
#     for i in values:
#         sum += i
#     return round(sum / len(values), 2)


# ans = calc_avg(10, 20, 40, 50)
# print(ans)


# def get_grade(score):
#     grades = {10: "A", 9: "A", 8: "B", 7: "C"}
#     return grades.get(score // 10, "F")


# score = int(input("점수를 입력하세요: "))
# print(get_grade(score))

import random


def get_gbb():
    options = ["가위", "바위", "보"]
    ans = random.randint(0, 2)
    return options[ans]


# 다른 예시
# # r = random.randint(0,2)
# # arr = '가위, 바위, 보'.split(',')
# # return arr[r]

# ans = get_gbb()
# print(ans)


def fac(n):
    if n == 0:
        return 1
    return n * fac(n - 1)


ans = fac(3)
print("fac(3) = ", ans)
