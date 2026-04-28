import pygame



# Game Setup 

# Constants
WIDTH = 600
HEIGHT = 720
X_length = 5
Y_length = 6
running = True
cellSize = WIDTH // X_length

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


# Board setup

def draw_board():
    board = pygame.Surface((cellSize * X_length, cellSize * Y_length))
    board.fill(LIGHT_GRAY)

    for x in range(X_length):
        for y in range(Y_length):
            pygame.draw.rect(board, BLACK, (x * cellSize, y * cellSize, cellSize, cellSize), 3)    

    return board

board = draw_board()
board_rect = board.get_rect(topleft=(0, 0))

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

print_grid()




while (running):

    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False


    screen.fill(BLACK)
    screen.blit(board, board_rect)
    group.update(event_list)
    group.draw(screen)

    pygame.display.flip()
    clock.tick(60)


pygame.quit()