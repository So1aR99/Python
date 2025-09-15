a = range(1, 10, 2)
print(a)
print(list(range(1, 10, 2)))

b = [range(1, 10, 2)]
print(b)
c = [i for i in range(1, 10, 2)]    # list comprehension
print(c, '\n')

array = [273, 32, 103, 57, 52]

for i in range(len(array)):
    print(f'{i}번째 반복: {array[i]}')

for i in range(len(c)-1, -1, -1):
    print(c[i], end='  ',)
print()

for i in reversed(range(len(c))):
    print(c[i], end='  ')
print()

for item in reversed(c):
    print(item, end='  ')