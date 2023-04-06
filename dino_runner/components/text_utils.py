from pygame.font import Font
from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

FONT_STYLE = 'freesansbold.ttf'
black_color = (0,0,0)


def get_message(message, size, width=SCREEN_WIDTH//2, height=SCREEN_HEIGHT//2):
    font = Font(FONT_STYLE, size)
    text = font.render(message, True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect
