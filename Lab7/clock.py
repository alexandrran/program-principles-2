import pygame
import time

pygame.init()
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

clock_image = pygame.image.load('main-clock.png')
arrow_seconds = pygame.image.load('left-hand.png')
arrow_minutes = pygame.image.load('right-hand.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    t = time.localtime()
    minutes = t.tm_min
    seconds = t.tm_sec

    angle_minutes = 360 - (minutes * 6 - 90)
    angle_seconds = 360 - (seconds * 6 - 90)

    arrow_rotated_minutes = pygame.transform.rotate(arrow_minutes, angle_minutes)
    arrow_rotated_seconds = pygame.transform.rotate(arrow_seconds, angle_seconds)

    screen.fill((255, 255, 255))

    rect_clock = clock_image.get_rect(center=(screen_width // 2, screen_height // 2))
    rect_minutes = arrow_rotated_minutes.get_rect(center=(screen_width // 2, screen_height // 2))
    rect_seconds = arrow_rotated_seconds.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(clock_image, rect_clock)
    screen.blit(arrow_rotated_minutes, rect_minutes)
    screen.blit(arrow_rotated_seconds, rect_seconds)

    pygame.display.flip()

pygame.quit()


