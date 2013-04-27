import texttable
def dichotomousSearch(f, a, b, d, n):
    """
    Returns minima of function f using dichotomous search
    (a, b): initial interval of uncertainty
    d: differnce between positions of two experiments
    n: number of function evaluations n should be even

    L_n = L_0 / 2**(n/2) + d / L_0 *(1 - 1 / 2**(n/2))
        Where, L_0 = initial interval of uncertainty = b - a
    """
    j = 2
    table = texttable.Texttable()
    table.add_row(["Function evals", "a", "b", "x1", "x2", "f(x1)", "f(x2)"])
    while j<= n:
        L_0 = b - a
        x1 = a + L_0 / 2.0 - d / 2.0
        x2 = x1 + d
        f1 = f(x1)
        f2 = f(x2)
        table.add_row([j, a, b, x1, x2, f1, f2])
        if f1 < f2:
            b = x2
        elif f1 > f2:
            a = x1
        else:
            a = x1
            b = x2
        j += 2
    print table.draw() + '\n'
    return (a, b)


def f(x):
    """
    Returns value of the function of f(x)
    """
    return x**2 + 54 / x
    #return x**4 - 15*x**3 + 72*x**2 - 1135*x
    #return np.sqrt((90*x - 30)**2 + (60*x)**2)
    #return -(12*x**5 - 45*x**4 + 40*x**3 + 5)
    #return np.sqrt(x**2 + (8*x / (x-3))**2)
    #return np.exp(x) - x**3
    #return -(2*np.sin(x) - x**2 / 10.0)

if __name__ == '__main__':
    print dichotomousSearch(f, 0, 10, 0.001, 10)
