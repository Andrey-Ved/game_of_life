from game_of_life.calculation._count_nearest_neighbors \
    import count_nearest_neighbors


def count_neighbors(game_field):
    len_x = len(game_field)
    len_y = len(game_field[0])
    counted_neighbors = [[0] * len_y for _ in range(len_x)]

    for x in range(len_x):
        for y in range(len_y):
            counted_neighbors[x][y] = count_nearest_neighbors(game_field, x, y)

    return counted_neighbors
