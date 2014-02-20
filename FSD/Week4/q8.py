import math

def f(x) :
    return g(x) + math.sqrt(h(x))
def g(x) :
    return 4 * h(x)
def h(x) :
    return x * x + k(x) - 1
def k(x) :
    return 2 * (x + 1)

print(f(2))
print(g(h(2)))
print(k(g(2) + h(2)))
print((f(0)+f(1)+f(2)))
print(f(-1) + g(-1) + h(-1) + k(-1))