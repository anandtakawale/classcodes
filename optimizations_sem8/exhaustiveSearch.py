import numpy as np
import texttable

def exhaustiveSearch(f, a, b, n):
    """
    Returns the interval in which minima occurs for following parameters
    f: function to be minimized
    (a, b): interval of uncertainty
    n: number of function evaluations

    >>>
    """
    interval = (b - a) / float(n + 1)
    x = a
    y = []
    table = texttable.Texttable()
    table.add_row(["Iteration", "x", "f(x)"])
    for i in range(n):
        x = x + interval
        y.append(f(x))
        table.add_row([i + 1, x, y[i]])
    print table.draw()
    for i in range(1, n - 1):
        if y[i - 1] <= y[i] <= y[i + 1]:
            return (a + i * interval, a + (i+2) * interval)


def f(x):
    """
    Returns value of function f at x
    """
    return np.exp(x) - x**3


if __name__ == '__main__':
    print exhaustiveSearch(f, 2, 5, 10)
    
