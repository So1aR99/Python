value = 1 + 2
str1 = "Hello" + 'World'
str2 = "Hello".__add__("World")
print(value)
print(str1)
print(str2)
str3 = "Hello" * 5 # 문자열 5번 복사, "Hello" + 5 는 불가 문자 + 숫자하려면 숫자에 큰따옴표 붙여 문자열로 인식해야함
print(str3)
str4 = 'Hello'.__mul__(5)
print(str4)

print("=" * 50) # 문자열 반복 연산자
print("-" * 50)
print("*" * 50)

# int ary[6] = {1, 2, 3, 4, 5, 6}
str5 = "안녕하세요"
print(str5[0])  # 안
print(str5[1])  # 녕
print(str5[2])  # 하
print(str5[3])  # 세
print(str5[4])  # 요

print(str5[-1]) # 요
print(str5[-2]) # 세
print(str5[-3]) # 하
print(str5[-4]) # 녕
print(str5[-5]) # 안
