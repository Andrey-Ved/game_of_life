import copy

from game_of_life.definition import Cell, CALCULATION_OPTION


def _counting_neighbors(field, x, y):
    count = 0

    for neighbor_x in range(x - 1, x + 2):
        if 0 <= neighbor_x < len(field):
            for neighbor_y in range(y - 1, y + 2):
                if 0 <= neighbor_y < len(field[0]):
                    if neighbor_x != x or neighbor_y != y:
                        if field[neighbor_x][neighbor_y] == Cell.LIFE:
                            count += 1
    return count


def _step_simple(game_field):
    old_field = copy.deepcopy(game_field)
    for x in range(len(game_field)):
        for y in range(len(game_field[0])):
            neighbors_number = _counting_neighbors(old_field, x, y)

            if game_field[x][y] == Cell.VOID:
                if neighbors_number == 3:
                    game_field[x][y] = Cell.LIFE

            if game_field[x][y] == Cell.LIFE:
                if not (1 < neighbors_number < 4):
                    game_field[x][y] = Cell.VOID


def _step_with_queue(game_field):
    pass


def _step_in_piecemeal(game_field):
    pass


#CALCULATION_OPTION = 2


def make_step(game_field):
    calculation_variant = {
        0: _step_simple,
        1: _step_with_queue,
        2: _step_in_piecemeal,
    }
    calculation_variant[CALCULATION_OPTION](game_field)
