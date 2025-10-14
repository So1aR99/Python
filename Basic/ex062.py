#r = input("반지름의 길이: ")
#if r.isdigit():
#    r = int(r)
#    area = 3.141592 * r ** 2
#    print("넓이는", area)
#else:
#    print("숫자를 넣어주세요.")
try:
    r = int(input("반지름의 길이: ")) # 발생될 수 있는 부분
except Exception as e:
    print("예외 발생")
    print(e)
else:
    area = 3.141592 * r ** 2
    print("넓이:", area)
finally:
    print("이것이 실행")