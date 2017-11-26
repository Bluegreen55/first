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

def get_row(matrix, row_number):
    row =[]
    len1 = len(matrix[1])

    for x in range(len1):
        tp = matrix[row_number][x]
        row.append(tp)
    print(row)
    return row

matrix = [
    [5, 9, 11, 2],
    [3, 2, 99, 3],
    [7, 1, 8, 2] ]

get_row(matrix, 1)
