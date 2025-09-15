import random

for _ in range(5):
    balls = [ball for ball in range(1, 46)]
    random.shuffle(balls)
    choice_balls = []
    for _ in range(6):
        random.shuffle(balls)
        choice_balls.append(balls.pop())
    choice_balls.sort()
    print(choice_balls)


#balls = [ball for ball in range(1, 46)] # 공들을 로또 구에 넣기
##balls = []
##for ball in range(1, 46):
##    balls.append(ball)
#print(balls)
#random.shuffle(balls) # 공 섞기
#print(balls)
#choice_balls = []
#for _ in range(6):
#    random.shuffle(balls)
#    choice_balls.append(balls.pop()) # 45 -> 44 -> 43...
#print(choice_balls)
#choice_balls.sort()
#print(choice_balls)