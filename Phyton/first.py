import pygame
import random


pygame.init()


screen = pygame.display.set_mode((800, 800))


pygame.display.set_caption("Advanced Snake Game")
icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(icon)


player_pos = [100, 50]
player_vel = [0, 0]
player_size = 10


food_pos = [random.randint(0, 780), random.randint(0, 580)]
food_size = 10


score = 0
game_over = False


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)


while not game_over:
# Process events
  for event in pygame.event.get():
# Quit the game if the user closes the window
    if event.type == pygame.QUIT:
      game_over = True

    # Update player position based on keypresses
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            player_vel = [0, -1]
        if event.key == pygame.K_DOWN:
            player_vel = [0, 1]
        if event.key == pygame.K_LEFT:
            player_vel = [-1, 0]
        if event.key == pygame.K_RIGHT:
            player_vel = [1, 0]

# Update player position
player_pos[0] += player_vel[0]
player_pos[1] += player_vel[1]

# Check for collision with food
if abs(player_pos[0] - food_pos[0]) < 10 and abs(player_pos[1] - food_pos[1]) < 10:
    score += 1
    food_pos = [random.randint(0, 780), random.randint(0, 580)]

# Check for collision with screen edges
if player_pos[0] < 0 or player_pos[0] > 790 or player_pos[1] < 0 or player_pos[1] > 590:
    game_over = True

# Fill the screen with black
screen.fill(black)

# Draw the player and food
pygame
