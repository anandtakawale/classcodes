import texttable
def goldensection(f, a, b, epsilon):
    """
    Returns minima for the function f within the interval [a,b]
    epsilon: permissible error
    Also prints the table before returning answer
    """
    itr = 0
    x1 = float(b)
    x2 = float(a)
    #creating a texttable object
    table = texttable.Texttable()
    table.add_row(["Iteration", "a", "b", "x1", "x2", "f(x1)", "f(x2)"])
    while (x1 - x2) >= epsilon:
        #length of region
        l = b - a
        #new x1 and x2
        x1 = a + 0.618 * l
        x2 = b - 0.618 * l
        f1 = f(x1)
        f2 = f(x2)
        #addting rows to table
        table.add_row([itr, a, b, x1, x2, f1, f2])
        #elimination of region
        if f2 < f1:
            b = x1
        elif f1 < f2:
            a = x2
        else:
            a = x2
            b = x1
        itr += 1
    print table.draw() + '\n'
    return (x1 + x2)/ 2

def f(x):
    """
    Returns value of the function of f(x)
    """
    return x**2 + 54 / x
    #return x**4 - 15*x**3 + 72*x**2 - 1135*x


