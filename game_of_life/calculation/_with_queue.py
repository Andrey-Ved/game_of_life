from copy import deepcopy
from multiprocessing import Manager
# from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Thread

from game_of_life.calculation._count_nearest_neighbors \
    import count_nearest_neighbors

from game_of_life.definition import Cell
from game_of_life.calculation.config import WORKERS_NUMBER


def worker(tasks, answers, lock, field):
    while not tasks.empty():
        x = len(field)
        with lock:
            if not tasks.empty():
                x = tasks.get()

        if x < len(field):
            count_row = []
            for y in range(len(field[x])):
                count_row.append(
                    count_nearest_neighbors(field, x, y)
                )

            if len(count_row) > 0:
                answers.put((x, count_row))


def count_neighbors(game_field):
    mproc_manager = Manager()

    lock = mproc_manager.Lock()
    tasks = mproc_manager.Queue()
    answers = mproc_manager.Queue()

    len_x = len(game_field)

    for x in range(len_x):
        tasks.put(x)

    # with ThreadPoolExecutor() as executor:
    #     futures = []
    #     for process in range(WORKERS_NUMBER):
    #         futures.append(executor.submit(worker, tasks, answers, lock, game_field))
    #
    #     for future in as_completed(futures):
    #         future.result()

    workers = []
    for process_index in range(WORKERS_NUMBER):
        worker_process = Thread(
            target=worker,
            args=(tasks, answers, lock, deepcopy(game_field))
        )
        workers.append(worker_process)

    for worker_process in workers:
        worker_process.start()

    for worker_process in workers:
        worker_process.join()

    counted_neighbors = [[] for _ in range(len_x)]

    while not answers.empty():
        x, count_row = answers.get()
        counted_neighbors[x] = count_row

    return counted_neighbors


def count_neighbors_demonstration():
    field_size = 10
    game_field = [[Cell.VOID] * field_size for _ in range(field_size)]

    for row in count_neighbors(game_field):
        print(row)


if __name__ == '__main__':
    count_neighbors_demonstration()
