import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    points = []
    drawing = False
    shape = 'circle'
    color = (255, 255, 255)

    while True:

        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():

            # determine if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                # determine if a letter key was pressed
                elif event.key == pygame.K_1:
                    shape = 'circle'
                elif event.key == pygame.K_2:
                    shape = 'square'
                elif event.key == pygame.K_3:
                    shape = 'eraser'
                elif event.key == pygame.K_r:
                    color = pygame.Color(255, 0, 0)
                elif event.key == pygame.K_g:
                    color = pygame.Color(0, 255, 0)
                elif event.key == pygame.K_b:
                    color = pygame.Color(0, 0, 255)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click starts drawing and grows radius
                    drawing = True
                    radius = min(200, radius + 1)
                elif event.button == 2:  # right click stops drawing
                    drawing = False
                elif event.button == 3:  # right click shrinks radius
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                if drawing:
                    position = event.pos
                    points = points + [position]
                    points = points[-256:]

        screen.fill((0, 0, 0))

        # draw all points
        i = 0
        while i < len(points) - 1:
            if shape == 'circle':
                drawCircleBetween(screen, i, points[i], points[i + 1], radius, color)
            elif shape == 'square':
                drawRectangleBetween(screen, i, points[i], points[i + 1], radius, color)
            elif shape == 'eraser':
                eraseBetween(screen, i, points[i], points[i + 1], radius)
            i += 1

        pygame.display.flip()

        clock.tick(60)


def drawCircleBetween(screen, index, start, end, width, color): # Draw circles
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)


def drawRectangleBetween(screen, index, start, end, width, color): # Draw rectangles
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.rect(screen, color, (x, y, width, width))


def eraseBetween(screen, index, start, end, width): # Erase everything
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, (0, 0, 0), (x, y), width)


main()
