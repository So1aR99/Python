list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력> "))
    print(f"{number_input}번째 요소: {list_number[number_input]}")
except ValueError as e:
    print("정수를 입력해주세요!")
    print("exception:", e)
except IndexError as e:
    print("리스트의 인덱스를 벗어낫어요!")
    print("exception:", e)