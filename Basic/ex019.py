import datetime

now = datetime.datetime.now()
m = now.month

if 3 <= m <= 5:
    print("현재는 봄입니다.")
elif 6 <= m <= 8:
    print('현재는 여름입니다.')
elif 9 <= m <= 11:
    print("현재는 가을입니다.")
else:
    print("현재는 겨울입니다.")