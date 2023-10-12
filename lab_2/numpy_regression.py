from numpy import*
import sys
import matplotlib.pyplot as plt

def poly(a,x):
    returnList = []
    for i in x:
        y = 0
        for j in range(len(a)):
            y += a[j]*(i**j)
        returnList.append(y)
    return returnList

def powers(list,a,b):
    matrix = []
    for i in list:
        row = []
        for e in range(a,b+1):
            row.append(i**e)
        matrix.append(row)
    return array(matrix)

file = sys.argv[1]
n = int(sys.argv[2])

dataMatrix = loadtxt(file)

transposedMatrix = transpose(dataMatrix)

x = transposedMatrix[0]
y = transposedMatrix[1]

x = [float(i) for i in x]
y = [float(i) for i in y]

Xp = powers(x,0,n)
Yp = powers(y,1,1)
Xpt = transpose(Xp)


a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
a = a[:,0]

X2 = linspace(x[0],x[-1]).tolist()
Y2 = poly(a,X2)

plt.plot(x,y,'ro')
plt.plot(X2,Y2)
plt.show()