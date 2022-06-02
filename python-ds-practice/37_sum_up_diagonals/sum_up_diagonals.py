def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    l = len(matrix[0])
    diag_left=[matrix[i][i] for i in range(l)] 
    diag_right=([matrix[l-1-i][i] for i in range(l-1,-1,-1)]) 
    return sum(diag_left)+ sum(diag_right)