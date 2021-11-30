def fibo_gen(n_max: int):
    a = 0
    b = 1
    n = 1
    while a <= n_max:
        yield a
        a = b
        b = n
        n = a + b


g = fibo_gen(10)
print(g)
print(list(g))
