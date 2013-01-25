import numpy as np
import pylab
def ottoEffi(r2 = 20, k = 1.4):
    """
    Plots efficiency vs compression ratio.
    r2 : last compression ratio
    k: specific heat ratio cp/cv- 1.4 for air standard cycles
    """
    #compression ratio
    r = np.arange(1, r2, 0.1)
    #calculating 
    eta = 1 - 1 / r**(k - 1)
    plotgraph(r, eta, 'Otto cycle')

def dieselEffi(vc, r2 = 20, k =1.4):
    """
    Plots efficiency vs compression ratio for diesel cycle.
    vc: cutoff ratio v3/v2 > 1
    r2: last compression ratio
    k: specific heat ratio
    """
    # compression ratio
    r = np.arange(1, r2, 0.1)
    #calculating efficiency
    eta = 1 - 1/r**(k - 1) *( vc**k - 1) / (k*(vc - 1))
    plotgraph(r, eta, 'Diesel cycle')

def plotgraph(x, y, title):
    """
    Helper function for plotting graphs.
    """
    pylab.plot(x, y, label = title)
    pylab.xlabel('Compression ratio')
    pylab.ylabel('Efficiency')

if __name__ == '__main__':
    pylab.figure()
    ottoEffi()
    dieselEffi(2)
    pylab.legend(loc = 'best')
    pylab.show()
    
