def print3_times() -> None:
    for _ in range(3):
        print("안녕하세요")

print3_times()

def print_n_times(value="None", n=1):
    for _ in range(n):
        print(value)

print_n_times("Hello", 2)
print_n_times(n=2, value="World")
print_n_times()