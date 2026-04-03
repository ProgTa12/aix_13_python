import datetime

now = datetime.datetime.now()

print(now)
print(f"{now.year}년")
print(f"{now.month}월")
print(f"{now.day}일")
print(f"{now.weekday()}요일")
print(f"{now.hour}시")
print(f"{now.minute}분")
print(f"{now.microsecond}초")

if now.hour < 12:
    print(f"현재시간 오전{now.hour}시 입니다.")
else:
    print(f"현재시간 오후{now.hour}시 입니다.")

if now.month >= 3 and now.month <=5:
    print(f"지금은 {now.month}월이므로 봄입니다.")
elif now.month >= 6 and now.month <=8:
    print(f"지금은 {now.month}월이므로 여름입니다.")
elif now.month >= 9 and now.month <=11:
    print(f"지금은 {now.month}월이므로 가을입니다.")
elif now.month >= 12 and now.month <=2:
    print(f"지금은 {now.month}월이므로 겨울입니다.")    
else:
    print("오류 발생했습니다.")

number = input("정수 입력: ")
last_character = number[-1]

if last_character in "02468":
    print("짝수입니다")
else :
    print("홀수입니다")