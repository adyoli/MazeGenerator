import pygame
import random

# Define constants for the maze
WIDTH = 800
HEIGHT = 800
ROWS = 20
COLS = 20
CELL_SIZE = WIDTH // COLS
WALL_THICKNESS = 5

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the maze
maze = []
for i in range(ROWS):
    row = []
    for j in range(COLS):
        cell = {'x': j * CELL_SIZE, 'y': i * CELL_SIZE, 'walls': [True, True, True, True], 'visited': False}
        row.append(cell)
    maze.append(row)

# Define a function to draw the maze
def draw_maze():
    screen.fill(BLACK)
    for i in range(ROWS):
        for j in range(COLS):
            cell = maze[i][j]
            x = cell['x']
            y = cell['y']
            if cell['walls'][0]: # top wall
                pygame.draw.line(screen, WHITE, (x, y), (x + CELL_SIZE, y), WALL_THICKNESS)
            if cell['walls'][1]: # right wall
                pygame.draw.line(screen, WHITE, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), WALL_THICKNESS)
            if cell['walls'][2]: # bottom wall
                pygame.draw.line(screen, WHITE, (x + CELL_SIZE, y + CELL_SIZE), (x, y + CELL_SIZE), WALL_THICKNESS)
            if cell['walls'][3]: # left wall
                pygame.draw.line(screen, WHITE, (x, y + CELL_SIZE), (x, y), WALL_THICKNESS)

# Define a function to get the neighbors of a cell
def get_neighbors(cell):
    i = cell['y'] // CELL_SIZE
    j = cell['x'] // CELL_SIZE
    neighbors = []
    if i > 0 and not maze[i - 1][j]['visited']: # top neighbor
        neighbors.append(maze[i - 1][j])
    if j < COLS - 1 and not maze[i][j + 1]['visited']: # right neighbor
        neighbors.append(maze[i][j + 1])
    if i < ROWS - 1 and not maze[i + 1][j]['visited']: # bottom neighbor
        neighbors.append(maze[i + 1][j])
    if j > 0 and not maze[i][j - 1]['visited']: # left neighbor
        neighbors.append(maze[i][j - 1])
    return neighbors

# Define a function to generate the maze
def generate_maze():
    stack = [maze[0][0]]
    while len(stack) > 0:
        current_cell = stack[-1]
        current_cell['visited'] = True
        neighbors = get_neighbors(current_cell)
        if len(neighbors) > 0:
            next_cell = random.choice(neighbors)
            if next_cell['x'] > current_cell['x']: # next cell is to the right
                current_cell['walls'][1] = False
                next_cell['walls'][3] = False
            elif next_cell['x'] < current_cell['x']: # next cell is to the left
                current_cell['walls'][3] = False
                next_cell['walls'][1] = False
            elif next_cell['y'] < current_cell['y']: # next cell is above
                current_cell['walls'][0] = False
                next_cell['walls'][2] = False
            elif next_cell['y'] > current_cell['y']: # next cell is below
                current_cell['walls'][2] = False
                next_cell['walls'][0] = False
            stack.append(next_cell)
        else:
            stack.pop()

# Generate the maze
generate_maze()

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the maze
    draw_maze()

    # Update the screen
    pygame.display.update()

    # Tick the clock
    clock.tick(60)

# Quit Pygame
pygame.quit()
