from enum import Enum


class Cell(Enum):
    VOID = 0
    LIFE = 1


class GameStage(Enum):
    INIT = 0
    LIFE = 1


class Button:
    def __init__(self, name, text):
        self.name = name
        self.text = text


BUTTONS_WITH_START = [
    Button(name='reset game', text='новая игра'),
    Button(name='start', text='старт'),
]

BUTTONS_WITH_STOP = [
    Button(name='reset game', text='новая игра'),
    Button(name='stop', text='стоп'),
]

TEXTS = {
    'game over': 'игра окончена',
    'window title': 'Game of Life',
}

FIELD_SIZE = 30

GAME_FIELD = [[Cell.VOID] * FIELD_SIZE for _ in range(FIELD_SIZE)]

FPS = 20
