import pygame
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((200, 200))
mixer.init()

songs = ['Blinding Lights.mp3', 'Mind Over Matter.mp3', 'R U Mine.mp3']
current_song = 0
mixer.music.load(songs[current_song])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_p]:
        mixer.music.play()
    if keys[pygame.K_s]:
        mixer.music.stop()
    if keys[pygame.K_n]:
        current_song = (current_song + 1) % len(songs)
        mixer.music.load(songs[current_song])
        mixer.music.play()
    if keys[pygame.K_b]:
        current_song = (current_song - 1) % len(songs)
        mixer.music.load(songs[current_song])
        mixer.music.play()

    pygame.display.flip()

pygame.quit()
