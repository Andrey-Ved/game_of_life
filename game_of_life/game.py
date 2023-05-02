import pygame

from game_of_life.UI.field_widget import GameFieldView
from game_of_life.step import make_step
from game_of_life.definition import *


class GameManager:
    def __init__(self):
        self._widget = GameFieldView(GAME_FIELD, TEXTS, BUTTONS_WITH_START)
        self.game_stage = GameStage.INIT

    def checking_ending(self):
        pass

    def click_handler(self, screen_x, screen_y):
        button_name = self._widget.pressed_button(screen_x, screen_y)

        if button_name:
            self.buttons_handler(button_name)
        else:
            self.cell_handler(
                *self._widget.get_click_coordinates(screen_x, screen_y)
            )

    @staticmethod
    def cell_handler(field_x, field_y):
        if GAME_FIELD[field_x][field_y] == Cell.VOID:
            GAME_FIELD[field_x][field_y] = Cell.LIFE
        else:
            GAME_FIELD[field_x][field_y] = Cell.VOID

    def buttons_handler(self, button_name):
        if button_name == 'reset game':
            for field_x in range(0, FIELD_SIZE):
                for field_y in range(0, FIELD_SIZE):
                    GAME_FIELD[field_x][field_y] = Cell.VOID

        elif button_name == 'start':
            self.game_stage = GameStage.LIFE
            self._widget.display_buttons(BUTTONS_WITH_STOP)

        elif button_name == 'stop':
            self.game_stage = GameStage.INIT
            self._widget.display_buttons(BUTTONS_WITH_START)

    def display_field(self):
        self._widget.display_field()


class Game:
    def __init__(self):
        self._manager = GameManager()
        self._make_step = make_step

    def main_loop(self):
        finished = False
        clock = pygame.time.Clock()

        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self._manager.click_handler(
                        *pygame.mouse.get_pos()
                    )

            clock.tick(FPS)

            if self._manager.game_stage == GameStage.LIFE:
                self._make_step(GAME_FIELD)

            self._manager.display_field()
            pygame.display.flip()
            self._manager.checking_ending()
