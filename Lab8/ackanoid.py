import pygame
import random

pygame.init()

# Set up screen dimensions and frame rate
W, H = 1200, 800
FPS = 60

# Initialize the Pygame window
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

# Paddle settings
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Ball settings
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Sound effect
collision_sound = pygame.mixer.Sound('catch.mp3')


# Function to handle ball-paddle collision
def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


# Block settings
# Create default blocks
default_block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
default_color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
                      for _ in range(len(default_block_list))]

# Select 3 unbreakable bricks
unbreakable_indices = random.sample(range(len(default_block_list)), 3)
unbreakable_block_list = [default_block_list.pop(index) for index in sorted(unbreakable_indices, reverse=True)]
unbreakable_color_list = [(255, 255, 255) for _ in range(3)]

# Select 4 bonus bricks
bonus_indices = random.sample(range(len(default_block_list)), 4)
bonus_block_list = [default_block_list.pop(index) for index in sorted(bonus_indices, reverse=True)]
bonus_color_list = [(255, 165, 0) for _ in range(4)]

# Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

# Variables for speed increase and paddle shrink
ball_speed_increase = 0.001
paddle_shrink_rate = 0.05

# Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Clear the screen
    screen.fill(bg)

    # Draw default bricks
    [pygame.draw.rect(screen, default_color_list[color], block) for color, block in enumerate(default_block_list)]

    # Drawing unbreakable bricks
    [pygame.draw.rect(screen, unbreakable_color_list[color], block) for color, block in
     enumerate(unbreakable_block_list)]

    # Drawing bonus bricks
    [pygame.draw.rect(screen, bonus_color_list[color], block) for color, block in enumerate(bonus_block_list)]

    # Draw paddle and ball
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    # Move the ball
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    # Ball collision with walls
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    if ball.centery < ballRadius + 50:
        dy = -dy

    # Ball-paddle collision
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    # Ball collision with default bricks
    hitIndex = ball.collidelist(default_block_list)
    if hitIndex != -1:
        hitRect = default_block_list.pop(hitIndex)
        hitColor = default_color_list.pop(hitIndex)
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        game_score += 1
        collision_sound.play()

    # Ball collision with unbreakable bricks
    hitIndex = ball.collidelist(unbreakable_block_list)
    if hitIndex != -1:
        dx, dy = detect_collision(dx, dy, ball, unbreakable_block_list[hitIndex])

    # Ball collision with bonus bricks (makes your paddle bigger)
    hitIndex = ball.collidelist(bonus_block_list)
    if hitIndex != -1:
        bonus_block_list.pop(hitIndex)
        paddleW += 20
        paddle = pygame.Rect(paddle.left - 10, paddle.top, paddleW, paddleH)

    # Update game score text
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)

    # Game over and win conditions
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(default_block_list):
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)

    # Move paddle based on keyboard input
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    # Increase ball speed
    ballSpeed += ball_speed_increase

    # Shrink paddle with time
    paddleW -= int(paddle_shrink_rate)
    paddle = pygame.Rect(paddle.left, paddle.top, paddleW, paddleH)

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)
