def square(x):
    return x ** 2

print(square(2))
v1 = [1, 2, 3, 4]
#print(square(v1))     x 오류
result = map(square, v1)
print(result)
for i in result:
    print(i, end="  ")
print()
need1 = lambda x: x ** 2
result2 = list(map(need1, [2, 4, 6, 8]))
print(result2)

result3 = list(map(lambda x: x ** 2, [2, 4, 6, 8, 10])) # 이름없는 함수(한번 사용하고 버림)
print(result3)

network = list(map(lambda x: x > 0.6, [0.1, 0.7, 0.8, 0.3, 0.9, 1.0]))
print(network)

network2 = list(filter(lambda x: x > 0.6, [0.1, 0.7, 0.8, 0.3, 0.9, 1.0]))

print(network2)

# 파일 처리
NT2_file = open("network2_data.txt", 'w', encoding='utf-8')
NT2_file.write(str(network2))
NT2_file.close()
