value = input("숫자를 넣어주세요    ")
if value.isdecimal():
    result = int(value) + 1000
    print(result)
else:
    print("숫자를 넣어주세요")

print("안녕" in "안녕하세요")