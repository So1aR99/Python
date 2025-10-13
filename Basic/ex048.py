# f(x) = x

def f(x):
    return x
print(f(2))

def f1(x):
    return (2 * x) + 1
print(f1(10))

def f2(x):
    return (x ** 2) + (2 * x) + 1
print(f2(10))

# 매개변수를 모두 곱하는 함수
def mul(*values):
    result = 1
    for value in values:
        result *= value
    return result
print(mul(5, 7, 9, 10))

# 반환 값 이용한 3의 배수 합계
def sum_besu3(n):
    sum = 0
    for i in range(1, n):
        if i % 3 == 0:
            sum = sum + i
    return sum
num = int(input('양의 정수를 입력하세요: '))
result = sum_besu3(num)
print('1 ~ %d까지의 정수 중 3의 배수의 합 : %d' % (num, result))

# 세 수중 가장 큰 수 찾기
def maxTwo(i, j):
    if i > j:
        return i
    else:
        return j
def maxThree(x, y, z):
    return maxTwo(x, maxTwo(y, z))
a = int(input("첫 번째 수를 입력하세요: "))
b = int(input("두 번째 수를 입력하세요: "))
c = int(input("세 번째 수를 입력하세요: "))
max_num = maxThree(a, b, c)
print("%d, %d, %d 중 가장 큰 수 : %d" % (a, b, c, max_num))

# 최소 공배수 구하기
def computeMinGong(x, y):
    if x > y:
        big = x
    else:
        big = y
    while(True):
        if((big % x == 0) and (big % y == 0)):
            result = big
            break
        big = big + 1
    return result
num1 = int(input("첫 번째 수를 입력하세요: "))
num2 = int(input("두 번째 수를 입력하세요: "))
min_gong = computeMinGong(num1, num2)
print('%d와 %d의 최소공배수 : %d' % (num1, num2, min_gong))
