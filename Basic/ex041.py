numbers = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
counter = {}
for number in numbers:
    counter[number] = numbers.count(number)
print(numbers,f'에서 사용된 숫자의 종류는 {len(counter)}개입니다')
print(f'참고: {counter}')
