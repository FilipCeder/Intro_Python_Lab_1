"""Takes a  matrix as input and returns a transposed version of the matrix"""
def transpose(matrix):
    if matrix != []:
        cols = len(matrix[0])
        rows = len(matrix)

        transposed_matrix = []

        for j in range(cols):
            transposed_row = []
            for i in range(rows):
                transposed_row.append(matrix[i][j])
            transposed_matrix.append(transposed_row)

        return transposed_matrix      
    else:
        return []  
        

"""Takes a list, a start and a stop value as input. 
The function returns a matrix  where the first colum is the input list and subsequent colums 
are the numbers of the first colum by the power of the current number in the range a:b"""
def powers(list,a,b):
    matrix = []
    for j in list:
        row = []
        for i in range(a,b+1):
            row.append(float(j)**i)
        matrix.append(row)

    return matrix

"""Takes the input of two matrices and return the product of them"""
def matmul(A,B):
    if A != [] or B != []:
        rows_A = len(A)
        cols_A = len(A[0])
        rows_B = len(B)
        cols_B = len(B[0])

        if cols_A == rows_B:
            C = []
            
            for i in range(rows_A):
                C_row = []
                for j in range(cols_B):
                    product = 0
                    for k in range(cols_A):
                        product += A[i][k] * B[k][j]
                    C_row.append(product)
                C.append(C_row)
        
            return C

        else:
            return "matmul not possible"
    
    else:
        return []

"""Takes the input of a matrix and returns the inverted version of the matrix"""  
def invert(A):
    row_A = len(A)
    cols_A = len(A[0])
    
    if row_A == cols_A and row_A == 2:
        det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
        inverted_matrix = [[A[1][1]/ det, -A[0][1]/ det,], [-A[1][0]/ det, A[0][0]/ det]]

        return inverted_matrix
    else:
        return "invert not possible"

"""Takes the path to a file with structured data as input. Return the data in a matrix"""
def loadtxt(file):
    matrix = []
    imp_file = open(file)
    for i in imp_file:
        j = i.split()
        j = [float(i) for i in j]
        matrix.append(j)
    imp_file.close()
    return matrix

