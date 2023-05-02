import pygame
from time import sleep

from game_of_life.definition import Cell
from game_of_life.UI.config import *


class GameFieldView:
    def __init__(self, field, texts, buttons):
        self._field = field
        self._texts = texts

        pygame.init()
        pygame.font.SysFont(FONT_NAME, TEXTS_FONT_SIZE)

        self._font = pygame.font.Font(None, TEXTS_FONT_SIZE)
        self._screen = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption(self._texts['window title'])

        self.display_buttons(buttons)
        self.display_field()

    def display_field(self):
        for field_x in range(0, FIELD_SIZE):
            for field_y in range(0, FIELD_SIZE):

                if self._field[field_x][field_y] == Cell.VOID:
                    cell_color = FIELD_COLOR_VOID
                else:
                    cell_color = FIELD_COLOR_LIFE

                pygame.draw.rect(
                    self._screen,
                    cell_color,
                    (
                        field_x * CELL_SIZE + LINE_WIDTH,
                        BUTTON_ZONE_SIZE + field_y * CELL_SIZE + LINE_WIDTH,
                        CELL_SIZE - LINE_WIDTH * 2,
                        CELL_SIZE - LINE_WIDTH * 2
                    )
                )

    def display_buttons(self, buttons):
        self._buttons = buttons
        self._button_number = len(self._buttons)
        self._button_width = WIDTH // self._button_number

        pygame.draw.rect(
            self._screen,
            BACKGROUND_COLOR,
            (0, 0, WIDTH, BUTTON_ZONE_SIZE)
        )

        for n in range(self._button_number):
            pygame.draw.rect(
                self._screen,
                BUTTONS_COLOR,
                (
                    LINE_WIDTH + n * self._button_width,
                    LINE_WIDTH, self._button_width - LINE_WIDTH * 2,
                    BUTTON_ZONE_SIZE - LINE_WIDTH * 2
                )
            )

            self._text_out(
                text=self._buttons[n].text,
                color=COLOR_OF_BUTTONS_LABELS,
                coordinates=(
                    n * self._button_width + self._button_width // 2,
                    BUTTON_ZONE_SIZE // 2
                )
            )

    def message_out(self, message):
        self._text_out(
            text=message,
            color=MESSAGE_COLOR,
            coordinates=(
                WIDTH // 2,
                BUTTON_ZONE_SIZE + WIDTH // 2
            )
        )
        pygame.display.flip()
        sleep(MESSAGE_DURATION)

    def _text_out(self, text, color, coordinates):
        text = self._font.render(text, True, color)

        text_rect = text.get_rect()
        text_rect.center = coordinates

        self._screen.blit(text, text_rect)

    def pressed_button(self, screen_x, screen_y):
        if screen_y > BUTTON_ZONE_SIZE:
            return None
        else:
            return self._buttons[
                screen_x // self._button_width
                ].name

    @staticmethod
    def get_click_coordinates(screen_x, screen_y):
        field_x = screen_x // CELL_SIZE
        field_y = (screen_y - BUTTON_ZONE_SIZE) // CELL_SIZE
        return field_x, field_y
