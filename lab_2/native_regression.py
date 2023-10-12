from matrix import*
import sys
import matplotlib.pyplot as plt


file = sys.argv[1]

dataMatrix = loadtxt(file)

transposedMatrix = transpose(dataMatrix)

x = transposedMatrix[0]
y = transposedMatrix[1]

x = [float(i) for i in x]
y = [float(i) for i in y]

Xp = powers(x,0,1)
Yp = powers(y,1,1)
Xpt = transpose(Xp)

[[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))

Y2 = [(b+(i*m)) for i in x]

plt.plot(x,y,'ro')
plt.plot(x,Y2)
plt.show()