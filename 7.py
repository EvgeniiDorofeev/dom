def create_matrix(size: int = 3, up_fill: int = 0, down_fill: int = 0):
    lst = []
    for i in range(size):
        lst.append([0] * size)
    for i in range(size):
        for j in range(size):
            if i == j:
                lst[i][j] = j + 1
            elif i > j:
                lst[i][j] = up_fill
            elif i < j:
                lst[i][j] = down_fill

    return lst

create_matrix() == [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
create_matrix(4) == [[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]]

create_matrix(up_fill=7) == [[1, 7, 7],
                             [0, 2, 7],
                             [0, 0, 3]]

create_matrix(up_fill=7, down_fill=9) == [[1, 7, 7],
                                          [9, 2, 7],
                                          [9, 9, 3]]


create_matrix(size=4, up_fill=7, down_fill=9) == [[1, 7, 7, 7],
                                                  [9, 2, 7, 7],
                                                  [9, 9, 3, 7],
                                                  [9, 9, 9, 4]]