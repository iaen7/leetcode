def spiralOrder( matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if matrix == []:
        return
    row = len(matrix)
    column = len(matrix[0])
    res = []
    i = 0
    j = 0
    while i < (row+1) / 2 and j < (column+1) / 2:
        ringPrint(j, column - j -1, i, row- i - 1,matrix,res)
        i += 1
        j += 1
    return res


def ringPrint( min_x, max_x, min_y, max_y, maxtrix, res):
    if max_y > min_y and max_x>min_x:
        for i in range(min_x, max_x + 1):
            res.append(maxtrix[min_y][i])
        for i in range(min_y + 1, max_y + 1):
            res.append(maxtrix[i][max_x])
        for i in range(max_x - 1, min_x - 1, -1):
            res.append(maxtrix[max_y][i])
        for i in range(max_y - 1, min_y, -1):
            res.append(maxtrix[i][min_x])
    elif max_y > min_y:
        for i in range(min_y, max_y + 1):
            res.append(maxtrix[i][max_x])
    elif max_x > min_x:
        for i in range(min_x, max_x + 1):
            res.append(maxtrix[min_y][i])
    else:
        res.append(maxtrix[min_y][min_x])

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print spiralOrder(matrix)
