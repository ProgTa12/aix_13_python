ans = input("나이를 입력하세요: ")
print(f"/{ans}/")
ans = ans.strip()
if ans : #공백이면 False
    print(f"입력값은 {ans}")
else:
    print("입력안함")