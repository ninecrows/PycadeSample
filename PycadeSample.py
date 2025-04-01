import pygame

pygame.init()

screen = pygame.display.set_mode((128 * 16, 48 * 16))

clock = pygame.time.Clock()

overlay = pygame.Surface((128*16, 48*16), 0, 32)
overlay.set_alpha(0)

running = True
while (running):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        elif event.type == pygame.KEYDOWN:
            print ("Key Down")
        elif event.type == pygame.KEYUP:
            print ("Key Up")

    screen.fill((255, 255, 255))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
