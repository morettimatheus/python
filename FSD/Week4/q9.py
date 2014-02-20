def f(a) :
    if a < 0 :
        return -1
    n = a
    while n > 0 :
        if n % 2 == 0 : # n is even
            n = n // 2
        elif n == 1 :
            return 1
        else :
            n = 3 * n + 1
    return 0

print(f(-1))
print(f(1))
print(f(2))
print(f(10))
print(f(100))