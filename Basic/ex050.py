# 피보나치 수열
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)
print(f(1))
print(f(2))
print(f(3))
print(f(4))
print(f(5))
print(f(6))

counter = 0
def f(n):
    print(f"fibonacci({format(n)})를 구합니다.")
    global counter
    counter += 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)
print(f(10))
print(f'counter : {counter}')