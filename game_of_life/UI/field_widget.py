import pygame
from time import sleep

from game_of_life.definition import Cell
from game_of_life.UI.config import *


class GameFieldView:
    def __init__(self, field, texts, buttons):
        self.field = field
        self.texts = texts

        pygame.init()
        pygame.font.SysFont(FONT_NAME, TEXTS_FONT_SIZE)

        self.font = pygame.font.Font(None, TEXTS_FONT_SIZE)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption(self.texts['window title'])

        self.display_buttons(buttons)
        self.display_field()

    def display_field(self):
        for field_x in range(0, FIELD_SIZE):
            for field_y in range(0, FIELD_SIZE):

                if self.field[field_x][field_y] == Cell.VOID:
                    cell_color = FIELD_COLOR_VOID
                else:
                    cell_color = FIELD_COLOR_LIFE

                pygame.draw.rect(
                    self.screen,
                    cell_color,
                    (
                        field_x * CELL_SIZE + LINE_WIDTH,
                        BUTTON_ZONE_SIZE + field_y * CELL_SIZE + LINE_WIDTH,
                        CELL_SIZE - LINE_WIDTH * 2,
                        CELL_SIZE - LINE_WIDTH * 2
                    )
                )

    def display_buttons(self, buttons):
        self.buttons = buttons
        self.button_number = len(self.buttons)
        self.button_width = WIDTH // self.button_number

        pygame.draw.rect(
            self.screen,
            BACKGROUND_COLOR,
            (0, 0, WIDTH, BUTTON_ZONE_SIZE)
        )

        for n in range(self.button_number):
            pygame.draw.rect(
                self.screen,
                BUTTONS_COLOR,
                (
                    LINE_WIDTH + n * self.button_width,
                    LINE_WIDTH, self.button_width - LINE_WIDTH * 2,
                    BUTTON_ZONE_SIZE - LINE_WIDTH * 2
                )
            )

            self.text_out(
                text=self.buttons[n].text,
                color=COLOR_OF_BUTTONS_LABELS,
                coordinates=(
                    n * self.button_width + self.button_width // 2,
                    BUTTON_ZONE_SIZE // 2
                )
            )

    def message_output(self, message):
        self.text_out(
            text=message,
            color=MESSAGE_COLOR,
            coordinates=(
                WIDTH // 2,
                BUTTON_ZONE_SIZE + WIDTH // 2
            )
        )
        pygame.display.flip()
        sleep(MESSAGE_DURATION)

    def text_out(self, text, color, coordinates):
        text = self.font.render(text, True, color)

        text_rect = text.get_rect()
        text_rect.center = coordinates

        self.screen.blit(text, text_rect)

    def pressed_button(self, screen_x, screen_y):
        if screen_y > BUTTON_ZONE_SIZE:
            return None
        else:
            return self.buttons[
                screen_x // self.button_width
                ].name

    @staticmethod
    def get_click_coordinates(screen_x, screen_y):
        field_x = screen_x // CELL_SIZE
        field_y = (screen_y - BUTTON_ZONE_SIZE) // CELL_SIZE
        return field_x, field_y
