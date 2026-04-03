# 인사말함수
def hello():
    print("안녕하세요")


def hello_3times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")


# def hello_ntimes(n):  # def hello_ntimes(n = 1)로 기본값 설정 가능
#     for i in range(n):
#         print("안녕하세요")


# def hello_whiletimes(n):
#     i = 0
#     while i < n:
#         print("안녕하세요")
#         i += 1


# def hello_msgtimes(msg="안녕하세요", n=1)도 가능
def hello_msgtimes(n=1, msg="안녕하세요"):
    for i in range(n):
        print(msg)


# hello()
# hello_3times()
# hello_ntimes(4)
# hello_whiletimes(4)
# hello_msgtimes(4, "방가방가")

# gugudan(3) -> 3단 구구단 출력
# gugudan() -> 2단 구구단 출력


# def gugudan(num=2):
#     for i in range(1, 10):
#         print(f"{num} * {i} = {num*i}")


# gugudan(5)


def gugudan(n1=1, n2=1):
    if n1 > n2:
        n1, n2 = n2, n1

    for i in range(n1, n2 + 1):
        for j in range(1, 10):
            print(f"{i} * {j} = {i * j}")
        print()


gugudan(6, 3)
