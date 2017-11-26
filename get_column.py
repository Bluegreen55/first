### TODO: Write a function that receives a matrix and a column number.
###       the output should be the column in the form of a list

### Example input:
# matrix = [
#    [5, 9, 11, 2],
#    [3, 2, 99, 3],
#    [7, 1, 8, 2]
# ]
#
# column_number = 1

### Example output:
# [9, 2, 1]
#

def get_column(matrix, column_number):
    column =[]
    len1 = len(matrix)


    for x in range(len1):
        tp = matrix[x][column_number]
        column.append(tp)
    print(column)
    return column

matrix = [
    [5, 9, 11, 2],
    [3, 2, 99, 3],
    [7, 1, 8, 2] ]

get_column(matrix, 1)
