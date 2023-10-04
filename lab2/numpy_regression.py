from numpy import *
import sys
import matplotlib.pyplot as plt

"""Takes a list, a start and a stop value as input. 
The function returns a matrix where the first column is the input list and subsequent columns
are the numbers of the first column by the power of the current number in the range start:end"""
def powers(list,start,end):
    matrix=[]
    for j in list:
        row = []
        for i in range(start,end+1):
            row.append(j**i)
        matrix.append(row)
    return array(matrix)

"""Calculates y values for the given x values using the input a values"""
def poly(a,x):
    returnList = []
    for i in x:
        y = 0
        for j in range(len(a)):
            y += a[j]*(i**j)
        returnList.append(y)
    return returnList


file = sys.argv[1]
n = int(sys.argv[2])
dataMatrix = loadtxt(file)
transposeMatrix = transpose(dataMatrix)

x = [float(i) for i in transposeMatrix[0]]
y = [float(i) for i in transposeMatrix[1]]

"""Calculates Y2 values using Polynomial regression formulas"""
Xp  = powers(x,0,n)
Yp  = powers(y,1,1)
Xpt = Xp.transpose()

a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
a = a[:,0]

X2 =linspace(x[0],x[-1]).tolist()
Y2 = poly(a,X2)


plt.plot(x,y,'ro')
plt.plot(X2,Y2)
plt.show()
