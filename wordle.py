import pygame

"""
TODO:
- Add typing letters
- Add printing letters
- Add keyboard
- Add guesses
- Add green, yellow, gray letters
- Add win screen, lose screen

"""

# Game Setup 

# Constants
WIDTH = 600
HEIGHT = 720
X_length = 5
Y_length = 6
running = True
cellSize = WIDTH // X_length
WORD = 'TESTS'

# Colors
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
GREEN, CREAM = (115, 149, 82), (235, 236, 208)
LIGHT_ORANGE = (186, 201, 73)
GRAY = (202, 203, 179)
RED = (255, 0, 0)
DARK_GRAY = (30, 30, 30)
MID_GRAY = (55, 55, 55)
LIGHT_GRAY = (180, 180, 180)

# pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wordle")
clock = pygame.time.Clock()
group = pygame.sprite.Group()

font = pygame.font.SysFont(None, 100)


# Grid logic

def print_grid():
    global WORD_LENGTH, GUESSES

    for x in range(GUESSES):
        for y in range(WORD_LENGTH):
            print(grid[x][y] , end= ' ')

        print()

WORD_LENGTH = 5
GUESSES = 6
grid = [[None] * WORD_LENGTH for _ in range(GUESSES)]

"""
TEST PURPOSES

grid[0][0] = 'T'
grid[0][1] = 'B'
grid[0][2] = 'E'
grid[0][3] = 'D'
grid[0][4] = 'S'

grid[1][0] = 'B'
grid[1][1] = 'E'
grid[1][2] = 'S'
grid[1][3] = 'T'
grid[1][4] = 'Y'

"""


print_grid()


# Board setup

def draw_board():
    board = pygame.Surface((cellSize * X_length, cellSize * Y_length))
    board.fill(DARK_GRAY)
    global font, grid

    for x in range(5):
        for y in range(6):
            cell = grid[y][x]
            rect = pygame.Rect(x * cellSize, y * cellSize, cellSize, cellSize)
            pygame.draw.rect(board, BLACK, (x * cellSize, y * cellSize, cellSize, cellSize), 3)
            if cell is not None:
                if cell == WORD[x]:
                    pygame.draw.rect(board, GREEN, (x * cellSize, y * cellSize, cellSize, cellSize), 3)
                elif cell in WORD:
                    pygame.draw.rect(board, RED, (x * cellSize, y * cellSize, cellSize, cellSize), 3)                   
                    
            
            if cell is not None:
                letter = font.render(cell, True, WHITE)
                text_rect = letter.get_rect(center=rect.center)
                board.blit(letter, text_rect)


    return board

board = draw_board()
board_rect = board.get_rect(topleft=(0, 0))

user_text = ''
input_rect = pygame.Rect(50, 30, 140, 32) # Text box rect


while (running):

    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            elif event.key == pygame.K_RETURN:
                print(user_text) # Submit text
            else:
                user_text += event.unicode # Add character


    

    screen.fill(BLACK)
    screen.blit(board, board_rect)
    group.update(event_list)
    group.draw(screen)

    text_surface = font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x , input_rect.y + 5))
    input_rect.w = max(5, text_surface.get_width() + 10)


    pygame.display.flip()
    clock.tick(60)


pygame.quit()