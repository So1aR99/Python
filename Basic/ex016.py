num = input("정수 입력 : ")

last_num = int(num[-1])

if last_num % 2 == 0:
    print("짝수")

if last_num % 2 == 1:
    print("홀수")


x = input("정수 입력 : ")
if x[-1] == '0' or x[-1] == '2' or x[-1] == '4' or x[-1] == '6' or x[-1] == '8':
    print("짝수")
else:

    print("홀수")


x = input("정수 입력 : ")
if x[-1] in '02468':
    print("짝수")
else:
    print("홀수")

