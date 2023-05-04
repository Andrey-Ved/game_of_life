from game_of_life.definition import Cell

from game_of_life.calculation.config import CALCULATION_OPTION

from game_of_life.calculation._simple \
    import count_neighbors as count_neighbors_simple
from game_of_life.calculation._with_queue \
    import count_neighbors as count_neighbors_with_queue
from game_of_life.calculation._with_map \
    import count_neighbors as count_neighbors_with_map


def count_neighbors(game_field, calculation_option=CALCULATION_OPTION):
    calculation_variant = {
        0: count_neighbors_simple,
        1: count_neighbors_with_queue,
        2: count_neighbors_with_map,
    }

    return calculation_variant[calculation_option](game_field)


def make_step(game_field):
    counted_neighbors = count_neighbors(game_field, )

    for x in range(len(game_field)):
        for y in range(len(game_field[0])):
            neighbors_number = counted_neighbors[x][y]

            if game_field[x][y] == Cell.VOID:
                if neighbors_number == 3:
                    game_field[x][y] = Cell.LIFE

            if game_field[x][y] == Cell.LIFE:
                if not (1 < neighbors_number < 4):
                    game_field[x][y] = Cell.VOID
