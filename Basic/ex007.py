# const char * str = "Hello";
# *(str + 0) = 'h';
# char str[6] = {"Hello"};
# str[0] = 'h';

str1 = "Hello"
print(len(str1))    # 문자열 길이 5

value = 2 * 2 * 2
value2 = 2 ** 3     # 2의 3제곱
print(value2)
print()

# 변수 선언과 할당
pi = 3.14159265
r = 10

# 변수 참조
print("원주율 =", pi)
print("반지름 =", r)
print("원의 둘레 =", 2 * pi * r)    # 원의 둘레
print("원의 넓이 =", pi * r ** 2)    # 원의 넓이
print("구의 부피 =", 4/3 * pi * r ** 3)     # 구의 부피
