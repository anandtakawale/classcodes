import texttable

def intervalHalving(f, a, b, n):
    """
    Returns the final interval of uncertainty of function f using interval halving.
    f: function to be minimized
    (a, b): initial interval of uncertainty
    n: number of function evaluations >= 3

    Final interval of uncertainty is
    L_n = (1 / 2)**((n-1)/2) * L_0
        where L_0: initial interval of uncertainty
    """
    j = 3 #As it requires 3 function evaluations in the first step
    tablelist = []  #list to be passed to print table
    tablelist.append(["j", "a", "b", "x1", "x0", "x2", "f(x1)", "f(x0)", "f(x2)"])
    while j <= n:   # continue iterating untill j becomes n
        L_0 = float(b - a)  #initial interval of uncertainty
        #intitializing points of function evaluations
        x0 = a + L_0 / 2
        x1 = a + L_0 / 4
        x2 = b - L_0 / 4
        #Function of function evalution
        f0 = f(x0)
        f1 = f(x1)
        f2 = f(x2)
        tablelist.append([j, a, b, x1, x0, x2, f1, f0, f2])
        #eliminating interval
        if f1 < f0 < f2:
            b = x0
        elif f1 > f0 > f2:
            a = x0
        else:
            a = x1
            b = x2
        j = j + 1
    tablePrint(tablelist)
    return (a, b)

def tablePrint(l):
    """
    (list of lists) --> None
    Prints the table of the list of lists
    """
    table = texttable.Texttable()
    for row in l:   # for each list in l
        table.add_row(row)
    print table.draw()
    return None

def f(x):
    """
    Returns value of the function of f(x)
    """
    return x**2 + 54 / x

if __name__ == '__main__':
    print intervalHalving(f, 0, 10, 10)
