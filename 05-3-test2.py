'''
숫자맞추기게임(LowHigh)
1~100사이 임의의숫자를 컴퓨터가 정한것을
스무고개 형식으로 맞추는 게임
출력 예시)
1~100사이 숫자 입력>> 70
낮춰주세요
1~100사이 숫자 입력>> 60
높여주세요
1~100사이 숫자 입력>> 65
정답입니다.
'''

# import random

# print("### 숫자맞추기게임 v0.1 ###")
# com = random.randint(1,100)
# num = 0

# while True:
#     num += 1
#     user = int(input(f"{num}번째시도 1~100사이 숫자 입력>> "))
#     if(com == user): 
#         break
#     print("낮춰주세요" if com < user else "높여주세요")
# print(f"정답은 {com}입니다. 정답 입력 횟수 {num}")

import random
print("### 숫자맞추기게임 v0.3 ###")
com = random.randint(1, 100)
low = 1
high = 100

for i in range(1, 7):
    user = int(input(f"{i}번째 시도 {low}~{high} 사이 숫자 입력>> "))
    
    if com == user:
        print(f"정답은 {com}입니다. 정답 입력 횟수 {i}")
        break
    
    low, high, msg = (user+1, high, "높여") if user < com else (low, user-1, "낮춰")
    print(f"{msg}주세요. \n후보 숫자 >> ", *range(low, high + 1))
else:
    print(f"당신은 바보입니까? 정답은 {com}이었습니다.") 