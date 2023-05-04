from time import sleep

from game_of_life.definition import Cell
from game_of_life.calculation.config import CALCULATION_DELAY


def count_nearest_neighbors(field, x, y):
    count = 0

    for neighbor_x in range(x - 1, x + 2):
        if 0 <= neighbor_x < len(field):
            for neighbor_y in range(y - 1, y + 2):
                if 0 <= neighbor_y < len(field[0]):
                    if neighbor_x != x or neighbor_y != y:
                        if field[neighbor_x][neighbor_y] == Cell.LIFE:
                            count += 1

    sleep(CALCULATION_DELAY) if CALCULATION_DELAY else None
    return count
