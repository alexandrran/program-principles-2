import pygame
import sys
import random
import time
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Create colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Background
background = pygame.image.load("AnimatedStreet.png")

# Create the display surface
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png")  # Load your coin image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global COINS
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


# Create sprite groups
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# Creating player and enemy instances
P1 = Player()
E1 = Enemy()

# Adding player and enemy to all_sprites group
all_sprites.add(P1)
all_sprites.add(E1)

# Adding enemies to enemies group
enemies.add(E1)

# Function to spawn coins
def spawn_coin():
    new_coin = Coin()
    coins.add(new_coin)
    all_sprites.add(new_coin)

# Adding a new event to spawn coins
SPAWN_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN_COIN, 2000)  # Adjust the time interval as needed

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SPAWN_COIN:
            spawn_coin()

    # Moving all sprites
    for entity in all_sprites:
        entity.move()

    # Handling collisions between player and coins
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)
    COINS += len(collected_coins)  # Increase score by the number of collected coins

    # Handling collisions between player and enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Drawing the background, scores, coins and sprites
    DISPLAYSURF.blit(background, (0, 0))
    coin_count = font_small.render("Coins: " + str(COINS), True, BLACK)
    DISPLAYSURF.blit(coin_count, (SCREEN_WIDTH - 10 - coin_count.get_width(), 10))
    scores = font_small.render("Score: " + str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)

    pygame.display.update()
    FramePerSec.tick(FPS)
