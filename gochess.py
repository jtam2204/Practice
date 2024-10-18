import pygame
import sys
import time

class GoGrid:
    def __init__(self):
        self.empty = True
        self.color = None

    def place_stone(self, color):
        self.empty = False
        self.color = color

    def remove_stone(self):
        self.empty = True
        self.color = None

    def has_liberties(self, board):
        row, col = self.get_position(board)
        liberties = set()

        def check_liberties(r, c):
            if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE and board[r][c].empty:
                liberties.add((r, c))
            elif 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE and board[r][c].color == self.color:
                liberties.update(board[r][c].has_liberties(board))

        check_liberties(row - 1, col)
        check_liberties(row + 1, col)
        check_liberties(row, col - 1)
        check_liberties(row, col + 1)

        return liberties

    def get_position(self, board):
        for r, row in enumerate(board):
            for c, grid in enumerate(row):
                if grid == self:
                    return r, c
        return -1, -1

def draw_board(screen, board):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = col * GRID_WIDTH
            y = row * GRID_WIDTH

            if board[row][col].empty:
                pygame.draw.rect(screen, BROWN, (x, y, GRID_WIDTH, GRID_WIDTH))
            elif board[row][col].color == 'black':
                pygame.draw.circle(screen, BLACK, (x + GRID_WIDTH // 2, y + GRID_WIDTH // 2), GRID_WIDTH // 2 - 3)
            elif board[row][col].color == 'white':
                pygame.draw.circle(screen, WHITE, (x + GRID_WIDTH // 2, y + GRID_WIDTH // 2), GRID_WIDTH // 2 - 3)

            pygame.draw.rect(screen, BLACK, (x, y, GRID_WIDTH, GRID_WIDTH), 1)

def undo_move(board, move_history):
    if move_history:
        row, col = move_history.pop()
        board[row][col].remove_stone()

def draw_timer(screen, font, elapsed_time):
    hours, remainder = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(remainder, 60)

    timer_surface = font.render(f"Timer: {int(hours):02}:{int(minutes):02}:{int(seconds):02}", True, BLACK)
    screen.blit(timer_surface, (GRID_SIZE * GRID_WIDTH + 10, 10))

def draw_turn_indicator(screen, font, turn):
    turn_surface = font.render(f"Turn: {turn.capitalize()}", True, BLACK)
    screen.blit(turn_surface, (GRID_SIZE * GRID_WIDTH + 10, 50))

def draw_quit_button(screen, font):
    quit_button = pygame.Rect(GRID_SIZE * GRID_WIDTH + 10, 90, 150, 30)
    pygame.draw.rect(screen, BLACK, quit_button, 1)

    quit_surface = font.render("Quit Game", True, BLACK)
    screen.blit(quit_surface, (GRID_SIZE * GRID_WIDTH + 20, 95))

    return quit_button

def draw_pass_button(screen, font):
    pass_button = pygame.Rect(GRID_SIZE * GRID_WIDTH + 10, 130, 150, 30)
    pygame.draw.rect(screen, BLACK, pass_button, 1)

    pass_surface = font.render("Pass", True, BLACK)
    screen.blit(pass_surface, (GRID_SIZE * GRID_WIDTH + 65, 135))

    return pass_button

def draw_restart_button(screen, font):
    restart_button = pygame.Rect(GRID_SIZE * GRID_WIDTH + 10, 170, 150, 30)
    pygame.draw.rect(screen, BLACK, restart_button, 1)

    restart_surface = font.render("Restart", True, BLACK)
    screen.blit(restart_surface, (GRID_SIZE * GRID_WIDTH + 45, 175))

    return restart_button

def restart_game():
    return [[GoGrid() for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)], []

# game rules
def is_legal_move(board, row, col, color):
    # Check if the move is within the board and the intersection is empty
    if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE and board[row][col].empty:
        # Check for the suicide rule
        temp_board = [[grid.empty for grid in row] for row in board]
        temp_board[row][col] = False
        if not has_liberties(temp_board, row, col):
            return False

        # Check for the ko rule
        if is_ko(board, temp_board):
            return False

        return True
    return False

def is_ko(board, temp_board):
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if board[r][c].empty != temp_board[r][c]:
                return False
    return True

def has_liberties(board, row, col):
    liberties = set()

    def check_liberties(r, c):
        if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE and board[r][c]:
            liberties.add((r, c))

    check_liberties(row - 1, col)
    check_liberties(row + 1, col)
    check_liberties(row, col - 1)
    check_liberties(row, col + 1)

    return liberties

def capture_stones(board, row, col, color):
    captured_stones = set()

    def dfs(r, c, visited):
        visited.add((r, c))
        current_stone = board[r][c]

        if not current_stone.empty and current_stone.color != color:
            liberties = current_stone.has_liberties(board)

            if not liberties:
                captured_stones.add((r, c))
            else:
                for lib in liberties:
                    if lib not in visited:
                        dfs(*lib, visited)

    visited = set()
    dfs(row, col, visited)

    print("Captured Stones:", captured_stones)  # Add this line for debugging

    for stone in captured_stones:
        board[stone[0]][stone[1]].remove_stone()

def handle_player_move(board, mouseX, mouseY, turn):
    col = mouseX // GRID_WIDTH
    row = mouseY // GRID_WIDTH

    if is_legal_move(board, row, col, turn):
        board[row][col].place_stone(turn)
        capture_stones(board, row, col, turn)  # Check for captures after placing stone

def is_game_over(board):
    # Implement your game-over condition here
    return False

GRID_SIZE = 9
GRID_WIDTH = 50
BROWN = (222, 184, 135)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

border_width = 10

screen_width =  GRID_SIZE * GRID_WIDTH + 200 + border_width
screen_height = GRID_SIZE * GRID_WIDTH + border_width
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Local Go Chess Program")

board = [[GoGrid() for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
move_history = []

turn = 'black'
start_time = time.time()
font = pygame.font.Font(None, 36)

# Main game loop
while not is_game_over(board):
    elapsed_time = time.time() - start_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos

            if 0 <= mouseX < GRID_SIZE * GRID_WIDTH and 0 <= mouseY < GRID_SIZE * GRID_WIDTH:
                if event.button == 1:  # Left-click
                    handle_player_move(board, mouseX, mouseY, turn)
                    move_history.append((mouseY // GRID_WIDTH, mouseX // GRID_WIDTH))
                    turn = 'white' if turn == 'black' else 'black'
                elif event.button == 3:  # Right-click
                    undo_move(board, move_history)
                    turn = 'white' if turn == 'black' else 'black'
            elif quit_button.collidepoint(mouseX, mouseY) and event.button == 1:
                pygame.quit()
                sys.exit()
            elif pass_button.collidepoint(mouseX, mouseY) and event.button == 1:
                # Implement pass logic here
                turn = 'white' if turn == 'black' else 'black'
            elif restart_button.collidepoint(mouseX, mouseY) and event.button == 1:
                # Restart the game
                board, move_history = restart_game()
                start_time = time.time()
                turn = 'black'

    screen.fill(BROWN)
    draw_board(screen, board)
    draw_timer(screen, font, elapsed_time)
    draw_turn_indicator(screen, font, turn)
    quit_button = draw_quit_button(screen, font)
    pass_button = draw_pass_button(screen, font)
    restart_button = draw_restart_button(screen, font)

    pygame.display.flip()