import time
now_time = time.time()
print(now_time)
future_time = now_time + 5.0    # 5초 후 시간

number = 0
while time.time() < future_time:
    number += 1

#while now_time < future_time:
#    number += 1
#    now_time = time.time()

print(number)