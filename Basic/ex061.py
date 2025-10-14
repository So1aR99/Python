numbers = [1, 2, 3, 4, 5, 6]
print("::".join(str(numbers).strip().split(", ")))

# yield 양보함
def test():
    print("A지점 통과")
    yield 1 # 주소를 던진다
    print("B지점 통과")
    yield 2
    print("C지점 통과")

output = test()
print("D지점 통과")
a = next(output)
print(a)
print("E지점 통과")
b = next(output)
print(b)
print("F지점 통과")
c = next(output)
print(c)
#output = test() 새로 호출하면 다시 사용 가능