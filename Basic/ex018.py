height = int(input('키를 입력해 주세요 : '))
weight = int(input('몸무게를 입력해 주세요 : '))

s = (height - 100) * 0.9
print('=' * 50)
print('키 : ', height)
print('몸무게 : ', weight)

if weight > s:
    print('딱 보기 좋습니다. 경우에 따라 다이어트가 필요합니다!')
else:
    print('표준 또는 마른 체형입니다!')

print('=' * 50)
