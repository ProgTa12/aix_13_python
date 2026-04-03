# # # try:
# # #     list1 = [10,20,30]
# # #     n = list1[3]
# # #     print(n)
# # # except:
# # #     print("오류 발생")
# # # print("end")

# # list_input_a = ['52', '273','32','스파이','103']

# # list_number = []
# # for item in list_input_a:
# #     try:
# #         float(item)
# #         list_number.append(item)
# #     except:
# #         pass
    
    
# # print(f" 내부에 있는 숫자는 {list_input_a}")
# # print(f"{list_number}입니다.")

# try:
#     number_input_a = int(input("정수 입력: "))
# except:
#     print("정수를 입력하지 않았습니다.")
# else:
#     print("원의 반지름: ", number_input_a)
#     print("원의 둘레: ", 2 * 3.14 * number_input_a)
#     print("원의 넓이: ", 3.14 * number_input_a * number_input_a)

try:
    list1 = [10,20,30]
    n = list1[3]
    print(n)
except Exception as ex:
    print("오류 발생")
    print('TYPE', type)
    print('ex', ex)
print("end")