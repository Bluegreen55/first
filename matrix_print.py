def matrix_print(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            m_ij = matrix[i][j]
            print(m_ij, '\t', end="")
        print('\n') # prints a new line
    return

r = [[40, 35, 5, 10, 15], [5, 25, 10, 45, 0], [40, 10, 10, 20, 5]]
matrix_print(r)
