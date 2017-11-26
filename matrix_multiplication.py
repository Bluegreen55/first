### TODO: Write a function called matrix_multiplication that takes
###       two matrices,multiplies them together and then returns
###       the results
###
###       Make sure that your function can handle matrices that contain
###       only one row or one column. For example,
###       multiplying two matrices of size (4x1)x(1x4) should return a
###       4x4 matrix

def get_row(matrix, row_number):
    row =[]
    len1 = len(matrix[0])
    for x in range(len1):
        tp = matrix[row_number][x]
        row.append(tp)
    print(row)
    return row

def get_column(matrix, column_number):
    column =[]
    len1 = len(matrix)

    for x in range(len1):
        tp = matrix[x][column_number]
        column.append(tp)
    print(column)
    return column

def dotproduct(vectora, vectorb):

    # variable for accumulating the sum
    result = 0

    # TODO: Use a for loop to multiply the two vectors
    # element by element. Accumulate the sum in the result variable
    v3 = 0
    lenx0 = len(vectora)
    lenx1 = len(vectorb)

    for x in range(lenx0):
        #for y in range(lenx1):
        v1 = vectora[x]
        v2 = vectorb[x]
        v3 += v1 * v2

    print(v3)
    return v3

def matrix_multiplication(matrixA, matrixB):

    ### TODO: store the number of rows in A and the number
    ###       of columns in B. This will be the size of the output
    ###       matrix
    ### HINT: The len function in Python will be helpful
    m_rows = len(matrixA)
    p_columns = len(matrixB[0])
    p_row = len(matrixB)
    rowA = []
    colB = []
    rtemp = []
    result = []
    result1 = []
    #t3 = 0
    print(m_rows)
    print(p_columns)
    print(matrixA)
    print(matrixB)

# lopp thru the rows
    for r in range(m_rows):
        #rowA  = get_row(matrixA,r)
        #new_row = []
        #print(rowA)
        #loop thru columns of B
        for c in range(p_columns):
            #colB = get_column(matrixB,c)
            #print(colB)
            #looop thru rows of B;
            for r2 in range(p_row):
                t3 = 0
                print(r)
                print(c)
                print(r2)
                t1 = matrixA[r][r2]
                print(t1)
                t2 = matrixB[r2][c]
                print(t2)
                t3 += t1 * t2
                print(t3)
                result1.append(t3)
    result.append(result1)
    print(result)

    return result

matrix_multiplication([[5], [2]], [[5, 1]]) #== [[25, 5], [10, 2]]
#matrix_multiplication([[4]], [[3]]) #== [[12]]
#matrix_multiplication([[2, 1, 8, 2, 1], [5, 6, 4, 2, 1]], [[1, 7, 2], [2, 6, 3], [3, 1, 1], [1, 20, 1], [7, 4, 16]])

    ### TODO:  Write a for loop within a for loop. The outside
    ###        for loop will iterate through m_rows.
    ###        The inside for loop will iterate through p_columns.

    ### TODO:  As you iterate through the m_rows and p_columns,
    ###        use your get_row function to grab the current A row
    ###        and use your get_column function to grab the current
    ###        B column.


    ### TODO: Calculate the dot product of the A row and the B column


    ### TODO: Append the dot product to an empty list called row_result.
    ###       This list will accumulate the values of a row
    ###        in the result matrix
    #row_result = []

    ### TODO: After iterating through all of the columns in matrix B,
    ###       append the row_result list to the result variable.
    ###       Reinitialize the row_result to row_result = [].
    ###       Your for loop will move down to the next row
    ###       of matrix A.
    ###       The loop will iterate through all of the columns
    ###       taking the dot product
    ###       between the row in A and each column in B.

    ### TODO: return the result of AxB
