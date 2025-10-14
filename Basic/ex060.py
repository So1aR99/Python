def test():
    print("함수가 호출")
    yield "TEST"

print("A 지점 통과")
print(test())
print("B 지점 통과")
test()