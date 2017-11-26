def loopf(m):
    """
    loop thru matrix with loop
    """
    r = []
    # m = [[8, 7, 1, 2, 3], [1, 5, 2, 9, 0], [8, 2, 2, 4, 1]]
    rows =3
    columns= 5
    # mylist = [[0 for x in range(columns)] for x in range(rows)]
    for i in range(rows):
        row = m[i]
        new_row = []
        for j in range(columns):
            m_ij = m[i][j]
            r_ij = 5 * m_ij
            new_row.append(r_ij)
        r.append(new_row)

    print(r)
    return r
        #print(m)

m = [[8, 7, 1, 2, 3], [1, 5, 2, 9, 0], [8, 2, 2, 4, 1]]
loopf(m)
