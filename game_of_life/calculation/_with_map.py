from concurrent.futures import ThreadPoolExecutor

from game_of_life.calculation._count_nearest_neighbors \
    import count_nearest_neighbors

from game_of_life.definition import Cell
from game_of_life.calculation.config import WORKERS_NUMBER


def worker(task):
    field, x = task

    row = []
    for y in range(len(field[x])):
        row.append(count_nearest_neighbors(field, x, y))

    return row


def count_neighbors(game_field):
    counted_neighbors = []

    tasks = [(game_field, x) for x in range(len(game_field))]
    with ThreadPoolExecutor(max_workers=WORKERS_NUMBER) as executor:
        for row in executor.map(worker, tasks):
            counted_neighbors.append(row)

    return counted_neighbors


def count_neighbors_demonstration():
    field_size = 10
    game_field = [[Cell.VOID] * field_size for _ in range(field_size)]

    for row in count_neighbors(game_field):
        print(row)


if __name__ == '__main__':
    count_neighbors_demonstration()
