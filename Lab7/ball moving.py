import pygame

pygame.init()
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
done = False
pygame.display.set_caption("Moving Ball")
ball_radius = 25
ball_color = pygame.Color('red')
clock = pygame.time.Clock()
ball_pos = [screen_width // 2, screen_height // 2]

speed = 20
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball_pos[1] = max(ball_pos[1] - speed, ball_radius)
    if keys[pygame.K_DOWN]:
        ball_pos[1] = min(ball_pos[1] + speed, screen_height - ball_radius)
    if keys[pygame.K_LEFT]:
        ball_pos[0] = max(ball_pos[0] - speed, ball_radius)
    if keys[pygame.K_RIGHT]:
        ball_pos[0] = min(ball_pos[0] + speed, screen_width - ball_radius)

    screen.fill(pygame.Color('white'))

    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)

    pygame.display.flip()
    clock.tick(60)