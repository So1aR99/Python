r = int(input('구의 반지름을 입력해주세요: '))
pi = 3.141592
volume = (4 / 3) * pi * (r ** 3)
print("= 구의 부피는 {:.2f}입니다.".format(volume))
area = 4 * pi * (r ** 2)
print(f"= 구의 겉넓이는 {area}입니다.")
