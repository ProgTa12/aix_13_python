'''
금광찾기게임(GoldMinder)
가로 세로 10x10공간안에 컴퓨터가 임의의 좌표에 금을 숨김
사용자가 임의의 x,y좌표를 입력하면
금과의 직선거리를 정수로 반환.
정확한 좌표입력시 "금을 찾았읍니다" 출력
### 금광찾기게임 v0.1 ###
금의 좌표를 입력하세요(10x10이내 x,y) 5,7
금과의 직선거리 : 5
+ + + + + + + + + +
+ + + + + + + + + +
+ + + + + + + + + +
+ + + + 5 + + + + +
+ + + + + + + + + +
+ + + + + + + + + +
+ + + + + + + + + +
'''

import random

com_x = random.randint(1, 10)
com_y = random.randint(1, 10)
gold_mine = [["+" for _ in range(10)] for _ in range(10)]
print("### 금광찾기게임 v0.1 ###")

while True:
    ans = input("금의 좌표를 입력하세요(10x10이내 x,y)>> ")
    coords = ans.split(',')
    user_x = int(coords[0])
    user_y = int(coords[1])

    is_correct = (user_x == com_x and user_y == com_y)
    gold_mine[user_y - 1][user_x - 1] = "💣" if is_correct else "❌"
    dist = round(((com_x - user_x)**2 + (com_y - user_y)**2)**0.5)

    print("\n--- 금광 ---")
    for row in gold_mine:
        print("    ".join(row))
    print("----------------------")

    if is_correct:
        print(f"금을 찾았습니다. (좌표: {user_x}, {user_y})")
        break

    print(f"금과의 직선거리는 {dist}입니다.")