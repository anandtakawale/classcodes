import texttable
import numpy as np
import pylab

def goldensection(f, a, b, epsilon):
    """
    Returns minima for the function f within the interval [a,b]
    epsilon: permissible error
    Also prints the table before returning answer
    """
    itr = 0
    x1 = float(b)
    x2 = float(a)
    #plotting of function in the range
    funcplot(f, a, b, 1000)
    #creating a texttable object
    table = texttable.Texttable()
    table.add_row(["Iteration", "a", "b", "x1", "x2", "f(x1)", "f(x2)"])
    while (b - a) >= epsilon:
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
    answer = (x1 + x2)/ 2.0
    pylab.plot(answer, f(answer), 'ro')
    pylab.show()
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


def funcplot(f, a, b, pts):
    """
    Plots function f in the guven range from a to b with pts as number of function evaluations.
    Function assumes that b > a and h
    """
    pylab.figure()
    h = float(b - a)/ (pts - 1)
    x = np.arange(a, b, h)
    y = f(x)
    pylab.plot(x, y)
    pylab.title("Function plot")
    pylab.xlabel("x")
    pylab.ylabel("f(x)")

if __name__ == '__main__':
    print goldensection(f, 0.1, 6, 0.0002) #to get minima
