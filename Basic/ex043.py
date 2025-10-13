numbers = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
new_numbers = [] # 빈 리스트
for number in numbers:
    if type(number) is list:
        #print("대상은 리스트 입니다.")
        for item in number:
            new_numbers.append(item)
    else:
        new_numbers.append(number)
print(new_numbers)
