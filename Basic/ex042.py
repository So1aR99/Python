dna = input("염기 서열을 입력해주세요: ")
a = 0
t = 0
g = 0
c = 0
for i in range(0, len(dna)):
    if dna[i] == 'a':
        a += 1
    if dna[i] == 't':
        t += 1
    if dna[i] == 'g':
        g += 1
    if dna[i] == 'c':
        c += 1
print(f'a의 개수: {a}')
print(f't의 개수: {t}')
print(f'g의 개수: {g}')
print(f'c의 개수: {c}')
