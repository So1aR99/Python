numbers = [number for number in range(10)]
print(numbers)
iterator = reversed(numbers)
print(iterator)

print("첫번째 호출")
for number in iterator:
    print(number, end='  ')
print("\n두번째 호출")
for number in iterator:
    print(number, end='  ')
print("\n세번째 호출")
iterator2 = reversed(numbers)
for number in iterator2:
    print(number, end='  ')
print()

temp = reversed([1, 2, 3, 4, 5, 6])

for i in temp:
    print(f"첫 번째 반복문: {i}")

for i in temp:
    print(f'두 번째 반복문: {i}')