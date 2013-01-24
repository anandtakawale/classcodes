import texttable

def fibonacciMethod(f, a, b, epsilon):
    """
    Returns minima of the function
    """
    #calculating number of iterations
    fn = (b - a) / epsilon
    n = fibFinder(fn)
    k = 0
    table = texttable.Texttable()
    table.add_row(["Iteration", "a", "b", "x1", "x2", "f(x1)", "f(x2)"])
    while k <= (n - 3):
        l = float(b - a)
        #creating factor obtained from fibonacci series
        factor = float(fib(n-k-1))/ fib(n-k)
        x1 = a + (1 -  factor) * l
        x2 = a + factor * l
        f1 = f(x1)
        f2 = f(x2)
        #adding rows to table
        table.add_row([k, a, b, x1, x2, f1, f2])
        #elimination of region
        if f2 < f1:
            a = x2
        elif f1 < f2:
            b = x1
        else:
            a = x2
            b = x1
        k += 1
    print table.draw() + '\n'
    return (x1 + x2) / 2


def fibFinder(fibo):
    """
    Returns number n such that fib(n) > fibo
    """
    n = 1
    while fib(n) < fibo:
        n += 1
    return n

def f(x):
    """
    Returns value of the function of f(x)
    """
    #return x**2 + 54 / x
    return x**4 - 15*x**3 + 72*x**2 - 1135*x

def fib(x, cache = {}):
    """
    Returns fibonacci series by using dynamic programming.
    Observe use of dictionary cache.
    """
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        if x not in cache.keys():
            cache[x] = fib(x-1) + fib(x-2)
        return cache[x]
