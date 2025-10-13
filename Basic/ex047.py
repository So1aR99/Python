def print_n_times(*args, n=2):
    for _ in range(n):
        for arg in args:
            print(arg)
        print()

print_n_times("안녕하세요.", "즐거운", "파이썬 프로그램")

def test(a, b=10, c=100):
    print(a + b + c)

test(10, 20, 30)
test(100)
test(100, 20)
#test()

def return_test() -> None:
    return

value = return_test()
print(value)