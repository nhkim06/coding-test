def getMatrix(title):
    count_row = 0
    A = []

    print(f"===\n{title}\nType the row numbers separated by commas (e.g. 1, 2, 3)\nType 'end' to finish\n===")

    while True:
        user_input = input(f'row[{count_row}] : ').strip()
        
        if user_input.lower() == 'end':
            if len(A) == 0:
                print("Error: Matrix can't be empty.")
                return None
            else:
                break

        try:
            row = list(map(int, user_input.split(',')))
            if len(row) == 0:
                print("Error: Row can't be empty.")
                continue
            A.append(row)
            count_row += 1
        except:
            print("Error: Didn't follow the correct format.")
            return None

    return A

def isMatrix(A):
    if not A or not all(isinstance(row, list) for row in A):
        return False

    col_length = len(A[0])
    if col_length == 0:
        return False

    return all(len(row) == col_length for row in A)

def standardMatrixProduct(A, B):
    if not (isMatrix(A) and isMatrix(B)): 
        return 'Error: A or B is not a valid matrix.'
    
    rowA, colA = len(A), len(A[0])  
    rowB, colB = len(B), len(B[0])

    if colA != rowB:
        return 'Error: cannot multiply A and B due to mismatched dimensions.'

    C = [[0 for _ in range(colB)] for _ in range(rowA)]

    for i in range(rowA):
        for j in range(colB):
            for k in range(colA):
                C[i][j] += A[i][k] * B[k][j]

    return C

def scalarMultiplication(A, k):
    """
    Multiply every element of matrix A by scalar k.
    A: list of lists (m x n)
    k: number (int or float)
    Returns: new matrix (m x n)
    """
    return [[k * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def hadamardProduct(A, B):
    """
    Element-wise (Hadamard) product of A and B.
    A, B: same-shaped matrices (lists of lists)
    Returns: new matrix of the same shape
    """
    m, n = len(A), len(A[0])
    # Optional: you could check that len(B)==m and len(B[0])==n
    return [[A[i][j] * B[i][j] for j in range(n)] for i in range(m)]


def outerProduct(u, v):
    """
    Outer product of vector u and v.
    u: length-m list
    v: length-n list
    Returns: m x n matrix with C[i][j] = u[i] * v[j]
    """
    return [[ui * vj for vj in v] for ui in u]


def kroneckerProduct(A, B):
    """
    Kronecker product of matrices A and B.
    A: m x n matrix
    B: p x q matrix
    Returns: (m*p) x (n*q) matrix
    """
    m, n = len(A), len(A[0])
    p, q = len(B), len(B[0])
    C = [[0] * (n * q) for _ in range(m * p)]
    for i in range(m):
        for j in range(n):
            a = A[i][j]
            for ii in range(p):
                for jj in range(q):
                    C[i*p + ii][j*q + jj] = a * B[ii][jj]
    return C

def main():
    A = getMatrix('Matrix A')
    if A is None: return

    B = getMatrix('Matrix B')
    if B is None: return

    print('===')
    print('A =', A)
    print('B =', B)

    result = multiplyMatrix(A, B)
    print('AB =', result)

if __name__ == "__main__":
    main()
