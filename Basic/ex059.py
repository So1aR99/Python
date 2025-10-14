from 혼자공부하는파이썬.ex058 import weight, height

with open("info.csv", 'r', encoding="utf-8") as file:
    for line in file:
        (name, weight, height) = line.strip().split(',')

        if not name or not weight or not height:
            continue

        bmi = int(weight) / ((int(height) / 100) ** 2)
        result = ''
        if 25 <= bmi:
            result = '과체중'
        elif 18.5 <= bmi:
            result = '정상 체중'
        else:
            result = '저체중'
        print(f'이름 : {name}\n몸무게 : {weight}\n키 : {height}')
        print(f'BMI : {bmi}')
        print(f'결과 : {result}')