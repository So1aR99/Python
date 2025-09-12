import datetime

now_date = datetime.datetime.now()

print(now_date)
print(type(now_date))
print(now_date.year, "년")
print(now_date.month, "월")
print(now_date.day, "일")
print(now_date.hour, "시")
print(now_date.minute, '분')
print(now_date.second, '초')

print(f'현재는 {now_date.year}년 {now_date.month}월 {now_date.day}일'
      f' {now_date.hour}시 {now_date.minute}분 {now_date.second}초')
