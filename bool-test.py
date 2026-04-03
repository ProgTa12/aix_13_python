print(10 == 100) # False
print(10 != 100) # True
print(10 < 100)  # True
print(10 > 100)  # False
print(10 <= 100) # True
print(10 >= 100) # False

# 문자는 문자의 순서에 따라 다르다. 한글은 가 > 나 > 다, 영어는 a > b > c순
a = "가방"
b = "하마"
print(a == b) # False
print(a != b) # True
print(a < b)  # True
print(a > b)  # False

c = 25
print(10 < c < 30) # True
print(10 < c < 20) # False

if c < 30:
    print("c는 30보다큼")
print("END")

c = 30
if c < 30:
    print("c는 30보다 큼")
print("END")

c = 35
if c < 30:
    print("c는 30보다 큼")
else: 
    print("정답")
print("END")

if not c < 30:
    print("c는 30보다 작음")
else:
    print("c는 30보다 큼")

score = 88
if score >= 90:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
else:
    grade = "F"

print(f"당신의 학점은 {grade}입니다.")

if score <= 100 and score >= 90:
    grade = "A"
elif score <= 89 and score >= 80:
    grade = "B"
elif score <= 79 and score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"당신의 학점은 {grade}입니다.")