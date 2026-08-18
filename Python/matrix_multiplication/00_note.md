# 코드 개선하기

### 1. getMatrix(title)
> 오류 방지용 코드들이 추가 됨.


내 코드 
```python
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
```
GPT 코드 

```python
while True: # 조건 삭제
    user_input = input(f'row[{count_row}] : ').strip() # 공백 제거
    
    if user_input.lower() == 'end': # 대소문자 상관없이 인식식
        if len(A) == 0:
            print("Error: Matrix can't be empty.")
            return None
        else:
            break

    try:
        row = list(map(int, user_input.split(',')))
        if len(row) == 0:                           # 빈 row 방지
            print("Error: Row can't be empty.")
            continue
        A.append(row)
        count_row += 1
    except:
        print("Error: Didn't follow the correct format.")
        return None

return A
```
---
<br> 

### 2. isMatrix(A)
> 코드 간소화
> - `all(isinstance(row, list) for row in A)` : row가 list인지 확인
> - `all(len(row) == col_length for row in A)` : 각 row의 길이 확인  
`C[i][j] += A[i][k] * B[k][j]`

내 코드 
```python
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
```
GPT 코드 

```python
                # 모든 row가 리스트인지 확인
if not A or not all(isinstance(row, list) for row in A): 
    return False

col_length = len(A[0]) 
if col_length == 0: # A[0]의 길이 확인
    return False

return all(len(row) == col_length for row in A) # 각 row의 길이 비교
```
---
<br>

### 3. standardMatrixProduct(A, B)
> 코드 간소화
> - `rowA, colA = len(A), len(A[0])` : 다중 할당
> - `[[0 for _ in range(colB)] for _ in range(rowA)]` : matrix 초기화

내 코드 
```python
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
```
GPT 코드 

```python
if not (isMatrix(A) and isMatrix(B)): 
    return 'Error: A or B is not a valid matrix.'

rowA, colA = len(A), len(A[0])  # 다중 할당	
rowB, colB = len(B), len(B[0])

if colA != rowB:
    return 'Error: cannot multiply A and B due to mismatched dimensions.'

C = [[0 for _ in range(colB)] for _ in range(rowA)] # 초기 matrix 추가

for i in range(rowA):
    for j in range(colB):
        for k in range(colA):
            C[i][j] += A[i][k] * B[k][j]

return C
```
---

### 4. scalarMultiplication(A, k)
> A에 결괏값을 저장하지 않고 바로 return 

내 코드 
```python
if not(isMatrix(A)): 
        return 'A is not matrix'
    
    row_len = len(A)
    col_len = len(A[0])

    for row_idx in range(row_len):
        for col_idx in range(col_len):
            A[row_idx][col_idx] *= k

    return A
```
GPT 코드 

```python
return [[k * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]
```

---

### 5. hadamardProduct(A, B)
> 결괏값을 변수에 저장하지 않고 바로 return 


내 코드 
```python
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
```
GPT 코드 

```python
m, n = len(A), len(A[0])
return [[A[i][j] * B[i][j] for j in range(n)] for i in range(m)]
```

---

### 6. outerProduct(u, v)
> 결괏값을 변수에 저장하지 않고 바로 return 


내 코드 
```python
u_len = len(u)
v_len = len(v)

C = [[0 for _ in range(v_len)] for _ in range (u_len)]

for row_idx in range(u_len):
    for col_idx in range(v_len):
        C[row_idx][col_idx] = u[row_idx] * v[col_idx]

return C
```
GPT 코드 

```python
return [[ui * vj for vj in v] for ui in u]
```

### 7. kroneckerProduct(A, B)
> 수정 필요 없음


내 코드 
```python
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
```
GPT 코드 

```python
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
```
