def transposeMatrix(matrix):
    # Write your code here.
    matrix_row= len(matrix)
    matrix_col= len(matrix[0])
    transpose_matrix=[]
    
    for i in range(0,matrix_col):
        temp=[]
        for j in range(0, matrix_row):
            temp.append(matrix[j][i])
        transpose_matrix.append(temp)
    
    
    return transpose_matrix


#Test Case - 01
matrix=[
    [1, 2],
    [3, 4],
    [5, 6]
]

print(transposeMatrix(matrix))