from matrix import *
import sys
import matplotlib.pyplot as plt

file = sys.argv[1]
dataMatrix = loadtxt(file)
transposeMatrix = transpose(dataMatrix)

x = [float(i) for i in transposeMatrix[0]]
y = [float(i) for i in transposeMatrix[1]]

"""Calculates Y2 values using linear regression formulas"""
Xp  = powers(x,0,1)
Yp  = powers(y,1,1)
Xpt = transpose(Xp)
[[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))
Y2 = [(b +(i * m)) for i in x]

plt.plot(x,y,'ro')
plt.plot(x,Y2)
plt.show()
