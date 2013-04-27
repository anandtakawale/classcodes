import texttable
import math

def fibonacciMethod(f, a, b, epsilon):
    """
    Returns minima of the function
    """
    #calculating number of iterations
    fn = (b - a) / epsilon
    n = fibFinder(fn)
    print n
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
            a = x1
        elif f1 < f2:
            b = x2
        else:
            a = x1
            b = x2
        k += 1
    print table.draw() + '\n'
    return (x1 + x2) / 2

def fibonacciIter(f, a, b, n):
    """
    Fibonacci search method based on number of iterations reuiqred as as per book
    f: function to be minimized
    (a, b): interval of search
    n: number of iterations required
    """
    L2star = float(fib(n - 2))/ fib(n) * (b - a)
    j = 2
    table = texttable.Texttable()
    table.add_row(["Function evals", "a", "b", "x1", "x2", "f(x1)", "f(x2)", "L2"])
    while j <= n:
        L1 = b - a
        if L2star > L1/2.0:
            x2 = a + L2star
            x1 = b - L2star
        else:
            x2 = b - L2star
            x1 = a + L2star
        f1 = f(x1)
        f2 = f(x2)
        #adding row to table
        table.add_row([j, a, b, x1, x2, f1, f2, L2star])
        #eliminating correct interval
        if f2 < f1:
            a = x1
            L2star = float(fib(n - j))/ fib(n - (j - 2)) * (b - a)
        elif f2 > f1:
            b = x2
            L2star = float(fib(n - j))/ fib(n - (j - 2)) * (b - a)
        else:
            a = x1
            b = x2
            L2star = float(fib(n - j))/ fib(n - (j - 2)) * (b - a)
            j += 1
        j += 1
        
    print table.draw(), '\n'
    return a, b
    


    
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
    return x**2 + 54 / x
    #return x**4 - 15*x**3 + 72*x**2 - 1135*x
    #return math.exp(x) - x**3

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

if __name__ == '__main__':
    print fibonacciIter(f, 0, 6, 10)
