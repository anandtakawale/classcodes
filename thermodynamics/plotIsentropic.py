import pylab
import numpy as np

def plotIsentropic(p1, p2, v1):
    """
    Plots isentropic process on the grpah.
    Assumes p2 > p1
    Hence assumes its compression
    """
    #considering monoatomic gas
    n = 1.4
    #determining constant on p*v**n = c
    c = p1 * v1**n
    #initializing step
    step = (p2 - p1) / 100.0
    #creating array for p values
    p = np.arange(p1, p2, step)
    #determining corresponding volumes at each point
    v = (c / p) **(1/n)
    pylab.plot(v, p, label = "Isentropic process C = " + str(c))
    pylab.title("Isentropic process")
    pylab.xlabel("Volume")
    pylab.ylabel("Pressure")
    pylab.legend(loc = 'best')

def plotIsothermal(p1, p2, v1):
    """
    Plots isothermal process
    """
    #determining constanr
    c = p1 * v1
    #initializing step
    step = (p2 - p1) / 100.0
    #creating array of p values
    p = np.arange(p1, p2, step)
    #determining corresponding volumes at each point
    v = (c / p)
    pylab.plot(v, p, label = "Isothermal process C = " + str(c))
    pylab.legend(loc = 'best')


    

if __name__ == "__main__":
    pylab.figure()
    plotIsentropic(4, 10, 10)
    plotIsothermal(4, 10, 10)
    pylab.show()
