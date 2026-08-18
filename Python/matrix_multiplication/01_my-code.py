'''
Matrix Multiplication
    - standardMatrixProduct(A, B)
    - scalarMultiplication(A, k)
    - hadamardProduct(A, B)
    - outerProduct(u, v)
    - kroneckerProduct(A, B)

'''

def getMatrix(title):
    # row by row로 Martix 입력받기 | Args: (string) title of message | Return : Matrix A or None
    count_row = 0
    user_input = ''
    A = []

    print(f"=== \n{title} \nType the row numbers in the format: \ne.g.) 1, 2, 3\nType 'end' to finish \n===")

    while user_input != 'end':
        user_input = input(f'row[{count_row}] : ')
        if user_input == 'end':
            return A

        try:
            A.append(list(map(int, user_input.split(', '))))
            count_row += 1
        except:
            print("Error: didn't follow the format")
            return None
    
    return A

def isMatrix(A):
    # A가 Matrix 인지 판별 | Args: (list) 판별할 대상 A | Return : True or False
    rowA_len = len(A)
    colA_len = len(A[0])
    count_row = 0

    for i in range(rowA_len):
        if len(A[i]) == colA_len:
            count_row += 1
    
    if count_row == rowA_len:
        return True
    else:
        return False

def isVector(u):
    # u가 Vector 인지 판별 | Args: (list) 판별할 대상 u | Return : True or False
    if isinstance(u, list) & all(not isinstance(x, list) for x in u):
        return True
    
    return False

def standardMatrixProduct(A, B):
    # 두 Matrix의 곱 반환 | Args: (list) Matrix A, (list) Matrix B | Return : Matrix AB
    if not(isMatrix(A) & isMatrix(B)): 
        return 'A or B is not matrix'
    
    rowA_len = len(A)
    colA_len = len(A[0])  
    rowB_len = len(B)
    colB_len = len(B[0])
    C = []
    rowC = []
    c = 0
    

    if colA_len != rowB_len:
        return 'cannot multiply A and B'

    for rowA_index in range(rowA_len):
        for colB_index in range(colB_len):
            for rowB_index in range(rowB_len):
                c += A[rowA_index][rowB_index] * B[rowB_index][colB_index]
            rowC.append(c)
            c=0
        C.append(rowC)
        rowC = []
    
    if isMatrix(C):
        return C
    else:
        return 'multiplication failed'

def scalarMultiplication(A, k):
    # Matrix의 스칼라 곱 반환 | Args: (list) Matrix A, (float) k | Return : Matrix Ak
    if not(isMatrix(A)): 
        return 'A is not matrix'
    
    row_len = len(A)
    col_len = len(A[0])

    for row_idx in range(row_len):
        for col_idx in range(col_len):
            A[row_idx][col_idx] *= k

    return A

def hadamardProduct(A, B):
    # 두 Matrix의 곱 반환 | Args: (list) Matrix A, (list) Matrix B | Return : Matrix AB
    if not(isMatrix(A) & isMatrix(B)): 
        return 'A or B is not matrix'
    
    rowA_len = len(A)
    colA_len = len(A[0])  
    rowB_len = len(B)
    colB_len = len(B[0])
    
    if rowA_len != rowB_len | colA_len != colB_len: 
        return 'A and B must have the same dimensions'

    C = [[0 for _ in range(colA_len)] for _ in range (rowA_len)]

    for row_idx in range(rowA_len):
        for col_idx in range(colA_len):
            C[row_idx][col_idx] = A[row_idx][col_idx] * B[row_idx][col_idx]

    return C


def outerProduct(u, v):
    # 두 Matrix의 곱 반환 | Args: (list) Matrix A, (list) Matrix B | Return : Matrix AB
    if not(isVector(u) & isVector(v)): 
        return 'u or v is not vector'

    u_len = len(u)
    v_len = len(v)

    C = [[0 for _ in range(v_len)] for _ in range (u_len)]

    for row_idx in range(u_len):
        for col_idx in range(v_len):
            C[row_idx][col_idx] = u[row_idx] * v[col_idx]

    return C

def kroneckerProduct(A, B):
    # 두 Matrix의 크로네커 곱 반환 | Args: (list) Matrix A, (list) Matrix B | Return : Matrix AB
    if not(isMatrix(A) & isMatrix(B)): 
        return 'A or B is not matrix'
    
    rowA_len = len(A)
    colA_len = len(A[0])  
    rowB_len = len(B)
    colB_len = len(B[0])

    C = [[0 for _ in range(colA_len*colB_len)] for _ in range(rowA_len*rowB_len)]
    
    for row_idx in range(rowA_len*rowB_len):
        for col_idx in range(colA_len*colB_len):
            C[row_idx][col_idx] = A[row_idx//rowA_len][col_idx//colA_len] * B[row_idx%rowB_len][col_idx%colB_len]

    return C

def main(): 
    # A = [[1, 2, 3], [4, 5, 6]]
    # B = [[1, 2], [3, 4], [5, 6]]
    # B = [[1, 2, 3], [4, 5, 6]]
    # u = [2, 5]
    # v = [3, 4, 1]
    A = [[1, 2], [3, 4]]
    B = [[0, 5], [6, 7]]

    # A = getMatrix('Matrix A')
    # B = getMatrix('Matrix B')

    # print('===')
    # print('A = ', A)
    # print('B = ', B)

    # print('AB = ', standardMatrixProduct(A, B))
    # print('Ak = ', scalarMultiplication(A, 3))
    # print('AB = ', hadamardProduct(A, B))
    # print('uvT = ', outerProduct(u, v))
    print('AB = ', kroneckerProduct(A, B))

main()