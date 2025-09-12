char = input('영어 소문자 하나를 입력하세요 : ')

if char in 'aeiou':
    print('%s -> 모음' % char)
else:
    print('%s -> 자음' % char)