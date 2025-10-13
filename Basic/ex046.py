def print_n_times(n, *values):
    for _ in range(n):
        for value in values:
            print(value)
        print()
print_n_times(3, "안녕", "파이썬", "프로그래밍")