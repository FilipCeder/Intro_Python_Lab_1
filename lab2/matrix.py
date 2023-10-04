"""Takes a matrix as input and returns a transposed version of the matrix"""
def transpose(matrix):
    if matrix != []:
        transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    else:
        transpose = []

    return transpose

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
    return matrix


"""Takes the input of two matrices and returns the product of them"""
def matmul(A,B):
    if A != [] or B !=[]:
        if len(A[0]) == len(B):

            C = [[sum(a*b for a,b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
            return C

        else:

            return "matrices cannot multiply"
    else:
        return []

"""Takes the input of a matrix and returns the inverted version of the matrix"""    
def invert(matrix):
    if len(matrix) == 2 and len(matrix[0]) == 2:

        det = (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
        invert = [[matrix[1][1]/det,-(matrix[0][1]/det)],[-(matrix[1][0]/det),matrix[0][0]/det]]

        return invert

    else:
        return "wrong input"

"""Takes the path to a file with structured data as input. Returns the data in a matrix"""
def loadtxt(file):
    matrix = []
    imp_file=open(file)
    for i in imp_file:
        j = i.split()
        j= [float(i) for i in j]
        matrix.append(j)
    imp_file.close()
    return matrix





