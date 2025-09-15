#while True:
#    print('.', end=' ')    # 무한루프

count = 0                   # 초기값
while count < 10:           # 탈출 조건
    print('.', end=' ')
    count += 1              # 탈출 조건을 만들어주는 변수

print()

values = [1, 2, 1, 2, 1, 2, 1, 2]
value = 2
while value in values:
    values.remove(value)

print(values)