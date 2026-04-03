m1 = {"name": "어벤저스 엔드게임", "type": "히어로 영화"}

# print(m1)

# 학생 정보
st1 = {"name": "홍길동", "hakbun": 1120}

print(st1["name"])  # 홍길동
print(st1["hakbun"])  # 1120

scoreDict = {
    "홍길동": [80, 70, 90],
    "김길동": [70, 70, 90],
}

print(scoreDict["홍길동"])  # [80,70,90]
# 문제 발생, 홍길동의 수학점수를 알 수 없어요
# 구조 변경하세요

scoreDict = {
    "홍길동": {"guk": 80, "math": 70, "eng": 90},
    "김길동": {"guk": 70, "math": 70, "eng": 90},
}

print("홍길동의 수학점수", scoreDict["홍길동"]["guk"])  # 80
# print("홍길동의 수학점수", scoreDict["홍길동"]["gu"]) # 에러(값이 없기 떄문)

n = "홍길동"
dict2 = {n: 90}

print(dict2)

# 추가 및 덮어쓰기
dict3 = dict()  # 빈 사전
print(dict3)
dict3["a"] = 70
dict3["b"] = 80
print(dict3)

dict3["a"] = 100
# dict3["b"] = 80
# print(dict3)

# del dict3["a"]
# print("삭제 후", dict3)
# del dict3["b"]

# ##### 학생점수관리
# scores = dict()
# scores["홍길동"] = {"guk": 70, "math": 80, "eng": 90}
# scores["박길동"] = {"guk": 80, "math": 90, "eng": 70}
# name = input("학생이름: ")
# # if name in scores:
# #     print(f"{name}의 점수 {scores[name]}")
# # else:
# #     print(f"{name}은 미등록학생")

# value = scores.get(name)
# # if value == None:
# #     print(f"{name}은 미등록학생")
# # else:
# #     print(f"{name}의 점수 {scores[name]}")

scores2 = {"홍": 70, "김": 80, "강": 75, "권": 90}

for k in scores2:
    print(f"{k} {scores2[k]}")
