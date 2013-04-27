import numpy as np

def steepestDescent(J, X):
    """
    Returns minima of a function
    X: initial guess as numpy array
    J: function to be minimized
    """
    S = getGradient(J, X)
    if np.sqrt(np.dot(S, S)) < 0.0001:
        return X
    lambda_star = getLambda(J, X, S)
    X_new = X - S * X
    return steepestDescent(J, X_new)

def getLambda(J, X, S):
    
def getGradient(J, X):
    """
    Returns the gradient of a function using Newton's central difference formula
    """
    grad = np.zeros(len(X))
    for i in range(len(X)):
        grad[i] = getPartial(X, J, i) #gets the partial derivative of J w.r.t x_
    return grad

def getPartial(X, J, i):
    """
    Returns the partial derivative of J
    """
    Xmin = X
    Xmax = X
    Xmin[i] = X[i] - 0.001
    Xmax[i] = X[i] + 0.001
    return (J(Xmax) - J(Xmin)) / 0.001 
    
        
def J(X):
    """
    Returns value of function to be minimized at point X
    """
    return 
