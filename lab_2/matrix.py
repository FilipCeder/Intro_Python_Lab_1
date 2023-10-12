def transpose(matrix):
    
    cols = len(matrix[0])
    rows = len(matrix)

    transposed_matrix = [] 

    for j in range(cols):
        transposed_row = []
        for i in range(rows):
            transposed_row.append(matrix[i][j])
        transposed_matrix.append(transposed_row)

    return transposed_matrix


def powers(list,a,b):
    matrix = []
    for i in list:
        row = []
        for e in range(a,b+1):
            row.append(i**e)
        matrix.append(row)
    return matrix

def matmul(A,B):
    cols_a = len(A[0])
    rows_a = len(A)
    cols_b = len(B[0])
    rows_b = len(B)

    if cols_a == rows_b:
        C = []
        for i in range(rows_a):
            rows_c = []
            for j in range(cols_b):
                element = 0
                for k in range(cols_a):
                    element += A[i][k] * B[k][j]
                rows_c.append(element)
            C.append(rows_c)
        return C
    else: 
        return "matmul not possible"


def invert(A):
    rows_A = len(A)
    cols_A = len(A[0])

    if cols_A == rows_A and cols_A == 2:
        det_A = A[0][0]*A[1][1] - A[0][1]*A[1][0]
        d = det_A
        invert_matrix = [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d, A[0][0]/d]]
        return invert_matrix

    else:
        return "invert not possible"


def loadtxt(file):
    matrix = []
    imp_file = open(file)
    for i in imp_file:
        j = i.split()
        matrix.append(j)
    imp_file.close()
    return matrix