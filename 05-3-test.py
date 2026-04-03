# t1 = (1, 3, 5)
# print(t1)
# print(t1[1])  # 3
# # t1[1] = 4  # 오류ㅡ 튜플은 변경불가능
# t2 = [3]
# print(type(t2))  # <class 'list'>
# t2 = (3,)
# print(type(t2))  # <class 'int'>


# 학생들의 점수를 입력받아 총점과 평균계산
def calc_total_avg(*values):
    total = sum(values)
    avg = total / len(values)
    return total, avg


# total, avg = calc_total_avg(10, 30, 50)
# print("total=", total)  # total
# print("avg=", avg)  # avg


a, b = 10, 20
print(a, b)

print(calc_total_avg)

def print_func(fn):
    fn(); fn(); fn();

def hello():
    print("Hello")

print_func(hello)
