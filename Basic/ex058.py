import random

hanguls = list("가나다라마바사아자차카타파하")

with open("info.csv", "w", encoding="utf-8") as file: # 엑셀에서 안깨짐 cp949, 표준은 utf-8
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)

        file.write("{}, {}, {}\n".format(name, weight, height))