def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print('Counting...')
    n = 20
    f_n = fib(n)
    print("Fibonacci's " + str(n) + "'th element is " + str(f_n))
