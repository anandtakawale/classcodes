import xlrd
import pylab


def readData(fileName, Col):
    """
    Reads data from file 'fileName' with column number Col
    """
    book = xlrd.open_workbook(fileName)
    sheet = book.sheet_by_index(1)
    dim = []
    for row in range(1, 234):   #cashew data from row 1 to 233
        dim.append(sheet.cell_value(row, Col))
    return dim

def scatterPlot(x, y, title):
    pylab.figure()
    pylab.plot(x, y, 'o')       #plot points
    pylab.xlabel(title.split(' ')[0] + " (in mm)")
    pylab.ylabel(title.split(' ')[2] + " (in mm)")
    pylab.title(title)

def muSigma(dimension):
    """
    Returns the mean and the standard deviation of the dimension.
    """
    mean = sum(dimension) / len(dimension)
    tot = 0.0
    for dim in dimension:
        tot += (dim - mean)**2
    stddev = (tot / (len(dimension) - 1))**0.5 #as sample is drawn from population
    return mean, stddev

def correlationCoeff(X, Y):
    """
    Returns the correaltion coefficient for the lists X and Y
    """
    meanX, sigmaX = muSigma(X)
    meanY, sigmaY = muSigma(Y)
    correl = []
    for i in range(len(X)):     #for each dimension in X and Y
        z1 = (X[i] - meanX) / sigmaX    #std unit for X
        z2 = (Y[i] - meanY) / sigmaY    #std unit for Y
        correl.append(z1 * z2)  #multiplication of std units
    return sum(correl) / len(correl)

def stdRegressionPlot(X, Y, r, title):
    """
    Plots the scatter plot in standard variable along with the regression line
    X: First list , will be plotted on X axis
    Y: Second list, will be plotted on Y axis
    r: correlation coefficent
    title: Title of the plot
    """
    xstd = []
    ystd = []
    meanX, sigmaX = muSigma(X)
    meanY, sigmaY = muSigma(Y)
    for i in range(len(X)):
        xstd.append((X[i] - meanX) / sigmaX)
        ystd.append((Y[i] - meanY) / sigmaY)
    pylab.figure()
    pylab.plot(xstd, ystd, 'o')
    pylab.xlabel(title.split(' ')[0])
    pylab.ylabel(title.split(' ')[2])
    pylab.title(title + ' in standard variables')
    x = [min(xstd), max(xstd)]
    y = [r * min(xstd), r * max(xstd)]
    pylab.plot(x, y, label =  "Regression line with r = " + str(r))
    pylab.legend(loc = 'best')

def slopeIntercept(X, Y):
    """
    Returns the slope and intercept of the regression line for X and Y list
    """
    r = correlationCoeff(X, Y)
    meanX, sigmaX = muSigma(X)
    meanY, sigmaY = muSigma(Y)
    slope = sigmaY / sigmaX * r     #slope = mu_y / mu_x * r
    intercept = meanY - slope * meanX
    return slope, intercept
    
def regressionLinePlot(X, Y, slope, intecept):
    """
    Plots the regression line using slope and intercept
    """
    x = []
    y = []
    for i in range(0, len(X), 10):
        x.append(X[i])
        y.append(slope * X[i] + intecept)
    pylab.plot(x,y, label = "Regression Line")

def residualPlot(X, Y, slope, intercept, title):
    """
    Draws the residual plot for the list
    """
    residue = []
    title = title + " Residue Plot"
    for i in range(len(X)):
        regressY = slope * X[i] + intercept
        residue.append(Y[i] - regressY)
    avgResidue = sum(residue) / len(residue)
    pylab.figure()
    pylab.plot(X, residue, 'o')
    #Plotting average residual line
    x = [min(X), max(X)]
    res = [avgResidue, avgResidue]
    pylab.plot(x, res, label = "Residue average line")
    pylab.title(title)
    pylab.xlabel("Breadth (in mm)")
    pylab.ylabel("Residue")
    
if __name__ == '__main__':
    fileName = "cashew_sizes.xls"
    length = readData(fileName, 1)
    breadth = readData(fileName, 2)
    thickness = readData(fileName, 3)
    mulength, sigmalength = muSigma(length)
    mubreadth, sigmabreadth = muSigma(breadth)
    muthickness, sigmathicknes = muSigma(thickness)
    #correlation coefficents
    rBL = correlationCoeff(breadth, length)
    rBT = correlationCoeff(breadth, thickness)
    #slope and intercept for breadth vs length
    slopeBL, interceptBL = slopeIntercept(breadth, length)
    scatterPlot(breadth, length, "Breadth vs Length")
    regressionLinePlot(breadth, length, slopeBL, interceptBL)
    stdRegressionPlot(breadth, length, rBL, "Breadth vs Length")
    residualPlot(breadth, length, slopeBL, interceptBL, "Breadth vs Length")
    #slope and intercept for breadth vs thickness
    slopeBT, interceptBT = slopeIntercept(breadth, thickness)
    scatterPlot(breadth, thickness, "Breadth vs Thickness")
    regressionLinePlot(breadth, thickness, slopeBT, interceptBT)
    residualPlot(breadth, thickness, slopeBT, interceptBT, "Breadth vs Thickness")
    pylab.legend(loc = 'best')
    pylab.show()
