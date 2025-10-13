#def recursion():
#    print("재귀함수")
#    return recursion()

#recursion()

def func1():
    print("Hello")

def func2():
    print("World")

def func3():
    print("Android")

func1()
func2()
func3()

def f(n):
    if n == 0:
        return 1
    else:
        result = n * f(n-1)
    return result
print(f(6))