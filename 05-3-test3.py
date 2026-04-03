'''
금광찾기게임(GoldMinder)
가로 세로 10x10공간안에 컴퓨터가 임의의 좌표에 금을 숨김
사용자가 임의의 x,y좌표를 입력하면
금과의 직선거리를 정수로 반환, 
정확한 좌표입력시 "금을 찾았습니다." 출력
###금광찾기게임 v0.1 ###
금의 좌표를 입력하세요(10x10이내 x,y) --- (5,7)
금과의 직선거리 : 5
'''
import random
###금광찾기게임 v0.1 ###

com_x = random.randint(1,10)
com_y = random.randint(1,10)

while True:
    ans = input("금의 좌표를 입력하세요(10x10이내 x,y)>>")
    user_x, user_y = ans.split(',')
    user_x, user_y = int(user_x), int(user_y)
    
    if(user_x == com_x and user_y == com_y):
        print("금을 찾았습니다.")
        break
    dist = round(((com_x-user_x)**2 + (com_y-user_y)**2)**0.5)
    print(f"금과의 직선거리는 {dist}입니다.")