import random

com_list = random.sample(range(0, 10), 3)
game_count = 0

while True:
    print(com_list)
    user_list = []
    
    try:
        user_input = input("\n숫자 3개를 입력하세요 (예: 1 2 3): ").split()
        user_list = [int(x) for x in user_input]
        
        if len(user_list) != 3:
            print("숫자 3개가 아닙니다.")
            continue 
    except ValueError:
        print("숫자만 입력 가능합니다.")
        continue
    
    game_count += 1 
    strike = 0
    ball = 0
    
    for i in range(3):
        if com_list[i] == user_list[i]:
            strike += 1
        elif user_list[i] in com_list:
            ball += 1
            
    if strike == 0 and ball == 0:
        print("OUT!")
    else:
        print(f"{strike} Strike, {ball} Ball")
    
    if strike == 3:
        print("3 Strike입니다!")
        break
    
print("-" * 20)
print(f"축하합니다! 3 Strike를 달성했습니다.")
print(f"총 시도 횟수: {game_count}")